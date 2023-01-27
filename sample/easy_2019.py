#!/usr/bin/env python3
import sys

def main():
	with sys.stdin as f:
		name = f.readline().strip()
		print(f'While we seem to disagree on this issue, {name}, I respect your opinion and look forward to further discussion!')

if __name__ == '__main':
	main()