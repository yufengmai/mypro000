#!/usr/bin/python
#coding=utf-8
import random
your_choice = 1
while your_choice != 33:
	your_choice = int(input("请输入：剪刀(0),石头(1),布(2):"))
	computer_choice = random.randrange(0,3)
	print ("your_choice={}".format(your_choice))
	print ("computer_choice={}".format(computer_choice))

	if your_choice == computer_choice:
		print("平局，要不再来一局")

	elif your_choice == 0 and computer_choice ==1:
		print("输了，不要走，洗洗手接着来，决战到天亮")
	elif your_choice == 0 and computer_choice ==2:
		print("赢了")

	elif your_choice == 1 and computer_choice ==2:
		print("输了，不要走，洗洗手接着来，决战到天亮")
	elif your_choice == 1 and computer_choice ==0:
		print("赢了")
		
	elif your_choice == 2 and computer_choice ==0:	
		print("输了，不要走，洗洗手接着来，决战到天亮")
	elif your_choice == 2 and computer_choice ==1:
		print("赢了")
