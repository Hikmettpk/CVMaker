# CVMaker

CVMaker, iş veya staj arayan öğrencilerin CV'lerini iş ilanlarına göre optimize etmelerine yardımcı olan bir araçtır. Yapay zeka destekli bu uygulama, CV'nizi hedeflediğiniz pozisyona uygun hale getirmenize yardımcı olur.

## 🚀 Özellikler

- PDF formatındaki CV'leri otomatik okuma ve analiz etme
- İş ilanlarına göre CV optimizasyonu
- Anahtar kelimelere göre CV içeriği önerisi
- OpenAI GPT entegrasyonu ile akıllı öneriler

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

1. CV'nizi PDF formatında `input` klasörüne yerleştirin

2. Uygulamayı çalıştırın:
python src/main.py


3. Konsol üzerinden gelen yönergeleri takip edin:
   - CV'nizin dosya adını girin
   - Hedeflediğiniz pozisyonun iş ilanını yapıştırın
   - Optimizasyon önerilerini inceleyin

## 📝 Örnek Kullanım

Test amaçlı örnek bir CV ile denemek için:
python src/data_processing/pdf_reader.py


## 🤝 Katkıda Bulunma

1. Bu depoyu fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik: özelliğin açıklaması'`)
4. Branch'inizi push edin (`git push origin feature/yeniOzellik`)
5. Pull Request oluşturun

## ⚠️ Önemli Notlar

- `.env` dosyanızı asla GitHub'a push etmeyin
- Büyük CV dosyaları için işlem süresi uzayabilir