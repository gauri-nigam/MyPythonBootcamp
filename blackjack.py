def blackjack(a,b,c):
	re=sum([a,b,c])

	if re <= 21:
		return re
	else:
		if 11 in [a,b,c]:
			re = re-10
			if re <= 21:
				return re
		else:
			return "Bust"
	
print(blackjack(9,9,11))