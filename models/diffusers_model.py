# import torch
# from diffusers import StableDiffusionPipeline

# # Load the Stable Diffusion model
# model_id = "CompVis/stable-diffusion-v1-4"  # or any other compatible model
# pipe = StableDiffusionPipeline.from_pretrained(model_id)
# pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

# # Define the latitude and longitude
# latitude = 34.0522  # Example: Los Angeles
# longitude = -118.2437

# # Create a prompt for generating an image
# prompt = f"An endangered species found at latitude {latitude}, longitude {longitude}, in its natural habitat, highly detailed and realistic"

# # Generate the image
# with torch.no_grad():
#     image = pipe(prompt).images[0]

# # Save the image
# image.save("endangered_species.png")

# # Display the image (optional)
# image.show()


# generate_image.py
import torch

# Load the pre-saved model
pipe = torch.load("stable_diffusion_model.pt")

# Define latitude and longitude
latitude = 34.0522  # Example: Los Angeles
longitude = -118.2437

# Create a prompt for generating an image
prompt = f"An endangered species found at latitude {latitude}, longitude {longitude}, in its natural habitat, highly detailed and realistic"

# Generate the image
with torch.no_grad():
    image = pipe(prompt).images[0]

# Save the image
image.save("endangered_species.png")
print("Image saved as endangered_species.png")

# Display the image (optional)
image.show()
