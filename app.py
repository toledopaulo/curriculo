from flask_cors import CORS
from flask import Flask, render_template, redirect

app = Flask(__name__)
CORS(app)

app.run()