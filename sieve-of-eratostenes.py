# Find last mark
def find_last_mark(n, n_list):
	for number in n_list:
		if number**2 <= n:
			last_mark = number
		else:
			break
	
	return last_mark

# Delete multiples of current_mark in n_list
def delete_multiples(current_mark, n_list):	
	for x in n_list:
		if x%current_mark == 0 and x != current_mark:
			n_list.remove(x)

	return n_list

def main():
	# Input n size of the list, generate it and convert to int
	n = int(input("\nEnter n: "))
	n_list = list(range(2,n+1))

	print("\nThe list generated is: " + str(n_list))

	last_mark = find_last_mark(n, n_list)

	for number in n_list:
		current_mark = number
		if (current_mark > last_mark):
			break

		n_list = delete_multiples(current_mark, n_list)
	
	print("\nThe list of prime numbers is: " + str(n_list) + "\n")

if __name__ == '__main__':
	main()