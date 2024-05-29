
import requests
import base64
from PIL import Image
from io import BytesIO
from pyzbar.pyzbar import decode

# Step 1: Download the Base64 encoded content
url = "https://gist.githubusercontent.com/professor-hillman/3f7f54d1ac36e385da5660ab12e92060/raw/9424fe9e4fcb3c5a53dc4591ceafdfe682534cc4/aceofbase64.txt"
response = requests.get(url)
base64_content = response.text.strip()

# Step 2: Decode the Base64 content to binary data
image_data = base64.b64decode(base64_content)

# Step 3: Save the binary data as a PNG file
with open("recovered.png", "wb") as image_file:
    image_file.write(image_data)

# Open the image using PIL to ensure it's saved correctly
image = Image.open(BytesIO(image_data))
image.save("recovered.png")

# Step 4: Extract the hidden message
decoded_objects = decode(Image.open("recovered.png"))
for obj in decoded_objects:
    hidden_message = obj.data.decode("utf-8")
    print(f"Flag: {hidden_message}")
