import React,{Component} from 'react';
import Header from './header.js';
import  { Redirect } from 'react-router-dom'


class Book extends  Component{

    constructor(props) {
        super(props);
        this.state = {
          counsellor_id:props.match.params.id,
          counsellor_name:'',
          start_time:'',
          end_time:'',
          entered_time:'',
          redirectToHome: false
        };
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleChange = this.handleChange.bind(this);
      }

      componentDidMount(){
          fetch(`http://127.0.0.1:8000/api/get-counsellor/${this.state.counsellor_id}/`, {
        headers: {
          Authorization: `JWT ${localStorage.getItem('token')}`
        }
      })
        .then(res => res.json())
        .then(json => {
          this.setState({ start_time: json[0].Consultation_start, end_time:json[0].Consultation_end, counsellor_name:json[0].Name });
        //   console.log(this.state);
        });
      }

      handleChange(event){
          this.setState({entered_time:event.target.value});
          
      }

      handleSubmit(event){
        event.preventDefault();
        let data = {"client_key":this.props.extra.user_id,"counsellor_key":this.state.counsellor_id,"Booking_time":this.state.entered_time};

        fetch('http://127.0.0.1:8000/api/book/', {
        method: 'POST',
        headers: {
            Authorization: `JWT ${localStorage.getItem('token')}`,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
        })
        .then(res => res.json())
        .then(json => {
            
            console.log(json);
            alert("Booked Successfully !!");

            this.setState({redirectToHome:true})
            
            
        });
        
    }

    render(){

        if(this.state.redirectToHome==true)
        {
            return <Redirect to='/'/>
        }

		console.log(this.state);


        return(

            <div>
            <Header {...this.props}/>
			
			

        	<div id="main">
            
            <h2>{this.state.counsellor_name} is availaible from {this.state.start_time} to {this.state.end_time}</h2>

            <h3>Please select a time that fits your schedule</h3>

            <centre>Please enter the time in 24-hour format ie. hh:mm</centre>

            <form onSubmit = {this.handleSubmit}>

            <div className = "12u$">
                <label>Booking Time</label>
            <input type = "time" placeholder = "Booking Time" value = {this.state.entered_time} onChange = {this.handleChange} required = {true} />
            
            </div>
            <hr/>
            <input type = "submit" class = "special" value = "Book Now !"/>

            </form>



        	</div>
            </div>

        )

    }


}


export default Book;