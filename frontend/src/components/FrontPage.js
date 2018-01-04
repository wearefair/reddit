import React from 'react';
import Topic from './Topic';

export default class FrontPage extends React.Component {
  constructor() {
    super();
    this.state = { title: 'FrontPage' };
    this.topics = [
      { title: 'Topic 1' },
      { title: 'Topic 2' },
    ];
  }

  render() {
    const listItems = this.topics.map(topic =>
      (
        <li key={topic.title}>
          <Topic title={topic.title} />
        </li>
      ),
    );

    return (
      <div>
        <p>{this.state.title}</p>
        <ul>
          {listItems}
        </ul>
      </div>
    );
  }
}
