# Black & White Image Converter

A simple Python project that converts a colored image into a black & white image using NumPy and Pillow.

## Features

* Convert colored images to black & white
* Uses NumPy for image processing
* Saves converted image automatically
* Beginner-friendly project


## How It Works

🖤 RGB to Black & White Image Converter
Convert any colored image to black & white using NumPy and Pillow — no OpenCV required.

🚀 How It Works

| Step | Action |
|------|--------|
| 1 | Read the image using Pillow |
| 2 | Convert to a NumPy array (3D matrix of RGB pixels) |
| 3 | Average R, G, B values → Grayscale |
| 4 | Apply threshold: pixel > 128 → white, else → black |
| 5 | Convert array back to image and save |
 
 
### Grayscale Formula

Gray = (R + G + B) / 3

 
### Threshold Logic

pixel > 128  →  255 (White)
pixel ≤ 128  →   0  (Black)

 


