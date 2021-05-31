import {React} from 'react';
import {Accordion,Card,Button} from 'react-bootstrap'
const Hospital=(props)=>
(   
<Accordion>
  <Card>
    <Card.Header>
      <Accordion.Toggle as={Button} variant="link" eventKey="0">
        {props.hospital.name}
      </Accordion.Toggle>
    </Card.Header>
    <Accordion.Collapse eventKey="0">
      <Card.Body>

      <Card>
        <Card.Header>Established-{props.hospital.established_date}</Card.Header>
            <Card.Body>
                <Card.Title>Address</Card.Title>
                    <Card.Text>
                    {props.hospital.address}
                    </Card.Text>
                <Button variant="primary" href={props.hospital.hospital_url} >Go To Hospital Website</Button>
        </Card.Body>
    </Card>
    
    </Card.Body>
    </Accordion.Collapse>
  </Card>
 
</Accordion>
)
export default Hospital;