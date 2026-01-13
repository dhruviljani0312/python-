

ind=int(input("Enter iphone price in india ruppe:"))
usa=int(input("Enter iphone price in usa $:"))

ruppe=usa*90
print("usa $ convert into ruppe are:",ruppe)

if ind<ruppe:
    print("iphone buy in india")
else:
    print("iphone buy in usa")
