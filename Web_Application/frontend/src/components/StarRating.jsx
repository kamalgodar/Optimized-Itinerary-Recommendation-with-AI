import React from 'react';
import { FaStar } from 'react-icons/fa';
import { useState } from 'react';

export default function StarRating() {
    const [rating, setRating] = useState([null]);
    const [hover, setHover] = useState([null]);

  return (
    <div>
        {[ ...Array(5)].map((star ,i) => {
            const ratingValue = i + 1;

            return (
                <label>
                    <input 
                    type='radio' 
                    name='rating' 
                    value={ratingValue} 
                    onClick={() => setRating(ratingValue)}
                     />
                    <FaStar 
                    className='star' 
                    color={ratingValue <= (hover || rating) ? "#ffc107" : "#d1d1c7" } 
                    size={ 20 }
                    onMouseEnter={() => setHover(ratingValue)}
                    onMouseLeave={() => setHover(null)}
                    />
                    {console.log(rating)}
                </label>
            );
        })}
        
    </div>
  )
}
