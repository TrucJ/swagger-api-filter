#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <swagger_file> <filter_file> <output_file>"
    exit 1
fi

# Assign command line arguments to variables
SWAGGER_FILE=$1
FILTER_FILE=$2
OUTPUT_FILE=$3

# Check if curl is installed
if ! command -v curl &> /dev/null; then
    echo "curl could not be found, please install it to proceed."
    exit 1
fi

# Call the API and save the response
response=$(curl -s -X POST -F "swagger=@${SWAGGER_FILE}" -F "filter=@${FILTER_FILE}" https://swagger-api-filter.vercel.app/filter/beauty)

# Check if the response contains an error
if echo "$response" | grep -q '"error"'; then
    echo "Error: $(echo "$response" | jq -r '.error')"
    exit 1
fi

# Save the filtered swagger to the output file
echo "$response" > "$OUTPUT_FILE"
echo "Filtered swagger file saved to $OUTPUT_FILE"
