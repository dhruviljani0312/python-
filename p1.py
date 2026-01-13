#write program to convert 3 digit amount into words

number = input("enter 3 digit amount:")
number=int(number)

first=number//100
mid=(number%100)//10
last=number%10

words=['zero ','one ','two ','three ','four ','five ','six ','seven ','eight ','nine ']
print(words[first],words[mid],words[last])