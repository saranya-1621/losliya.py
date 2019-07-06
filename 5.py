afs=input()
ahs=1
for d1 in range (len(afs)-1):
  aph=afs[d1]+afs[d1+1]
  m1=int(aph)
  if m1<=26 and afs[d1]!="0":
      ahs+=1
if ahs==3:
  print(ahs)
else:
  print(ahs+(ahs-1)//2)
