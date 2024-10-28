# load_model.py
import torch
from diffusers import StableDiffusionPipeline

# Load the Stable Diffusion model
model_id = "CompVis/stable-diffusion-v1-4"  # or any other compatible model
pipe = StableDiffusionPipeline.from_pretrained(model_id)
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

# Save the model pipeline to be used by other files
torch.save(pipe, "stable_diffusion_model.pt")
print("Model loaded and saved as stable_diffusion_model.pt")
