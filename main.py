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
        return '<h1>Too low</h1>'
    elif user_guess > random_num:
        return '<h1>Too high</h1>'
    elif user_guess == random_num:
        return '<h1>You found me</h1>'


if __name__ == '__main__':
    app.run(debug=True)
