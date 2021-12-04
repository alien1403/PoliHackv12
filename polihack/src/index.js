import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import HomePage from './components/HomePage/HomePage';
import ProductPage from './components/ProductPage/ProductPage';
import LoginPage from './components/LoginPage/LoginPage';
import RegisterPage from './components/RegisterPage/RegisterPage';
import ClujPage from './components/cities/Cluj/cluj';
import BucurestiPage from './components/cities/Bucuresti/bucuresti';


ReactDOM.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>

        <Route path="/" element={<App/>}>
          <Route path="home" element={<HomePage/>}></Route>
          <Route path="product" element={<ProductPage/>}></Route>
          <Route path="login" element={<LoginPage/>}></Route>
          <Route path="register" element={<RegisterPage/>}></Route>
          <Route path="product/cluj" element ={<ClujPage/>}></Route>
          <Route path="product/bucuresti" element ={<BucurestiPage/>}></Route>
          
        </Route>

      </Routes>
    </BrowserRouter>
    
  </React.StrictMode>,
  document.getElementById('root')
);

reportWebVitals();
