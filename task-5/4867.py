ans = []
for N in range(2,10000):
    sum1= sum(int(i) for i in str(N) if int(i) %2 == 0)
   # sum2 = sum(map(lambda x:int(x) if int(x) %2 == 0, else 0, str(N))
   sum2 = sum(map(int,str(N)[1::2]))
  # sum3 = sum(int(str(N)[i]) for i in str(N) if range(len(str(N))) if i % 2 !=0 )
  R = abs(sum1 -sum2)
  if R == 9:
      print(N)
      break