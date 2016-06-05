# -*- coding:utf8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # 简单工厂函数基类
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TRAEDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'zhyh2010@mail.ustc.edu.cn'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN') or '1435589631@qq.com'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    # 简单工厂函数派生类， 用于开发
    DEBUG = True
    MAIL_SERVER = 'mail.ustc.edu.cn'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'zhyh2010@mail.ustc.edu.cn'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
    # 测试派生类
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or \
                              'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
    # 使用派生类
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or \
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite')

# 有点类似， 简单工厂中的选择判断模块
config = {
    'development' : DevelopmentConfig,
    'testing' : TestingConfig,
    'production' : ProductionConfig,

    'default' : DevelopmentConfig
}