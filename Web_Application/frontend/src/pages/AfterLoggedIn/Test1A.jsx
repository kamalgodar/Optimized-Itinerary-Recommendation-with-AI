import React from 'react';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import Login from '../Login/Login';
import useToken from '../../useToken';
import Test0 from '../Test1';

function Test1A() {
    const { token, setToken } = useToken();
  
    if(!token) {
      return <Login setToken={setToken} />
    }
    const theme = createTheme();


  return (
    <Test0/>

  );
}

export default Test1A;
