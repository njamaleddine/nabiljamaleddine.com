import os

from flask import Flask, render_template

from utils.toolbelt import coerce_bool


app = Flask(__name__)

app.config.update(
    DEBUG=coerce_bool(os.environ.get('DEBUG', False)),
    SECRET_KEY=os.environ.get('SECRET_KEY', 'REPLACE_THIS')
)


@app.route('/', methods=['GET'])
def index():
    """ Homepage """
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
