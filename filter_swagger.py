import argparse
from swagger_filter import filter_swagger

def main():
    parser = argparse.ArgumentParser(description="Filter Swagger APIs based on a specified filter list.")
    parser.add_argument('-i', '--input', type=str, required=True, help="Path to the input Swagger file.")
    parser.add_argument('-f', '--filter', type=str, required=True, help="Path to the filter file.")
    parser.add_argument('-o', '--output', type=str, required=True, help="Path to the output filtered Swagger file.")

    args = parser.parse_args()

    with open(args.input, 'r') as f:
        input_data = f.read()

    with open(args.filter, 'r') as f:
        filter_data = f.read()

    try:
        filtered_swagger = filter_swagger(input_data, filter_data)
    except Exception as e:
        print(f"Error: {e}")
        return

    with open(args.output, 'w') as f:
        f.write(filtered_swagger)

    print("Filtered and created new Swagger file successfully.")

if __name__ == "__main__":
    main()
