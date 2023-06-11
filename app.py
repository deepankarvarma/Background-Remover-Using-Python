import streamlit as st
import cv2
import numpy as np
import rembg

def remove_background(image):
    result = rembg.remove(image)
    return result

def main():
    st.title("Background Remover")
    
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    
    if uploaded_image is not None:
        image = np.array(bytearray(uploaded_image.read()), dtype=np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        
        st.subheader("Original Image")
        st.image(image, channels="RGB")
        
        removed_background = remove_background(image)
        
        st.subheader("Background Removed")
        st.image(removed_background, channels="RGBA")
    

if __name__ == "__main__":
    main()
