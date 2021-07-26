import React, { useState, useEffect } from 'react';

import InfiniteScroll from 'react-infinite-scroll-component';

import Spinner from './Spinner';
import BlogCard from './BlogCard';

function BlogList() {

    const [page, setPage] = useState(1);
    const [hasMore, setHasMore] = useState(true);
    const [loading, setLoading] = useState(true);
    const [blogs, setBlogs] = useState([])

    useEffect(() => {
        axios({
            method: 'GET',
            url: '../api/blogs',
            params: {
                page: page,
            },
        }).then(res => {
            const { next, results } = res.data
            if (!next) setHasMore(false)
            setBlogs(prevBlogs => {
                return [...new Set([...prevBlogs, ...results])]
            })
            setLoading(false)
        })
    }, [page])

    if (loading) return <Spinner />

    return (
        <section className="blog_area mt-5 pt-5">
            <div className="container">
                <div className="row">
                    <div className="col-lg-8">
                        <InfiniteScroll
                            dataLength={blogs.length}
                            next={() => {
                                setPage(page + 1)
                            }}
                            hasMore={hasMore}
                            loader={<Spinner />}
                            className="blog_left_sidebar"
                            style={{ overflowY: 'hidden', overflowX: 'hidden' }}
                        >
                            {blogs.map(blog => (
                                <BlogCard key={blog.id} blog={blog} />
                            ))}
                        </InfiniteScroll>
                    </div>
                </div>
            </div>
        </section>
    )
}

export default BlogList
