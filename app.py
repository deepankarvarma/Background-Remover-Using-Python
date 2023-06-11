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
    
    # Add custom CSS style for the page background
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("https://images.wallpaperscraft.com/image/single/background_blemishes_dark_91678_1920x1080.jpg");
        background-size: cover;
    }
    </style>
    '''
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    if uploaded_image is not None:
        image = np.array(bytearray(uploaded_image.read()), dtype=np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        input_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        st.subheader("Original Image")
        st.image(input_image, channels="RGB")
        
        removed_background = remove_background(image)
        removed_background = cv2.cvtColor(removed_background, cv2.COLOR_BGR2RGB)
        
        st.subheader("Background Removed")
        st.image(removed_background, channels="RGBA")
    

if __name__ == "__main__":
    main()
