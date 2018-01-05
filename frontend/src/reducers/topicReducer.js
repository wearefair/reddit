import initialState from './initialState';
import { FETCH_TOPICS, RECEIVE_TOPICS } from '../actions/topicActions';

export default function topics(state = initialState.topics, action) {
  let newState;
  switch (action.type) {
    case FETCH_TOPICS:
      return action;
    case RECEIVE_TOPICS:
      console.log('here');
      newState = action.topics;
      return newState;
    default:
      return state;
  }
}
