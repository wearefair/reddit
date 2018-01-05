import React from 'react';
import PropTypes from 'prop-types';
import TopicRow from './TopicRow';
import styles from './styles/Topic-styles';

class Topic extends React.Component {
  constructor() {
    super();
    this.state = { title: 'Topic' };
  }

  render() {
    const { topicId } = this.props.match.params;

    const topic = {
      title: 'Title',
      votes: 20,
      commentCount: 1000,
    };

    return (
      <div style={styles.container}>
        <TopicRow title={topic.title} votes={topic.votes} commentCount={topic.commentCount} />
        {topicId}
      </div>
    );
  }
}

Topic.propTypes = {
  match: PropTypes.shape({
    params: PropTypes.shape({
      topicId: PropTypes.string.isRequired,
    }),
  }),
};

Topic.defaultProps = {
  match: {},
};

export default Topic;
