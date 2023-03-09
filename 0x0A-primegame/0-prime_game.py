#!/usr/bin/python3


def isPrime(num):
	'''Check whether a number is prime
	or not
		Return: None, num <=1
		Return: True, if prime number
		Return: False, if not prime number
	'''
	if num <= 1:
		return None
	sqrt = num ** 0.5
	iteration_length = int(sqrt + 1)
	for i in range(2, iteration_length):
		if num % i == 0:
			return False
	return True

def switchPlayer(current_player):
	'''Switches player from Maria to Ben
	or vice versa'''
	if current_player not in ['Maria', 'Ben']:
		raise ValueError("Invalid Player")
	if current_player == 'Maria':
		return 'Ben'
	elif current_player == 'Ben':
		return 'Maria'

def isWinner(x, nums):
	pass


if __name__ == '__main__':
	print(isWinner(5, 0))
	print(isPrime(1))