import random
def player():
    ok=1
    while(ok==1):
        print("what do you want to play?")
        q=int(input("1.ROCK 2.PAPER 3.SCISSOR 4.GIVE UP"))
        if(q==4):
            print("enna bayanthutiya kolantha?? HAHAHHAAAA")
            exit()
        if(q>4 or q<1):
            ok=1
            print("thappu thappa input kudutha manda melaye adippen")
        else:
            ok=0
    return q
def ai():
    e=0
    e=random.randint(1,3)
    return e

def checker(z,x):
    p=0
    a=0
    print(z,x)
    if(z==1 and x==3):
        p=1
        a=0
        return p,a
    if(z==2 and x==1):
        p=1
        a=0
        return p,a
    if(z==3 and x==2):
        p=1
        a=0
        return p,a
    if(x==1 and z==3):
        a=1
        p=0
        return p,a
    if(x==2 and z==1):
        a=1
        p=0
        return p,a
    if(x==3 and z==2):
        a=1
        p=0
        return p,a
    else:
        a=0
        p=0
        return p,a

game=int(input("number of games you want to play?"))
j=0
for j in range(game):
    app=0
    apa=0
    t=player()
    if(t==1):
    	print("YOUR MOVE : ROCK")
    if(t==2):
    	print("YOUR MOVE : PAPER")
    if(t==3):
    	print("YOUR MOVE : SCISSOR")
    y=ai()
    if(y==1):
    	print("AI MOVE : ROCK")
    if(y==2):
    	print("AI MOVE : PAPER")
    if(y==3):
    	print("AI MOVE : SCISSOR")
    pp,pa=checker(t,y)
    app+=pp
    apa+=pa
    if(j==(game-1)):
        if(app>apa):
            print("u win")
            print("UR POINT:",app)
            exit()
    if(j==(game-1)):
        if(apa>app):
            print("lol ai won HAHAHAAA!")
            print("U LOST BY:",(apa-app))
            exit()
    if(j==(game-1)):
        print("tie")
        print("AI AND PLAYER POINT:",app)
        exit()


    