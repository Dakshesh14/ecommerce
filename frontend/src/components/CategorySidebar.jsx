import React, { useState, useEffect } from 'react';

function CategorySidebar({ setCategory }) {

    const [categories, setCategories] = useState([]);

    useEffect(() => {
        axios({
            method: 'GET',
            url: '../api/category'
        }).then(res => {
            setCategories(res.data);
        })
    }, [])

    const handleChange = e => {
        setCategory(e.target.value)
    }

    return (
        <ul className="main-categories">
            <li className="common-filter">
                <ul>
                    <li className="filter-list">
                        <input
                            className="pixel-radio"
                            type="radio"
                            id="All"
                            value=''
                            name="brand"
                            onChange={handleChange}
                        />
                        <label htmlFor="All">All</label>
                    </li>
                    {
                        categories.map(ct => (
                            <li className="filter-list" key={ct.id}>
                                <input
                                    className="pixel-radio"
                                    type="radio"
                                    id={ct.ct}
                                    value={ct.ct}
                                    name="brand"
                                    onChange={handleChange}
                                />
                                <label htmlFor={ct.ct}>{ct.ct}</label>
                            </li>
                        ))
                    }
                </ul>
            </li>
        </ul>
    )
}

export default CategorySidebar
