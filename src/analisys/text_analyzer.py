from src.data_process.pdf_reader import read_pdf

def analyze_cv(cv_text, job_requirements):
    """
    CV metni ile iş gereksinimlerini karşılaştırır ve basit öneriler üretir.
    :param cv_text: PDF’den çıkarılan CV metni
    :param job_requirements: İş ilanındaki gereksinimler (string)
    :return: Öneriler listesi
    """
    suggestions = []
    
    # Gereksinimleri satır satır ayır (basit bir yaklaşım)
    req_lines = job_requirements.lower().split("\n")
    cv_text_lower = cv_text.lower()

    # Örnek kontrol: Bazı anahtar kelimeleri ara
    keywords = [ "scala", "git", "mikroservis", "ingilizce", "python","serverless"]
    for keyword in keywords:
        if keyword in req_lines and keyword not in cv_text_lower:
            suggestions.append(f"CV’nde '{keyword}' bulunmuyor, eğer tecrüben varsa ekle.")
        elif keyword in cv_text_lower:
            suggestions.append(f"CV’nde '{keyword}' var, bunu daha fazla vurgulayabilirsin.")

    return suggestions


if __name__ == "__main__":

    cv_text = read_pdf("examples/HikmetTopakCV.pdf")
    with open("examples/ilan.txt", "r", encoding="utf-8") as f:
        job_reqs = f.read()
    
    suggestions = analyze_cv(cv_text, job_reqs)
    print("Öneriler:")
    for suggestion in suggestions:
        print(f"- {suggestion}")
