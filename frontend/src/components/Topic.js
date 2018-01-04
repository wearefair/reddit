import React from 'react';
import PropTypes from 'prop-types';
import styles from './styles/Topic-styles';

class Topic extends React.Component {
  constructor() {
    super();
    this.state = { title: 'Topic' };
  }

  render() {
    const { topicId } = this.props;

    return (
      <div style={styles.container}>Topic {topicId}</div>
    );
  }
}

Topic.propTypes = {
  topicId: PropTypes.number.isRequired,
};

export default Topic;
