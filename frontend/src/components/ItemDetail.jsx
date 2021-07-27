import React, { useState } from 'react';

import {
    useParams,
} from 'react-router-dom';


// importing actions
import useFetchItemDetail from '../actions/useFetchItemDetail';

// importing components
import Spinner from './Spinner';
import Carousel from './Carousel';
import TopProducts from './TopProducts';

function ItemDetail() {

    let { slug } = useParams();
    const [quantity, setQuantity] = useState(1);

    const { loading, item } = useFetchItemDetail(slug);

    if (loading) {
        return <Spinner />
    }

    const handleChange = e => {
        setQuantity(e.target.value);
    }

    return (
        <>
            <div className="product_image_area">
                <div className="container">
                    <div className="row s_product_inner">
                        <div className="col-lg-6">
                            <div className="s_Product_carousel">
                                <div className="single-prd-item">
                                    <Carousel images={item.images}></Carousel>
                                </div>
                            </div>
                        </div>
                        <div className="col-lg-5 offset-lg-1">
                            <div className="s_product_text">
                                <h3>
                                    {item.title}
                                </h3>
                                <h2>${item.price}</h2>
                                <ul className="list">
                                    <li>
                                        <a className="active" href="#">
                                            <span>Category</span> : {item.category}
                                        </a>
                                    </li>
                                    <li>
                                        <a href="#">
                                            <span>Availibility</span> : {item.status}
                                        </a>
                                    </li>
                                </ul>
                                <p>{item.content}</p>

                                <div className="product_count mt-2">
                                    <label htmlFor="qty">Quantity:</label>
                                    <input type="text" name="qty" id="sst" size="2" maxLength="12" title="Quantity:"
                                        className="input-text qty" value={quantity} onChange={handleChange} />
                                    <span
                                        className="button primary-btn ml-2"
                                        type="button"
                                        onClick={() => addToCart(item.title_slug, quantity)}
                                    >Add to Cart</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <TopProducts items={item.featured_products} />
        </>
    )
}

export default ItemDetail
