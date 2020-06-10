import os

arr = map(str, range(2, 11))
arr.append("jack")
arr.append("ace")
arr.append("king")
arr.append("queen")

brr = ["_of_clubs", "_of_diamonds", "_of_hearts", "_of_spades"]

base_url = "https://raw.githubusercontent.com/hayeah"

for i in brr:
	for j in arr:
		name = base_url + "/playing-cards-assets/master/svg-cards/%s%s.svg" % (j, i)
		os.system("wget " + name)
