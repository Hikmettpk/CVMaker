import os
from dotenv import load_dotenv
from openai import OpenAI
from src.data_process.pdf_reader import read_pdf

load_dotenv()

class CVAnalyzer:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY bulunamadı. Lütfen .env dosyasına ekleyin.")
        self.client = OpenAI(api_key=api_key)

    def generate_suggestions(self, cv_text, job_requirements):
        prompt = f"""
        Aşağıdaki CV ve iş ilanı metinlerini analiz et. İş ilanında belirtilen gereksinimlere göre CV’yi nasıl iyileştirebileceğime dair spesifik öneriler sun. Türkçe cevap ver.

        ### CV:
        {cv_text}

        ### İş İlanı:
        {job_requirements}

        ### Öneriler:
        """
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sen bir kariyer danışmanısın ve CV optimizasyonu konusunda uzmansın."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        return response.choices[0].message.content

if __name__ == "__main__":
    cv_text = read_pdf("examples/HikmetTopakCV.pdf")
    with open("/Users/hikmettopak/Desktop/Projects/CVMaker/examples/ilan.txt", "r", encoding="utf-8") as f:
        job_reqs = f.read()
    
    analyzer = CVAnalyzer()
    suggestions = analyzer.generate_suggestions(cv_text, job_reqs)
    print("OpenAI Önerileri:")
    print(suggestions)