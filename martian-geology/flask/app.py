from flask import Flask, render_template, send_file
from flask_flatpages import FlatPages

from os.path import join


class Config:
    FLATPAGES_ROOT = 'articles'
    FLATPAGES_EXTENSION = '.md'
    FLATPAGES_MARKDOWN_EXTENSIONS = ['toc']
    FLATPAGES_EXTENSION_CONFIGS = {
        'toc': {
            'permalink': 'True',
            'permalink_class': 'octicon-link'
        }
    }


app = Flask(__name__)
app.config.from_object(Config())
flatpages = FlatPages(app)


@app.route('/articles/<permalink>')
def article(permalink):
    article = flatpages.get_or_404(permalink)
    all_articles = [article for article in flatpages]
    
    return render_template(
        'article.html',
        article=article,
        all_articles=all_articles
    )
