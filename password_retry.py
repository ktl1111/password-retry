password = 'a123456'
guess = 3

while guess > 0:
	user_input = input('請輸入密碼(最多輸入三次)：')
	if user_input == password:
		print('登入成功！')
		break
	else:
		guess = guess - 1
		print('密碼錯誤，還有', guess, '次機會')
