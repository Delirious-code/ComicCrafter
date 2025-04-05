import React, { useState } from "react";
import "./StoryGenerator.css";

const StoryGenerator = () => {
  const [prompt, setPrompt] = useState("");
  const [story, setStory] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!prompt.trim()) {
      setError("Please enter a prompt.");
      return;
    }
    setError("");
    setLoading(true);
    setStory("");

    try {
      const response = await fetch("http://localhost:5000/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt }),
      });
      const data = await response.json();
      if (response.ok && data.story) {
        setStory(data.story);
      } else {
        setError(data.error || "Error generating story.");
      }
    } catch (err) {
      setError("Failed to connect to the server.");
    }
    setLoading(false);
  };

  const handleSave = () => {
    if (!story) return;
    const blob = new Blob([story], { type: "text/html" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "generated_story.html";
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  return (
    <div className="story-generator-container">
      {/* Left Panel: Input Area */}
      <div className="left-panel">
        <h2>Enter Prompt</h2>
        <form onSubmit={handleSubmit}>
          <textarea
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            placeholder="Type your prompt here..."
            rows={10}
            required
          />
          <button type="submit">Generate Story</button>
        </form>
        {error && <p className="error">{error}</p>}
      </div>

      {/* Right Panel: Story Output */}
      <div className="right-panel">
        <h2>Generated Story</h2>
        {loading ? (
          <p>Generating story, please wait...</p>
        ) : (
          <>
            <div
              className="story-output"
              dangerouslySetInnerHTML={{ __html: story }}
            />
            {story && (
              <button onClick={handleSave} style={{ marginTop: "10px" }}>
                Save Story
              </button>
            )}
          </>
        )}
      </div>
    </div>
  );
};

export default StoryGenerator;
