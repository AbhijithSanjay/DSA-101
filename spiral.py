mat = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]]
r=len(mat)
c=len(mat[0])
i,j=0,0
dr=[0,1,0,-1]
dc=[1,0,-1,0]
cp=[[False]*c for x in range(r)]
d=0
ar=[]
for x in range(r*c):
    ar.append(mat[i][j])
    cp[i][j]=True
    nr,nc=i+dr[d],j+dc[d]
    if 0<=nr<r and 0<=nc<c and cp[nr][nc]==False:
        i,j=nr,nc
    else:
        d=(d+1)%4
        i+=dr[d]
        j+=dc[d]
    
print(ar)





