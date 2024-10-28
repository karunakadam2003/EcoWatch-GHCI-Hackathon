# generate_images.py
import torch
from diffusers import StableDiffusionPipeline
from fetch_species_data import fetch_species_data

# Load the pre-trained model
model_path = "stable_diffusion_model.pt"
pipe = torch.load(model_path)

def generate_image_for_species(species_name):
    """Generate an image for a specific species using Stable Diffusion."""
    prompt = f"A highly detailed and realistic depiction of an endangered species, {species_name}, in its natural habitat."
    
    with torch.no_grad():
        image = pipe(prompt).images[0]
        filename = f"{species_name.replace(' ', '_')}.png"
        image.save(filename)
        print(f"Saved image for {species_name} as {filename}")

def main():
    # Define latitude and longitude
    latitude = 34.0522  # Los Angeles example
    longitude = -118.2437  # Los Angeles example

    # Fetch endangered species data
    species_list = fetch_species_data(latitude, longitude)
    
    if species_list:
        print(f"Generating images for {len(species_list)} endangered species.")
        
        for species_name in species_list:
            generate_image_for_species(species_name)
            
        print("Image generation for all species completed.")
    else:
        print("No endangered species found for the given location.")

if __name__ == "__main__":
    main()
