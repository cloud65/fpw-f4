import React from "react";
import { Card, Pagination, Row, Spinner } from 'react-bootstrap'
import {useHistory, useParams, Link} from "react-router-dom";
import { Request } from './Request'

import EdaCard from './EdaCard'

const limit=6;

const EdaList=props=> {
   
    const [responseData, setData] = React.useState({})    
    const [loading, setLoading] = React.useState(false)
    
    const history = useHistory();
    const params = useParams();
    
    const data = responseData.results || [];
    const page = Number(params.page || 1);
    const category = params.category;
    const count = responseData.count;
    const pageCount = Math.trunc(count/limit)+1;
    
    const onLoad=(data)=>{
        setLoading(false); 
        setData(data)
    }
    
    React.useEffect(()=>{ 
        Request(`/eda/?search=${category}&limit=${limit}&offset=${limit*(page-1)}`, onLoad)
    }, [params.page, params.category])
    
    if (loading) return <Spinner animation="border" role="status"/>
  
    const pages=[];
    for (let number = 1; number <= pageCount; number++) {
        const handleClick=()=>history.push('/list/'+number+'/'+params.category)
      pages.push(
       <Pagination.Item key={number} active={number === page} 
        onClick={handleClick}>
          {number}
        </Pagination.Item>
      );
    }
    
    return (
    <Card className='height-100'>
      <Card.Header as="h5">
        Рецепты
      </Card.Header>
      <Card.Body>
        <Card.Title>Выберите рецепт для просмотра</Card.Title>
            <Row md={3}>
                {data.map(e=><EdaCard key={e.guid} {...e}/>)}
            </Row>
        <Pagination className='pagination-bottom'>{pages}</Pagination>
      </Card.Body>
    </Card>    
  );
}


export default EdaList;