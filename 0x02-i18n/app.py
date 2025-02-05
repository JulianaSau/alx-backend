#!/usr/bin/env python3
"""Flask app with current time display"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
from typing import Union, Dict
import pytz
from datetime import datetime


class Config:
    """Config class for Flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Returns user dictionary or None if ID cannot be found
    or if login_as was not passed"""
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request():
    """Find user if any and set it as global on flask.g.user"""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Get locale based on priority"""
    # 1. Locale from URL parameters
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    # 2. Locale from user settings
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    # 3. Locale from request header
    header_locale = request.accept_languages.best_match(
            app.config['LANGUAGES'])
    if header_locale:
        return header_locale

    # 4. Default locale
    return app.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone() -> str:
    """Get timezone based on priority"""
    try:
        # 1. Find timezone parameter in URL parameters
        timezone = request.args.get('timezone')
        if timezone:
            pytz.timezone(timezone)
            return timezone

        # 2. Find timezone from user settings
        if g.user and g.user['timezone']:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']

    except pytz.exceptions.UnknownTimeZoneError:
        pass

    # 3. Default to UTC
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/', strict_slashes=False)
def index() -> str:
    """Home page"""
    # Get the current time in the user's timezone
    timezone = pytz.timezone(get_timezone())
    current_time = datetime.now(timezone)

    # Format the time according to the locale
    formatted_time = format_datetime(current_time)

    return render_template('index.html', current_time=formatted_time)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
