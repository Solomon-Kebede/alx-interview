#!/usr/bin/python3


# level = 'VERBOSE'
level = 'CRITICAL'

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

def generateMultiples(num, length):
	'''Generate a set of multiples of `num`
	with a length of `length`'''
	return {(num * i) for i in range(1, length + 1)}

def logger(log='', level=level):
	'''logger function (debugging purposes)'''
	if level == 'VERBOSE':
		print(log)

def isWinner(x, nums):
	'''Returns the winner of the prime game
	for `x` rounds and a list of `nums`
	# May require handling error for `x` the round of numbers
	'''
	rounds = x
	cached_prime_numbers = {}
	# First Player for the start of the game
	current_player = 'Maria'
	# Score board increases for round winner
	score_board = {'Maria': 0, 'Ben': 0}
	logger('{} Rounds'.format(rounds))
	for index in range(len(nums)):
		num = nums[index]
		logger('\tRound #{}'.format(index))
		# (1, num] - num included, the case for handled at the end
		current_range = range(2, num + 1)
		# current round playing set
		current_set = set(current_range)
		logger('\t\tCurrent set: {}'.format(current_set))
		if current_set == set():
			score_board[current_player] += 1
			logger(f"\t\t\tscore_board '{score_board}'")
			current_player = switchPlayer(current_player)
		already_removed = set()
		for n in current_range:
			if n in already_removed or current_set == set():
				continue
			# current_set_size is updated on each round
			current_set_size = len(current_set)
			logger("\t\tcurrent number: {} \
				and current_player: {} and \
				current_set_size = {}".format(n, current_player,
					current_set_size)
				)
			# check if number is cached # if it is retrieve from cache
			n_is_prime = cached_prime_numbers.get(n)
			# if number is not cached compute and save to cache
			if n_is_prime is None:
				n_is_prime = isPrime(n)
				cached_prime_numbers[n] = n_is_prime
				logger('\t\t\t\tBefore: {}'.format(current_set))
				multiples = generateMultiples(n, int(current_set_size / n) + 1)
				logger('\t\t\t\tThe multiples: {}'.format(multiples))
				current_set.difference_update(multiples)
				logger('\t\t\t\tAfter: {}'.format(current_set))
				already_removed = already_removed.union(multiples)
				logger('\t\t\t\tAlready removed: {}'.format(already_removed))
				if current_set == set():
					score_board[current_player] += 1
					logger(f"\t\t\tscore_board '{score_board}'")
			elif n_is_prime is True:
				logger('\t\t\t\tBefore: {}'.format(current_set))
				multiples = generateMultiples(n, int(current_set_size / n) + 1)
				logger('\t\t\t\tThe multiples: {}'.format(multiples))
				current_set.difference_update(multiples)
				logger('\t\t\t\tAfter: {}'.format(current_set))
				already_removed = already_removed.union(multiples)
				logger('\t\t\t\tAlready removed: {}'.format(already_removed))
				if current_set == set():
					score_board[current_player] += 1
					logger(f"\t\t\tscore_board '{score_board}'")
			current_player = switchPlayer(current_player)
		logger()
	scores = list(score_board.values())
	if scores[0] == scores[1]:
		return None
	elif scores[0] != scores[1]:
		biggest_score = max(scores)
		biggest_score_index = scores.index(biggest_score)
		winner_name = list(score_board.items())[biggest_score_index][0]
		return winner_name


if __name__ == '__main__':
	print(isWinner(5, [4, 5, 1]))
	# print(isPrime(1))
	# print(generateMultiples(5, 10))
	print(isWinner(5, [4, 5, 1, 1]))