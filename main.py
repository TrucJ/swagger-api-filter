import json
from copy import deepcopy
import argparse

def filter_swagger(input_swagger, input_filter, output_file):
    # Read the Swagger file
    with open(input_swagger, 'r') as f:
        swagger = json.load(f)

    # Read the filter file
    with open(input_filter, 'r') as f:
        api_filter = json.load(f)

    # Filter the necessary APIs
    filtered_paths = {path: swagger['paths'][path] for path in api_filter['paths'] if path in swagger['paths']}
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

    # Write to a new Swagger file
    with open(output_file, 'w') as f:
        json.dump(filtered_swagger, f, indent=2)

    print("Filtered and created new Swagger file successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Filter Swagger APIs based on a specified filter list.")
    parser.add_argument('-i', '--input_swagger', type=str, required=True, help="Path to the input Swagger file.")
    parser.add_argument('-f', '--input_filter', type=str, required=True, help="Path to the filter file.")
    parser.add_argument('-o', '--output_file', type=str, required=True, help="Path to the output filtered Swagger file.")

    args = parser.parse_args()

    filter_swagger(args.input_swagger, args.input_filter, args.output_file)
