import ollama
import re
import os

# 🔹 Function to Generate Story from Mistral
def generate_story(prompt, max_length=1000):
    """
    Generate a story using Mistral via Ollama and format it in HTML.
    This function assumes that Ollama is running and that your Mistral model is available.
    """
    try:
        if not prompt.strip():
            return "Error: Prompt cannot be empty."
        
        print(f"Generating story for prompt: {prompt}")
        html_prompt = (
            f"{prompt}\n\n"
            "Write a long, detailed, and immersive story in HTML format. "
            "Wrap the title in <h1> tags and each paragraph in <p> tags. "
            "Give dialogues to characters within inverted commas, but keep the narration plain. "
            "Keep the text below 1000 words. "
            "Do not include any extra text outside of the HTML structure."
        )

        response = ollama.chat(
            model="mistral",
            messages=[{"role": "user", "content": html_prompt}],
            options={'num_predict': max_length}
        )
        
        story = response["message"]["content"]
        print("Generated Story (first 500 chars):\n", story[:500])
        
        # Remove Markdown-style backticks if present
        story = re.sub(r"^```html\s*", "", story.strip())
        story = re.sub(r"```$", "", story.strip())
        
        return story
    except Exception as e:
        print(f"Error during generation: {e}")
        return f"Error: {e}"

# 🔹 Format Story into Beautiful HTML
def format_story_for_site(story):
    """Extract title and paragraphs and build styled HTML (no images)."""
    
    # Extract Title (First <h1>)
    title_match = re.search(r"<h1>(.*?)<\/h1>", story, re.IGNORECASE)
    title = title_match.group(1) if title_match else "Generated Story"
    
    # Extract Paragraphs
    paragraphs = re.findall(r"<p>(.*?)<\/p>", story, re.IGNORECASE)
    
    # Build HTML Content
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        html, body {{
            height: 100%;
            font-family: 'Arial', sans-serif;
            background-color:rgb(6, 16, 43) !important;
            color: #e0e0e0 !important;
            max-width: 800px;
            margin: 0 auto;
            padding: 40px 20px;
            line-height: 1.6;
            text-align: center;
        }}
        .story-container {{
            text-align: left;
            padding: 20px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(3, 218, 198, 0.3);
            white-space: pre-line;
        }}
        h1 {{
            color: #03DAC6;
            font-size: 2.5em;
            margin-bottom: 15px;
        }}
        .comic-image {{
            width: 100%;
            max-width: 600px;
            margin: 15px 0;
            border-radius: 8px;
            box-shadow: 0px 4px 10px rgba(255, 255, 255, 0.2);
        }}
    </style>
</head>
<body>
    <h1>{title}</h1>
    <div class="story-container">"""

    for paragraph in paragraphs:
        html_content += f"\n        <p>{paragraph}</p>"

    html_content += "\n    </div>\n</body>\n</html>"

    return html_content

# 🔹 Save Story to HTML File
def save_story_html(html_story, save_dir="outputs", filename="story.html"):
    """Save the HTML story to disk."""
    try:
        os.makedirs(save_dir, exist_ok=True)
        path = os.path.join(save_dir, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html_story)
        print(f"Saved story to: {path}")
        return path
    except Exception as e:
        print(f"Save error: {e}")
        return None
