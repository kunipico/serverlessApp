from flask import Flask
from flask_login import LoginManager
# from flask_sessionstore import Session
from flask_session import Session
# import boto3

app = Flask(__name__)
app.config.from_object('flask_blog.config')
Session(app)

login_manager = LoginManager()
login_manager.init_app(app)

from flask_blog.lib.utils import setup_auth
setup_auth(login_manager)

from flask_blog.views import views, entries
login_manager.login_view = "login"
login_manager.login_message = "ログインしてください。"

# @app.route('/')
# def show_entries():
#   return "Hello World!"

#DB初期化用コマンド。
#Flask-Scriptを使用しようとしたが、現在ではサポートされていなかったためFlask-CLIを使用する構成に変更した。
def create_app():
    app = Flask(__name__)
    app.config.from_object('flask_blog.config')
    
    @app.cli.command("init-db")
    def init_db():
        print("Init DB start !!!")
        """Create DynamoDB table if it doesn't exist."""
        from flask_blog.models.entries import Entry
        from flask_blog.models.sessions import SessionModel
        if not Entry.exists():
            Entry.create_table(read_capacity_units=5, write_capacity_units=2)
            print("Entry Table created.")
        if not SessionModel.exists():
            SessionModel.create_table(read_capacity_units=5, write_capacity_units=2)
            print("Session Table created.")
    return app 