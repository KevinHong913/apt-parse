# [START app]


# [START imports]
import logging
from flask import Flask, render_template, request
from google.appengine.ext import ndb
# [END imports]

# Import SQLAlchemy
# from flask.ext.sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')


# [START form]
@app.route('/form')
def form():
    return render_template('form.html')
# [END form]


# [START submitted]
@app.route('/submitted', methods=['POST'])
def submitted_form():
    name = request.form['name']
    email = request.form['email']
    site = request.form['site_url']
    comments = request.form['comments']

    # [END submitted]
    # [START render_template]
    return render_template(
        'submitted_form.html',
        name=name,
        email=email,
        site=site,
        comments=comments)
    # [END render_template]


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500


class Task(ndb.Model):
    description = ndb.StringProperty()
    done = ndb.BooleanProperty()


@app.route('/datastore')
def run_datastore():
    # [START datastore_quickstart]
    # Imports the Google Cloud client library

    task = Task(
        description='Sandy', done=False)
    task.put()

    return render_template('form.html')
# if __name__ == '__main__':
#   run_datastore()
