"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app

import pyodbc

server = 'DESKTOP-LPSI64O\SQLNAYANI' 
database = 'hospital'
connection = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';')


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return "Hello" 

@app.route('/columns')
def Columns():
    """Renders the column page"""
    cursor = connection.cursor()
    table = 'patient'
    return render_template(
        'columns.html',
        title='Columns',
        message='All column names.',
        col = cursor.execute("SELECT Column_Name FROM INFORMATION_SCHEMA.Columns WHERE TABLE_NAME=?",table)
    )
    cursor.close()

@app.route('/tables')
def Tables():
    """Renders the table page"""
    cursor = connection.cursor()
    return render_template(
        'tables.html',
        title='Tables',
        message='All table names.',
        table = cursor.execute("SELECT Table_Name FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='Base Table' AND TABLE_CATALOG=?",database)
    )
    cursor.close()
    

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
