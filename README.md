## Banknot Tanıma Projesi

Bu proje, türk lirası banknotlarını tespit etmek için bir makine öğrenmesi modeli kullanır. Kullanıcılar, bir banknot görüntüsü yükleyerek hangi banknot türü olduğunu tahmin edebilirler. Projede, TensorFlow ile eğitilmiş bir model ve Streamlit tabanlı bir arayüz kullanılmıştır.

## Proje Yapısı

turkis_banknot.py: Ana uygulama dosyası. Bu dosya, görüntüyü işleyip modeli kullanarak tahmin yapar ve sonuçları Streamlit arayüzünde gösterir.

model.h5: TensorFlow formatında eğitilmiş model dosyası.

## Kullanım

Proje linki :https://6fspeervugyisudjdnrf8u.streamlit.app/

## Arayüz

Projenin yayınlanmış haline aşağıdaki linkten ulaşabilirsiniz:
Streamlit Arayüzü

## Nasıl Çalışır?

Girdi Yükleme: Kullanıcı, bir banknot görüntüsü yükler.

İşleme: Görüntüyün boyutları modele uygun olacak şekilde yeniden boyutlandırılır ve normalleştirilir.

Tahmin: Model, girdi görüntüsünün hangi tür banknot olduğunu tahmin eder.

Sonuç: Tahmin edilen banknot türü arayüzde gösterilir.

Gerekli Kütüphaneler

TensorFlow

NumPy

Pillow

OpenCV

Streamlit

## Model

Model, türk lirası banknotlarını tanımlamak için eğitilmiştir. Aşağıdaki banknot türlerini tanır:

5 TL

10 TL

20 TL

50 TL

100 TL

200 TL

## Destek

Herhangi bir sorun yaşarsanız lütfen geliştiriciyle iletişime geçin veya bu doküman altında bir konu oluşturun.
