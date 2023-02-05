import React from "react";
import { Link } from "react-router-dom";

import { Card } from 'react-bootstrap'

const CategoryCard=props=> {
     
    return (
    <Card className='card-height'>
      <Card.Body>
        <Card.Img variant="top" src={"/api/image/"+props.image} />
        <Card.Title><Link to={'/list/1/'+props.guid}>{props.name}</Link></Card.Title>        
      </Card.Body>
    </Card>
  );
}


export default CategoryCard;