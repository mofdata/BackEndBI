#!/usr/bin/env bash

# Purpose: Gunicorn starter
# Author: manojit.gautam@gmail.com

# Name of an application
NAME="MOFBI"

# project directory
PROJECTDIR=/home/code/webapps/bi_web/

# bi project virutalenv directory
VENVDIR=/home/code/webapps/bi_web/venv

# Project source directory
SRCDIR=/home/code/webapps/bi_web/src

# Sock file as gunicorn will communicate using unix socket
SOCKFILE=$PROJECTDIR/gunicorn.sock

# User who runs the app
USER=code

# the group to run as
GROUP=code

# how many worker processes should Gunicorn spawn
NUM_WORKERS=4


# Activate the virtual environment
source $VENVDIR/bin/activate



# move to src dir !IMPORTANT otherwise it won't work.
cd $SRCDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec $VENVDIR/bin/gunicorn wsgi:app \
  -b 0.0.0.0:5000 \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-
