import React from 'react'
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import { Grid } from '@mui/material';
import { useState } from 'react';
import StarRating from './StarRating';

function ReadMore({ children, maxCharacterCount = 100}) {
  const text = children;
  const [isTruncated, setIsTruncated] = useState(true)
  const resultString = isTruncated ? text.slice(0, 100) : text ;

  function toggleIsTruncated(){
    setIsTruncated(!isTruncated)
  }

  return (
    <p>{resultString}<span style={{ color: '#e35930' }} onClick={toggleIsTruncated}>{isTruncated ? "Read More" : "Read Less"}</span></p>
  );
}
  
function CardComponent(props) {

  const [rate, setRate] = useState("");

  const [userid, setUserid] = useState(1);

  const handleSubmit = (e) => {
    e.preventDefault();
    props.onSubmit([rate, userid, props.id]);
  }

    return (
        <div>
          <form onSubmit={e => {handleSubmit(e)}}>
          <Card elevation={3} sx={{ maxWidth: 300 }}>
                <CardMedia
                    component="img"
                    height="200"
                    image= {`http://127.0.0.1:8000${props.photo}`}
                />
                <CardContent>
                  <Typography gutterBottom variant="h5" component="div">
                    {props.title}
                    {props.id}
                  </Typography>
                  {/* <Typography gutterBottom variant="h7" component="div">
                    Address
                  </Typography> */}
                  <Typography variant="body2" color="text.secondary">
                    <ReadMore>
                    {props.description}
                    </ReadMore>
                  </Typography>
                </CardContent>
                <CardActions>
                  <Grid container>
                    <Grid item style={{paddingRight: 20}}>
                      <Button size="small" variant='contained' color='success' >Rating {props.rating}</Button>
                    </Grid>
                    <Grid item style={{marginTop: 0}}>
                      <StarRating />
                    </Grid>
                    <Grid item style={{ marginTop: 10, paddingRight: 20, marginBottom:10 }}> 
                      <Button size="small" variant='contained'>Favourite</Button>
                    </Grid>

                    <Grid container>
                      <Grid item xs={2}>
                        <label>Rate</label>
                      </Grid>
                      <Grid item xs={7}>
                        <input
                          type='text'
                          name='rate'
                          placeholder=""
                          value={rate}
                          onChange={e => setRate(e.target.value)}
                        />
                      </Grid>
                      <Grid item xs={3}>
                        <button type='submit'>Enter</button>
                      </Grid>

                    </Grid>
                  </Grid>
                  
                </CardActions>
            </Card>

          </form>
            
        </div>
    );
}

export default CardComponent;