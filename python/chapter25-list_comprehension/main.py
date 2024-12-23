# list comprehension = A concise way to create lists in python 
# compact and easier to read than traditional loops 
# [expression for value  in iterable if condition]


doubles =[]

# for x in range(1,11):
#     doubles.append(x*2)

# print(doubles)

# print()


# doubles=[expression for value in iterable]
# doubles=[expression for x in range(1,11)]
# doubles=[x*2 for x in range(1,11)]

doubles=[x*2 for x in range(1,11)]

print(doubles)

triples=[x*3 for x in range (1,25)]
print(triples)

squares=[z**2 for z in range(1,24)]
print(squares)


fruits =["apple","orange","banana","coconut"]

fruits=[ fruit.upper() for fruit in fruits]
print(fruits)


fruits_chars = [fruit[0] for fruit in fruits]
print(fruits_chars)


numbers = [1,-2,3,-4,5,-6]
postivie_nums = [num for num in numbers if num >= 0]
print(postivie_nums)


numbers = [1, -2, 3, -4, 5, -6]
negative_nums = [num for num in numbers if num < 0]
print(negative_nums)


numbers = [1, -2, 3, -4, 5, -6,8,12,-14]
even_nums = [num for num in numbers if num%2== 0]
print(even_nums)



grades =[85,43,75,90,61,100,33,15]


passing_grade=[grade for grade in grades if grade>=60]
print(passing_grade)