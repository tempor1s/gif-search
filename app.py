from flask import Flask, render_template, request
from tenor import gif_search, get_popular_gifs, get_random_gifs

app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
    display_gifs = True

    query = request.args.get('query')
    req_type = request.args.get('type')
    gifs = None

    if req_type == 'search':
        gifs = gif_search(query)['results']
    elif req_type == 'random':
        gifs = get_random_gifs()['results']
    else:
        gifs = get_popular_gifs()['results']

    if not gifs:
        display_gifs = False

    return render_template('index.html', gifs=gifs, display=display_gifs)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
