import os
import sys
import subprocess

def run_postman_collection(collection, environment, report_file):
    try:
        # Define Newman command with arguments
        newman_args = [
            'newman', 'run', collection,
            '--reporters', 'cli,junit',
            '--reporter-junit-file', report_file
        ]
        
        if environment:
            newman_args.extend(['--environment', environment])

        # Execute Newman command
        subprocess.run(newman_args, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    collection = os.getenv('INPUT_COLLECTION')
    environment = os.getenv('INPUT_ENVIRONMENT')
    report_file = os.getenv('INPUT_REPORT_FILE')

    if not collection or not report_file:
        print("Error: 'collection' and 'report-file' inputs are required.")
        sys.exit(1)

    run_postman_collection(collection, environment, report_file)

if __name__ == "__main__":
    main()
