# CVMaker

CVMaker, iş veya staj arayan öğrencilerin CV'lerini iş ilanlarına göre optimize etmelerine yardımcı olan bir araçtır. Yapay zeka destekli bu uygulama, CV'nizi hedeflediğiniz pozisyona uygun hale getirmenize yardımcı olur.

## 🚀 Özellikler

- PDF formatındaki CV'leri otomatik okuma ve analiz etme
- İş ilanlarına göre CV optimizasyonu
- Anahtar kelimelere göre CV içeriği önerisi
- OpenAI GPT entegrasyonu ile akıllı öneriler
- Streamlit ile kullanıcı dostu arayüz

## 📋 Gereksinimler

- Python 3.8 veya üzeri
- OpenAI API anahtarı
- pip (Python paket yöneticisi)

## ⚙️ Kurulum

1. Projeyi klonlayın:

git clone https://github.com/kullanici_adiniz/CVMaker.git

cd CVMaker


2. Sanal ortam oluşturun ve aktif edin:

Linux/macOS için:

python3 -m venv venv

source venv/bin/activate


Windows için:

python -m venv venv

venv\Scripts\activate


3. Gerekli kütüphaneleri yükleyin:

pip install -r requirements.txt


4. `.env` dosyası oluşturun:
- Proje ana dizininde `.env` adında bir dosya oluşturun
- Aşağıdaki içeriği ekleyin:
bash
OPENAI_API_KEY=your_api_key_here
- `your_api_key_here` yerine [OpenAI API](https://platform.openai.com/api-keys) anahtarınızı yazın

## 🎯 Kullanım

1. Uygulamayı çalıştırın:
streamlit run app.py


2. Tarayıcınızda otomatik olarak açılan arayüzü kullanın:
   - CV'nizi PDF formatında yükleyin
   - Hedeflediğiniz pozisyonun iş ilanını yapıştırın
   - "CV'yi Analiz Et" butonuna tıklayın
   - Optimizasyon önerilerini inceleyin

## 🌐 Canlıya Alma

Streamlit uygulamanızı ücretsiz olarak canlıya almak için:

1. [Streamlit Community Cloud](https://streamlit.io/cloud) hesabı oluşturun
2. GitHub'a projenizi yükleyin (özel repo olabilir)
3. Streamlit Cloud'da "New app" butonuna tıklayın
4. GitHub reponuzu seçin ve app.py dosyasını belirtin
5. Gerekli gizli değişkenleri (OPENAI_API_KEY) ekleyin
6. "Deploy" butonuna tıklayın

## 🤝 Katkıda Bulunma

1. Bu depoyu fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik: özelliğin açıklaması'`)
4. Branch'inizi push edin (`git push origin feature/yeniOzellik`)
5. Pull Request oluşturun

## ⚠️ Önemli Notlar

- `.env` dosyanızı asla GitHub'a push etmeyin
- Büyük CV dosyaları için işlem süresi uzayabilir
- Streamlit Community Cloud'da uygulamanızı canlıya alırken API anahtarınızı gizli değişken olarak ekleyin