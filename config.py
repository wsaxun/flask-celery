import os

_app_root = os.path.join(os.path.dirname(os.path.realpath(__file__)))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    @staticmethod
    def init_app(app):
        pass

class Dev_Config(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(_app_root, 'data-dev.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    @classmethod
    def init_app(cls,app):
        from common.log import cur_timestamp,setup_logger
        import logging
        file_base_name = 'app_{0}.log'.format(cur_timestamp())
        setup_logger(_app_root,file_base_name,level=logging.INFO,enable_logger=False)

class Dev_Mysql_Config(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@192.168.2.129:3308/nbudb'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    @classmethod
    def init_app(cls,app):
        from common.log import cur_timestamp,setup_logger
        import logging
        file_base_name = 'app_{0}.log'.format(cur_timestamp())
        setup_logger(_app_root,file_base_name,level=logging.INFO,enable_logger=False)

config = {
    'default':Dev_Mysql_Config,
    'Dev_Config':Dev_Config,
    'Dev_Mysql_Config':Dev_Mysql_Config,
}

