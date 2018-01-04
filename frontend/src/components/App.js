import React, { Component } from 'react';
import FrontPage from './FrontPage';
import styles from './styles/App-styles';

class App extends Component {
  constructor() {
    super();
    this.state = { title: 'Faireddit' };
  }

  render() {
    return (
      <div style={styles.container}>
        <FrontPage />
      </div>
    );
  }
}

export default App;
