import React from 'react';

import {
    Link,
} from 'react-router-dom';

function BlogCard({ blog }) {
    return (
        <article className="row blog_item">
            <div className="col-md-3">
                <div className="blog_info text-right">
                    <ul className="blog_meta list">
                        <li>
                            <a href="#">
                                {blog.date_added}
                                <i className="lnr lnr-calendar-full"></i>
                            </a>
                        </li>
                    </ul>
                </div>
            </div>
            <div className="col-md-9">
                <div className="blog_post">
                    <img src={blog.thumbnail_small} alt={blog.title} />
                    <div className="blog_details">
                        <Link to={"/blog/" + blog.title_slug}>
                            <h2>{blog.title}</h2>
                        </Link>
                        <p>{blog.about}</p>
                    </div>
                </div>
            </div>
        </article>
    )
}

export default BlogCard
