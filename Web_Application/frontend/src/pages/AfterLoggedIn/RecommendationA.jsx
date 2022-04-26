import React from 'react';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import Login from '../Login/Login';
import useToken from '../../useToken';
import HeaderA from '../HeaderA';
import Recommendation from '../Recommendation';

export default function RecommendationA() {
    const { token, setToken } = useToken();
  
    if(!token) {
      return <Login setToken={setToken} />
    }
    const theme = createTheme();


  return (
    
  <Recommendation/>


  );
}


