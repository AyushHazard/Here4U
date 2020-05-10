import React,{Component} from 'react';
import ReactDOM from 'react-dom';



class Talk extends  Component{

     
    
    constructor(props){
        super(props);
        this.state = {value: ''};

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleReset = this.handleReset.bind(this);
    }

    handleChange(event) {
        this.setState({value: event.target.value});
      }

    handleSubmit(event){

        alert('Description Submitted !!');
        event.preventDefault();
        // const element
        console.log(this.state.value)
        // ReactDOM.render({{"Hey"}}, document.getElementById('problem-description');)
        this.setState({value: ''});
    }

    handleReset(event){
        this.setState({value: ''});
    }


    render(){
        return(

        	<div id="main">

            <header className="major">
                <h1>Talk to a counsellor</h1>
                <h4>Please describe how you feel briefly. =) </h4>
            </header>
            <form onSubmit = {this.handleSubmit} onReset = {this.handleReset}>

            <div className = "12u$">
            <textarea id = 'problem-description' placeholder='Write your heart out !!' required = {true} onChange={this.handleChange} value = {this.state.value} rows = "6"></textarea>
            </div>
            
            <div className="12u$">
            <p>{"\n"}</p>
				<ul className="actions">
					
					<li><input type="submit" value="Submit" className="special" /></li>
					<li><input type="reset" value="Reset" /></li>
					<li>
						
						<input id = "extra_data" type="file" name="extra_data"/>
					</li>
					
				</ul>
			</div>



            </form>


        	</div>

        )

    }


}


export default Talk;