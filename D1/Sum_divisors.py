def sum_of_divisors(n):
	summ = 0
	i = n
	while i:
		if n % i == 0:
			summ += i
		i -= 1
	return summ
def main():
	print(sum_of_divisors(1000))
if __name__ == '__main__':
	main()