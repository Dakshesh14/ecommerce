import axios from 'axios';
import { useState, useEffect } from 'react'

function useFetch(page) {

    const [items, setItems] = useState([]);
    const [hasMore, setHasMore] = useState(false);
    const url = "http://127.0.0.1:8000/api/items/"

    useEffect(() => {
        let cancel
        axios({
            method: 'GET',
            url: url,
            params: {
                page: page,
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
    }, [page])

    return { hasMore, items }
}

export default useFetch