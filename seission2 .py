contacts={"mohamed":"01043530807","Ahmad":"01154367891","Ayman":"01567891290"}
print(contacts.keys())
name=input("mohamed")
if name in contacts:
    print("{contacts [name]}")
else:
    print("this name is not in this contact")