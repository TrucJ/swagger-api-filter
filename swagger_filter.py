import json
from copy import deepcopy

def filter_swagger(input_data, filter_data):
    # Read the Swagger file
    swagger = json.loads(input_data)

    # Read the filter file
    api_filter = json.loads(filter_data)

    # Filter the necessary APIs and methods
    filtered_paths = {}
    for path, methods in api_filter['paths'].items():
        if path in swagger['paths']:
            filtered_paths[path] = {method: swagger['paths'][path][method] for method in swagger['paths'][path] if method in methods}

    definitions = set()

    # Function ref handle references
    def ref(data):
        if isinstance(data, dict):
            for key in data:
                if key == '$ref':
                    obj_name = data[key].split('/')[-1]
                    definitions.add(obj_name)
                    # Call ref() to handle references
                    ref(swagger['definitions'][obj_name])
                else:
                    ref(data[key])
        if isinstance(data, list):
            for item in data:
                ref(item)

    # Filter the relevant objects
    for path, path_item in filtered_paths.items():
        for data in path_item.values():
            ref(data)

    # Create a new Swagger file
    filtered_swagger = deepcopy(swagger)
    filtered_swagger['paths'] = filtered_paths
    filtered_swagger['definitions'] = {name: swagger['definitions'][name] for name in swagger['definitions'] if name in definitions}

    return json.dumps(filtered_swagger, indent=2)
