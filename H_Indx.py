class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #T(C(N)==O(N)) and S(C(N)==O(1)) as it requires Non Memory space allocation Iteraitvely 
        citations.sort(reverse=True)#List's Sorting In Descending Order 
        for indx,cit in enumerate(citations):#Iterating through array's Indxes
            if indx>=cit:return indx#Printing Atleast (array's(indx))
        return len(citations)#Printing List's Length 
