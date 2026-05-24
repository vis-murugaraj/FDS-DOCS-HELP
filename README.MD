# FDS Systems Documentation Portal (draft)

A small Flask web app that serves as a draft design for the future
documentation site at `docs.fdssys.com` for **FDS Systems Limited**.

> This is an early visual and structural draft. Copy, branding and
> navigation are placeholders intended to be refined.

## Features

- Clean homepage with hero section and section cards
- Top navigation menu shared across all pages
- Pages for Getting Started, Guides, API Reference, FAQ and Contact
- Individual guide detail pages
- Friendly 404 page
- Plain CSS, no build step, no JavaScript framework

## Project structure

```
vis-fds-help/
├── app.py               # Flask app: routes and site data
├── requirements.txt     # Python dependencies
├── templates/           # Jinja2 HTML templates
│   ├── base.html
│   ├── home.html
│   ├── getting_started.html
│   ├── guides.html
│   ├── guide_detail.html
│   ├── api_reference.html
│   ├── faq.html
│   ├── contact.html
│   └── 404.html
└── static/
    └── css/
        └── style.css
```

## Requirements

- Python 3.10 or newer
- pip

## Running locally

```bash
# 1. (Recommended) create a virtual environment
python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py
```

Then open <http://localhost:5000> in your browser.

## Customising the content

Most page content lives in plain Python data structures at the top of
`app.py` (`SITE`, `NAV_ITEMS`, `HOME_CARDS`, `GUIDES`, `FAQS`).
Edit those to update text without touching templates.

Visual styling lives in `static/css/style.css`.
