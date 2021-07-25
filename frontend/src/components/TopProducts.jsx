import React from 'react';

// importing components
import ItemCard from './ItemCard';

function TopProducts({ items }) {
    return (
        <section className="related-product-area section-margin--small mt-5 pt-5">
            <div className="container">
                <div className="section-intro pb-60px">
                    <p>Popular Item in the market</p>
                    <h2>Top <span className="section-intro__style">Product</span></h2>
                </div>
                <div className="row mt-30">
                    {
                        items.map(item => (
                            <ItemCard item={item} key={item.id} />
                        ))
                    }
                </div>
            </div>
        </section>
    )
}

export default TopProducts
