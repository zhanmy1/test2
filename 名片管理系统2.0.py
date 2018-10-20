def print_menu():
	print("="*50)
	print("      名片管理系统      ")
	print(" 1.添加一个新的名片")
	print(" 2.删除一个名片")
	print(" 3.修改一个名片")
	print(" 4.查找一个名片")
	print(" 5.显示所有名片")
	print(" 6.退出系统")
	print("="*50)


#1.打印功能提示
print_menu()


#用来存储名片
card_infors = []

while True:
	#获取用户的输入
	num = int(input("请输入操作序号："))
	#根据用户的数据执行相应的功能

	if num==1:
		new_name = input("请输入新的名字：")
		new_QQ = input("请输入新的QQ：")
		new_sex = input("请输入性别：")
		new_addr = input("请输入新的住址：")

	#定义一个新的字典，用来储存一个新的名片

		new_infor = {}
		new_infor['name'] = new_name
		new_infor['QQ'] = new_QQ
		new_infor['sex'] = new_sex
		new_infor['addr'] = new_addr

	#将一个字典添加到列表中
		card_infors.append(new_infor)
		#print(card_infors)  #for test
		print("添加成功！")

	elif num==2:
		remove_name = input("请输入你要删除名片的名字：")
		remove_flag = 0 #默认没找到
		for temp in card_infors:
			if remove_name==temp['name']:
				card_infors.remove(temp)
				remove_flag = 1#表示找到了
				print("已删除！")
				#print(card_infors)
				break
		if remove_flag == 0:
			print("查无此人！")
	elif num==3:
		change_name = input("请输入你要修改名片的名字：")
		change_word = int(input("请输入你要修改的内容:1.名字 2.QQ 3.性别 4.住址:     "))

		#change_name_1 = input("请输入修改后的名字：")
		#change_QQ = input("请输入修改后的QQ")
		#change_sex = input("请输入修改后的性别")
		#change_addr = input("请输入修改后的住址")
		change_flag = 0#默认表示没找到
		for temp in card_infors:
			if change_name==temp['name']:
				if change_word==1:
					change_name_1 = input("请输入修改后的名字：")
					temp['name'] = change_name_1
				if change_word==2:
					change_QQ = input("请输入修改后的QQ")
					temp['QQ'] = change_QQ
				if change_word==3:
					change_sex = input("请输入修改后的性别")
					temp['sex'] = change_sex
				if change_word==4:
					change_addr = input("请输入修改后的住址")
					temp['addr'] = change_addr
				
			print("修改成功！")
				#print(card_infors)  #for test
			change_flag = 1
			break
		if change_flag==0:
			print("查无此人！")
				

	elif num==4:

		find_name = input("请输入要查找的姓名：")
		print("姓名\tQQ\t性别\t地址")
		find_flag = 0 #默认表示没有找到
		for temp in card_infors:
			if find_name == temp['name']:
				print("%s\t%s\t%s\t%s"%(temp['name'],temp['QQ'],temp['sex'],temp['addr']))
				find_flag = 1#表示已经找到了
				break
			#判断是否找到了
		if find_flag == 0:
			print("查无此人！")

	elif num==5:
		print("姓名\tQQ\t性别\t地址")
		for temp in card_infors:
			print("%s\t%s\t%s\t%s"%(temp['name'],temp['QQ'],temp['sex'],temp['addr']))


	elif num==6:
		print("成功退出！")
		break
	else:
		print("您的输入有误，请重新输入！")
	print("")

