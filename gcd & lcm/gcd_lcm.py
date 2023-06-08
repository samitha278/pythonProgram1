def main():
	n1 = int(input())
	n2 = int(input())

	dic1 = prime_fact(n1)
	dic2 = prime_fact(n2)

	print(f"gcd of {n1} & {n2}: {gcd(dic1,dic2)}")
	print(f"lcm of {n1} & {n2}: {lcm(dic1,dic2)}")

	return 0

def gcd(dic1,dic2):

	set1 = {i for i in dic1.keys()}
	set2 = {i for i in dic2.keys()}

	inte_lst = list(set1.intersection(set2))

	gcd_value = 1
	for i in inte_lst:
		gcd_value *= i * min(dic1[i],dic2[i])

	return gcd_value

def lcm(dic1,dic2):

	set1 = {i for i in dic1.keys()}
	set2 = {i for i in dic2.keys()}

	union_lst = list(set1.union(set2))

	lcm_value = 1
	for i in union_lst:
		lcm_value*=i

	return lcm_value

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
