#Depth Limited Search

graph={

'0':['1','2'],

'1':['3','4'],

'2':['5','6'],

'5':[],

'6':[],

'3':[],'4':[]

}

visited=[]

queue=[]

def dls(visited,graph,node,limit,initial):

        visited.append(node)

        queue.append(node)

        while queue:

                m = queue.pop(0)

                print(m, end=" ")

                initial=initial+1

                if(initial!=limit+1):

                        for val in graph[m]:

                                if(val[0]):

                                        dls(visited,graph,val[0],limit,initial)

limit=int(input("Enter The Limit\n"))

initial=0

print("Path After DLS Traversal")

dls(visited,graph,'0',limit,initial)