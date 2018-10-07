import request from '../util/request';

const delay = millisecond => {
  return new Promise(resolve => {
      setTimeout(resolve, millisecond);
  })
};

export default {
    namespace: 'puzzlecards',
    state: {
        data: [],
        counter: 0,
    },

    effects: {
      *queryInitCards(_, sagaEffects) {
          const {call, put} = sagaEffects;
          const endPointURI = '/user/register';
          const puzzle = yield call(request, endPointURI);

          yield put({type: 'addNewCard', payload: puzzle});
          yield call(delay, 3000);
          const puzzle2 = yield call(request, endPointURI);
          yield put({type: 'addNewCard', payload: puzzle2});
      }
    },

    reducers: {
        addNewCard(state, {payload: newCard}) {
            const nextCounter = state.counter + 1;
            const newCardWithId = {...newCard, id: nextCounter};
            const nextData = state.data.concat(newCardWithId);
            return {
                data: nextData,
                counter: nextCounter,
            };
        }
    }

};