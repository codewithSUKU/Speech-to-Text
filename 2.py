from textblob  import TextBlob

file1=open("2.txt","r+")
a=file1.read()


print("orginal text : "+str(a))

b=TextBlob(a)

print("corrected text : "+str(b.correct()))

file1.close()

d=open("2.txt","w")
d.write(str(b.correct()))
d.close()