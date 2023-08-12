f = open("C:\\Users\\ghant\\OneDrive\\Desktop\\CD programs\\manu.txt" ,"r")
data=f.read()
sp=data.split()
w={}
for i in sp:
    if i in w:
        w[i]+=1
    else:
        w[i]=1
print(w)
for i , j in w.items():
    print(f"{i}:{j}")
