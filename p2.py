#write program to convert 4 digit amount into words

number = input("enter four digit amount")
number =int(number)

first=number//100
mid1=(number%1000)//100
mid2=(number%100)//10
last=number%10


words=['zero ','one ','two ','three ','four ','five ','six ','seven ','eight ','nine ']
print(words[first] ,words[mid1] ,words[mid2] ,words[last])