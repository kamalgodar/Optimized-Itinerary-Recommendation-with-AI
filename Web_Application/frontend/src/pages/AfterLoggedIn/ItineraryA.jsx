import React from 'react';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import Login from '../Login/Login';
import useToken from '../../useToken';
import Itinerary from '../Itinerary';
import HeaderA from '../HeaderA';

function ItineraryA() {
    const { token, setToken } = useToken();
  
    if(!token) {
      return <Login setToken={setToken} />
    }
    const theme = createTheme();


  return (
    <>
    <HeaderA/>
    <Itinerary/>
    </>

  );
}

export default ItineraryA;
