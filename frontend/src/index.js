import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import Provider from 'react-redux';
import configureStore from './store/configureStore';
import App from './components/App';
import Topic from './components/Topic';

ReactDOM.render(
  (
    <Provider store={configureStore()}>
      <BrowserRouter>
        <Switch>
          <Route path="/" component={App}>
            <Route path="/topic" component={Topic} />
          </Route>
        </Switch>
      </BrowserRouter>
    </Provider>
  ),
  document.getElementById('app'),
);
