#program to implement longest common subsequence
def lcs(s1,s2,x,y):
    x=len(s1)
    y=len(s2)
    arr=[[0 for m in range(y+1)]for m in range(x+1)]
    #building the matrix in bottom-up way
    for i in range (x+1):
        for j in range (y+1):
            #to fill 0th column and 0th row with zero
            if i==0 or j==0:
                arr[i][j]=0
            #matched case:
            elif s1[i-1]==s2[j-1]: 
               arr[i][j]=1+arr[i-1][j-1]
            #unmatched case:
            else:
               arr[i][j]=max(arr[i-1][j],arr[i][j-1])
    return arr[i][j]        
#driver program 
s1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s2="KEERTHI"
x=len(s1)
y=len(s2)
print("length of the searcg string:",lcs(s1,s2,x,y))



