"""
Portfolio Flask Application
A production-ready portfolio website for a Python Full-Stack Developer.
"""

import os
from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-change-in-production')

# Flask-Mail configuration (uses environment variables for security)
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS', 'True') == 'True'
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME', '')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD', '')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME', '')
app.config['CONTACT_EMAIL'] = os.environ.get('CONTACT_EMAIL', 'janamonijagan9@gmail.com')

mail = Mail(app)

# ---------------------------------------------------------------------------
# Portfolio Data (edit this to customize your portfolio)
# ---------------------------------------------------------------------------
PORTFOLIO_DATA = {
    "name": "JANAMONI JAGAN",
    "title": "Python Full-Stack Developer",
    "tagline": "Building intelligent, scalable applications with Python, AI & modern web tech.",
    "short_bio": (
        "I'm a Computer Science student and self-taught developer who loves turning complex "
        "problems into elegant, production-ready software. I specialise in Python back-end "
        "systems, generative AI pipelines, and full-stack web applications."
    ),
    "long_bio": (
        "Currently pursuing my B.Tech in Computer Science, I've spent the past two years "
        "building real-world applications that combine classical software engineering with "
        "cutting-edge AI. From deploying LangChain RAG chatbots powered by Google's Gemini API "
        "to engineering ML pipelines for customer-churn prediction, I thrive at the intersection "
        "of data, intelligence, and clean architecture. I'm passionate about open-source, "
        "continuous learning, and shipping software that actually solves problems."
    ),
    "email": "janamonijagan9@gmail.com",
    "phone": "+91 9391241870",
    "location": "Hyderabad, India",
    "github": "https://github.com/yourusername",
    "linkedin": "https://linkedin.com/in/yourusername",
    "leetcode": "https://leetcode.com/yourusername",
    "resume_url": "/static/resume.pdf",

    # ------------------------------------------------------------------
    # Skills – grouped by category
    # ------------------------------------------------------------------
    "skills": [
        {
            "category": "Languages",
            "icon": "code",
            "skills": ["Python", "Java", "SQL", "JavaScript"]
        },
        {
            "category": "Frameworks & Libraries",
            "icon": "layers",
            "skills": ["LangChain", "Scikit-Learn", "Flask", "Django", "Pandas", "NumPy", "NLTK"]
        },
        {
            "category": "AI / ML",
            "icon": "cpu",
            "skills": ["LLMs", "RAG", "Prompt Engineering", "NLP", "Supervised Learning",
                      "Unsupervised Learning", "Feature Engineering", "Gemini API"]
        },
        {
            "category": "Databases",
            "icon": "database",
            "skills": ["MySQL", "PostgreSQL", "MongoDB", "SQLite"]
        },
        {
            "category": "Cloud & Tools",
            "icon": "cloud",
            "skills": ["Google Cloud", "Git", "GitHub", "Jupyter", "VS Code", "Colab"]
        },
        {
            "category": "Front-End",
            "icon": "monitor",
            "skills": ["HTML5", "CSS3", "JavaScript", "Chart.js", "Tailwind CSS", "Bootstrap"]
        },
    ],

    # ------------------------------------------------------------------
    # Projects
    # ------------------------------------------------------------------
    "projects": [
        {
            "id": 1,
            "name": "AI-Powered Document Chatbot",
            "description": (
                "An intelligent document Q&A system built with LangChain and Google's Gemini API. "
                "Users upload PDFs; the RAG pipeline chunks, embeds, and retrieves relevant context "
                "so the LLM answers questions accurately—no hallucination."
            ),
            "tech": ["Python", "LangChain", "Gemini API", "RAG", "Flask", "ChromaDB"],
            "features": [
                "PDF ingestion & vector embedding pipeline",
                "Retrieval-Augmented Generation (RAG)",
                "Streaming chat interface",
                "Conversation memory & history",
            ],
            "github": "https://github.com/yourusername/ai-chatbot",
            "demo": "#",
            "image": "https://picsum.photos/seed/chatbot/600/380",
            "category": "ai",
        },
        {
            "id": 2,
            "name": "Customer Churn Prediction",
            "description": (
                "End-to-end ML pipeline that predicts customer churn for a telecom dataset. "
                "Includes thorough EDA, feature engineering, class-imbalance handling, "
                "and a Scikit-Learn gradient-boosting model achieving 89 % F1 score."
            ),
            "tech": ["Python", "Scikit-Learn", "Pandas", "NumPy", "Matplotlib", "SMOTE"],
            "features": [
                "Exploratory Data Analysis with visualisations",
                "Feature engineering & selection",
                "SMOTE for class-imbalance correction",
                "Model comparison & hyperparameter tuning",
            ],
            "github": "https://github.com/yourusername/churn-prediction",
            "demo": "#",
            "image": "https://picsum.photos/seed/churn/600/380",
            "category": "ml",
        },
        {
            "id": 3,
            "name": "Clinic Management System",
            "description": (
                "Offline-first desktop application for small clinics. Manages patient records, "
                "visit history, prescription tracking, and generates printable reports—"
                "all stored locally in SQLite with automated backup & restore."
            ),
            "tech": ["Electron", "React", "Express", "SQLite", "JavaScript"],
            "features": [
                "Offline-first with local SQLite storage",
                "Patient registration & visit tracking",
                "PDF report generation",
                "Automated backup & one-click restore",
            ],
            "github": "https://github.com/yourusername/clinic-management",
            "demo": "#",
            "image": "https://picsum.photos/seed/clinic/600/380",
            "category": "fullstack",
        },
        {
            "id": 4,
            "name": "Real-Time Data Dashboard",
            "description": (
                "Interactive analytics dashboard built with Flask and PostgreSQL. "
                "Live charts refresh automatically via WebSocket, "
                "displaying KPIs, trends, and filterable data tables."
            ),
            "tech": ["Flask", "PostgreSQL", "Chart.js", "JavaScript", "WebSocket", "Bootstrap"],
            "features": [
                "Real-time chart updates via WebSocket",
                "Dynamic filtering & date-range selection",
                "PostgreSQL query optimisation",
                "Export data as CSV",
            ],
            "github": "https://github.com/yourusername/data-dashboard",
            "demo": "#",
            "image": "https://picsum.photos/seed/dashboard/600/380",
            "category": "fullstack",
        },
    ],

    # ------------------------------------------------------------------
    # Education Timeline
    # ------------------------------------------------------------------
    "education": [
        {
            "degree": "B.Tech – Computer Science Engineering",
            "institution": "Keshav Memorial College of Engineering",
            "period": "2023 – 2026",
            "score": "CGPA: 7.4",
            "icon": "🎓",
        },
        {
            "degree": "Diploma – Electronics",
            "institution": "Govt. Institute of Electronics",
            "period": "2020 – 2023",
            "score": "64.1 %",
            "icon": "⚡",
        },
        {
            "degree": "Secondary School Certificate (SSC)",
            "institution": "Zilla Parishad High School",
            "period": "2019 – 2020",
            "score": "CGPA: 9.5",
            "icon": "📚",
        },
    ],

    # ------------------------------------------------------------------
    # Certifications
    # ------------------------------------------------------------------
    "certifications": [
        {"name": "Python", "issuer": "FreeCodeCamp", "year": "2025"},
        {"name": "SQL", "issuer": "Udemy", "year": "2024"},
        {"name": "Frontend Development (HTML, CSS, JS)", "issuer": "Udemy", "year": "2024"},
    ],

    # ------------------------------------------------------------------
    # Achievements
    # ------------------------------------------------------------------
    "achievements": [
        "Solved 100+ problems on LeetCode",
        "Deployed an AI production app using LangChain & Gemini API",
        "Delivered Python ML / NLP projects end-to-end",
        "Self-learning Deep Learning, GenAI & LLMs",
    ],
}


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.route('/')
def index():
    """Main portfolio page."""
    return render_template('index.html', data=PORTFOLIO_DATA)


@app.route('/contact', methods=['POST'])
def contact():
    """
    Handle contact form submission.
    Validates input server-side, then sends an email via Flask-Mail.
    Returns JSON so the front-end can display success/error without a page reload.
    """
    # --- Server-side validation ---
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    subject = request.form.get('subject', '').strip()
    message_body = request.form.get('message', '').strip()

    errors = {}
    if not name or len(name) < 2:
        errors['name'] = 'Name must be at least 2 characters.'
    if not email or '@' not in email:
        errors['email'] = 'A valid email address is required.'
    if not subject or len(subject) < 3:
        errors['subject'] = 'Subject must be at least 3 characters.'
    if not message_body or len(message_body) < 10:
        errors['message'] = 'Message must be at least 10 characters.'

    if errors:
        return jsonify({'success': False, 'errors': errors}), 400

    # --- Send email (only if MAIL_USERNAME is configured) ---
    if app.config['MAIL_USERNAME']:
        try:
            msg = Message(
                subject=f"[Portfolio Contact] {subject}",
                recipients=[app.config['CONTACT_EMAIL']],
                reply_to=email,
                body=(
                    f"Name:    {name}\n"
                    f"Email:   {email}\n"
                    f"Subject: {subject}\n\n"
                    f"Message:\n{message_body}"
                ),
            )
            mail.send(msg)
        except Exception as exc:
            app.logger.error("Mail send failed: %s", exc)
            return jsonify({'success': False, 'error': 'Email delivery failed. Please try again later.'}), 500

    return jsonify({'success': True, 'message': 'Thanks! I will get back to you soon.'})


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=os.environ.get('FLASK_DEBUG', 'False') == 'True')
