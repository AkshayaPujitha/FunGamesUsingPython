def validation(l):
    for i in range(0,3):
        if l[i][0]==l[i][1]==l[i][2] and l[i][0]!=" " and l[i][1]!=" " and l[i][2]!=" ":
            return 1
    for j in range(0,3):
        if l[0][j]==l[1][j]==l[2][j] and l[0][j]!=" " and l[1][j]!=" " and l[2][j]!=" ":
            return 1
    if l[0][0]==l[1][1]==l[2][2] and l[0][0]!=" " and l[1][1]!=" " and l[2][2]!=" ":
        return 1
    if l[0][2]==l[1][1]==l[2][0] and l[0][2]!=" " and l[1][1]!=" " and l[2][0]!=" ":
        return 1
    return 0


def tic_tac_toe(ch,l,num,turn):
    if num==0 or num>9:
        print("Invalid Input")
        return 0
    i=((num+2)//3)-1
    j=(num)%3
    if j==0:
        j=2
    else:
        j-=1
    if l[i][j]!=" ":
        print("OOPS!!Block is already Selected")
        return 0
    l[i][j]=ch
    #print(l)

    for i in range(0,3):
        print(" ------ ")
        print(" {}|{}|{} ".format(l[i][0],l[i][1],l[i][2]))

    val=validation(l)
    if val==0:
        return 1
    else:
        c=(turn%2)+1
        print("Player {} Won!!!!!".format(c))
        exit()



print("Welcome To Tic Tac Toe!!!!")
print("Select the block number ranging (0-9)")
print("-----------")
print(" 1 | 2 | 3 ")
print("-----------")
print(" 4 | 5 | 6 ")
print("-----------")
print(" 7 | 8 | 9 ")
#l = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print("For instance if player selects 9")
print("-----------")
print("   |   |   ")
print("-----------")
print("   |   |   ")
print("-----------")
print("   |   | X ")
l=[[" "," "," "],[" "," "," "],[" "," "," "]]
m=[]
turn=0
while True:
    if len(m)==9:
        print("Draw Match")
        break
    if turn%2==0:
        num=int(input("(Player 1)Select the block:"))
        m.append(num)
        ch="X"
        turn+=tic_tac_toe(ch,l,num,turn)
    else:
        num=int(input("(Player 2)Select the block:"))
        m.append(num)
        ch="O"
        turn+=tic_tac_toe(ch,l,num,turn)

#Things to be done Validation has to be given ,condition checking ,Invalid Inuput





