
```py
import random

from sqlalchemy import false
# def celebrity(matrix):

def celebrity(matrix):
    n=len(matrix)
    #For all potential celebrities

    for i in range(n):
        eliminated = False
        # For every other person
        for j in range(n):
            if not eliminated:
                if i==j: #same person
                    continue
                if matrix[i][j] or not matrix[j][i]:
                    eliminated = True
        
        if not eliminated:
            return i

    return -1


def main():
    matrix = [[random.randint(0,1)]*5 for i in range(5)]

    for i in range(random.randint(0,len(matrix)-1)):
        for j in range(len(matrix)):
            matrix[i][j] = 0
            matrix[j][i] = 1
    
    celeb = celebrity(matrix)


if __name__ == "__main__":
    main()

```

Time complexity: O(n*n) <br>
Space Complexity: O(1)

---


```py
import random

from sqlalchemy import false
# def celebrity(matrix):

def celebrity(matrix):
    n = len(matrix)

    #The first two people we begin eliminating
    u,v = 0,1
    for i in range(2,n+1):
        if matrix[u][v]:
            u = i
        else:
            v = i

    celeb = None
    if u==n:
        celeb = v
    else:
        celeb = u
    
    eliminated = false

    for person in range(n):
        if person == celeb:
            continue
        if matrix[celeb][person] or not matrix[person][celeb]:
            eliminated = True
    
    if not eliminated:
        return celeb
    
    return -1


def main():
    matrix = [[random.randint(0,1)]*5 for i in range(5)]

    for i in range(random.randint(0,len(matrix)-1)):
        for j in range(len(matrix)):
            matrix[i][j] = 0
            matrix[j][i] = 1
    
    celeb = celebrity(matrix)


if __name__ == "__main__":
    main()
```

Time complexity: O(n) <br>
Space Complexity: O(1)