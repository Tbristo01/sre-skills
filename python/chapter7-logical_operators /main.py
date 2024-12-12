# Logical Operator = evaluate multiple conditions ( or , and , not)
# or = at least one condition must be true 
# and = both conditions must be True 
# not = inverts the condition ( not False , not True)


# temp = 25
# is_raining = True

# if temp > 35 or temp<0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The ourdoor event is still scheduled")



temp =-1
is_sunny= False

if temp >=28 and is_sunny:
    print("It is HOT outside" )
    print("It is SUNNY" )
elif temp <=0 and is_sunny:
    print("It is COLD outside")
    print("It is SUNNY")
elif temp<28 and temp>0 and is_sunny:
    print("It is WARM outside")
    print("It is SUNNY")
elif temp <=0 and not is_sunny:
    print("It is COLD outside")
    print("It is CLOUDY")
elif temp<28 and temp>0 and not is_sunny:
    print("It is WARM outside")
    print("It is CLOUDY")