import React, {Component} from 'react';
import Header from './components/header.js';
import Footer from './components/footer.js';
import Routes from './routes';

class App extends Component{
  constructor(props) {
    super(props);
    this.state = {
      logged_in: localStorage.getItem('token') ? true : false,
      username: '',
      user_type:'',
      user_id:''
    };
  }

  componentDidMount() {
    if (this.state.logged_in) {
      fetch('http://127.0.0.1:8000/api/current-user/', {
        headers: {
          Authorization: `JWT ${localStorage.getItem('token')}`
        }
      })
        .then(res => res.json())
        .then(json => {
          this.setState({ username: json.username, user_id:json.id });
          if(json.detail)
          {
            localStorage.removeItem('token');
            this.setState({ logged_in: false, username: '' });
          }
          console.log(json)
        });

        fetch('http://127.0.0.1:8000/api/check/', {
        headers: {
          Authorization: `JWT ${localStorage.getItem('token')}`
        }
      })
        .then(res => res.json())
        .then(json => {
          this.setState({ user_type: json.status });
          console.log(this.state);
        });


    }
  }

  handle_login = (e, data) => {
    e.preventDefault();
    fetch('http://127.0.0.1:8000/api/token-auth/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
      .then(res => res.json())
      .then(json => {
        localStorage.setItem('token', json.token);
        console.log(json);
        this.setState({
          logged_in: true,
          username: json.user.username
        });
      });

      fetch('http://127.0.0.1:8000/api/check/', {
        headers: {
          Authorization: `JWT ${localStorage.getItem('token')}`
        }
      })
        .then(res => res.json())
        .then(json => {
          this.setState({ user_type: json.status });
          console.log(this.state);
        });
  };

  handle_logout = () => {
    localStorage.removeItem('token');
    this.setState({ logged_in: false, username: '' });
  };

  handle_signup = (e, data) => {
    e.preventDefault();
    fetch('http://127.0.0.1:8000/api/signup/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
      .then(res => res.json())
      .then(json => {
        localStorage.setItem('token', json.token);
        this.setState({
          logged_in: true,
          displayed_form: '',
          username: json.username
        });
      });
  };
  
  render(){
    return (
    <div>
      
        {/* <Header/> */}
        <Routes handle_login={this.handle_login} 
        handle_signup={this.handle_signup} 
        logged_in={this.state.logged_in} 
        handle_logout={this.handle_logout}
        user_type = {this.state.user_type}
        username = {this.state.username}
        user_id = {this.state.user_id}/>
        <Footer/>
      
    </div>
  );
}

}

export default App;
