from PyDictionary import PyDictionary
dictionary=PyDictionary()
def search(a):
    x=dictionary.meaning(a)['Noun']
    print(x)
    for i in x:
        print(i)
a=input("enter a word")
search(a)