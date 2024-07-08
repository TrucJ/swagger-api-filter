from flask import Flask, request, jsonify
import json
from copy import deepcopy
import os

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return 'pong'

def filter_swagger(input_data, filter_data):
    # Read the Swagger file
    swagger = json.loads(input_data)

    # Read the filter file
    api_filter = json.loads(filter_data)

    # Filter the necessary APIs and methods
    filtered_paths = {}
    for path, methods in api_filter['paths'].items():
        if path in swagger['paths']:
            filtered_paths[path] = {method: swagger['paths'][path][method] for method in methods if method in swagger['paths'][path]}

    filtered_definitions = {}

    # Filter the relevant objects
    for path, path_item in filtered_paths.items():
        for method, operation in path_item.items():
            if 'parameters' in operation:
                for parameter in operation['parameters']:
                    if 'schema' in parameter and '$ref' in parameter['schema']:
                        ref = parameter['schema']['$ref'].split('/')[-1]
                        filtered_definitions[ref] = swagger['definitions'][ref]

            if 'responses' in operation:
                for response in operation['responses'].values():
                    if 'schema' in response and '$ref' in response['schema']:
                        ref = response['schema']['$ref'].split('/')[-1]
                        filtered_definitions[ref] = swagger['definitions'][ref]

    # Create a new Swagger file
    filtered_swagger = deepcopy(swagger)
    filtered_swagger['paths'] = filtered_paths
    filtered_swagger['definitions'] = filtered_definitions

    return json.dumps(filtered_swagger, indent=2)

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

if __name__ == '__main__':
    app.run(debug=True)
