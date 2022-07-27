
changes = [500,100,50,10,5,1]

def main():
	money = int(input())
	money = 1000 - money
#	print(money)
	answer = 0

	for change in changes:
		while True:
			money -= change
			if(money < 0):
				money += change
				break
			answer += 1
#print(change,money)
	print(answer)

main()
	
