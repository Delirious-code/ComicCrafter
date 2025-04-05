import React from 'react';

const StoryFrame = () => {
  return (
    <div style={{ width: '100%', height: '100%' }}>
      <iframe 
        src="http://localhost:5000/static/story.html"
        style={{ width: '100%', height: '100%', border: 'none' }}
        title="Generated Story"
      />
    </div>
  );
};

export default StoryFrame;
