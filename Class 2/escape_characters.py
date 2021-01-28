my_text = "this is a quote symbol"

my_text2 = 'this is a quote " symbol'  #Bad Way

my_text3 = "this is a quote \" symbol"

my_text4 = "this is a \' \n quote \n symbol" #extra line

print(my_text)
print(my_text2)
print(my_text3)
print(my_text4)

print("*" * 10)


line_length = input("What length is the line?" >)
character = input("What character should I use?")

print(character*int(line_length))