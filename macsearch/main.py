import argparse
import sys
from os import getenv


API_KEY_ENV_VAR_NAME = 'MACSEARCH_API_KEY'
API_KEY_FROM_ENV = getenv(API_KEY_ENV_VAR_NAME)


def main() -> None:
    args = _parse_args()
    print(args)
    if args.api_key is None:
        print('Missing API key', file=sys.stderr)
        exit(1)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Search network device information by MAC address.')
    parser.add_argument('mac', help='MAC address')
    parser.add_argument('--api-key', help=f'API key to use, supersedes environment variable {API_KEY_ENV_VAR_NAME}')

    args = parser.parse_args()
    if args.api_key is None:
        args.api_key = API_KEY_FROM_ENV

    return args


if __name__ == '__main__':
    main()
