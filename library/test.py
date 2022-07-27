

def main():
	warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
	subject = input("input sub : ")

	if subject in warn_investment_list:
		print("Warning!!!")
	else:
		print("Safe!!!")




main()
