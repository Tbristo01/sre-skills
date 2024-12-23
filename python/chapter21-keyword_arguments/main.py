# keyword arguments = an argument preceded by an identifier . 
# helps with readability 
# order of the arguments doesnt matter 
# 1.positional , 2.defautl ,3.keyword,4.arbitrary 


def hello(greeting , title , first , last):
    print(f"{greeting} {title}.{first} {last}")


hello(greeting="Hello",title="Mr",first="Spongbob",last="Squarepants")


for x in range(1,11):
    print(x,end=" ")

print()

print("1","2","3","4","5",sep="-")



def get_phone_number(country , area , first, last):
        return f"{country}-{area}-{first}-{last}"


phoneNumber=get_phone_number(country=1,area=212,first=867,last=2121)

print(phoneNumber)