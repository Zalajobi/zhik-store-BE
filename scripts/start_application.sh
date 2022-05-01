#!/usr/bin/env bash

export FLASK_APP=app.py;
export FLASK_ENV=development;
export FLASK_RUN_PORT=5001;

start_application(){
    flask run
}

start_application
