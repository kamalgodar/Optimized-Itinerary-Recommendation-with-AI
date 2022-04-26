import axios from 'axios';

export default axios.create({
    // baseURL: 'http://localhost:3006/',
    baseURL: 'http://127.0.0.1:8000/',
});