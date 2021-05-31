import  {ListGroup} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import React from 'react';
import Hospital from './hospital/hospital';
import axios from 'axios';

export default class App extends React.Component {

  constructor(){
    super();
    this.state=
      {
        list_of_hosp:[]
      }
  }

  async componentDidMount()
  {    
    const data=await axios.get('http://127.0.0.1:8000/hospitals/');  
    this.setState({list_of_hosp:data.data});    
  }
   
  render()
  {
    
  return (    
      this.state.list_of_hosp.map(hospital=>
        (
        <React.Fragment>
          <ListGroup>
          <ListGroup.Item><Hospital hospital={hospital}/></ListGroup.Item>
          </ListGroup>
        </React.Fragment>   
        )
      ))
    }                   
}


