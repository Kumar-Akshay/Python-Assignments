
print ("\nEight Queen Problem \n")
#Domain of CSP
Domain=8

#chessboard with N*N and initial assign every square 0
chessboard = [[0]*Domain for _ in range(Domain)]

for i in chessboard:
    print (i)
print("\n\n Wait Solution in Process and 1 Means Queen position 0 means Empty\n")

def Queen(n):
    #if n is 0, solution found
    if n==0:
        return True
    for i in range(0,Domain):
        for j in range(0,Domain):

	# Checking place a queen put here or not.
    # Queen will not be placed if the place is being attacked or already occupied than Backtracking it.
            if (not(check_constraint(i,j))) and (chessboard[i][j]!=1):
                chessboard[i][j] = 1
                if Queen(n-1)==True: #recusrion n-1
                    return True
                chessboard[i][j] = 0

    return False


# Checking Constraint of Queen to Digonal and Row and Column
def check_constraint(i,j):
	#if there is a queen in row or column attack
    for k in range(0,Domain):
        if chessboard[i][k]==1 or chessboard[k][j]==1:
            return True
		
	#if there is a queen in diagonals attack
    for k in range(0,Domain):
        for l in range(0,Domain):
            if (k+l==i+j) or (k-l==i-j):
                if chessboard[k][l]==1:
                    return True
    return False

#Functional Call Queen()
Queen(Domain)
#Print Solution
for i in chessboard:
    print (i)
print("\nSolution \n")