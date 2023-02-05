import axios from 'axios';

export const Request = (url, callback)=> {
    axios({
          method: 'get',
          url: '/api'+url,
    })
    .then(response=> {
        callback(response.data)
    })
    .catch(err=>{
        callback(null)        
    })
  } 
