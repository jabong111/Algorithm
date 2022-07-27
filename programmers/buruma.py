
def solutino(n, lost, reserve):
	answer = 0
	_lost = set(lost) - set(reserve)
	_reserve = set(reserve) - set(lost)

	print(_lost)
	print(_reserve)

	for person in _reserve:
		b = person + 1
		f = person - 1

		if f in _reserve:
			_lost.remove(f)
		elif b in _reserve:
			_lost.remove(b)

	answer = n - len(_lost)
	print(answer)

	
	return answer


n = int(input())

lost = input().split(" ")

for i in range(len(lost)):
	lost[i] = int(lost[i]) 

reserve = input().split(" ")

for i in range(len(reserve)):
	reserve[i] = int(reserve[i]) 

main(n,lost,reserve)
