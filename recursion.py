import sys
sys.setrecursionlimit(10000000)
sys.set_int_max_str_digits(10000000)

class Solution:    
    results = {}

    def fib(self,n):
        if n <= 1:
            return n
        if n in self.results:
            return self.results[n]
  
        res = self.fib(n-1) + self.fib(n-2)
        self.results[n] = res
        return res

    def reverseArray(self, arr):
        # code here
        return arr[::-1]

sol = Solution()
print(sol.reverseArray([1,2,3,4,5]))


    #     t = 0
    # #Complete this function
    # def printNos(self,n):
    #     #Your code here
    #     if self.t < n:
    #         self.t+=1
    #         print(self.t)
    #         self.printNos(n)
    #     return
    #Complete this function
    # def printNos(self,n):
    #     #Your code here
    #     while self.t < n:
    #         self.t += 1
    #         print(self.t, end = ' ')


    # def printNos(self, n):
    #     # Code here
    #     if(n != 0):
    #         print(n, end = ' ')
    #         self.printNos(n-1)
    #     return
    # def startPrinting(self,i,n):
    #     if i > n:
    #         return
    #     print(i)
    #     self.startPrinting(i+1,n)
    # def printNos(self,n):
    #     self.startPrinting(1,n)
    # def startPrinting(self,i,n):
    #     if i > n:
    #         return
    #     self.startPrinting(i+1,n)
    #     print(i)
    # def printNos(self,n):
    #     self.startPrinting(1,n)

    # # def printSummition(self,i,total):
    # #     if i < 1:
    # #         print(total)
    # #         return
    # #     self.printSummition(i-1,total+i)

    # # def printSum(self,n):
    # #     self.printSummition(n,0)

    # # def fact(self,n):
    # #     if n == 0 :
    # #         return 1 
    # # #     return n*self.fact(n-1)
    # # def swap(self,arr,l,r):
    # #     if l > r:
    # #         return
    # #     arr[l],arr[r] = arr[r],arr[l]
    # #     self.swap(arr,l+1,r-1)


    # # def revArray(self,arr: list):
    # #     self.swap(arr,0,len(arr)-1)

    # def checkPalindrome(self,l,string:list,r):
    #     if l > r:
    #         return True
    #     if string[l] == string[r]:
    #         return self.checkPalindrome(l+1,string,r-1)
    #     return False

    # # def isPalindrome(self,string):
    # #     string = [*string]
    # #     return self.checkPalindrome(0,string,len(string)-1)