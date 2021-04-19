wanking = input('你有沒有打過手槍呢？')
if wanking != '有' and wanking != '沒有':
	print('只能輸入有或沒有')
	raise SystemExit 
age = input('你現在幾歲？')
age = int(age)
if 	wanking == '有':
	if age >= 18:
		print('那你可以打了!')
	else:
		print('偷打手槍！')
elif wanking == '沒有':
	if age >= 18:
		print('打起來！')
	else:
		print('不可以偷打喔！')