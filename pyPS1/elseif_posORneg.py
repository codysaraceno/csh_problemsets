#!/usr/bin/env python3

age = 50

if age < 0:
	print('Positive age. You were born 32 years ago')

#elif age > 50 and age%3 == 0:
	#print('you are greater than 50 and divisible by 3')

#elif age%3 == 0:
	#print('You are divisible by 3!')

#elif age > 50:
	#print('you have one foot in the grave :")')

#elif age < 50 and age%2 == 0:
	#print('you are young and even :)')

#elif age%2 == 0:
	#print('you are even stevens') 

#elif age == 0:
	#print('You are currently being born! ah!')

elif age > 0:
	print('yes, it" s positive')
	if age < 50:
		print('yes, it is less than 50')
	if age < 49:
		print('yes, less than 49 too')
	if age%2 == 0:
		print('yes, it is also even')
	if age < 50 and  age%2 == 0:
		print('yes, it is an even number that is smaller than 50')

elif age < 50:
	print('ok, you" re not THAT old')

else:
	print('Negative age. You will be born in 32 years')
