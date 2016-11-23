import random
import json
import os.path
import collections
def countLetters(word,let):
    count=0
    for letter in word:
        if(letter==let):
            count+=1
    return count
def examiner():
    print("1. Frequencies:{'a':.1,'b':.3,'c':.6}, Length:50,  Samples:3")
    print("2. Frequencies:{'a':.9,'b':.05,'c':.05}, Length:50,  Samples:3")
    user= input("Which one would you like to examine (enter 0 to exit)?")
    if(user=="1"):
        x=generator({"a":.1,"b":.3,"c":.6},50)
        a=countLetters(x,"a")
        a = float("{0:.2f}".format(a))
        b=countLetters(x,"b")
        b = float("{0:.2f}".format(b))
        c=countLetters(x,"c")
        c = float("{0:.2f}".format(c))
        print("|  a  |  b  |  c  |")
        print("-------------------")
        print("|"+str(a/50)+" |"+str(b/50)+" |"+str(c/50)+" |")
        x=generator({"a":.1,"b":.3,"c":.6},50)
        a=countLetters(x,"a")
        a = float("{0:.2f}".format(a))
        b=countLetters(x,"b")
        b = float("{0:.2f}".format(b))
        c=countLetters(x,"c")
        c = float("{0:.2f}".format(c))
        print("|"+str(a/50)+" |"+str(b/50)+" |"+str(c/50)+" |")
        x=generator({"a":.1,"b":.3,"c":.6},50)
        a=countLetters(x,"a")
        a = float("{0:.2f}".format(a))
        b=countLetters(x,"b")
        b = float("{0:.2f}".format(b))
        c=countLetters(x,"c")
        c = float("{0:.2f}".format(c))
        print("|"+str(a/50)+" |"+str(b/50)+" |"+str(c/50)+" |")
    elif(user=="2"):
        x=generator({"a":.9,"b":.05,"c":.05},50)
        a=countLetters(x,"a")
        a = float("{0:.2f}".format(a))
        b=countLetters(x,"b")
        b = float("{0:.2f}".format(b))
        c=countLetters(x,"c")
        c = float("{0:.2f}".format(c))
        print("|  a  |  b  |  c  |")
        print("-------------------")
        print("|"+str(a/50)+" |"+str(b/50)+" |"+str(c/50)+" |")
        x=generator({"a":.9,"b":.05,"c":.05},50)
        a=countLetters(x,"a")
        a = float("{0:.2f}".format(a))
        b=countLetters(x,"b")
        b = float("{0:.2f}".format(b))
        c=countLetters(x,"c")
        c = float("{0:.2f}".format(c))
        print("|"+str(a/50)+" |"+str(b/50)+" |"+str(c/50)+" |")
        x=generator({"a":.9,"b":.05,"c":.05},50)
        a=countLetters(x,"a")
        a = float("{0:.2f}".format(a))
        b=countLetters(x,"b")
        b = float("{0:.2f}".format(b))
        c=countLetters(x,"c")
        c = float("{0:.2f}".format(c))
        print("|"+str(a/50)+" |"+str(b/50)+" |"+str(c/50)+" |")
    elif(user!="0"):
        examiner()

def experimenter(dics, lens, samp):
    with open("datafile.txt","w") as f:
        f.write(generator(dics, lens)+"\n")
    if samp>1:
        experimenters(dics, lens, samp-1)
def experimenters(dics, lens, samp):
    with open("datafile.txt","a") as f:
        f.write(generator(dics, lens)+"\n")
    if samp>1:
        experimenters(dics, lens, samp-1)
def generator(dics, lens):
    a=0
    at=""
    b=0
    bt=""
    c=0
    ct=""
    i=0
    results=""
    for name, age in dics.items():
        if i==0:
            a=age*100
            at=name
        if i==1:
            b=age*100
            bt=name
        if i==2:
            c=age*100
            ct=name
        i+=1
    for x in range(0, lens):
        y=random.randint(0,100)
        if(y<=a):
            results+=at
        elif(y<a+b):
            results+=bt
        elif(y<=a+b+c):
            results+=ct
    return results
generator({"a":.1,"b":.3,"c":.6},50)
def compressor(s):
    count=0
    last=""
    tcount=0
    result=""
    for c in s:
        if count==0:
            last=c
            result+=c
        elif last==c:
            tcount+=1
        else:
            if tcount>0:
                result+=str(tcount)
            tcount=0
            last=c
            result+=last
        count+=1
    return result
def decompressor(s):
    last=""
    result=""
    count=0
    for c in s:
        if count==0:
            last=c
            result+=c
        elif c.isdigit():
            result+=last*int(c)
        else:
            last=c
            result+=last
        count+=1
    return result
x=compressor('aaaaaaabaaaaaacaaaaaaaaaaaaaaaaaaabaaaaaaaabaabaca')
decompressor(x)
