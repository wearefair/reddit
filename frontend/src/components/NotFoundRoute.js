import React, { Component } from 'react';

class NotFoundRoute extends Component {
  constructor() {
    super();
    this.state = { title: '404' };
  }

  render() {
    return (
      <div>
        404!
      </div>
    );
  }
}

export default NotFoundRoute;
