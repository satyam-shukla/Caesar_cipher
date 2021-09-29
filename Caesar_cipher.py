a=input("Enter any word :- ")
shift=int(input("Please enter your key :-"))
alp="abcdefghijklmnopqrstuvwxyz"
ctext="  "
new=0
for i in a:
	if i.lower() or i.upper() in a:
		new=alp.index(i) + shift
		ctext+=alp[new%26]
	else:
		ctext+=i
print("The ciphertext is :- " + ctext)