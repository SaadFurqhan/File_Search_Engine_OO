from flask import Flask
import os



template_dir = os.path.abspath('../Flask_UI/templates')
app = Flask(__name__, template_folder=template_dir)



