import sys
import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

# Ensuring the backend can find the text generation module
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from text_gen import generate_story  # Importing the story generation function

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allowing all origins


GENERATED_HTML_FILE = os.path.join(os.path.dirname(__file__), 'static', 'formatted_generated_story.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        if not data or "prompt" not in data:
            return jsonify({"error": "Prompt is required"}), 400

        prompt = data["prompt"].strip()
        if not prompt:
            return jsonify({"error": "Prompt cannot be empty"}), 400

        # Generating the story and save it as an HTML file
        story = generate_story(prompt)
        
        # Saving the generated story as HTML to the static folder
        with open(GENERATED_HTML_FILE, 'w') as html_file:
            html_file.write(story)  

        return jsonify({"story": story})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/generated_story', methods=['GET'])
def serve_generated_story():
    try:
        # Serve the generated HTML file from the static folder
        return send_from_directory(os.path.dirname(GENERATED_HTML_FILE), 'formatted_generated_story.html')
    except Exception as e:
        return jsonify({"error": f"Failed to fetch the generated story: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
