# test_api_xpress

A custom GitHub Action to run Postman collections using Newman.

## Usage

```yaml
uses: your-username/test_api_xpress@v0.1.0
with:
  collection: 'path/to/your/collection.json'
  environment: 'path/to/your/environment.json'
  report-file: 'path/to/your/report.xml'
