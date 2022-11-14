from flask import Flask, url_for
import math

#define a function to do integration of f(x) btw. a and b:
def Integral(n, a, b):
    dx = (b - a) / n
    intgr = 0.0
    for i in range(1, n):

      intgr = intgr + dx * abs(math.sin(dx*(i+1/2)+a))

    return intgr
appFlask = Flask(__name__)
@appFlask.route('/numericalintegralservice/')
@appFlask.route('/numericalintegralservice/<a>/<b>')
def finalIntegral(a = 0,b=3.14):
    m=Integral(1000,float(a),float(b))
    return str(m)

appFlask.run(debug=True, port=5000)
