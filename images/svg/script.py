import os

arr = map(str,range(2,11))
arr.append("jack")
arr.append("ace")
arr.append("king")
arr.append("queen")

brr = ["_of_clubs","_of_diamonds","_of_hearts","_of_spades"]

for i in brr:
	for j in arr:
		name = "https://raw.githubusercontent.com/hayeah/playing-cards-assets/master/svg-cards/"+j+i+".svg"
		os.system("wget " + name)