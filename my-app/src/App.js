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
        <a
          className="App-link"
          href="https://www.harvard-rarediseases.org/"
          target="_blank"
          rel="noopener noreferrer"
        >
          Rare Diseases
        </a>
      </header>
    </div>
  );
}

export default App;

