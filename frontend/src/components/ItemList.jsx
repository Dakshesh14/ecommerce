import React, { useState } from 'react';

import InfiniteScroll from 'react-infinite-scroll-component';

// importing actions
import useFetch from '../actions/useFetchItems';

// importing components
import ItemCard from './ItemCard';
import Spinner from './Spinner';

function ItemList() {

    const [page, setPage] = useState(1)
    const { hasMore, items } = useFetch(page);

    return (
        <section className="section-margin--small mb-5">
            <div className="container">
                <div className="row">
                    <div className="col-xl-3 col-lg-4 col-md-5">
                        <div className="sidebar-categories">
                            <div className="head">Browse Categories</div>
                            <ul className="main-categories">
                                <li className="common-filter">
                                    <form action="#">
                                        <ul>
                                            <li className="filter-list">
                                                <input className="pixel-radio" type="radio" id="men" name="brand" />
                                                <label htmlFor="men">Men<span> (3600)</span></label>
                                            </li>
                                            <li className="filter-list">
                                                <input className="pixel-radio" type="radio" id="women" name="brand" />
                                                <label htmlFor="women">Women<span> (3600)</span></label>
                                            </li>
                                            <li className="filter-list">
                                                <input className="pixel-radio" type="radio" id="accessories" name="brand" />
                                                <label htmlFor="accessories">Accessories<span> (3600)</span></label>
                                            </li>
                                            <li className="filter-list">
                                                <input className="pixel-radio" type="radio" id="footwear" name="brand" />
                                                <label htmlFor="footwear">Footwear<span> (3600)</span></label>
                                            </li>
                                            <li className="filter-list">
                                                <input className="pixel-radio" type="radio" id="bayItem" name="brand" />
                                                <label htmlFor="bayItem">Bay item<span> (3600)</span></label>
                                            </li>
                                            <li className="filter-list">
                                                <input className="pixel-radio" type="radio" id="electronics" name="brand" />
                                                <label htmlFor="electronics">Electronics<span> (3600)</span></label>
                                            </li>
                                            <li className="filter-list">
                                                <input className="pixel-radio" type="radio" id="food" name="brand" />
                                                <label htmlFor="food">Food<span> (3600)</span></label>
                                            </li>
                                        </ul>
                                    </form>
                                </li>
                            </ul>
                        </div>
                    </div>
                    <div className="col-xl-9 col-lg-8 col-md-7">
                        <div className="filter-bar d-flex flex-wrap align-items-center">
                            <div className="sorting mr-auto">
                                <select>
                                    <option value="1">Default sorting</option>
                                    <option value="1">Default sorting</option>
                                    <option value="1">Default sorting</option>
                                </select>
                            </div>
                            <div>
                                <div className="input-group filter-bar-search">
                                    <input type="text" placeholder="Search" />
                                    <div className="input-group-append">
                                        <button type="button"><i className="ti-search"></i></button>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className="lattest-product-area pb-40 category-list">
                            <InfiniteScroll
                                dataLength={items.length}
                                next={() => {
                                    setPage(page + 1)
                                }}
                                hasMore={hasMore}
                                loader={<Spinner />}
                                className="row"
                                style={{ overflowY: 'hidden' }}
                            >
                                {items.map(item => (
                                    <ItemCard key={item.id} item={item} />
                                ))}
                            </InfiniteScroll>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    )
}

export default ItemList
