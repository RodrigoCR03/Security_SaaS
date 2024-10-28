import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { Provider } from 'react-redux';
import store from './store';
import Dashboard from './pages/dashboard';
import Login from './pages/login';
import Register from './pages/register';
import Privacy from './pages/privacy';
import AVSD from './pages/avsd';

function App() {
  return (
    <Provider store={store}>
      <Router>
        <Switch>
          <Route exact path="/" component={Login} />
          <Route path="/register" component={Register} />
          <Route path="/dashboard" component={Dashboard} />
          <Route path="/privacy" component={Privacy} />
          <Route path="/avsd" component={AVSD} />
          {/* Outras rotas conforme necessário */}
        </Switch>
      </Router>
    </Provider>
  );
}

export default App;
