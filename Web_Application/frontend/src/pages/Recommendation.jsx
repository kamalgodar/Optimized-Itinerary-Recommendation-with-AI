import React from 'react'
import CardComponent from '../components/Card'

import { Button, Container, Grid, TextField, Typography } from "@mui/material";
import { Box } from "@mui/system";
import { makeStyles } from '@mui/styles';
import { useState, useRef, useCallback } from 'react';
import { useEffect } from 'react';
import axios from 'axios';
import users from './data';
import HeaderA from './HeaderA';
import api from '../api/base';

const useStyles = makeStyles({
  root: {
    backgroundColor: 'red',
    color: (props) => props.color,
  },
  cover: {
      padding: 10,
      margin: 10,
      border: 5,
      borderStyle: 'solid',
      borderColor: '#4287f5',
      borderWidth: 2,
  },
});

export default function Recommendation(props) {
  const classes = useStyles();
    const [search1, setSearch1] = useState(['Swayambhu']);
    const [posts, setPosts] = useState([]);

    const apiCall1 = async () => {
      try {
        let response = await api.get(`/api/places/recommend/${search1}`);
        console.log(response.data);
        setPosts(response.data);
      } catch (err) {
        console.log(err);
      }
    };

    const getData = (data) => {
      console.log(data[0]);
      console.log(data[1]);
      console.log(data[2]);

      const bodycontent = {
        'rating': data[0],
        'user_id': data[1],
        'place_id': data[2]
      };

      axios
      .post('http://127.0.0.1:8000/api/rating/', bodycontent)
      .then(response => {
        console.log(response)
      })
      .catch(error => {
        console.log(error.response)
      })
    }
    
    useEffect( () => {
      apiCall1();
    },[]);

    const handleSubmit = (e) => {
      e.preventDefault();
      apiCall1();
  };

    return (
      <>
      <HeaderA/>
        <Container className={classes.cover}>
            <h3>Content Recommendation</h3>
            <form className='ui form' onSubmit={e => {handleSubmit(e)}}>
                <div className='field' style={{margin:5}}>
                    <input 
                    type="text"
                    name="name"
                    placeholder="Search.."
                    value={search1}
                    onChange={(e) => setSearch1(e.target.value)}
                    />
                    <button style={{margin:5}} type='submit'> Search </button>
                </div>
            </form>
            <Box >
                
                <Grid container spacing={3} justifyContent="center">
                    {posts.map((cheq) => (
                        <Grid item lg={3} md ={6} sm={6}> <CardComponent onSubmit={getData} id={cheq.id} title={cheq.name} description={cheq.description} photo={cheq.photo} rating={cheq.avg_rating}/> </Grid>
                    ))}
                </Grid>
            </Box> 
        </Container>
        </>
    )
}

