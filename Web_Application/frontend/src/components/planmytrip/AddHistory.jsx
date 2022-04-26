import React, { useState, useEffect } from 'react';
import History from '../components/planmytrip/History';
import AddHistory from '../components/planmytrip/AddHistory';

import { v4 as uuid } from "uuid";
import api from '../api/base';
import HeaderA from './HeaderA';

function AddHistory() {
    // const LOCAL_STORAGE_KEY = "x";
    const [x, setX] = useState([]);

    // Retrieve History
    const retrieveHistory = async () => {
      const response = await api.get("/hotels/");
      return response.data;
    };

    const addHistoryHandlerr = async (y) => {
        console.log(y);
        const request = {
          id: uuid(),
          ...y
        }

        const response = await api.post("/hotels/", request)
        setX([...x, response.data]);
    };

    const removeHistoryHandler = async (id) => {
      await api.delete(`/hotels/${id}`);
      const newHistoryList = x.filter((y) => {
        return y.id !== id;
      });
      
      setX(newHistoryList);
    };

    useEffect(() => {
      // const retriveHistories = JSON.parse(localStorage.getItem(LOCAL_STORAGE_KEY));
      // if (retriveHistories) setX(retriveHistories);
      const getAllHistory = async () => {
        const allHistory = await retrieveHistory();
        if(allHistory) setX(allHistory);
      };
      getAllHistory();
    }, []);
    
    useEffect(() => {
      // localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(x));
    }, [x]);

  return (
    <div>
      <HeaderA/>
      <div className='ui container'>
        <AddHistory addHistoryHandler={addHistoryHandlerr} />
        <History x={x} getHistoryId={removeHistoryHandler} />
      </div>
    </div>
    
  );
}

export default AddHistory;