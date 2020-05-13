import React,{Component} from 'react';
import Header from './header.js';



class Faqs extends  Component{

    render(){

        

		console.log(this.props);


        return(

            <div>
            <Header {...this.props}/>
			
			

        	<div id="main">

            <h2>Under Construction</h2>



        	</div>
            </div>

        )

    }


}


export default Faqs;