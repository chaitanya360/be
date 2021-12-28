#Name :Omkar Bhagwat
#Rollno :11
#Assignment No :3(BestFirstSearch Algorithm)

li1 = list()
li2 = []
SuccList = dict()
#SuccList ={ 'A':[['B',3],['C',2]], 'B':[['A',5],['C',2],['D',2],['E',3]], 'C':[['A',5],['B',3],['F',2],['G',4]], 'D':[['H',1],['I',99]],'F': [['J',99]],'G':[['K',99],['L',3]]}

n = int(input("\nEnter no. of start nodes :"))
for i in range(n):
    s = input("\nEnter start node :")
    n1 = int(input("\nEnter no of end nodes :"))
    for j in range(n1):
        e = input("\nEnter end node :")
        c = int(input("\nEnter cost :"))
        li1.append(e)
        li1.append(c)
        #print(li1)
        li2.append(li1)
        li1 = []
    print(li2)
    SuccList[s] = li2
    li2 = []

print(SuccList)

Start=input("\nEnter Start node :")
Goal=input("\nEnter Goal node :")
Closed = list()
SUCCESS = True
FAILURE = False
State = FAILURE


def GOALTEST(N):
 if N == Goal:
  return True
 else:
  return False

def MOVEGEN(N):
 New_list=list()
 if N in SuccList.keys():
  New_list=SuccList[N]

 return New_list

def APPEND(L1,L2):
 New_list=list(L1)+list(L2)
 return New_list

def SORT(L):
 L.sort(key = lambda x: x[1])
 return L

def BestFirstSearch():
 OPEN=[[Start,5]]
 CLOSED=list()
 global State
 global Closed
 while (len(OPEN) != 0) and (State != SUCCESS):
  print("------------")
  N= OPEN[0]
  print("N=",N)
  del OPEN[0] #delete the node we picked

  if GOALTEST(N[0])==True:
   State = SUCCESS
   CLOSED = APPEND(CLOSED,[N])
   print("CLOSED=",CLOSED)
  else:
   CLOSED = APPEND(CLOSED,[N])
   print("CLOSED=",CLOSED)
   CHILD = MOVEGEN(N[0])
   print("CHILD=",CHILD)
   for val in OPEN:
     if val in CHILD:
         CHILD.remove(val)
   for val in CLOSED:
      if val in CHILD:
          CHILD.remove(val)
   OPEN = APPEND(CHILD,OPEN) #append movegen elements to OPEN
   print("Unsorted OPEN=",OPEN)
   SORT(OPEN)
   print("Sorted OPEN=",OPEN)
 Closed=CLOSED
 return State

BestFirstSearch()
