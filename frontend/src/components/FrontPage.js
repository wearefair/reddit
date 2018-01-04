import React from 'react';
import { Link } from 'react-router-dom';
import TopicRow from './TopicRow';
import styles from './styles/FrontPage-styles';

export default class FrontPage extends React.Component {
  constructor() {
    super();
    this.state = { title: 'Fairreddit FrontPage' };
    this.topics = [
      { title: 'Topic 1', votes: 20, commentCount: 100 },
      { title: 'Topic 2', votes: 10, commentCount: 5000 },
    ];
  }

  render() {
    const listItems = this.topics.map(topic =>
      (
        <li key={topic.title} style={styles.topicsContainer}>
          <TopicRow title={topic.title} votes={topic.votes} commentCount={topic.commentCount} />
        </li>
      ),
    );

    return (
      <div>
        <p style={styles.title}>{this.state.title}</p>
        <div style={styles.filterLinksContainer}>
          <Link to="#hot">Hot</Link>
          <Link to="#new">New</Link>
          <Link to="#controversial">Controversial</Link>
        </div>
        <ul style={styles.listTopicsContainer}>
          {listItems}
        </ul>
      </div>
    );
  }
}
