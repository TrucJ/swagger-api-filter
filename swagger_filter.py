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

    filtered_definitions = {}
    
    def ref(name):
        obj_name = name.split('/')[-1]
        obj = swagger['definitions'][obj_name]
        filtered_definitions[obj_name] = obj
        if 'properties' in obj:
            for prop in obj['properties'].values():
                if '$ref' in prop:
                    ref(prop['$ref'])
                if 'items' in prop and '$ref' in prop['items']:
                    ref(prop['items']['$ref'])

    # Filter the relevant objects
    for path, path_item in filtered_paths.items():
        for method, operation in path_item.items():
            if 'parameters' in operation:
                for parameter in operation['parameters']:
                    if 'schema' in parameter and '$ref' in parameter['schema']:
                        ref(parameter['schema']['$ref'])

            if 'responses' in operation:
                for response in operation['responses'].values():
                    if 'schema' in response and '$ref' in response['schema']:
                        ref(response['schema']['$ref'])

    # Create a new Swagger file
    filtered_swagger = deepcopy(swagger)
    filtered_swagger['paths'] = filtered_paths
    filtered_swagger['definitions'] = filtered_definitions

    return json.dumps(filtered_swagger, indent=2)
