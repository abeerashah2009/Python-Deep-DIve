#!/usr/bin/env python3
import argparse

# Create the parser
parser = argparse.ArgumentParser(description='A simple greeting application.')

# Add arguments
parser.add_argument('--name', type=str, help='The name of the person to greet.')
parser.add_argument('--count', type=int, default=1, choices=[1, 2, 3],
                    help='How many times to greet (default: 1).')

# Parse the arguments
args = parser.parse_args()

name = args.name if args.name else 'Stranger'
for _ in range(args.count):
    print(f'Hello, {name}!')
