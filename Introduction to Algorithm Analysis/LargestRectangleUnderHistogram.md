```py
class Solution:
    def findMin(self,A,i,j):
        min = A[i]
        while i<=j:
            if min > A[i]:
                min = A[i]
            i = i+1
        return min

    def largestRectangleArea(self, A: List[int]) -> int:
        maxArea = 0
        for i in range(len(A)):
            for j in range(i,len(A)):
                minimum_height = self.findMin(A,i,j)
                maxArea = max(maxArea,(j-i+1)*minimum_height) 
        return maxArea  
```

Time Complexity : O(n*n*n)<br>
Space Complexity : O(1)

---

```py
def largestRectangleArea(self, A: List[int]) -> int:
    maxArea = 0
    for i in range(len(A)):
        minimum_height = A[i]
        for j in range(i,len(A)):
            minimum_height = min(minimum_height,A[j])
            maxArea = max(maxArea,(j-i+1)*minimum_height)
    return maxArea
                
```

Time Complexity : O(n*n)<br>
Space Complexity : O(1)

---

```py
class Solution:
    def largestRectangleArea(self, height: List[int]) -> int:
        stack=[]; i=0; maxArea=0
        while i<len(height):
            if stack==[] or height[i] > height[stack[-1]]:
                stack.append(i)
            else:
                curr = stack.pop()
                width = i if stack==[] else i-stack[-1]-1
                maxArea = max(maxArea,width*height[curr])
                i-=1
            i+=1
        
        while stack != []:
            curr = stack.pop()
            width=i if stack==[]  else len(height)-stack[-1]-1
            maxArea = max(maxArea,width*height[curr])
        
        return maxArea
```

Time Complexity : O(n)<br>
Space Complexity : O(n)


---

