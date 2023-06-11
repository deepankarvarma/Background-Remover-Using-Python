import streamlit as st
import cv2
import numpy as np
import tempfile
import os

def remove_background(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to create a mask
    _, mask = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Apply morphological operations to remove noise
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=3)
    sure_bg = cv2.dilate(opening, kernel, iterations=3)

    # Create a mask image with transparent background
    transparent_mask = cv2.cvtColor(sure_bg, cv2.COLOR_GRAY2BGRA)
    transparent_mask[:, :, 3] = 0

    # Apply the mask to the original image
    result = cv2.bitwise_and(image, image, mask=sure_bg)

    # Convert the result to RGB
    result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

    return result

# Streamlit app
st.title("Background Remover")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Save the uploaded file to a temporary directory
    temp_dir = tempfile.mkdtemp()
    temp_path = os.path.join(temp_dir, uploaded_file.name)
    with open(temp_path, 'wb') as f:
        f.write(uploaded_file.read())

    # Display the uploaded image
    image = cv2.imread(temp_path)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Remove the background
    result = remove_background(temp_path)

    # Display the result
    st.image(result, caption='Background Removed', use_column_width=True)

    # Clean up the temporary directory
    os.remove(temp_path)
    os.rmdir(temp_dir)
