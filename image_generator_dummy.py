# # # import requests

# # # def fetch_species_data(latitude, longitude, radius=5):
# # #     """Fetch species occurrence data from GBIF API."""
# # #     url = "https://api.gbif.org/v1/occurrence/search"
# # #     params = {
# # #         "decimalLatitude": latitude,
# # #         "decimalLongitude": longitude,
# # #         "radius": radius,
# # #         "hasCoordinate": True,
# # #         "limit": 10  # Limit results for testing; adjust as needed
# # #     }
    
# # #     response = requests.get(url, params=params)
    
# # #     if response.status_code == 200:
# # #         return response.json()['results']
# # #     else:
# # #         print(f"Error fetching data: {response.status_code}")
# # #         return []


# # # def generate_image(prompt):
# # #     """Generate an image using DeepAI API."""
# # #     url = "https://api.deepai.org/api/text2img"
# # #     headers = {
# # #         'api-key': '20f37707-e528-4ce5-a64e-c257621bc0e3'  # Replace with your actual API key
# # #     }
# # #     data = {
# # #         'text': prompt
# # #     }
    
# # #     response = requests.post(url, headers=headers, data=data)
    
# # #     if response.status_code == 200:
# # #         image_url = response.json()['output_url']
# # #         print(f"Generated image URL for '{prompt}': {image_url}")
# # #         return image_url
# # #     else:
# # #         print("Error generating image:", response.text)
# # #         return None



# # # def main():
# # #     latitude = 43.6532  # Example latitude (Toronto)
# # #     longitude = -79.3832  # Example longitude (Toronto)
    
# # #     # Fetch species data based on coordinates
# # #     species_data = fetch_species_data(latitude, longitude)
    
# # #     if species_data:
# # #         print(f"Found {len(species_data)} species.")
        
# # #         for species in species_data:
# # #             species_name = species.get('scientificName', 'Unknown Species')
# # #             generate_image(species_name)  # Generate images for each species
        
# # #         print("Image generation completed.")
# # #     else:
# # #         print("No species found.")

# # # if __name__ == "__main__":
# # #     main()

# # import requests

# # def fetch_species_data(latitude, longitude):
# #     """Fetch species occurrence data from GBIF API."""
# #     url = "https://api.gbif.org/v1/occurrence/search"
# #     params = {
# #         "decimalLatitude": latitude,
# #         "decimalLongitude": longitude,
# #         "radius": 5,
# #         "hasCoordinate": True,
# #         "limit": 10
# #     }
    
# #     response = requests.get(url, params=params)
    
# #     if response.status_code == 200:
# #         return response.json()['results']
# #     else:
# #         print(f"Error fetching data: {response.status_code}")
# #         return []

# # def generate_image_with_picsart(prompt):
# #     """Generate an image using Picsart's AI image generator."""
# #     print(f"Visit Picsart and enter the prompt: '{prompt}'")

# # def main():
# #     latitude = 43.6532  # Example latitude (Toronto)
# #     longitude = -79.3832  # Example longitude (Toronto)
    
# #     # Fetch species data based on coordinates
# #     species_data = fetch_species_data(latitude, longitude)
    
# #     if species_data:
# #         print(f"Found {len(species_data)} species.")
        
# #         for species in species_data:
# #             species_name = species.get('scientificName', 'Unknown Species')
# #             generate_image_with_picsart(species_name)  # Prompt user to generate image
            
# #         print("Image generation instructions provided.")
# #     else:
# #         print("No species found.")

# # if __name__ == "__main__":
# #     main()

# import requests
# from PIL import Image
# from io import BytesIO

# def fetch_species_data(latitude, longitude):
#     """Fetch species occurrence data from GBIF API."""
#     url = "https://api.gbif.org/v1/occurrence/search"
#     params = {
#         "decimalLatitude": latitude,
#         "decimalLongitude": longitude,
#         "radius": 5,
#         "hasCoordinate": True,
#         "limit": 10  # Limit results for testing; adjust as needed
#     }
    
#     response = requests.get(url, params=params)
    
#     if response.status_code == 200:
#         return response.json()['results']
#     else:
#         print(f"Error fetching data: {response.status_code}")
#         return []

# def generate_image_with_craiyon(prompt):
#     """Generate an image using Craiyon's API and return the image URL."""
#     url = "https://api.craiyon.com/generate"
#     data = {
#         'prompt': prompt
#     }

#     response = requests.post(url, json=data)
    
#     if response.status_code == 200:
#         # Extract the image URLs from the response
#         images = response.json().get('images', [])
#         return images
#     else:
#         print("Error generating image:", response.text)
#         return []

# def save_images(image_urls, species_name):
#     """Save generated images locally."""
#     for i, img_url in enumerate(image_urls):
#         try:
#             img_response = requests.get(img_url)
#             img = Image.open(BytesIO(img_response.content))
#             img.save(f"{species_name.replace(' ', '_')}_{i + 1}.png")
#             print(f"Saved image: {species_name.replace(' ', '_')}_{i + 1}.png")
#         except Exception as e:
#             print(f"Error saving image for {species_name}: {e}")

# def main():
#     latitude = 43.6532  # Example latitude (Toronto)
#     longitude = -79.3832  # Example longitude (Toronto)
    
#     # Fetch species data based on coordinates
#     species_data = fetch_species_data(latitude, longitude)
    
#     if species_data:
#         print(f"Found {len(species_data)} species.")
        
#         for species in species_data:
#             species_name = species.get('scientificName', 'Unknown Species')
#             print(f"Generating image for: {species_name}")
            
#             # Generate images using Craiyon
#             image_urls = generate_image_with_craiyon(species_name)
            
#             if image_urls:
#                 save_images(image_urls, species_name)  # Save the generated images
            
#         print("Image generation completed.")
#     else:
#         print("No species found.")

# if __name__ == "__main__":
#     main()

# from diffusers import StableDiffusionPipeline
# import torch

# # Load the pipeline
# pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16).to("cuda")

# # Generate an image
# prompt = "A detailed illustration of Wohlfahrtia vigil"
# image = pipe(prompt).images[0]

# # Save the generated image
# image.save("wohlfahrtia_vigil.png")

# import torch
# from diffusers import StableDiffusionPipeline

# # Load the pipeline
# device = "cuda" if torch.cuda.is_available() else "cpu"
# pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16).to(device)

# # Generate an image based on a prompt
# prompt = "A detailed illustration of Wohlfahrtia vigil"
# image = pipe(prompt).images[0]

# # Save the generated image
# image.save("wohlfahrtia_vigil.png")
# print("Image saved as wohlfahrtia_vigil.png")