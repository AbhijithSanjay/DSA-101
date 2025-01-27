mat = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]]
r=len(mat)
c=len(mat[0])
mr,mc,mxr,mxc=0,0,r-1,c-1
ar=[]
while(len(ar)<r*c):
    for j in range(mc,mxc+1):
        ar.append(mat[mr][j])
    mr+=1
    for i in range(mr,mxr+1):
        ar.append(mat[i][mxc])
    mxc-=1
    for j in range(mxc,mc-1,-1):
        ar.append(mat[mxr][j])
    mxr-=1
    for i in range(mxr,mr-1,-1):
        ar.append(mat[i][mc])
    mc+=1
print(ar)

