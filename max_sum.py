#Created by Drumil Mahajan
# New York University, November 2016

#The max_sum array is a two dimensional array of size n*m which contains the maximum sum 
#that can be acheieved till you reach node i,j where 0 <= i <= n and 0 <= j <= m 


def maximum_sum(p):
    
    max_sum =  [[0]*len(p[0]) for i in range(len(p))]
    
    for j in range(0,len(p[0])):
        for i in range(0,len(p)):            
            if i == 0 and j == 0:
                max_sum[i][j] = p[i][j]
            
            elif i == 0 and j > 0:
                max_sum[i][j] = p[i][j] + max_sum[i][j-1] 
                
            elif j == 0 and i > 0:                        
                max_sum[i][j] = p[i][j] + max_sum[i-1][j]     
            
            if i>0 and j>0:
                if max_sum[i-1][j] > max_sum[i][j-1]:
                    max_sum[i][j] = max_sum[i-1][j] + p[i][j] 
                else:
                    max_sum[i][j] = max_sum[i][j-1] + p[i][j]
                               
    return max_sum[len(p)-1][len(p[0])-1]                
                        

 

def main():
    
    rows = int(raw_input("Enter the number of rows in the matrix "))
    columns = int(raw_input("Enter the number of columns in the matrix "))
    matrix = []
    for i in range(0,rows):
        row = raw_input("Enter the " + str(i+1) + " row. Each row will have " + str(columns) + " elements.").split()
        row = [int(i) for i in row]
        matrix.append(row)
    #print matrix
    #max_sum =  [[0]*len(matrix[0]) for i in range(len(matrix))]
    #print max_sum
    print maximum_sum(matrix)
      
main()      
      
        

'''
    
    *****************************************
    *                                       *
    *       Pseudo Code for max_sum         *
    *                                       *                    
    *****************************************


MAXIMUM-SUM(p[0...n][0....m]):
    
    //2-D array to store max sum that can be achieved till node i,j
    //where 0 <= i <= n and 0 <= j <= m 
    max_sum[0...n][0...m]
    
    // For loops to iterate through the complete p array
    for j from 0 to n: 
        for i from 0 to m:
            
            //For first node: 0,0    
            if i ==0 and j == 0:
                max_sum[i][j] = p[i][j]
            
            //For first row        
            else if i == 0 and j > 0:
                max_sum[i][j] = p[i][j] + max_pizza[i][j-1]
                
            //For first coloumn      
            else if j == 0 and i > 0:                        
                max_sum[i][j] = p[i][j] + max_pizza[i-1][j]
                
            //For rows and coloumns more than 0
            else:  
                
                // For calculating max sum at node i,j where i and j > 1
                // we select the max of the node to the north of it 
                // and the node west of it and add it to the value at current node.
                if sum[i-1][j] >= sum[i][j-1]:
                    max_sum[i][j] = sum[i-1][j] + p[i][j] 
                else:
                    max_sum[i][j] = max_sum[i][j-1] + p[i][j]
            
    // Returns the maximum sum that can be achieved by travelling through a matrix from 0,0 to the opposite
                
Running time is O(n*m)

The max_sum array is a two dimensional array of size n*m which contains the maximum sum 
that can be acheieved till you reach node i,j where 0 <= i <= n and 0 <= j <= m  
               
                
'''     
