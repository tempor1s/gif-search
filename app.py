from flask import Flask, render_template, request
import requests
import json
from tenor import gif_search, get_popular_gifs

app = Flask(__name__)


@app.route('/')
# @app.route('/search', methods=['GET', 'POST'])
def index():
    """Return homepage."""
    # TODO: Extract query term from url

    # TODO: Make 'params' dict with query term and API key
    display_gifs = True

    query = request.args.get('query')
    results = gif_search(query)['results']

    gifs = []
    for gif in results:
        gifs.append(gif)

    if not gifs:
        display_gifs = False

    return render_template('index.html', gifs=gifs, display=display_gifs)

    # popular_gifs = get_popular_gifs()['results']
    # gifs = []
    # for gif in popular_gifs:
    #     gifs.append(gif)
    # print('rendering most popular gifs!')
    # return render_template('index.html', gifs=gifs)


if __name__ == '__main__':
    app.run(debug=True)
