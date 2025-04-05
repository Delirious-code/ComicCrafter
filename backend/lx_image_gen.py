import os
import torch
from diffusers import StableDiffusionPipeline
from PIL import Image


MODEL_PATH = "/Users/apple/stable-diffusion-webui/models/Stable-diffusion/comicDiffusion_v2_diffusers/"
SAVE_DIR = "/Users/apple/Desktop/NLP Run/ComicCrafter/backend/static"
os.makedirs(SAVE_DIR, exist_ok=True)

device = "cpu"  # Force using CPU to avoid memory issue on MPS


def load_model():
    print("🔹 Loading Stable Diffusion Model...")
    try:
        pipe = StableDiffusionPipeline.from_pretrained(MODEL_PATH)
        pipe.to(device)
        print("✅ Model Loaded Successfully!")
        return pipe
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return None

def generate_comic_image(pipe, text, image_name):
    """Generate an image using Stable Diffusion based on paragraph text."""
    try:
        text = text.strip()
        if len(text) < 20:  # Skip very short paragraphs
            print(f"⚠️ Skipping short text: {text[:30]}...")
            return None

        print(f"🖼️ Generating image for: {text[:50]}...")
        
        # Run the generation on the model pipeline
        with torch.no_grad():  # Disable gradient calculations for inference
            image = pipe(text).images[0]  # Generate image
            if image:
                image_path = os.path.join(SAVE_DIR, image_name)
                image.save(image_path)  # Save the image to disk
                print(f"✅ Image saved at: {image_path}")
                return f"/static/{image_name}"  # Return relative path for HTML
            else:
                print("❌ No image generated.")
                return None
    except Exception as e:
        print(f"❌ Error generating image: {e}")
        return None
