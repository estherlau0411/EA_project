from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g

@app.route('/')
def index():
    title = "百老匯電影"
    return render_template('index.html.j2')