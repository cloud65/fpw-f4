import React from "react";
import { Card, Pagination, Row, Spinner} from 'react-bootstrap'
import {useHistory, useParams} from "react-router-dom";

import { Request } from './Request'
import CategoryCard from './CategoryCard'

const limit=6;

const Categories=props=> {
    const [responseData, setData] = React.useState({})
    const [loading, setLoading] = React.useState(false)
     
    const history = useHistory();
    const params = useParams();
    
    const data = responseData.results || [];
    const page = Number(params.page || 1);
    const count = responseData.count;
    const pageCount = Math.trunc(count/limit)+1;
    
    React.useEffect(()=>{
        setLoading(true)
        Request(`/categories/?limit=${limit}&offset=${limit*(page-1)}`, (data)=>{setLoading(true); setData(data)})
    }, [params.page])
    
    if (loading) return <Spinner animation="border" role="status"/>
    
    const pages=[];
    for (let number = 1; number <= pageCount; number++) {
        const handleClick=()=>history.push('/category/'+number)
      pages.push(
       <Pagination.Item key={number} active={number === page} 
        onClick={handleClick}>
          {number}
        </Pagination.Item>
      );
    }
    
    
    
    return (
    <Card className='height-100'>
      <Card.Header as="h5">Выберите категорию для просмотра</Card.Header>
      <Card.Body>
        <Row md={3}>
            {data.map(e=><CategoryCard key={e.guid} {...e}/>)}
        </Row>
        <Pagination className='pagination-bottom'>{pages}</Pagination>
      </Card.Body>
    </Card>    
  );
}


export default Categories;