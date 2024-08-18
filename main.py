import os
import json
import requests
import sys

def run_postman_collection(collection_path, report_file):
    with open(collection_path, 'r') as file:
        collection = json.load(file)

    results = []
    
    for item in collection.get('item', []):
        request = item.get('request', {})
        method = request.get('method', 'GET')
        url = request.get('url', {}).get('raw', '')
        headers = {header['key']: header['value'] for header in request.get('header', [])}
        body = request.get('body', {}).get('raw', '')

        try:
            response = requests.request(method, url, headers=headers, data=body)
            result = {
                'url': url,
                'method': method,
                'status_code': response.status_code,
                'response_body': response.text
            }
            results.append(result)
        except requests.RequestException as e:
            results.append({
                'url': url,
                'method': method,
                'error': str(e)
            })
            sys.exit(1)

    # Save results to a file
    with open(report_file, 'w') as file:
        json.dump(results, file, indent=2)

def main():
    collection = os.getenv('INPUT_COLLECTION')
    report_file = os.getenv('INPUT_REPORT_FILE')

    if not collection or not report_file:
        print("Error: 'collection' and 'report-file' inputs are required.")
        sys.exit(1)

    run_postman_collection(collection, report_file)

if __name__ == "__main__":
    main()
