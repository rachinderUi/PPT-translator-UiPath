from charset_normalizer import from_path
from flask import Flask, jsonify, request
from translate import Translator

app = Flask(__name__)

@app.route("/", methods = ['POST','GET'])
def index():
    return "<h1> PPT Translator API </h1>"

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
    if request.method == 'POST' or request.method=='GET':
    ### Getting data
        to_lang = request.values.get("to_lang")
        input_string = request.values.get("input_string")
        
        ### Translating
        translator_obj  = Translator(to_lang=to_lang)
        translation = translator_obj.translate(input_string)
        return jsonify(translation)
    

if __name__=='__main__':
    app.run(debug=True)
    
    