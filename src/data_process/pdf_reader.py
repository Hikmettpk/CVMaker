import pdfplumber


def read_pdf(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ''
            for page in pdf.pages:
                text += page.extract_text()
            return text
    except Exception as e:
        return f"Hata: {str(e)}"
    

if __name__ == "__main__":
    # Test için
    sample_cv_path = "examples/HikmetTopakCV.pdf"  # Örnek dosya yolu
    extracted_text = read_pdf(sample_cv_path)
    print("Çıkarılan metin:")
    print(extracted_text)
    