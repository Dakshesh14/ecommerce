import axios from 'axios';
import { useState, useEffect } from 'react';

function useFetch(slug) {

    const [loading, setLoading] = useState(true);
    const [item, setItem] = useState({});
    const url = `http://127.0.0.1:8000/api/item/${slug}`

    useEffect(() => {
        setLoading(true)
        axios({
            method: 'GET',
            url: url,
        }).then(res => {
            setItem(res.data);
            setLoading(false)
        })
    }, [slug])

    return { loading, item }
}

export default useFetch