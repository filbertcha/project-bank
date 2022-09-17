x = input("say :").lower().strip()
say = x[0 : 10]
if (say[0 : 5]== "hello") :
    print("$0")
elif (say[0] == "h") and not ( say == "hello") :
    print("$20")
else :
    print("$100")
