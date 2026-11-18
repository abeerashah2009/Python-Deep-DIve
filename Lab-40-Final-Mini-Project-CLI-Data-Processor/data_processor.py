import argparse
import json
import logging
import sys

import requests

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def fetch_data(source):
    """Return parsed JSON from an HTTP(S) URL, a file:// URL or a local path."""
    if source.startswith('http://') or source.startswith('https://'):
        response = requests.get(source, timeout=10)
        response.raise_for_status()
        return response.json()
    path = source[len('file://'):] if source.startswith('file://') else source
    with open(path) as f:
        return json.load(f)


def save_data_to_file(data, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    logging.info(f"Data successfully saved to {file_path}")


def parse_arguments():
    parser = argparse.ArgumentParser(description='CLI Data Processor')
    parser.add_argument('--url', type=str,
                        default='https://jsonplaceholder.typicode.com/posts',
                        help='API URL, file:// URL or local file path to read JSON from')
    parser.add_argument('--out', type=str, required=True, help='Path to save JSON data')
    return parser.parse_args()


def validate(data):
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise ValueError('JSON must be a list of objects')


def main():
    args = parse_arguments()
    logging.info("Started fetching data from %s", args.url)
    try:
        data = fetch_data(args.url)
        validate(data)
        logging.info("Fetched and validated %d records", len(data))
        save_data_to_file(data, args.out)
    except (requests.exceptions.RequestException, OSError, ValueError) as err:
        logging.error("Failed: %s", err)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
