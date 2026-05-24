"""
FDS Systems Limited - Documentation Portal (draft)

A small Flask application that serves as a draft design for a future
documentation site at docs.fdssys.com.

Run locally:
    pip install -r requirements.txt
    python app.py

Then open http://localhost:5000 in your browser.
"""

from flask import Flask, render_template, abort

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Site-wide data
# ---------------------------------------------------------------------------
# Keeping content in plain Python dictionaries makes it easy for a beginner
# to extend the portal without touching templates or HTML.

SITE = {
    "company": "FDS Systems Limited",
    "short_name": "FDS Systems",
    "domain": "docs.fdssys.com",
    "tagline": "Documentation, guides and API references for FDS Systems products.",
    "year": 2026,
}

# Navigation menu shown in the header on every page.
# `endpoint` matches the Flask view function name.
NAV_ITEMS = [
    {"endpoint": "home", "label": "Home"},
    {"endpoint": "getting_started", "label": "Getting Started"},
    {"endpoint": "guides", "label": "Guides"},
    {"endpoint": "api_reference", "label": "API Reference"},
    {"endpoint": "faq", "label": "FAQ"},
    {"endpoint": "contact", "label": "Contact"},
]

# Cards displayed on the homepage. Each one links into a section of the docs.
HOME_CARDS = [
    {
        "title": "Getting Started",
        "description": "Set up your account and run through the basics in a few minutes.",
        "endpoint": "getting_started",
        "cta": "Start here",
    },
    {
        "title": "Guides",
        "description": "Step-by-step walkthroughs for common tasks and workflows.",
        "endpoint": "guides",
        "cta": "Browse guides",
    },
    {
        "title": "API Reference",
        "description": "Endpoints, request/response formats and authentication details.",
        "endpoint": "api_reference",
        "cta": "Read the reference",
    },
    {
        "title": "FAQ",
        "description": "Quick answers to the questions we hear most often.",
        "endpoint": "faq",
        "cta": "See FAQ",
    },
]

# A simple list of guide articles. In a real site these would live in a
# database or in Markdown files; for a draft, hard-coded data is fine.
GUIDES = [
    {
        "slug": "installation",
        "title": "Installing the FDS Systems client",
        "summary": "Download, install and verify the FDS Systems desktop client.",
    },
    {
        "slug": "first-project",
        "title": "Creating your first project",
        "summary": "Set up a project, invite collaborators and configure permissions.",
    },
    {
        "slug": "integrations",
        "title": "Connecting to third-party systems",
        "summary": "Wire FDS Systems into the tools your team already uses.",
    },
    {
        "slug": "troubleshooting",
        "title": "Troubleshooting common issues",
        "summary": "Diagnose and resolve the most frequent problems users report.",
    },
]

FAQS = [
    {
        "question": "What is the FDS Systems documentation portal?",
        "answer": (
            "It is the central place to find product guides, API references "
            "and answers to common questions about FDS Systems products."
        ),
    },
    {
        "question": "Is this the final design?",
        "answer": (
            "No. This is an early draft of docs.fdssys.com. Content, branding "
            "and navigation are all expected to evolve."
        ),
    },
    {
        "question": "How do I report a documentation issue?",
        "answer": (
            "Use the Contact page to send us a short description of the "
            "problem and a link to the page where you found it."
        ),
    },
    {
        "question": "Can I contribute to the documentation?",
        "answer": (
            "Yes. Get in touch via the Contact page and we will share our "
            "contribution guidelines."
        ),
    },
]


# ---------------------------------------------------------------------------
# Make site-wide data available to every template
# ---------------------------------------------------------------------------
@app.context_processor
def inject_globals():
    return {"site": SITE, "nav_items": NAV_ITEMS}


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------
@app.route("/")
def home():
    return render_template("home.html", cards=HOME_CARDS)


@app.route("/getting-started")
def getting_started():
    return render_template("getting_started.html")


@app.route("/guides")
def guides():
    return render_template("guides.html", guides=GUIDES)


@app.route("/guides/<slug>")
def guide_detail(slug):
    guide = next((g for g in GUIDES if g["slug"] == slug), None)
    if guide is None:
        abort(404)
    return render_template("guide_detail.html", guide=guide)


@app.route("/api-reference")
def api_reference():
    return render_template("api_reference.html")


@app.route("/faq")
def faq():
    return render_template("faq.html", faqs=FAQS)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.errorhandler(404)
def not_found(_error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    # debug=True gives helpful error pages while you are developing.
    app.run(host="0.0.0.0", port=5000, debug=True)
