import random
def flipCoin():
    x=random.randrange(2)
    if x==1:
        return("heads")
    else:
        return("tails")
def casino(money):#money is in cents
    head=0
    ormoney=money
    for i in range(0,300):
        if money<100:
            return ([i,head,ormoney-money])
        else:
            money=money-100
            x= flipCoin()
            if x=="heads":
                money=money+120
                head=head+1
    return ([i,head,ormoney-money])
def eveningAtCasino(list):
    totalflip=0
    head=0
    money=0
    for x in list:
        totpos=totpos+x
        y=casino(x)
        totalflip=totalflip+y.pop(0)
        head=head+y.pop(0)
        money=money+y.pop(0)
    print("total possible: "+totpos+" Coin flips: "+str(i)+" Heads: "+str(head)+" Money: "+str(money))
lists=[]
while true
    nb = input('Choose a number if 0 then quit')
    if nb<=0:
        break
  lists.append(nb)  
eveningAtCasino(lists)
