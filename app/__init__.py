#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()


def setting_app():
    from app import app_blueprint
    app.register_blueprint(app_blueprint)

    app.config.from_pyfile('../config.py')

    return app


manager = Manager(app)

