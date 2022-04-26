import React from 'react';

const HistoryCard = (props) => {
  const { id, name, address, contact, photo } = props.y;

  return (
    <div className='item' style={{ marginTop: '20px'}}>
      <div className='content'>
        <div className='header'>Name: {name}</div>
        <div>Address: {address}</div>
        <div>Contact: {contact}</div>
        <div>Photo: {photo}</div>
      </div>
        <i
          className='trash alternate outline icon'
          style={{ color: 'red', marginTop: '7px' }}
          onClick={() => props.clickHandler(id)}
        ></i>
      {/* <button onClick={(id) => props.clickHandler(id)}>Delete</button> */}
    </div>
  );
};

export default HistoryCard;
