def main():
	n1 = int(input())
	n2 = int(input())

	print(gcd(n1,n2))

def gcd(n1,n2):

	dic1 = prime_fact(n1)
	dic2 = prime_fact(n2)

	set1 = {i for i in dic1.keys()}
	set2 = {i for i in dic2.keys()}

	inte_lst = list(set1.intersection(set2))

	gcd_value = 1
	for i in inte_lst:
		gcd_value *= i * min(dic1[i],dic2[i])

	return gcd_value


def prime_fact(n):
	prime_nums = [2,3,5,7,11,13,17,19,23,29]

	pfDic = {}
	temp = n 
	counter = 0

	while temp!=1:
		remain = temp%prime_nums[counter]

		if remain == 0:
			try:
				pfDic[prime_nums[counter]] += 1
			except:
				pfDic[prime_nums[counter]] =1
			temp = temp//prime_nums[counter]
		else:
			counter+=1

	return pfDic


if __name__ == '__main__':
	main()
