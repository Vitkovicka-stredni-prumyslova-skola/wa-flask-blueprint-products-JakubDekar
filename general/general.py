from flask import Blueprint, render_template

general_bp = Blueprint('general_bp', __name__,
    template_folder='templates',
    static_folder='static')

@general_bp.route('/')
def index():
    return render_template('general/index.html')

categories = ['Mužské ', 'Ženské', 'zlato'] 
@general_bp.route('/categories')
def display_categories():
    return render_template('index.html', categories=categories)
