from flask import Blueprint, render_template
from flask import current_app as app
from datetime import date
from .models import db, Quote
from .api_data import retrieve_and_store_data


main_bp = Blueprint('main_bp', __name__)

@main_bp.route("/")
def hello_world():    
    return "<p>Hello, World!</p>"

@main_bp.route("/home", methods=['GET', 'POST'])
def home():
    today_date = date.today()
    today_quote = db.session.execute(db.select(Quote).where(Quote.date == today_date)).scalar()
    if today_quote:
        return render_template('index.html', daily_quote=today_quote)
    else:
        retrieve_and_store_data()
        today_quote = db.session.execute(db.select(Quote).where(Quote.date == today_date)).scalar()
        return render_template('index.html', daily_quote=today_quote)



@main_bp.route("/about")
def about():
    return render_template('about.html')

@main_bp.route("/projects")
def projects():
    return render_template('projects.html')

@main_bp.route("/contact")
def contact():
    return render_template('contact.html')
