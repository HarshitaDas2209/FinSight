import React from 'react'
import Navigation from './components/Navigation'
import Forecasting from './components/Forecasting'
import Planning from './components/Planning'
import Reports from './components/Reports'
import MarketInsights from './components/MarketInsights'
// import Navbar from './components/Navbar'


import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

const App = () => {
  return (
    <div className="App">
    <div>

     

      <Router>
     
        <Routes>
          <Route path="/" element={<Navigation/>} />

          <Route path="/Forecasting" element={<Forecasting />} />

          <Route path="/Planning" element={<Planning />} />
          <Route path="/Reports" element={<Reports />} />

          <Route path="/MarketInsights" element={<MarketInsights />} />
        </Routes>
      </Router>
    </div>
  </div>
  )
}

export default App
