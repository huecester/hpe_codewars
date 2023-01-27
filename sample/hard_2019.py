#!/usr/bin/env python3
from typing import List
import re
import sys

def parse_line(line: str) -> List[bool]:
	return [True if c == '#' else False for c in line]

def parse_state(list: List[bool]) -> str:
	return ''.join(['#' if c else '.' for c in list])

def sum_indexes(list: List[bool], offset: int) -> int:
	# TODO: fix my life
	indexes = [i - offset if c else 0 for i, c in enumerate(list)]
	return sum(indexes)

def main():
	with sys.stdin as stdin:
		# Input
		initial_state = stdin.readline().strip().replace('initial state: ', '')
		t11_password = int(stdin.readline().strip())
		t1000_password = int(stdin.readline().strip())
		patterns = []
		while (line := stdin.readline().strip()) != '0':
			patterns.append(parse_line(line))

		offset = 4
		i = 0
		while True:
			if initial_state[i] == '#':
				break
			offset -= 1
			i += 1

		initial_state = f'....{initial_state.strip(".")}....'
		state = parse_line(initial_state)

		sum = sum_indexes(state, offset)
		for i in range(11):
			next_state = [False] * len(state)

			for pattern in patterns:
				for i in range(len(state) - len(pattern)):
					if pattern in state[i:i+len(pattern)]:
						next_state[i+len(pattern)//2] = True

			sum += sum_indexes(next_state, offset)
			state = next_state

		print(sum)

if __name__ == '__main__':
	main()