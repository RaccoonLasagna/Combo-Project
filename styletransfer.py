import streamlit as st
import tensorflow_hub as hub
import tensorflow as tf
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
import os
import cv2

#Title text
st.title("""Style Transfer AI""")

# style transfer's model
model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

# defining load image function for the model
def load_image(img_path):
    img = tf.io.read_file(img_path)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = img[tf.newaxis, :]
    return img

#defining display image function to...display images
def display_image(image_file):
    img = Image.open(image_file)
    return img

# image check
content_check = False
style_check = False

# uploading images
def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames, key=1)
    return os.path.join(folder_path, selected_filename)

def file_selector2(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames, key=2)
    return os.path.join(folder_path, selected_filename)


content_image = file_selector()
style_image = file_selector2()



#show inputted image
if content_image and style_image is not None:
    st.image(display_image(content_image), width=250)
    st.write(content_image)
    st.image(display_image(style_image), width=250)
    st.write(style_image)
    loaded_content_image = load_image(content_image)
    loaded_style_image = load_image(style_image)
    content_check = True
    style_check = True

#click button after uploading images
if content_check and style_check == True:
    next = st.button("next")
#if button clicked, style + show image
if next == True:
    stylized_image = model(tf.constant(loaded_content_image), tf.constant(loaded_style_image))[0]
    cv2.imwrite('generatedimage.jpg', cv2.cvtColor(np.squeeze(stylized_image)*255, cv2.COLOR_BGR2RGB))
    st.image(display_image('generatedimage.jpg'))