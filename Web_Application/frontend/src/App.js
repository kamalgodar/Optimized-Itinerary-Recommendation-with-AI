import './App.css';
import Home from './pages/Home';
import Header from './components/Header';
import { createTheme, ThemeProvider } from '@mui/material/styles';

import { BrowserRouter, Route, Routes } from 'react-router-dom';
import PlanmytripA from './pages/AfterLoggedIn/PlanmytripA';
import ItineraryA from './pages/AfterLoggedIn/ItineraryA';
import Test1A from './pages/AfterLoggedIn/Test1A';
import Signup from './pages/Signup';
import Homecheck from './pages/Homecheck';
import LoginA from './pages/AfterLoggedIn/LoginA';
import Logout from './pages/Logout';
import RecommendationA from './pages/AfterLoggedIn/RecommendationA';

function App() {

  const theme = createTheme();
  return (
    <BrowserRouter>
    <ThemeProvider theme={theme}>
      <div className="App">

        <Routes>
          <Route exact path="/" element={<Homecheck />}></Route>
          <Route exact path="/recommendation" element={<RecommendationA />}></Route>
          <Route exact path="/planmytrip" element={<PlanmytripA />}></Route>
          <Route exact path="/itinerary" element={<ItineraryA />}></Route>
          <Route exact path="/login" element={<LoginA />}></Route>
          <Route exact path="/signup" element={<Signup />}></Route>
          <Route exact path="/test1" element={<Test1A />}></Route>
          <Route exact path="/logout" element={<Logout />}></Route>

        </Routes>

      </div>
    </ThemeProvider>
      
    </BrowserRouter>
  );
}

export default App;
