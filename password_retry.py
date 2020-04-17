password = 'a123456'
guess = 3

while guess > 0:
	guess = guess - 1 #每問一次密碼就用掉一次剩餘機會
	user_input = input('請輸入密碼(最多輸入三次)：')
	if user_input == password:
		print('登入成功！')
		break
	else:
		print('密碼錯誤!')
		if guess > 0:
			print('還有', guess, '次機會')
		else:
			print('沒機會嘗試了!')

