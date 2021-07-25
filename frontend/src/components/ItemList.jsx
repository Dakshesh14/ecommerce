import React, { useState } from 'react';

import InfiniteScroll from 'react-infinite-scroll-component';

// importing actions
import useFetch from '../actions/useFetchItems';

// importing components
import ItemCard from './ItemCard';
import Spinner from './Spinner';
import CategorySidebar from './CategorySidebar'

function ItemList() {

    const [page, setPage] = useState(1)

    // for ordering/filtering/search/etc...
    const [category, setCategory] = useState('');
    const [ordering, setOrdering] = useState('');
    const [search, setSearch] = useState('');

    const { hasMore, items } = useFetch(page, category, ordering, search);

    const handleChange = e => {
        setOrdering(e.target.value);
    }

    const handleSubmit = e => {
        e.preventDefault();
        setSearch(e.target[0].value);
    }

    return (
        <section className="section-margin--small mb-5">
            <div className="container">
                <div className="row">
                    <div className="col-xl-3 col-lg-4 col-md-5">
                        <div className="sidebar-categories">
                            <div className="head">Browse Categories</div>
                            <CategorySidebar setCategory={setCategory} />
                        </div>
                    </div>
                    <div className="col-xl-9 col-lg-8 col-md-7">
                        <div className="filter-bar d-flex flex-wrap align-items-center">
                            <div className="sorting mr-auto">
                                <select onChange={handleChange} className="custom-select">
                                    <option value="price">Price (low to high)</option>
                                    <option value="-price">Price (high to low)</option>
                                </select>
                            </div>
                            <div>
                                <form onSubmit={handleSubmit}>
                                    <div className="input-group filter-bar-search">
                                        <input type="text" placeholder="Search" />
                                        <div className="input-group-append">
                                            <button type="submit"><i className="ti-search"></i></button>
                                        </div>
                                    </div>
                                </form>
                            </div>
                        </div>
                        {
                            items.length < 1
                                ?
                                <p className="ml-3 text-muted">No post {search && "with title " + search} found...</p>
                                :
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
                        }
                    </div>
                </div>
            </div>
        </section>
    )
}

export default ItemList
