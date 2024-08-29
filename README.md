# Swagger Filter

## Introduction

`Swagger Filter` is a Python script designed to filter specific APIs and methods from a Swagger file based on a provided filter file. The filtered Swagger file will only contain the specified APIs and methods, making it easier to work with large Swagger files by narrowing down the scope to what you actually need.

## Features

- Filter specific APIs and methods from a Swagger file.
- Retain only the relevant objects (parameters and responses) associated with the filtered APIs.
- Output the filtered Swagger file to a specified location.

## Requirements

- Python 3.x
- `Flask` library

## Usage

### Filter File Format

The filter file should be a JSON file with the following structure:

```json
{
    "paths": {
        "/items": ["get"],
        "/items/{itemId}": ["get", "post"]
    }
}
```

In this example, the filter file specifies that only the `GET` method for `/items` and both `GET` and `POST` methods for `/items/{itemId}` should be retained in the filtered Swagger file

### Use the API

You can use tools like `curl` to test the API.

Using `curl`:

```bash
curl -X POST -F 'swagger=@path/to/swagger.json' -F 'filter=@path/to/filter.json' https://swagger-filter.vercel.app/filter
```

Replace `path/to/swagger.json` and `path/to/filter.json` with the actual file paths.

### Running locally

1. **Clone the Repository**:

```bash
git clone https://github.com/TrucJ/swagger-filter.git
cd swagger-filter
```

2. **Install Dependencies**:

```bash
pip install Flask
```

3. **Prepare your Swagger and Filter files**:

Ensure you have your Swagger JSON file and filter JSON file prepared.

4. **Run the Script**:

Use the following command to run the script:

```bash
python filter_swagger.py -i path/to/swagger.json -f path/to/filter.json -o path/to/filtered_swagger.json
```

Replace `path/to/swagger.json`, `path/to/filter.json`, and `path/to/filtered_swagger.json` with the actual paths to your Swagger file, filter file, and the desired output file respectively.

### Example

If your Swagger file is located at `./swagger.json`, your filter file is at `./filter.json`, and you want to output the filtered Swagger file to `./filtered_swagger.json`, you would run:

```bash
python filter_swagger.py -i ./swagger.json -f ./filter.json -o ./filtered_swagger.json
```

### Output

The script will create a new Swagger JSON file at the specified output path containing only the filtered APIs and methods. It will also print a success message:

```bash
Filtered and created new Swagger file successfully.
```
