word1=input("enter first word:")
word2=input("enter another word:")
count=0
if (len(word1)==len(word2)):
    for x in word2:
        if word1.count(x)>0:
            count+=1
if count==len(word1):
    print("They are Anagram")
else:
    print("They are not Anagram")

