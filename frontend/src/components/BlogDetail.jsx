import React, { useState, useEffect } from 'react';
import {
    useParams
} from 'react-router-dom';

function BlogDetail() {

    let { slug } = useParams()

    const [blog, setBlog] = useState({});

    useEffect(() => {
        axios({
            method: 'GET',
            url: `../api/blog/${slug}`
        }).then(res => {
            setBlog(res.data);
        })
    }, [])

    return (
        <div className="container mt-5 pt-5">
            <div className="row">
                <div className="single-post row">
                    <div className="col-lg-8 col-md-9">
                        <div className="feature-img">
                            <img className="img-fluid" src={blog.thumbnail} alt="" />
                        </div>
                    </div>
                    <div className="col-lg-9 col-md-9 blog_details">
                        <h2>{blog.title}</h2>
                        <p dangerouslySetInnerHTML={{ __html: blog.content }} className="mt-5" />
                    </div>
                </div>
            </div>
        </div>
    )
}

export default BlogDetail
