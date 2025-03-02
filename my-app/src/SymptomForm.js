import React, { useState } from 'react';

const SymptomForm = () => {
    const [symptoms, setSymptoms] = useState('');
    const [results, setResults] = useState(null);
  
    const handleSubmit = async (event) => {
      event.preventDefault();
      const symptomList = symptoms.split(',').map(s => s.trim());
      try {
        const response = await fetch('http://127.0.0.1:8000/normalize', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ symptoms: symptomList })
        });
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const result = await response.json();
        setResults(result);
      } catch (error) {
        console.error('Failed to fetch:', error);
      }
    };
  

  return (
    <div>
      <h1>Symptom Normalizer</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="symptoms">Enter symptoms (comma-separated): </label>
        <input
          type="text"
          id="symptoms"
          name="symptoms"
          value={symptoms}
          onChange={(e) => setSymptoms(e.target.value)}
          required
        />
        <button type="submit">Normalize</button>
      </form>
      {results && (
        <div id="results">
          <h2>Results</h2>
          <pre>{JSON.stringify(results, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default SymptomForm;