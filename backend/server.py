#!/usr/bin/env python

import connexion
from flask import send_from_directory, redirect
from flask_cors import CORS
from backend import AVAILABLE_MODELS
from os import path, getcwd


class Project:
    def __init__(self, LM, config):
        self.config = config
        self.lm = LM()


def get_all_projects():
    res = {}
    for k in projects.keys():
        res[k] = projects[k].config
    return res


def analyze(analyze_request):
    project = analyze_request.get('project')
    text = analyze_request.get('text')

    res = {}
    if project in projects:
        p = projects[project] # type: Project
        res = p.lm.check_probabilities(text, topk=20)

    return {
        "request": {'project': project, 'text': text},
        "result": res
    }



CONFIG_FILE = "server.yaml"
app = connexion.App(__name__)
app.add_api(path.join(getcwd() , CONFIG_FILE))

#########################
#  some non-logic routes
#########################

@app.route('/')
def redir():
    return redirect('client/index.html')


@app.route('/client/<path:path>')
def send_static(path):
    """ serves all files from ./client/ to ``/client/<path:path>``

    :param path: path from api call
    """
    return send_from_directory('client/dist/', path)


@app.route('/data/<path:path>')
def send_data(path):
    """ serves all files from the data dir to ``/data/<path:path>``

    :param path: path from api call
    """
    print('Got the data route for', path)
    return send_from_directory(args.dir, path)


