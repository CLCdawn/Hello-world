

def convert_roma_number_to_integer(str):
	def numlize(a):
		if a == 'I':
			a = "1"
		elif a == 'V':
			a = "5"
		elif a == 'X':
			a = "10"
		elif a == 'L':
			a = "50"
		elif a == 'C':
			a = "100"
		elif a == 'D':
			a = "500"
		else:
			a = "1000"
		return a
	list_str = list(str)
	list_str0 = []
	num = 0

	for i in list_str:
		list_str0.append(int(numlize(i)))
	# 将字符转换为数字

	if len(str)==1:
		num = list_str0[0]
	else:
		for i in range(0, len(str)-1):
			if list_str0[i]<list_str0[i+1]:
				if list_str0[i]== 1 or list_str0[i] == 10 or list_str0[i] == 100:
					list_str0[i] = list_str0[i+1]-list_str0[i]
					list_str0[i+1] = 0
				else:
					pass
			else:
				pass
		for i in list_str0:
			num = num + i

	return num



def convert_integer_to_roma_number(i):
	list_num = []
	while i>0:
		a = i%10
		list_num.append(a)
		i = i//10
	list_num.reverse()
	def change(s):
		if s == 1:
			a1 = "I"
		elif s == 2:
			a1 = "II"
		elif s == 3:
			a1 = "III"
		elif s == 4:
			a1 = "IV"
		elif s == 5:
			a1 = "V"
		elif s == 6:
			a1 = "VI"
		elif s == 7:
			a1 = "VII"
		elif s == 8:
			a1 = "VIII"
		else:
			a1 = "IX"
		return a1

	if len(list_num)==1:
		a = change(list_num[0])

	elif len(list_num)==2:
		a1 = change(list_num[-1])
		a2 = change(list_num[-2])
		a2 = a2.replace("I","X").replace("V","L")
		a = str(a2+a1)

	# elif len(list_num)==3:
	# 	a1 = change(list_num[-1])
	# 	a2 = change(list_num[-2])
	# 	a2 = a2.replace("I","X").replace("V","L")
	# 	a3 = change(list_num[-3])
	# 	a3 = a3.replace("I","C").replace("V","D")
	# 	a = str(a3+a2+a1)

	else:
		a =""

	return a
