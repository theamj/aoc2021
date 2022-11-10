
f = open('01des/data.txt',"r")
lines = f.readlines()
i = 0
forrige = 151

for m in lines :
    if int(m) > forrige : i = i+1

    forrige = int(m)
print (i) 