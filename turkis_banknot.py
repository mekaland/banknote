import cv2 
import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np


model = load_model('model.h5')


def img_preprocess(img):

    img = img.resize((30, 30))  
    img = np.array(img)
    img = img / 255.0  
    img = np.expand_dims(img, axis=0)  
   
    if len(img.shape) == 3 and img.shape[-1] != 3:
        img = np.stack([img] * 3, axis=-1)  
    
    img = img.astype('float32')  
    return img

st.title('Tr Banknot @kadirdagli')
st.write('Banknot resmini yükleyin')
file = st.file_uploader('Bir resim seç', type=['jpg', 'jpeg', 'png'])

class_names = ['5', '10', '20', '50', '100', '200']

if file is not None:
    img = Image.open(file)
    st.image(img, caption='Yüklenen resim')
    
    image = img_preprocess(img)
    prediction = model.predict(image)
    
    predicted_class = np.argmax(prediction)
    
    st.write(f'Tahmin: {class_names[predicted_class]}')
