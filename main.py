f = open("this.txt","r")
data = f.read()
content = data.replace("Donkey","#####@@@")

f = open("this.txt","w")
data = f.write(content)
print(content)
f.close()
