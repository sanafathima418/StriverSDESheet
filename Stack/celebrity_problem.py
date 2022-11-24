# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """

        # Approach 1(TLE): Brute Force, check indegree and outdegree of each person 
        # If you find a person whose indegree is n and outdegree is 0 then celebrity found
        # TC: O(N^2) to traverse over 2D adjacency matrix of graph
        # SC: O(N) + O(N) for indegree and outdegree

        # degree array;
        indegree = [0 for x in range(n)]
        outdegree = [0 for x in range(n)]

        # Query for all edges
        for i in range(n):
            for j in range(n):
                if i != j and knows(i, j):
                    # Set the degrees
                    outdegree[i] += 1
                    indegree[j] += 1
        
        # Find a person with indegree n-1
        # and out degree 0
        for i in range(n):
            if (indegree[i] == n - 1 and
                    outdegree[i] == 0):
                return i

        return -1

        # Approach 2(Optimized): With 2 pointers
        # Use start and end pointers until start <= end
        # TC: O(N) + O(N) to check possible celebrity candidates and then check if sortlisted canditates know anyone else
        # SC: O(1)
        start = 0
        end = n-1
        
        while(start < end):
            if knows(start,end):
                # if start knows end, then start cannot be celebrity
                start += 1
            else:
                # if start does not know end, then end cannot be celebrity
                end -= 1
        
        # start is the celebrity candidate now
        for i in range(n):
            if start != i:
                # candidate knowing himself does not count
                if knows(start,i) or not knows(i,start):
                    # If candidate knows someone or someone does not know the candidate, then no celebrity 
                    return -1
        # If not already returned, celebrity exists and is equal to start
        return start