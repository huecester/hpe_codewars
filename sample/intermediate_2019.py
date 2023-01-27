#!/usr/bin/env python3
import sys

def main():
	with sys.stdin as stdin:
		f0 = int(stdin.readline().strip())
		f1 = int(stdin.readline().strip())
		n = int(stdin.readline().strip())

		prev = f1
		next = f0 + f1
		for i in range(n):
			if i == 0:
				print(f0)
			elif i == 1:
				print(f1)
			else:
				print(next)
				tmp = next + prev
				prev = next
				next = tmp

if __name__ == '__main__':
	main()