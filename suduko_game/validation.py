def check():
    pass

def validate(dic):
    l=[[1,0,4,2,0,7,9,8,0],
       [0,8,0,0,0,0,6,0,2],
       [6,0,0,8,0,3,0,0,7],
       [0,0,0,9,4,1,0,6,0],
       [3,0,0,0,0,0,0,0,9],
       [0,7,0,6,3,5,0,0,0],
       [4,0,0,5,0,2,0,0,1],
       [2,0,7,0,0,0,0,9,0],
       [0,5,9,1,0,4,3,0,6]]
    for i in dic:
        num=int(i[3::])
        print(num)
        row=num//9
        column=(num-1)-(row*9)
        #print(row,column)
        l[row][column]=int(dic[i])
        value=check(l)
        if value:
            pass
        else:
            return False



if __name__=="__main__" :
    dic={'num12':2}
    validate(dic)