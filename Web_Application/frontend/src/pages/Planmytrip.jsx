import React, { Component } from 'react';
import Avatar from '@mui/material/Avatar';
import AssignmentIcon from '@mui/icons-material/Assignment';

import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';

import {Formik, Form, Field} from 'formik';
import {
  MenuItem,
} from '@mui/material';
import {LocalizationProvider} from '@mui/lab';
import AdapterDateFns from '@mui/lab/AdapterDateFns';

import {DateTimePicker, DatePicker} from 'formik-mui-lab';

class Planmytrip extends Component {
    state = {
      destination: "",
      placeofinterest: "",
      adults: "",
      kids: "",
      budget: "",
    };

    handleSubmit = (e) => {
        e.preventDefault();
        if (this.state.destination === "" || this.state.adults === "" || this.state.kids === "" || this.state.budget === "") {
            alert("All the fields are mandatory.");
            return;
        }
        this.props.addHistoryHandler(this.state);
        this.setState({destination:"", placeofinterest:"", adults:"", kids:"", budget:""});
    };

  render() {
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
        <Box
          sx={{
            marginTop: 6,
            marginBottom: 6,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            // border: 'blue solid 1px',
          }}
        >
          <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
            <AssignmentIcon />
          </Avatar>
          <h2>Plan My Trip</h2>
          <form className="ui form" onSubmit={this.handleSubmit}>
            <Box style={{ height:400, width:500}}>
              <Grid container spacing={2}>
                <Grid item xs={12} sm={6}>
                  <div className="field">
                    <label>Destination</label>
                    <input
                      type="text"
                      name="name"
                      placeholder="Destination"
                      value={this.state.destination}
                      onChange={(e) => this.setState({ destination: e.target.value })}
                    />
                  </div>
                </Grid>

                <Grid item xs={12} sm={6}>
                  <div className="field">
                    <label>Place of Interest</label>
                    <input
                      type="text"
                      name="name"
                      placeholder="Place of Interest"
                      value={this.state.placeofinterest}
                      onChange={(e) => this.setState({ placeofinterest: e.target.value })}
                    />
                  </div>
                </Grid>

                <Grid item xs={12} sm={6}>
                  <div className="field">
                    <label>Adults</label>
                    <input
                      type="text"
                      name="name"
                      placeholder="Adults"
                      value={this.state.adults}
                      onChange={(e) => this.setState({ adults: e.target.value })}
                    />
                  </div>
                </Grid>

                <Grid item xs={12} sm={6}>
                  <div className="field">
                    <label>Kids</label>
                    <input
                      type="text"
                      name="name"
                      placeholder="Kids"
                      value={this.state.kids}
                      onChange={(e) => this.setState({ kids: e.target.value })}
                    />
                  </div>
                </Grid>
                
                <Grid item xs={12} sm={12}>
                  <div className="field">
                    <label>Budget</label>
                    <input
                      type="text"
                      name="name"
                      placeholder="Budget"
                      value={this.state.budget}
                      onChange={(e) => this.setState({ budget: e.target.value })}
                    />
                  </div>
                </Grid>

                <Grid item xs={12} sm={6}>
                  <div className="field">
                    <label>Start Date</label>
                    <Field
                      component={DateTimePicker}
                      name="dateTime"
                      // label="Start Date"
                    />
                  </div>
                </Grid>
                
                <Grid item xs={12} sm={6}>
                  <div className="field">
                    <label>End Date</label>
                    <Field
                      component={DatePicker}
                      name="date"
                      // label="End Date"
                    />
                  </div>
                </Grid>
              </Grid>

              <Button className="ui button blue" style={{marginTop:30}}>Plan</Button>

            </Box>
          </form>
        </Box>
        </LocalizationProvider>
      </Formik>
      );
  }
}

export default Planmytrip;
