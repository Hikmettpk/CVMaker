import os
import sys
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename

# Add the project root to the Python path so we can import the modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.data_process.pdf_reader import read_pdf
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

app = Flask(__name__,
            template_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), '../../templates')),
            static_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), '../../static')))

app.config['UPLOAD_FOLDER'] = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../uploads'))
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


class CVAnalyzer:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found. Please add it to the .env file.")
        self.client = OpenAI(api_key=api_key)

    def generate_suggestions(self, cv_text, job_requirements):
        prompt = f"""
        Verilen CV ve iş ilanı metinlerini detaylı olarak analiz et. 
        İş ilanında belirtilen tüm teknik, deneyimsel ve kişisel gereksinimleri belirle; ardından CV'deki mevcut bilgileri bu gereksinimlerle karşılaştır. 
        Eksik ya da detaylandırılması gereken alanlar tespit edildiğinde, kullanıcıya somut ve doğrudan kopyalayıp kullanabileceği metin örnekleri sun. 
        Örneğin, mevcut ifadeyi daha açıklayıcı, etkileyici veya iş ilanındaki beklentilere uygun hale getirecek şekilde yeniden yazılmış örnek cümleler, eklenebilecek detaylı açıklamalar ve format önerileri ver. 
        Böylece, kullanıcı önerilen metinleri direkt olarak CV'sine ekleyebilir veya genel tavsiyeler doğrultusunda kendi düzenlemesini gerçekleştirebilir.

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
            max_tokens=1000
        )

        return response.choices[0].message.content


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    # Check if a CV file was uploaded
    if 'cv_file' not in request.files:
        return jsonify({'error': 'No CV file uploaded'}), 400

    file = request.files['cv_file']

    # Check if the file was selected
    if file.filename == '':
        return jsonify({'error': 'No CV file selected'}), 400

    # Check if the file is allowed
    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not allowed. Please upload a PDF.'}), 400

    # Get job requirements from form
    job_requirements = request.form.get('job_requirements', '')

    # Save the file
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # Extract text from PDF
    cv_text = read_pdf(filepath)

    # Generate suggestions
    analyzer = CVAnalyzer()
    try:
        suggestions = analyzer.generate_suggestions(cv_text, job_requirements)
        return jsonify({'suggestions': suggestions})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        # Clean up uploaded file
        if os.path.exists(filepath):
            os.remove(filepath)


if __name__ == '__main__':
    app.run(debug=True)