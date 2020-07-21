from flask_migrate import Migrate



from app import *

if __name__ == '__main__':
    import sys

    # insert at 1, 0 is the script path (or '' in REPL)
    sys.path.insert(1, '/home/ubuntu/test_flask_git/flask_knesset_backend')
    app = create_app(os.getenv('FLASK_CONFIG') or 'default')
    migrate = Migrate(app, db)
    app.run()