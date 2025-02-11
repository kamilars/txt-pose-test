from flask import Flask, Response, request, jsonify, send_file
import functions_framework
from run import *

def delete_file(filename):
    if file_exists(filename):
        os.remove(filename)
        print("pose file deleted.")

app = Flask(__name__)

@app.route('/')
def text_to_gif():
    text = request.args.get('text')
    if not text:
        response = {
            "error": "Invalid request",
            "message": "The request is missing required parameters."
        }
        return jsonify(response), 400
    
    print(text)
    run_code(text)
        
    try:
        # pose_file_path = 'result.pose'
        # posefile = send_file(pose_file_path, mimetype='application/pose', as_attachment=True)
        return send_file('result.gif', mimetype='image/gif', as_attachment=True)
        # send_file('result.gif', )

    except Exception as e:
        # Handle exceptions if the file is not found or other errors occur
        #return str(e), 404
        data = {
            'message': 'No POSE could be created - None of the words could be translated'
        }
        
        # Returning a tuple with response data and status code
        return jsonify(data), 404

    
if __name__== "__main__":
    app.run(host="0.0.0.0", port=int("8000"), debug=True)
