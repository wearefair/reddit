import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import App from './components/App';
import Topic from './components/Topic';

ReactDOM.render(
  (
    <BrowserRouter>
      <Switch>
        <Route path="/" component={App}>
          <Route path="/topic" component={Topic} />
        </Route>
      </Switch>
    </BrowserRouter>
  ),
  document.getElementById('app'),
);
