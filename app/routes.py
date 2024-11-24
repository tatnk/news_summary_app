from flask import Blueprint, render_template, request
from .scraper import NewsScraper
from .summarizer import summarize_text

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/search', methods=['POST'])
def search():
    keyword = request.form['keyword']
    articles = NewsScraper().get_news_articles(keyword)
    return render_template('results.html', articles=articles)

@main.route('/summary/<int:id>')
def summary(id):
    article = NewsScraper().get_news_articles_by_id(id)
    summary = summarize_text(article['content'])
    return render_template('summary.html', article=article, summary=summary)
