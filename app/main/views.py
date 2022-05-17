from flask import render_template, request, redirect, url_for
from . import main

#Views 
@main.route('/')
def index():
    """ View root page that returns the index page and its data
    """
    title = "Welcome to home page"
    return render_template('index.html', title = title)


