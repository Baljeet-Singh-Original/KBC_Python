question= [
	"How many continents are there?",  
	"What is the capital of India?",
	"NG mei kaun se course padhaya jaata hai?"
]

option= [
	["Four", "Nine", "Seven", "Eight"], 
	["Chandigarh", "Bhopal", "Chennai", "Delhi"],
	["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
solution = [3, 4, 1]
n=0
k=1
for i in question:
	print("Aapka Sawal hai: ")
	print(i)
	print("Aapke options hain: ")
	for i in option[n]:
		if k==5:
			k=1
		print(k, i)
		k+=1
		
	inp=int(input())
	if inp==solution[n]:
		print("sahi hai")
	else:
		print("galat hai")
		print("Aap haar gye")
		break
	n+=1