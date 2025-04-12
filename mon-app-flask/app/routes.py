from flask import Blueprint, render_template, request, redirect, url_for
from .models import Article
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    articles = Article.query.all()
    return render_template('index.html', articles=articles)

@main.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        new_article = Article(
            title=request.form['title'],
            content=request.form['content']
        )
        db.session.add(new_article)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('create.html')

@main.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    article = Article.query.get_or_404(id)
    if request.method == 'POST':
        article.title = request.form['title']
        article.content = request.form['content']
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('edit.html', article=article)

@main.route('/delete/<int:id>')
def delete(id):
    article = Article.query.get_or_404(id)
    db.session.delete(article)
    db.session.commit()
    return redirect(url_for('main.index'))
