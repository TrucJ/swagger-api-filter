from flask import Flask, request, jsonify
import json
from swagger_filter import filter_swagger

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return 'pong'

@app.route('/filter', methods=['POST'])
def filter_api():
    if 'swagger' not in request.files or 'filter' not in request.files:
        return jsonify({"error": "Both 'swagger' and 'filter' files are required."}), 400
    
    swagger_file = request.files['swagger']
    filter_file = request.files['filter']

    swagger_content = swagger_file.read().decode('utf-8')
    filter_content = filter_file.read().decode('utf-8')

    try:
        filtered_swagger = filter_swagger(swagger_content, filter_content)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(json.loads(filtered_swagger))

@app.route('/filter/beauty', methods=['POST'])
def filter_beauty_api():
    if 'swagger' not in request.files or 'filter' not in request.files:
        return jsonify({"error": "Both 'swagger' and 'filter' files are required."}), 400
    
    swagger_file = request.files['swagger']
    filter_file = request.files['filter']

    swagger_content = swagger_file.read().decode('utf-8')
    filter_content = filter_file.read().decode('utf-8')

    try:
        filtered_swagger = filter_swagger(swagger_content, filter_content)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return filtered_swagger

if __name__ == '__main__':
    app.run(debug=True)
