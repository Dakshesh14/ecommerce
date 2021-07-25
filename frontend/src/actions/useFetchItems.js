import axios from 'axios';
import { useState, useEffect } from 'react'

function useFetch(page, category, ordering, search) {

    const [items, setItems] = useState([]);
    const [hasMore, setHasMore] = useState(false);
    const url = "../api/items/"

    useEffect(() => {
        setItems([])
    }, [category, ordering, search])

    useEffect(() => {
        let cancel
        axios({
            method: 'GET',
            url: url,
            params: {
                page: page,
                search: search,
                ct_filter: category,
                ordering: ordering,
            },
            cancelToken: new axios.CancelToken(c => cancel = c),
        }).then(res => {
            if (!res.data.next) setHasMore(false)
            setItems(items => {
                return [...new Set([...items, ...res.data.results])]
            })
        }).catch(e => {
            if (axios.isCancel(e)) return setItems([])
        })
        return () => cancel()
    }, [page, category, ordering, search])

    return { hasMore, items }
}

export default useFetch