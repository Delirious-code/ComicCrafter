import React, { useEffect, useState } from 'react';

const StoryDisplay = () => {
  const [htmlContent, setHtmlContent] = useState("");

  useEffect(() => {
    // Adjust the URL to match how you serve your static files in Flask
    // If Flask is serving the static folder at /static/story.html, do:
    fetch("http://localhost:5000/static/story.html")
      .then(response => response.text())
      .then(html => setHtmlContent(html))
      .catch(error => console.error("Error fetching story:", error));
  }, []);

  return (
    <div
      className="story-output"
      // We trust our own HTML generation, so it's safe to use dangerouslySetInnerHTML
      dangerouslySetInnerHTML={{ __html: htmlContent }}
    />
  );
};

export default StoryDisplay;
