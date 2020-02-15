from flask import Flask, render_template, redirect, url_for, Response, send_file
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, IntegerField, FloatField, SubmitField, validators, ValidationError
from bokeh.embed import server_document
from bokeh.server.server import Server
#from bokeh.themes import Theme
from tornado.ioloop import IOLoop

app2 = Flask(__name__)
Bootstrap(app2)
#app2.config['SECRET_KEY'] = '45df55653df23224'

def modify_doc(doc):
    #layout = plot.plot_iV()
    layout = plot2.plot(400, 400)
    doc.add_root(layout)
    #doc.theme = Theme(filename="theme.yaml")

@app2.route("/home", methods = ['POST', 'GET'])
@app2.route('/', methods=['GET', 'POST'])
def ivapp_page():
    #script = server_document('http://10.107.32.38:5006/bkapp')
    return render_template("home.html",title='EE770')
    #return render_template("home.html",title='EE765_distributions', script=script)

def iv_worker():
    # Can't pass num_procs > 1 in this configuration. If you need to run multiple
    # processes, see e.g. flask_gunicorn_embed.py
    server = Server({'/bkapp': modify_doc}, io_loop=IOLoop(), allow_websocket_origin=["10.107.32.38:5006"])
    #server = Server({'/bkapp': modify_doc}, io_loop=IOLoop(), allow_websocket_origin=["localhost:5000"])
    server.start()
    server.io_loop.start()

#from threading import Thread
#Thread(target=iv_worker).start()

if __name__ == '__main__':
    app2.run()
