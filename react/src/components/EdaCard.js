import React from "react";
import { Link } from "react-router-dom";

import { Card, Button } from 'react-bootstrap'

const EdaCard=props=> {
    return (
    <Card>
      <Card.Body>
        <Card.Title><Link to={'/detail/'+props.guid}>{props.name}</Link></Card.Title>
        <Card.Body className>
        {
            props.categories.map(e=>{
                return <div key={e.guid}>
                    <Link to={'/list/1/'+e.guid}>{e.name}</Link>
                </div>
            })
        }

        </Card.Body>
        <Card.Img variant="bottom" src={"/api/image/"+props.image} />        
      </Card.Body>
    </Card>
  );
}


export default EdaCard;