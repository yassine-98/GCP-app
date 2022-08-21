
from time import sleep
from flask import jsonify,render_template
def hello(request) : 
    #  return jsonify(
    #      {
    #          "Message":'Test'
    #      }) 

      return render_template('index.html')

    
