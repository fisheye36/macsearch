import argparse
import sys
from os import getenv
from typing import Any, NoReturn

import requests


API_KEY_ENV_VAR_NAME = 'MACSEARCH_API_KEY'
API_KEY_FROM_ENV = getenv(API_KEY_ENV_VAR_NAME)

API_URL = 'https://api.macaddress.io/v1'
REQUEST_TIMEOUT = 1.0


def main() -> None:
    args = _parse_args()
    if args.api_key is None:
        _print_error_and_exit('Missing API key')

    try:
        response = query_api(
            api_key=args.api_key,
            mac_address=args.mac,
        )
    except requests.RequestException as e:
        _print_error_and_exit(f'Error while doing a request: {e}')

    response_json = response.json()
    if response.status_code == requests.codes.ok:
        manufacturer_name = response_json['vendorDetails']['companyName']
        print(f'Company that manufactured the device with MAC address {args.mac} is:\n'
              f'{manufacturer_name}')
    else:
        error_message = response_json['error']
        _print_error_and_exit(f'API error: {error_message}')


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Search network device information by MAC address.')
    parser.add_argument('mac', help='MAC address')
    parser.add_argument('--api-key', help=f'API key to use, supersedes environment variable {API_KEY_ENV_VAR_NAME}')

    args = parser.parse_args()
    if args.api_key is None:
        args.api_key = API_KEY_FROM_ENV

    return args


def _print_error_and_exit(error: Any) -> NoReturn:
    print(error, file=sys.stderr)
    exit(1)


def query_api(api_key: str, mac_address: str) -> requests.Response:
    api_params = {
        'apiKey': api_key,
        'output': 'json',
        'search': mac_address,
    }
    response = requests.get(API_URL, params=api_params, timeout=REQUEST_TIMEOUT)
    return response


if __name__ == '__main__':
    main()
