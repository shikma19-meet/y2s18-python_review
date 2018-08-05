# # Write your solution for 1.1 here!
# # sum =0
# # for i in range(1,101):
# # 	if (i % 2 == 0):
# # 		sum = sum + i
# # 	else:
# # 		i = sum + i
# # print (sum)
# # number = 0
# # sum =0 
# # while (sum < 10000):
# # 	number = number +1
# # 	sum  = sum  + number 
# # print (number)

# def is_prime(x):
# 	check = True 
# 	y =x 
# 	while (x>0 and y>0):
# 		if (x % y ==0):
# 			y = y-1
			
# 		else:
# 			print ("this isn't a prime number, sorry :(")
# 			y = y-1
# 			check = False 
# 	return check 
			



# print(is_prime(6))

#making superheros 
class superheros :
	def __init__(self, name, superpower,strength ):
		self.name = name 
		self.superpower = superpower
		self.strength = int(strength)

	def print_about(self):
		print("my name is "+ self.name)
		print ("my superpower is "+ self.superpower)
		print("the amount of strength I have is "+ str(self.strength))
superhero = superheros("Jenny","the cat lover", 7)
superhero.print_about()