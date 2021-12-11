import random
from flask import Flask

app = Flask(__name__)

random_num = random.randint(0, 9)


@app.route('/')
def greeting():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<div style="width:30%;height:0;padding-bottom:56%;position:relative;"><iframe ' \
           'src="https://giphy.com/embed/oJ8gRS9lwBGpHiQaZC" width="100%" height="50%" style="position:absolute" ' \
           'frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div><p><a ' \
           'href="https://giphy.com/gifs/bigbluetvshow-oJ8gRS9lwBGpHiQaZC">via GIPHY</a></p> '


@app.route('/<int:user_guess>')
def guess(user_guess):
    if user_guess < random_num:
        return '<h1 style="color: red";>Too low</h1>' \
               '<div style="width:100%;height:0;padding-bottom:125%;position:relative;"><iframe ' \
               'src="https://giphy.com/embed/jD4DwBtqPXRXa" width="100%" height="100%" style="position:absolute" ' \
               'frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div><p><a ' \
               'href="https://giphy.com/gifs/work-digging-jD4DwBtqPXRXa">via GIPHY</a></p>'
    elif user_guess > random_num:
        return '<h1 style="color: purple";>Too high</h1>' \
               '<div style="width:100%;height:0;padding-bottom:94%;position:relative;"><iframe ' \
               'src="https://giphy.com/embed/3o6ZtaO9BZHcOjmErm" width="100%" height="100%" ' \
               'style="position:absolute" ' \
               'frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div><p>' \
               '<a href="https://giphy.com/gifs/dog-puppy-fly-3o6ZtaO9BZHcOjmErm">via GIPHY</a></p>'
    elif user_guess == random_num:
        return '<h1 style="color: green";>You found me</h1>' \
               '<div style="width:100%;height:0;padding-bottom:105%;position:relative;"><iframe ' \
               'src="https://giphy.com/embed/4T7e4DmcrP9du" width="100%" height="100%" style="position:absolute" ' \
               'frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div><p><a ' \
               'href="https://giphy.com/gifs/puppy-biscuit-emerging-4T7e4DmcrP9du">via GIPHY</a></p>'


if __name__ == '__main__':
    app.run(debug=True)
