/* eslint react/prop-types: 0 */
import React from 'react';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import * as topicActions from '../actions/topicActions';
import TopicRow from './TopicRow';
import styles from './styles/FrontPage-styles';

class FrontPage extends React.Component {
  constructor() {
    super();
    this.state = { title: 'Fairreddit FrontPage' };
  }

  componentWillMount() {
    this.props.topicActions.fetchTopics();
  }

  render() {
    const listItems = this.props.topics.map(topic =>
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

function mapStateToProps(state) {
  return { topics: state.topics };
}

function mapDispatchToProps(dispatch) {
  return { topicActions: bindActionCreators(topicActions, dispatch) };
}

export default connect(mapStateToProps, mapDispatchToProps)(FrontPage);
