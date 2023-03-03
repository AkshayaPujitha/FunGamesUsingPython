import numpy as np

l=[[1,0,4,2,0,7,9,8,0],
       [0,8,0,0,0,0,6,0,2],
       [6,0,0,8,0,3,0,0,7],
       [0,0,0,9,4,1,0,6,0],
       [3,0,0,0,0,0,0,0,9],
       [0,7,0,6,3,5,0,0,0],
       [4,0,0,5,0,2,0,0,1],
       [2,0,7,0,0,0,0,9,0],
       [0,5,9,1,0,4,3,0,6]]
def check(grid,row,column,number):
    r=row
    c=column
    for i in range(0,9):
        if grid[row][i]==number and i!=column:
            print("in row")
            return False
    #checks the column
    for i in range(0,9):
        if grid[i][column]==number and i!=row:
            print("In column")
            return False
    row=row//3
    column=column//3
    if row==1:
        row=3
    elif row==2:
        row=6
    if column==1:
        column=3
    elif column==2:
        column=6
    #checks 3X3 square grid
    for i in range(row,row+3):
        for j in range(column,column+3):
            if  (i!=r and j!=c) and  grid[i][j]==number:
                #print(i,j)
                print("here 3X3")
                return False
    
    return True

def validate(existed):
    global l
    #print(l)
    if len(existed)!=0:
        for i in existed:
            
            num=int(i[3::])

            row=num//9
            if num%9==0:
                row=row-1
            column=(num-1)-(row*9)
            if existed[i]=='':
                l[row][column]=0
                continue
            l[row][column]=int(existed[i])
    print(np.matrix(l))
    flag=1
    error=[] 
    validated=[]
    #print(dic,"dixdd")
    for i in existed:
        num=int(i[3::])
        #print(num)
        row=num//9
        if num%9==0:
            row=row-1
        column=(num-1)-(row*9)
        #print(row,column)
        try:
            x=int(existed[i])
        except:
            continue
        value=check(l,row,column,x)
        #print(value)
        if value:
            l[row][column]=int(existed[i])
            validated.append(i)
            pass
        else:
            flag=0
            l[row][column]=int(existed[i])
            error.append(i)
    if flag==0:
        return False,error
    return True,validated


if __name__=="__main__" :
    dic={'num1':3,'num2':2,'num3':3}
    m=validate(dic)
    print(m)