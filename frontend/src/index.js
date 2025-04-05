import React from 'react';
import ReactDOM from 'react-dom/client';
import StoryGenerator from './components/StoryGenerator';

const container = document.getElementById('root');
const root = ReactDOM.createRoot(container);
root.render(
  <React.StrictMode>
    <StoryGenerator />
  </React.StrictMode>
);
