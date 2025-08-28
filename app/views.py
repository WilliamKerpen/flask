from app import app
from flask import render_template, url_for,request, redirect
from app.models import Contato
from app.forms import ContatoForm

@app.route('/')
def homepage():
    usuario = 'William'
    return render_template('index.html',usuario = usuario )


@app.route('/contato/', methods= ['GET','POST'])
def contato():
    form = ContatoForm()
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('homepage'))

    return render_template('contato.html',form=form)

@app.route('/contato/lista/')
def contatoLista():
    if request.method == 'GET':
        pesquisa = request.args.get ('pesquisa', '')

    dados = Contato.query.order_by('nome')
    if pesquisa != '':
        dados = dados.filter_by(nome=pesquisa)

    context = {'dados': dados.all()}

    return render_template('contato_lista.html', context=context)

@app.route('/contato/<int:id>/')
def contatoDetail(id):
    obj = Contato.query.get(id)

    return render_template('contato_detail.html', obj=obj)