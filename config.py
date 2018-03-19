# import os
# basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'hard to guss string'
    BLOG_MAIL_SUBJECT_PREFIX = '[Team]'
    BLOG_MAIL_SENDER = '2034653239@qq.com'
    BLOG_MAIL_USERER = '1802738987@qq.com'
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_POST = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = '2034653239@qq.com'  # os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = 'ptwbyczpstvbbffa'  # os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:adminastor@localhost:3306/test'


class TestingConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}