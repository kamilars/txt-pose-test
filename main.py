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
        # Assuming result.pose is in the same directory as your Flask app
        pose_file_path = 'result.pose'

        # Send the file as response
        posefile = send_file(pose_file_path, mimetype='application/pose', as_attachment=True)
        delete_file(pose_file_path)
        return posefile

    except Exception as e:
        # Handle exceptions if the file is not found or other errors occur
        #return str(e), 404
        data = {
            'message': 'No POSE could be created - None of the words could be translated'
        }
        
        # Returning a tuple with response data and status code
        return jsonify(data), 418

    
if __name__== "__main__":
    app.run(host="0.0.0.0", port=int("3000"), debug=True)
