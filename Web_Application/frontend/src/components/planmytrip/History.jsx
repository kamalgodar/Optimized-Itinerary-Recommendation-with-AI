import React, { useState } from 'react';
import HistoryCard from './HistoryCard';

const History = (props) => {
  console.log(props);
  const deleteHistoryHandler = (id) => {
    props.getHistoryId(id);
  };

  const renderHistory = props.x.map((y) => {
    return (
      <HistoryCard y={y} clickHandler={deleteHistoryHandler} key={y.id} />
    );
  });

  return (
    <div className='ui celled list'>
        <h2>Histories:</h2>
      {renderHistory}
    </div>
    );
};

export default History;
