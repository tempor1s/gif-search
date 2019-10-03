from flask import Flask, render_template, request
from tenor import gif_search, get_popular_gifs, get_random_gifs

app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
    # Get query and 'type' from query string
    query = request.args.get('query')
    req_type = request.args.get('type')
    # Since we are passing this through before we set it, we have to init both of the vars
    gifs = None
    display_gifs = True

    # Check the request type, if none then set gifs to popular gifs, otherwise get one of the others
    if req_type == 'search':
        gifs = gif_search(query)['results']
    elif req_type == 'random':
        gifs = get_random_gifs()['results']
    else:
        gifs = get_popular_gifs()['results']

    # Set display gifs to false if gifs is empty or none
    if not gifs:
        display_gifs = False

    # Render the template with index.html and gifs.html
    return render_template('index.html', gifs=gifs, display_gifs=display_gifs)


if __name__ == '__main__':
    app.run(debug=False, port=5000)
