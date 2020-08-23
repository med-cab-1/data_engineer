"""
Main app/routing for Med-Cab
"""


from flask import Flask

def create_app():
    """
    Create and configuration our Flask App
    """

    app = Flask(__name__)

    @app.route('/')
    def root():
        return 'Hello, World!'

    return app
