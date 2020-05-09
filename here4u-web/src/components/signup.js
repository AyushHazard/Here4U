import React,{Component} from 'react';
import ReactDOM from 'react-dom';



class SignUp extends  Component{

     
    
    constructor(props){
        super(props);
        this.state = {username: '', password: '', password2: ''};

        this.handleChangeUsername = this.handleChangeUsername.bind(this);
        this.handleChangePassword = this.handleChangePassword.bind(this);
        this.handleConfirmPassword = this.handleConfirmPassword.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleReset = this.handleReset.bind(this);
    }

    handleChangeUsername(event) {
        this.setState({username: event.target.value});
      }
    
      handleChangePassword(event) {
        this.setState({password: event.target.value});
      }

      handleConfirmPassword(event) {
        this.setState({password2: event.target.value});
      }  

    handleSubmit(event){

        
        event.preventDefault();
        // const element
        if(this.state.password==this.state.password2){
            console.log(this.state.username)
        console.log(this.state.password)
        console.log(this.state.password2)
        this.setState({username: '',password: '',password2: ''});
        }
        else
        {
            console.log(this.state.password.length)
            alert('The passwords do not match !!!')
        }
        // ReactDOM.render({{"Hey"}}, document.getElementById('problem-description');)
        
    }

    handleReset(event){
        this.setState({username: '',password: '', password2: ''});
    }


    render(){
        return(

        	<div id="main">

            <header className="major">
                <h2>Sign up !!</h2>
                
            </header>
            <form onSubmit = {this.handleSubmit} onReset = {this.handleReset}>

            <div className = "12u$">
            <input type = "text" placeholder = "Set Username" value = {this.state.username} onChange = {this.handleChangeUsername} required = {true}/>
            </div>

            <div className = "12u$">
                <p>{"\n"}</p>
            <input type = "password" placeholder = "Set Password" value = {this.state.password} onChange = {this.handleChangePassword} required = {true}/>
            </div>

            <div className = "12u$">
                <p>{"\n"}</p>
            <input type = "password" placeholder = "Confirm Password" value = {this.state.password2} onChange = {this.handleConfirmPassword} required = {true}/>
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

        )

    }


}


export default SignUp;