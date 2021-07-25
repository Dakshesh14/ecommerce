import React from 'react';

import {
    Link,
} from 'react-router-dom';

function ItemCard({ item }) {
    return (
        <div className="col-md-6 col-lg-4">
            <div className="card text-center card-product">
                <div className="card-product__img">
                    <img className="card-img" src={item.thumbnail} alt="" />
                    <ul className="card-product__imgOverlay">
                        <li><button><i className="ti-shopping-cart"></i></button></li>
                    </ul>
                </div>
                <div className="card-body">
                    <p>{item.category}</p>
                    <h4 className="card-product__title">
                        <Link to={'item/' + item.title_slug}>{item.title}</Link>
                    </h4>
                    <p className="card-product__price">${item.price}</p>
                </div>
            </div>
        </div>
    )
}

export default ItemCard
