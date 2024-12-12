# indexing = accessing elements of a sequence using [] (indexing operators)
# [start:end:skip]
# not counting starts at 0
credit_number="1234-5678-9012-3452"

# first char in string 
print(credit_number[0])

# first 4 numbers of a string 
print(credit_number[:4])
print(credit_number[5:9])
print(credit_number[5:])

# find the last char of a string 
print(credit_number[-1])

# step using indexing of a string
print(credit_number[::2])

# printing the last 4 of string using negative indexing 
last_digits=credit_number[-4:]
print(f"xxxx-xxxx-xxxx-{last_digits}")

# reversing string usign negative step
credit_number=credit_number[::-1]
print(credit_number)