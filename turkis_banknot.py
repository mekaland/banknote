import cv2 
import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

# Modeli yükleme
model = load_model('model.h5')

# Görüntü işleme fonksiyonu
def img_preprocess(img):
    # Modelin beklediği giriş boyutuna uygun şekilde yeniden boyutlandırma
    img = img.resize((224, 224))  # Burada 224x224, modelin beklediği boyuta göre değiştirilebilir
    img = np.array(img)
    img = img / 255.0  # Normalizasyon
    img = np.expand_dims(img, axis=0)  # Batch boyutu ekleme
    img = img.astype('float32')  # Veri tipini uygun şekilde dönüştürme
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
