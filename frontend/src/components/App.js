import React, { Component } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { Provider } from 'react-redux';
import configureStore from '../store/configureStore';
import FrontPage from './FrontPage';
import Topic from './Topic';
import NotFoundRoute from './NotFoundRoute';
import styles from './styles/App-styles';

const store = configureStore();

class App extends Component {
  constructor() {
    super();
    this.state = { title: 'Faireddit' };
  }

  render() {
    return (
      <div style={styles.container}>
        <Provider store={store}>
          <BrowserRouter>
            <Switch>
              <Route path="/topic/:topicId" component={Topic} />
              <Route exact path="/" component={FrontPage} />
              <Route path="*" exact component={NotFoundRoute} />
            </Switch>
          </BrowserRouter>
        </Provider>
      </div>
    );
  }
}

export default App;
