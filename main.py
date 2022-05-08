
from time import sleep
from flask import jsonify,render_template
def hello(request) : 
    #  return jsonify(
    #      {
    #          "Message":'zabi'
    #      }) 

      return render_template('index.html')

    
