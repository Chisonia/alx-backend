#!/usr/bin/env python3
'''Lang module'''
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _


class Config:
    """Configuration class for the Flask app."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """Determine the best match for supported languages."""
    # Check if the 'locale' query parameter is present in the URL
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    # Default to the browser's preferred language
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """Route for the index page."""
    return render_template("0-index.html",
                           home_title=_("home_title"),
                           home_header=_("home_header"))


if __name__ == "__main__":
    app.run(debug=True)
