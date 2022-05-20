def PerkalianMatriks(A,B,D):
    for i in range(0,len(A[0])):
        D_Sementara=[]
        for j in range(0,len(A[0])):
            total=0
            for k in range(0,len(B)):
                total = total + A[i][k] * B[k][j]

                D_Sementara.append(total)
            D.append(D_Sementara)