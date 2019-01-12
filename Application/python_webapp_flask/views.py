"""
Routes and views for the flask application.
"""

from datetime import datetime

from flask import render_template
from python_webapp_flask import app


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Questions? Comments?'
    )


@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Openroom flask is a room booking system.'
    )


@app.context_processor
def inject_global_organization_name():
    return dict(global_organization_name="Wyoming, Inc.")

