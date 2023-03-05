#!/usr/bin/python3
"""
0. Minimum Operations
"""


def minOperations(n):
	'''List out and Check the combinations
	of all valid copy paste operations'''
	CopyAll = '1'
	Paste = '0'
	refined = []
	for combination in range(2**n):
		str_bin_combo = str(bin(combination))
		val = list(str_bin_combo.split('b')[1])
		for i in range(n):
			operation = val[i]
			if (i + 1) < len(val):
				next_operation = val[i + 1]
			else:
				if len(val) > 1 and val[len(val) - 1] != CopyAll:
					refined.append(val)
				break
			if operation == CopyAll and next_operation != Paste:
				break
			if operation == Paste and i == 0:
				break
	final_list = []
	for combination in refined:
		char = 'H'
		clipboard = ''
		operation_info = {}
		operation_info['operations'] = []
		operation_info['operation_count'] = 0
		for each_operation in combination:
			if each_operation == CopyAll:
				clipboard = char + ''
				operation_info['operation_count'] += 1
				operation_info['operations'].append(each_operation)

			elif each_operation == Paste:
				char = char + clipboard
				operation_info['operation_count'] += 1
				operation_info['operations'].append(each_operation)
		operation_info['char'] = char
		operation_info['char_count'] = len(char)
		final_list.append(operation_info)
	
	filtered_operation_counts = []
	for each in final_list:
		if each['char_count'] == n:
			# print(each)
			filtered_operation_counts.append(each['operation_count'])
	# print(filtered_operation_counts)
	min_ops_count = min(filtered_operation_counts)
	# print(f'Minimum operation: {min_ops_count}')
	# print()
	return min_ops_count


if __name__ == '__main__':
	minOperations(9)
	minOperations(4)
	minOperations(12)
