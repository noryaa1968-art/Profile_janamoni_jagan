# 🚀 Python Developer Portfolio

A production-ready, single-page portfolio website built with **Flask + vanilla CSS + JavaScript**.
Dark/light mode, typing effect, scroll animations, project filtering, and a contact form with server-side validation — no heavy frontend framework required.

---

## 📁 Project Structure

```
portfolio/
├── app.py                  # Flask application & portfolio data
├── requirements.txt        # Python dependencies
├── Procfile                # Gunicorn entry point (Railway / Render)
├── .env.example            # Environment variable template
├── .gitignore
├── README.md
│
├── templates/
│   └── index.html          # Single-page Jinja2 template
│
└── static/
    ├── css/
    │   └── style.css       # Full design system (dark + light)
    ├── js/
    │   └── main.js         # All interactivity
    └── images/             # Put your profile photo / project screenshots here
        └── (placeholder)
```

---

## ⚡ Quick Start (Local)

### 1. Clone & enter the directory
```bash
git clone https://github.com/yourusername/portfolio.git
cd portfolio
```

### 2. Create and activate a virtual environment
```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
```bash
cp .env.example .env
# Open .env and fill in your details
```

### 5. Run the development server
```bash
flask run
# Visit http://127.0.0.1:5000
```

---

## 🎨 Customisation Guide

### Personal info & content
All portfolio data lives in the `PORTFOLIO_DATA` dictionary in **`app.py`**.
Edit it directly — no database needed.

```python
PORTFOLIO_DATA = {
    "name":     "Your Name",          # ← change this
    "email":    "you@example.com",    # ← and this
    "github":   "https://github.com/yourusername",
    # … etc.
}
```

### Adding / editing projects
Find the `"projects"` key in `PORTFOLIO_DATA`.
Each project is a dict:
```python
{
    "name":        "My Awesome App",
    "description": "What it does in 2-3 sentences.",
    "tech":        ["Python", "Flask", "React"],
    "features":    ["Feature 1", "Feature 2"],
    "github":      "https://github.com/you/repo",
    "demo":        "https://live-demo-url.com",   # or "#" to hide
    "image":       "https://picsum.photos/seed/myapp/600/380",
    "category":    "fullstack",   # "fullstack" | "ai" | "ml"
}
```

### Colours
Open `static/css/style.css` and edit the `:root` token block at the top:
```css
:root {
  --accent:   #2F81F7;   /* main blue — change to any colour */
  --accent-2: #58A6FF;   /* lighter variant */
  --green:    #3FB950;   /* achievement / feature tick */
  --purple:   #A371F7;   /* certification icon */
}
```

### Profile photo
Replace the Picsum URL in `templates/index.html` (search for `picsum.photos/seed/profile`)
with your own image path:
```html
<img src="/static/images/profile.jpg" alt="Profile photo" … />
```

### Resume
Drop your `resume.pdf` into `static/` and update the path in `PORTFOLIO_DATA`:
```python
"resume_url": "/static/resume.pdf",
```

### Contact form email
Set `MAIL_USERNAME`, `MAIL_PASSWORD`, and `CONTACT_EMAIL` in your `.env` file.
For Gmail, generate an **App Password** (Google Account → Security → App passwords).

---

## 🌐 Deployment

### Option A — Railway (recommended, free tier available)

1. Push your repo to GitHub.
2. Create a new project at [railway.app](https://railway.app) → **Deploy from GitHub**.
3. Add environment variables in Railway's dashboard (paste from your `.env`).
4. Railway auto-detects the `Procfile` and deploys. Done!

### Option B — Render

1. Create account at [render.com](https://render.com).
2. New → **Web Service** → connect your GitHub repo.
3. Build command: `pip install -r requirements.txt`
4. Start command: `gunicorn app:app`
5. Add environment variables under **Environment**.

### Option C — PythonAnywhere (free tier)

1. Upload your project (or `git clone` from a Bash console).
2. Create a virtualenv and `pip install -r requirements.txt`.
3. Go to **Web** tab → Add new web app → Manual configuration → Python 3.10.
4. Set the WSGI file to point to your `app` object:
   ```python
   import sys
   sys.path.insert(0, '/home/yourusername/portfolio')
   from app import app as application
   ```
5. Set environment variables in the WSGI file or via the **Files** tab.

---

## 🔧 Tech Stack

| Layer       | Technology                  |
|-------------|-----------------------------|
| Back-end    | Python 3.10+ · Flask 3      |
| Templating  | Jinja2                      |
| Styling     | Custom CSS (no framework)   |
| JavaScript  | Vanilla ES2020+             |
| Email       | Flask-Mail                  |
| Server      | Gunicorn                    |
| Fonts       | Google Fonts (Inter + JetBrains Mono) |
| Icons       | Font Awesome 6              |

---

## 📝 License

MIT — use it, fork it, make it yours.
