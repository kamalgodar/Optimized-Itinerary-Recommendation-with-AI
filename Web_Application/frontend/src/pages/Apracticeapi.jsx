import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Test0() {
  const [posts, setPosts] = useState([]);

  // const apiCall = async () => {
  //   let response = await axios.get('https://randomuser.me/api');
  //   let res = response.data.results;
  //   console.log(res);
  //   setPosts(res);
  //   return res;
  // };

  const apiCall1 = async () => {
    try {
      let response = await axios.get('https://randomuser.me/api');
      console.log(response);
      setPosts(response.data.results);
    } catch (err) {
      console.log(err);
    }
  };

  const apiCall2 = () => {
    return axios.get('https://randomuser.me/api')
      .then(response => {
        console.log(response);
        setPosts(response.data.results);
      })
      .catch(err => {
        console.log(err);
      });
  }

  useEffect( () => {
    apiCall2();
  },[]);
    
  // useEffect( () => { 
  //     async function apiCall3() {
  //       try {
  //         let res = [];
  //         res = await axios.get('https://randomuser.me/api');
  //         console.log(res.data.results);
  //         setPosts(res.data.results);
  //       } catch (err) {
  //         console.log(err);
  //       }
  //     }
  //     apiCall3();
  // }, []);


  return (
    <div>
      Basics: Working with API
      {/* Doesn't work ERROR: Objects are not valid as a React child (found: [object Promise]).
      If you meant to render a collection of children, use an array instead. */}

      {/* {apiCall1()} */}

      {posts.map((post) => (
        <div key={post.login.uuid}>{post.gender}</div>
      ))}

      {/* key required so no error. Error: Every child must have a unique key */}
      {/* key may be the unique value from api */}
      {/* OR, create a index and assign. Example: posts.map((post, index)) */}

    </div>
  );
}

export default Test0;
