# from flask import Flask, render_template, request
# from app import app
from app.models.post import Post
from google.appengine.ext import ndb
from flask import Blueprint, request, jsonify
from datetime import datetime
from app.utility.json_encoder import JSONEncoder

from parser import parse_url

mod_posts = Blueprint('mod_posts', __name__)

@mod_posts.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    new_post = Post()
    new_post.name = request.json['name']
    new_post.price = request.json['price']
    new_post.date = datetime.now()
    new_post.url = request.json['url']
    new_post.description = request.json['description']
    new_post.put();
    response = JSONEncoder().encode(new_post.getValue())
    return response

@mod_posts.route('/parse', methods=['GET'])
def getParser():
    response = parse_url()

    return JSONEncoder().encode({'result': response})

