from charset_normalizer import from_path
from flask import Flask, jsonify, request
from translate import Translator
import os
import flasgger
from flasgger import Swagger


app = Flask(__name__)
Swagger(app=app)

@app.route("/", methods = ['POST','GET'])
def index():
    return "<h1> UiPath PPT Translator API </h1>"

@app.route("/translate_via_postman", methods = ['POST','GET'])
def translate_via_postman():
    if request.method == 'POST' or request.method=='GET':
        ### Getting data
        to_lang = request.json["to_lang"]
        input_string = request.json["input_string"]
        
        ### Translating
        translator_obj  = Translator(to_lang=to_lang)
        translation = translator_obj.translate(input_string)
        return jsonify(translation)
    
@app.route("/translate_via_uipath",methods=['POST','GET'])
def translate_via_uipath():
    """Translation via UiPath.
    This is using docstrings for specifications
    ---
    parameters:
        - name: to_lang
          in: query
          type: string
          required: true
        - name: input_string
          in: query
          type: string
          required: true
    responses:
        200:
             description: The output values
        
    """
    if request.method == 'POST' or request.method=='GET':
    ### Getting data
        to_lang = request.values.get("to_lang")
        input_string = request.values.get("input_string")
        
        ### Translating
        translator_obj  = Translator(to_lang=to_lang)
        translation = translator_obj.translate(input_string)
        return jsonify(translation)
    

if __name__=='__main__':
    port = os.environ.get("PORT",5000)
    app.run(debug=False, host="0.0.0.0", port=port)
    
    