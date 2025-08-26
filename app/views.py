from app import app
from flask import render_template, url_for

@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/outra_pagina')
def nova_rota():
    return render_template('outra_pagina.html')