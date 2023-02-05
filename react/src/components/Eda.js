import React from "react";
import { Link } from "react-router-dom";
import { useParams} from "react-router-dom";
import { Request } from './Request'
import { Card, Nav, Container, Row, Col, Image  } from 'react-bootstrap'

const Eda=props=> {
    const [data, setData] = React.useState({categories: [], ingredients:[], items:[]})
    const params = useParams();
    
    React.useEffect(()=>{ 
        Request(`/eda/${params.page}/`, setData)
    }, [params.page])
     
    const categories = data.categories.map(e=>{
        return <Nav.Item key={e.guid}>
            <Nav.Link as={Link}  to={'/list/1/'+e.guid}>{e.name}</Nav.Link>
        </Nav.Item>
    })
            
    const ingredients = data.ingredients.map(e=>{
        return <Row key={e.ingredient.guid}>
            <Col xs={6}>{e.ingredient.name}</Col>
            <Col xs={6}>{e.count}</Col>
        </Row>
    })
    
    const items = data.items.map(e=>{
        return <Card key={e.guid}>
            <Row>
                <Col xs={5}>
                    <Image src={"/api/image/"+e.guid} fluid/>
                </Col>
                <Col xs={1}/>
                <Col xs={6}>{e.text}</Col>
            </Row>
        </Card>
    }) 
    
            
    console.log(data)
    
    return (
    <Card className='height-100'>
      <Card.Header as="h5">{data.name}</Card.Header>
      <Card.Body>
        <div className='eda-content-owner'>
            <div className='eda-content'>
            <Nav>{categories}</Nav>
            <Card>
              <Card.Header as="h6">Ингридиенты</Card.Header>
              <Card.Body>
              {ingredients}            
              </Card.Body>            
            </Card>
            {items}
        </div></div>
      </Card.Body>
    </Card>
  );
}


export default Eda;