#!/usr/bin/env python3
"""
   Simple flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel, localeselector


class Config:
    """
    configuring babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Get the best locale match for the current request."""

    # Get the user's preferred languages from the Accept-Language header.
    languages = request.accept_languages

    # Return the best match with our supported languages.
    return languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def home_page() -> str:
    """
    routes to the home page
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
