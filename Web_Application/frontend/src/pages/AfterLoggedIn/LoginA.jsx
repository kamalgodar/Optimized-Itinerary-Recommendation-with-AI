import React from 'react';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import Login from '../Login/Login';
import useToken from '../../useToken';
import Test2 from '../HomeA';

function LoginA() {
    const { token, setToken } = useToken();
  
    if(!token) {
      return <Login setToken={setToken} />
    }
    const theme = createTheme();


  return (
    
    <Test2/>

  );
}

export default LoginA;
