import React from 'react'

import { Button, Container, Grid, TextField, Typography } from "@mui/material";
import { Box } from "@mui/system";
import { makeStyles } from '@mui/styles';
import { useState, useRef, useCallback } from 'react';

import 'mapbox-gl/dist/mapbox-gl.css'
import 'react-map-gl-geocoder/dist/mapbox-gl-geocoder.css'

import Geocoder from 'react-map-gl-geocoder'

import * as jsondata from '../data/data0'
// import jsondata from '../data/data1.json'

import ReactMapGL, { Marker, Popup } from 'react-map-gl';

const MAPBOX_TOKEN = 'pk.eyJ1Ijoia2FtYWxnb2RhciIsImEiOiJjazVpOGwxbWgwYnllM2ptbm43ajF0ZmQ0In0.f1zLLWQiv7d5tIc-Lu9n0w'

const useStyles = makeStyles({
  root: {
    backgroundColor: 'red',
    color: (props) => props.color,
  },
  cover: {
      padding: 10,
      margin: 10,
      border: 3,
      borderStyle: 'solid',
      borderColor: '#4287f5',
      borderWidth: 5,
  },
});

function Mapbox() {
    const [viewport, setViewport] = useState({
        latitude: 27.682200,
        longitude: 85.323816,
        width: '75vw',
        height: '60vh',
        zoom: 14,
        pitch: 30,
    });

    const [selectedMarker, setSelectedMarker] = useState(null);

    const classes = useStyles();

    const geocoderContainerRef = useRef();
    const mapRef = useRef();
    const handleViewportChange = useCallback(
        (newViewport) => setViewport(newViewport),
        []
    );

    return (
        <Container className={classes.cover}>
            <Box>
                <Grid container>
                    <Grid item style={{ flexGrow:1 }}><Typography variant="h5" style={{ textAlign:'left' }}>Maps</Typography></Grid>
                </Grid>
            </Box>
            <Box>
            {/* <div ref={geocoderContainerRef} style={{ position: "absolute", top: 20, left: 20, zIndex: 1 }} /> */}
                <ReactMapGL
                    ref={mapRef}
                    {...viewport}
                    mapStyle={'mapbox://styles/kamalgodar/ckz5h5lys00h215ldob7bu2fc'}
                    mapboxApiAccessToken='pk.eyJ1Ijoia2FtYWxnb2RhciIsImEiOiJjazVpOGwxbWgwYnllM2ptbm43ajF0ZmQ0In0.f1zLLWQiv7d5tIc-Lu9n0w'
                    onViewportChange={(viewport) => {
                        setViewport(viewport);
                    }}
                >
                    <Geocoder
                        mapRef={mapRef}
                        containerRef={geocoderContainerRef}
                        onViewportChange={handleViewportChange}
                        mapboxApiAccessToken={MAPBOX_TOKEN}
                        position="top-left"
                    />

                    {jsondata.hotel.map((x, index) => (
                        <Marker key={x.id} latitude={x.coordinats[0]} longitude={x.coordinats[1]} offsetTop={-(viewport.zoom*2)/2}>
                            <Button onClick={(e) => {
                                e.preventDefault();
                                setSelectedMarker(x);
                            }}>
                            <img src='/images/redmarker.png'
                                width={viewport.zoom * 2}
                                height={viewport.zoom * 2}
                            />
                            </Button>
                            
                        </Marker>
                    ))}
                    {selectedMarker && <Popup latitude={selectedMarker.coordinats[0]} longitude={selectedMarker.coordinats[1]} onClose={()=>{setSelectedMarker(null);}}>
                        <Box>
                            <h4>{selectedMarker.name}</h4>
                            <h5>{selectedMarker.Contact}</h5>
                            <h5>{selectedMarker.location}</h5>
                        </Box>
                    </Popup>}

                </ReactMapGL>
            </Box>
            
        </Container>
    )
}

function Test() {
    const classes = useStyles();
    return (
        <div>
            This is a test page.
            <Mapbox />
        </div>
    )
}

export default Test;
