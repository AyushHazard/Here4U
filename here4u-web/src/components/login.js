import React,{Component} from 'react';
import ReactDOM from 'react-dom';
import { withRouter } from 'react-router-dom'
import PropTypes from 'prop-types';
import Header from './header.js';

class Login extends  Component{

     
    
    constructor(props){
        super(props);
        console.log(this.props)
        this.state = {username: '', password: ''};

        this.handleChangeUsername = this.handleChangeUsername.bind(this);
        this.handleChangePassword = this.handleChangePassword.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleReset = this.handleReset.bind(this);
    }

   

    handleChangeUsername(event) {
        this.setState({username: event.target.value});
      }
    
      handleChangePassword(event) {
        this.setState({password: event.target.value});
      }

    handleSubmit(event){

        console.log(this.props.extra);
        
        event.preventDefault();
        // const element
        console.log(this.state)
        this.props.extra.handle_login(event,this.state);
        // console.log(this.state.password)
        // ReactDOM.render({{"Hey"}}, document.getElementById('problem-description');)
        this.setState({username: '',password: ''});
    }

    handleReset(event){
        this.setState({username: '',password: ''});
    }


    render(){

        

		


        return(

            <div>
            <Header {...this.props}/>

        	<div id="main">

            <header className="major">
                <h2>Log in</h2>
                
            </header>
            <form onSubmit = {this.handleSubmit} onReset = {this.handleReset}>

            <div className = "12u$">
                <label>Username</label>
            <input type = "text" placeholder = "Username" value = {this.state.username} onChange = {this.handleChangeUsername} required = {true}/>
            </div>

            <div className = "12u$">
                <p>{"\n"}</p>
                <label>Password</label>
            <input type = "password" placeholder = "Password" value = {this.state.password} onChange = {this.handleChangePassword} required = {true}/>
            </div>
            
            <div className="12u$">
            <p>{"\n"}</p>
				<ul className="actions">
					
					<li><input type="submit" value="Submit" className="special" /></li>
					<li><input type="reset" value="Reset" /></li>
					
					
				</ul>
			</div>



            </form>


        	</div>
            </div>

        )

    }


}


export default Login;