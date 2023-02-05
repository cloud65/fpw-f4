import React from "react";
import {Route, Switch} from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';
import "../styles/App.css";

import {Container, Navbar, Nav} from 'react-bootstrap'
import { Link } from "react-router-dom";

import Categories from './Categories'
import EdaList from './EdaList'
import Eda from './Eda'


const App=props=> {
    
    return (
    <Container fluid="md" className='main-conteiner height-100'>
        <Navbar bg="dark" variant="dark">
            <Container>
              <Navbar.Brand as={Link} to='/'>Главная</Navbar.Brand>             
            </Container>
        </Navbar>
        <Switch>
            <Route path="/category/:page">
                <Categories />
            </Route>
            <Route path="/list/:page/:category">
                <EdaList />
            </Route>
            <Route path="/detail/:page">
                <Eda />
            </Route>
            <Route>
                <Categories />
            </Route>
        </Switch>
    </Container>
  );
}




export default App;