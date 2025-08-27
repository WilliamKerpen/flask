from app import app
from flask import render_template, url_for,request, redirect
from app.models import Contato
from app.forms import ContatoForm

@app.route('/')
def homepage():
    usuario = 'William'
    return render_template('index.html',usuario = usuario )


@app.route('/contato', methods= ['GET','POST'])
def contato():
    form = ContatoForm()
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('homepage'))

    return render_template('contato.html',form=form)