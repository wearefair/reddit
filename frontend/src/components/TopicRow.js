import React from 'react';
import PropTypes from 'prop-types';
import { MdArrowDropUp, MdArrowDropDown } from 'react-icons/lib/md';
import { Link } from 'react-router-dom';
import styles from './styles/TopicRow-styles';


class TopicRow extends React.Component {
  constructor() {
    super();
    this.state = { title: 'Topic' };
  }

  render() {
    const { title, votes, commentCount } = this.props;

    return (
      <div style={styles.container}>
        <div style={styles.voteContainer}>
          <Link to="/upvote" style={styles.arrowLink}>
            <MdArrowDropUp size={32} />
          </Link>
          {votes}
          <Link to="/downvote" style={styles.arrowLink}>
            <MdArrowDropDown size={32} />
          </Link>
        </div>
        <div style={styles.topicContainer}>
          <Link to="/topic/1234" style={styles.topicLink}>
            <p style={styles.topicTitle}>
              {title}
            </p>
          </Link>
          <Link to="/topic/comments" style={styles.commentLink}>
            <p style={styles.commentCount}>
              {commentCount} comments
            </p>
          </Link>
        </div>
      </div>
    );
  }
}

TopicRow.propTypes = {
  title: PropTypes.string.isRequired,
  votes: PropTypes.number.isRequired,
  commentCount: PropTypes.number.isRequired,
};

export default TopicRow;
