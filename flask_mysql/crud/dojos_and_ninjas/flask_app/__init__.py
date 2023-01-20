# import flask from Flask
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "sapientia et doctrina:wisdom and learning"
