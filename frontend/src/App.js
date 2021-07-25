import React from 'react';
import {
    BrowserRouter as Router,
    Switch,
    Route,
} from 'react-router-dom';

import ItemList from './components/ItemList';
import ItemDetail from './components/ItemDetail';
import BlogList from './components/BlogList';
import BlogDetail from './components/BlogDetail';

function App() {
    return (
        <>
            <h1>This is react</h1>
            <Router>
                <Switch>
                    <Route
                        path='/items'
                        component={ItemList}
                        exact
                    />
                    <Route
                        path='/item/:slug'
                        component={ItemDetail}
                        exact
                    />
                    <Route
                        path='/blogs'
                        component={BlogList}
                        exact
                    />
                    <Route
                        path='/blog/:slug'
                        component={BlogDetail}
                        exact
                    />
                </Switch>
            </Router>
        </>
    )
}

export default App