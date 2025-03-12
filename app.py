import streamlit as st
import os
import tempfile
from dotenv import load_dotenv
import PyPDF2
from openai import OpenAI

# .env dosyasını yükle
load_dotenv()

# OpenAI istemcisini yapılandır
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Sayfa yapılandırması
st.set_page_config(
    page_title="CVMaker - CV Optimizasyon Aracı",
    page_icon="📝",
    layout="wide",
)

# Başlık ve açıklama
st.title("📝 CVMaker")
st.subheader("CV'nizi İş İlanlarına Göre Optimize Edin")
st.markdown("""
Bu uygulama, CV'nizi hedeflediğiniz iş pozisyonuna göre optimize etmenize yardımcı olur.
PDF formatındaki CV'nizi yükleyin ve hedeflediğiniz pozisyonun iş ilanını girin.
""")

# PDF'den metin çıkarma fonksiyonu
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# OpenAI API ile CV analizi yapma
def analyze_cv_with_openai(cv_text, job_description):
    prompt = f"""
    Verilen CV ve iş ilanı metinlerini detaylı olarak analiz et. 
        İş ilanında belirtilen tüm teknik, deneyimsel ve kişisel gereksinimleri belirle; ardından CV'deki mevcut bilgileri bu gereksinimlerle karşılaştır. 
        Eksik ya da detaylandırılması gereken alanlar tespit edildiğinde, kullanıcıya somut ve doğrudan kopyalayıp kullanabileceği metin örnekleri sun. 
        Örneğin, mevcut ifadeyi daha açıklayıcı, etkileyici veya iş ilanındaki beklentilere uygun hale getirecek şekilde yeniden yazılmış örnek cümleler, eklenebilecek detaylı açıklamalar ve format önerileri ver. 
        Böylece, kullanıcı önerilen metinleri direkt olarak CV'sine ekleyebilir veya genel tavsiyeler doğrultusunda kendi düzenlemesini gerçekleştirebilir.

    
    CV:
    {cv_text}
    
    İş İlanı:
    {job_description}
    """
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Sen bir CV ve kariyer danışmanısın. İş arayanların CV'lerini iş ilanlarına göre optimize etmelerine yardımcı oluyorsun."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1500
    )
    
    return response.choices[0].message.content

# Ana uygulama arayüzü
st.header("CV Yükle")
uploaded_file = st.file_uploader("CV'nizi PDF formatında yükleyin", type="pdf")

st.header("İş İlanı")
job_description = st.text_area("Hedeflediğiniz pozisyonun iş ilanını buraya yapıştırın", height=200)

if uploaded_file is not None and job_description:
    if st.button("CV'yi Analiz Et"):
        with st.spinner("CV analiz ediliyor..."):
            # Geçici dosya oluştur
            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                tmp_file_path = tmp_file.name
            
            # PDF'den metin çıkar
            cv_text = extract_text_from_pdf(tmp_file_path)
            
            # Geçici dosyayı sil
            os.unlink(tmp_file_path)
            
            # CV'yi analiz et
            analysis = analyze_cv_with_openai(cv_text, job_description)
            
            # Sonuçları göster
            st.header("Analiz Sonuçları")
            st.markdown(analysis)
            
            # CV'nin orijinal içeriğini göster
            with st.expander("CV İçeriği"):
                st.text(cv_text)
else:
    st.info("Lütfen CV'nizi yükleyin ve iş ilanını girin, ardından 'CV'yi Analiz Et' butonuna tıklayın.")

# Footer
st.markdown("---")
st.markdown("© 2024 CVMaker | Yapay Zeka Destekli CV Optimizasyon Aracı") 