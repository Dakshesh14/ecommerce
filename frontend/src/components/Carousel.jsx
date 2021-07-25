import React from 'react'

function Carousel({ images }) {
    return (
        <div id="item_image_carousel" className="carousel slide carousel-fade" data-ride="carousel">
            <div className="carousel-inner">
                {
                    images.map((img, index) => (
                        <div key={img.image} className={"carousel-item" + (index === 0 ? " active" : '')}>
                            <img src={'..' + img.image} className="d-block w-100" alt="item photo" />
                        </div>
                    ))
                }
            </div>
            <a className="carousel-control-prev" href="#item_image_carousel" role="button" data-slide="prev">
                <span className="carousel-control-prev-icon" aria-hidden="true"></span>
                <span className="sr-only">Previous</span>
            </a>
            <a className="carousel-control-next" href="#item_image_carousel" role="button" data-slide="next">
                <span className="carousel-control-next-icon" aria-hidden="true"></span>
                <span className="sr-only">Next</span>
            </a>
        </div>
    )
}

export default Carousel
