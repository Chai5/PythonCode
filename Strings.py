# it doesn't matter if you use simple or doble commas
str = 'simple message'
hello_msg = "hello "
result = hello_msg + str
# you can replace "\n" with other symbols that you use for edit the text
# result = str + "\n" + hello_msg
size = len(result)
letter = result[0]
letter = result[len(result)-1]
# use a negative index in order to print from right to left
letter = result[-2]
# use ":" to split a string
split = result[2:]                  #from the 2 element to the end 
split = result[:5]                  #from the first element to the 5 element
split = result[2:6]                 #from the second element to the 6 element
# use "::" to split a string in specific length
split = result[::-1]                #reverse the whole string
split = result[0:len(result)-1:2]   #take a element of the string each 2 index

# differents ways to print a string
print(result)
print(letter)
print(split)
print("leght of result:", len(result))
print(f"leght of result: {size}")
print("hello"[0])                   #one element of the string
print('hello'[1:3])