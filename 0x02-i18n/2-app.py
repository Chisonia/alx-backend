#!/usr/bin/env python3
'''Best match language module'''
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configuration class for the Flask app."""
    LANGUAGES = ["en", "fr"]  # Supported languages
    BABEL_DEFAULT_LOCALE = "en"  # Default language
    BABEL_DEFAULT_TIMEZONE = "UTC"  # Default timezone


app = Flask(__name__)
app.config.from_object(Config)  # Use Config class for app configuration

babel = Babel(app)  # Instantiate Babel object and bind it to the app


@babel.localeselector
def get_locale():
    """Determine the best match for supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """Route for the index page."""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True)
