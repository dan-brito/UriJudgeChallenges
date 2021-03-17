X = int(input())

count = 0
odds = []
while len(odds) < 6:
    if (X + count) % 2 != 0:
        odd = X+count
        print(odd)
        odds.append(odd)
        count +=1
    else:
        count +=1
  



