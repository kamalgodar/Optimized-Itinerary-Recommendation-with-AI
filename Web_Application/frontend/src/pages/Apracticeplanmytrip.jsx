import * as React from 'react';
import { useState } from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import AssignmentIcon from '@mui/icons-material/Assignment';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import InputAdornment from '@mui/material/InputAdornment';

import {Formik, Form, Field} from 'formik';
import {
  MenuItem,
} from '@mui/material';
import {LocalizationProvider} from '@mui/lab';
import AdapterDateFns from '@mui/lab/AdapterDateFns';

import {DateTimePicker} from 'formik-mui-lab';

const luxuries = [
  {
      value: 'economy',
      label: 'Economy',
  },
  {
      value: 'business',
      label: 'Business',
  },
  {
      value: 'first',
      label: 'First',
  },
];

const numbers = [
  {
      value: 'One',
      label: '1',
  },
  {
      value: 'Two',
      label: '2',
  },
  {
      value: 'Three',
      label: '3',
  },
  {
    value: 'Four',
    label: '4',
  },
  {
    value: 'Five',
    label: '5',
  },
];

function Planmytrip() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [luxury, setLuxury] = useState("economy");

  const handleChange = (event) => {
    setLuxury(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    // eslint-disable-next-line no-console
    console.log({
      email: data.get('email'),
      password: data.get('password'),
    });
  };

  return (
    <Formik
    initialValues={{
      tags: [],
      date: new Date(),
      time: new Date(),
      dateTime: new Date(),
    }}
  >
    <LocalizationProvider dateAdapter={AdapterDateFns}>
      <Form>
      <Container component="main" maxWidth="xs">
        <Box
          sx={{
            marginTop: 6,
            marginBottom: 6,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            border: 'blue solid 2px',
          }}
        >
          <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
            <AssignmentIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            Plan My Trip
          </Typography>

          <Box component="form" noValidate onSubmit={handleSubmit} sx={{ mt: 3 }}>
            <Grid container spacing={2}>
            <Grid item xs={12} sm={6}>
                <TextField
                  required
                  fullWidth
                  label="Destination"
                />
              </Grid>
              <Grid item xs={12} sm={6} >
                <TextField
                  required
                  fullWidth
                  label="Places of Interest"
                />
              </Grid>
              <Grid item xs={12} sm={6} >
                <TextField
                  required
                  fullWidth
                  label="Adults"
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <TextField
                  required
                  fullWidth
                  label="Kids"
                />
              </Grid>
              
              <Grid item xs={12} sm={6} >
                <TextField
                  required
                  fullWidth
                  label="Budget"
                  InputProps={{
                    startAdornment: <InputAdornment position="start">NPR</InputAdornment>,
                  }}
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <TextField
                  required
                  fullWidth
                  select
                  label="Luxury Level"
                  value={luxury}
                  onChange={handleChange}
                >
                {luxuries.map((option) => (
                <MenuItem key={option.value} value={option.value}>
                  {option.label}
                </MenuItem>
              ))}
              </TextField>
              </Grid>

              <Grid item>
                <Field
                  component={DateTimePicker}
                  name="dateTime"
                  label="Start Date"
                />
              </Grid>
              <Grid item >
                <Field
                  component={DateTimePicker}
                  name="dateTime"
                  label="End Date"
                />
              </Grid>

            </Grid>
            <Button
              type="submit"
              fullWidth
              variant="contained"
              href="/"
              sx={{ mt: 3 }}
            >
              Plan
            </Button>

          </Box>
        </Box>
      </Container>
      </Form>
      </LocalizationProvider>
    </Formik>
  );
}

export default Planmytrip;