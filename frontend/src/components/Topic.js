import React from 'react';
import PropTypes from 'prop-types';

class Topic extends React.Component {
  constructor() {
    super();
    this.state = { title: 'Topic' };
  }

  render() {
    const { title } = this.props;

    return (
      <div>
        <p>{title}</p>
      </div>
    );
  }
}

Topic.propTypes = {
  title: PropTypes.string.isRequired,
};

export default Topic;
