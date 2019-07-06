f1=input()
h1=1
for d1 in range (len(f1)-1):
  hp=f1[d1]+f1[d1+1]
  m1=int(hp)
  if m1<=26 and f1[d1]!="0":
      h1+=1
if h1==3:
  print(h1)
else:
  print(h1+(h1-1)//2)
