import numpy as np
from PIL import Image

# Open image
img = Image.open("input.jpg")

# Convert image to numpy array
img_array = np.array(img)

# Convert RGB to grayscale
gray = np.mean(img_array, axis=2)

# Convert grayscale to black & white
bw = np.where(gray > 128, 255, 0)

# Convert back to image
bw_image = Image.fromarray(bw.astype(np.uint8))

# Save image
bw_image.save("output.jpg")

print("Black & White image saved!")