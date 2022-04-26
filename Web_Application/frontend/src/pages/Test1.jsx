import React, { useEffect } from 'react'

import { Button, Container, Grid, TextField, Typography } from "@mui/material";
import { Box } from "@mui/system";
import { makeStyles } from '@mui/styles';
import { useState, useRef, useCallback } from 'react';

import axios from 'axios';

import 'mapbox-gl/dist/mapbox-gl.css'
import 'react-map-gl-geocoder/dist/mapbox-gl-geocoder.css'

import Geocoder from 'react-map-gl-geocoder'

import * as jsondata from '../data/data0'
import * as jsondata2 from '../data/data2'
// import jsondata1 from '../data/response.json'

import ReactMapGL, { Marker, Popup } from 'react-map-gl';
import { Source, Layer } from 'react-map-gl';
import { GeolocateControl, geolocateStyle } from 'react-map-gl';

import Currentlocation from '../components/Currentlocation';
import HeaderA from './HeaderA';

const MAPBOX_TOKEN = 'pk.eyJ1Ijoia2FtYWxnb2RhciIsImEiOiJjazVpOGwxbWgwYnllM2ptbm43ajF0ZmQ0In0.f1zLLWQiv7d5tIc-Lu9n0w'

const useStyles = makeStyles({
  root: {
    backgroundColor: 'red',
    color: (props) => props.color,
  },
  cover: {
      padding: 10,
      margin: 10,
    //   border: 5,
    //   borderStyle: 'solid',
    //   borderColor: '#4287f5',
    //   borderWidth: 2,
  },
});

function Test0() {

    const classes = useStyles();

    const [selectedMarker, setSelectedMarker] = useState(null);

    const [starting, setStarting] = useState([]); //start place
    const [destination, setDestination] = useState([]); //destination place

    const [userLocation, setUserLocation] = useState({});
    const location = Currentlocation();
    var lat = Number(location.coordinates.lat);
    var long = Number(location.coordinates.lng);

    const [startlat, setStartlat] = useState(lat);
    const [startlong, setStartlong] = useState(long);
    const [destlat, setDestlat] = useState(0);
    const [destlong, setDestlong] = useState(0);

    const [coordinatevalue, setCoordinatevalue] = useState([]);

    const [fromapi, setFromapi] = useState([]);

    const [viewport, setViewport] = useState({
        latitude: 27.682200,
        longitude: 85.323816,
        width: '75vw',
        height: '70vh',
        zoom: 14,
        pitch: 30,
    });

    const handleSubmit = (e) => {
        e.preventDefault();
        mapboxGeocode();
        mapboxGeocode2();
        getCoordinates();
        apiCall2();
    };

    const mapboxGeocode = async () => {
        let response = await axios.get(`https://api.mapbox.com/geocoding/v5/mapbox.places/${starting}.json?access_token=pk.eyJ1IjoicmFuamFuNDM1IiwiYSI6ImNrNWIzdnNqeTE2ZjgzZG82OG40aG82ejcifQ.nrFTVyOERu6YhgS66Gxr8A`);
        console.log(response.data.features[0].geometry.coordinates);
        setStartlong(response.data.features[0].geometry.coordinates[0]);
        setStartlat(response.data.features[0].geometry.coordinates[1]);
    };

    const mapboxGeocode2 = async () => {
        let response = await axios.get(`https://api.mapbox.com/geocoding/v5/mapbox.places/${destination}.json?access_token=pk.eyJ1IjoicmFuamFuNDM1IiwiYSI6ImNrNWIzdnNqeTE2ZjgzZG82OG40aG82ejcifQ.nrFTVyOERu6YhgS66Gxr8A`);
        console.log(response.data.features[0].geometry.coordinates);
        setDestlong(response.data.features[0].geometry.coordinates[0]);
        setDestlat(response.data.features[0].geometry.coordinates[1]);
    };

    const getCoordinates = async () => {
        let response = await axios.get(`https://api.mapbox.com/directions/v5/mapbox/driving/${long},${lat};${destlong},${destlat}?geometries=geojson&access_token=pk.eyJ1IjoicmFuamFuNDM1IiwiYSI6ImNrNWIzdnNqeTE2ZjgzZG82OG40aG82ejcifQ.nrFTVyOERu6YhgS66Gxr8A`);
        let data = response.data.routes[0].geometry.coordinates;
        console.log(data);
        let data1 = JSON.stringify(data);
        console.log(data1);
        setCoordinatevalue(data);
      };

    // points is an array of [[long, lat],[long, lat]]
    // const coordinates = [[85.320351,27.694653],[85.317555,27.690084],[85.316131,27.688521],[85.318615,27.684670],[85.318749,27.683173],[85.319566,27.682085],[85.320894,27.682750]];\

    const geocoderContainerRef = useRef();
    const mapRef = useRef();
    const handleViewportChange = useCallback(
        (newViewport) => setViewport(newViewport),
        []
    );

    const apiCall2 = async () => {
        try {
            let response = await axios.get('http://127.0.0.1:8000/api/itinerary/1');
            console.log(response.data);
            setFromapi(response.data);
        } catch (err) {
            console.log(err);
        }
    };

    useEffect( () => {
        apiCall2();
        mapboxGeocode();
        mapboxGeocode2();
        getCoordinates();
    },[]);

    const dataOne = {
        type: "Feature",
        properties: {},
        geometry: {
            type: "LineString",
            coordinates: coordinatevalue
        }
    };
    
    return (
      <div>
        <HeaderA/> 
        <Container className={classes.cover}>
            <Box>
                <Grid container>
                    <Grid item style={{ flexGrow:1 }}><Typography variant="h5" style={{ textAlign:'left' }}>Maps</Typography></Grid>
                </Grid>
            </Box>
            <Box>
                <Grid container>
                    <Grid item xs={9}>
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
                            position="top-right"
                        />

                        {/* -ve indicates left and up */}
                        {jsondata.hotel.map((x, index) => (
                            <Marker key={x.id} latitude={x.coordinats[0]} longitude={x.coordinats[1]} offsetTop={-(viewport.zoom*2)} offsetLeft={-(viewport.zoom*2)}>
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
                            </Box>
                        </Popup>}

                        <Marker latitude={Number(location.coordinates.lat)} longitude={Number(location.coordinates.lng)} offsetTop={-(viewport.zoom*2)} offsetLeft={-(viewport.zoom*2)}>
                            <img src='/images/bluemarker.png'
                                        width={viewport.zoom * 2}
                                        height={viewport.zoom * 2}
                                    />
                        </Marker>

                        <Source id="polylineLayer" type="geojson" data={dataOne}>
                            <Layer
                              id="lineLayer"
                              type="line"
                              source="my-data"
                              layout={{
                                "line-join": "round",
                                "line-cap": "round"
                              }}
                              paint={{
                                "line-color": "rgba(255, 0, 0, 0.8)",
                                "line-width": 5
                              }}
                            />
                        </Source>  
                        </ReactMapGL>
                    </Grid>
                </Grid>
                
            </Box>

            <Box >
                <form className='ui form' onSubmit={e => {handleSubmit(e)}}>
                    <div className='field' style={{margin:5}}>
                    <label>Starting Point</label>
                        <input 
                        type="text"
                        name="name"
                        placeholder="Starting Point"
                        value={starting}
                        onChange={(e) => setStarting(e.target.value)}
                        />
                    </div>
                    <div className='field' style={{margin:5}}>
                        <label>Destination Point</label>
                        <input 
                        type="text"
                        name="name"
                        placeholder="Destination Point"
                        value={destination}
                        onChange={(e) => setDestination(e.target.value)}
                        />
                    </div>

                    <div>
                        {
                            location.loaded 
                            ? JSON.stringify(location)
                            : "Location data unavailable"
                        }
                    </div>
                    <button type='submit'>Enter</button>
                </form>
            </Box>

        </Container>
      </div>
    )
}

export default Test0;
