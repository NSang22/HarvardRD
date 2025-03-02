import dna from './dna.png';
import './App.css';
import SymptomForm from './SymptomForm';
// import { BrowserRouter, Route, Routes } from 'react-router-dom';


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={dna} className="App-logo" alt="logo" />
        <p>
          <code>StickyGenome</code>
        </p>
        <SymptomForm />
        
      <div style={{ marginTop: '30px' }}>
        <a
          className="App-link"
          href="https://www.harvard-rarediseases.org/"
          target="_blank"
          rel="noopener noreferrer"
        >
          Rare Diseases
        </a>
      </div>
      </header>
    </div>
  );
}

export default App;

