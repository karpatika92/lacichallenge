
# coding: utf-8

# In[89]:

import numpy as np
edges= np.array([[0,1],[0,2],[0,3],[2,3]])
[0,1] in edges
cucc=set(range(5))
print(cucc)
[1,2,2].index(2)


# In[161]:

import numpy as np
edges= np.array([[1,2],[0,2],[0,3],[2,3]])
class karpatiGraphSolution:
    def __init__(self,edges):
        assert type(edges)==numpy.ndarray, "input is not an edge list"
        self.edgeList=edges
        self.numNodes=np.amax(edges)+1
    def give_me_matrix(self):
        res=[[0] * self.numNodes for i in range(self.numNodes)]
        for edge in self.edgeList:
            res[edge[0]][edge[1]]=1
            self.adjMat=res
        return res
    def isConnected(self):
        rowSums=np.asarray(self.adjMat).sum(0)
        colSums=np.asarray(self.adjMat).sum(1)
        print(rowSums)
        print(colSums)
        total=rowSums+colSums
        res=0 not in total
        return res
    def isStronglyConnected(self):
        rowSums=np.asarray(self.adjMat).sum(0)
        colSums=np.asarray(self.adjMat).sum(1)
        print(rowSums)
        print(colSums)
        res=0 not in rowSums & 0 not in colSums
        return res
    def MST(self):
        assert self.isConnected, "Sorry, your graph is not connected"
        treeMST=set()
        nodeInMST=set()
        nodeInMST.add(self.edgeList[0][0])
        print(nodeInMST)
        for edge in self.edgeList:
                if (edge[1] in nodeInMST and edge[0] not in nodeInMST):
                    print("LOL")
                    treeMST.add((edge[0],edge[1]))
                    nodeInMST.add(edge[0])
                    print(nodeInMST)
                elif (edge[0] in nodeInMST and edge[1] not in nodeInMST):
                    print("LOL2")
                    nodeInMST.add(edge[1])
                    treeMST.add((edge[1],edge[0]))
                    print(nodeInMST)
                    #nodeInMST.add(edge[1])
                if len(nodeInMST)==self.numNodes:
                    print("BREAKING")
                    break

        return(treeMST)
sol=karpatiGraphSolution(edges)
cucc=sol.give_me_matrix()
cucc3=sol.MST()                              
print(cucc3)


# In[144]:

var = 100
if var == 200:
   print "1 - Got a true expression value"
   print var
elif var == 150:
   print "2 - Got a true expression value"
   print var
elif var == 100:
   print "3 - Got a true expression value"
   print var
else:
   print "4 - Got a false expression value"
   print var

print "Good bye!"


# In[ ]:




# In[ ]:



