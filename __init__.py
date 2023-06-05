import flask
import logging
import urllib.parse
import six
from calculator import calculate
from flask import request

from simpleCalculator import NumericStringParser

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['POST'])
def hello():
    if 'value' in request.args:
        print("Valor com espaço: " + six.moves.urllib.parse.quote(request.args['value']))
        value = str(urllib.parse.unquote(urllib.parse.quote(request.args['value'], safe=' /+')))
    else:
        return "Error: No value field provided. Please specify a value."
    
    print('O valor recebido foi:' + value)
    nsp = NumericStringParser()
    result = nsp.eval(value)
    print(result)
    
    
    return ('O valor recebido foi:' + str(result))

app.run()


