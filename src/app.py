from flask import Flask

from api.default import bp as default_bp

app = Flask(__name__)
app.register_blueprint(default_bp)

if __name__ == '__main__':
    app.run()
