import { createStore, applyMiddleware, combineReducers } from 'redux';
import thunk from 'redux-thunk';
import threatReducer from './reducers/threatReducer';
// Importar outros reducers conforme necessário

const rootReducer = combineReducers({
  threats: threatReducer,
  // Outros reducers
});

const store = createStore(rootReducer, applyMiddleware(thunk));

export default store;
