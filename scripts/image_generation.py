import base64
import os
import requests
from dotenv import load_dotenv
load_dotenv()

engine_id = "stable-diffusion-xl-1024-v1-0"
api_host = os.getenv('API_HOST', 'https://api.stability.ai')
api_key = os.getenv("STABILITY_API_KEY")


async def create_image(prompt):
    response = requests.post(
        f"{api_host}/v1/generation/{engine_id}/text-to-image",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        json={
            "text_prompts": [
                {
                    "text": prompt
                }
            ],
            "cfg_scale": 7,
            "height": 1024,
            "width": 1024,
            "samples": 1,
            "steps": 40,
        },
    )

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))


    data = response.json()
    folder_path = "./images/"
    existing_images = os.listdir(folder_path)
    image_count = len(existing_images)
    image_base64 = ""
    for i, image in enumerate(data["artifacts"]):
        image_number = i + image_count
        image_path = os.path.join(folder_path, f"v1_txt2img_{image_number}.png")
        with open(image_path, "wb") as f:
            f.write(base64.b64decode(image["base64"]))
        if image["base64"] != None:
            image_base64 = image["base64"]

    return image_base64
