#!/usr/bin/env bash

gunicorn -w 3 -b :8000 editor.wsgi