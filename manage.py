import os
# from flask_migrate import Migrate
from flask_script import Manager,Shell
from app import create_app, db
from app.models import User, Role, Permission, Post
app = create_app('default')
#manager = Manager(app)
# migrate = Migrate(app, db) os.getenv('FLASK_CONFIG') or

app.run()


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role, Permission=Permission, Post=Post)


@app.cli.command()
def test():
    """单元测试"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


#if __name__ == '__main__':
   #manager.run()

