import heapq
class MinHeap(object):
  def __init__(self): self.h = []
  def heappush(self,x): heapq.heappush(self.h,x)
  def heappop(self): return heapq.heappop(self.h)
  def __getitem__(self,i): return self.h[i]
  def __len__(self): return len(self.h)
class MaxHeap(MinHeap):
  def heappush(self,x): heapq.heappush(self.h,MaxHeapObj(x))
  def heappop(self): return heapq.heappop(self.h).val
  def __getitem__(self,i): return self.h[i].val
class MaxHeapObj(object):
  def __init__(self,val): self.val = val
  def __lt__(self,other): return self.val > other.val
  def __eq__(self,other): return self.val == other.val
  def __str__(self): return str(self.val)
from sys import stdin,stdout
cin = stdin.readline;cout = stdout.write
for _ in xrange(int(cin())):
    n,k = map(int,cin().split())
    array,back= list(),list()
    for i in xrange(n):
        array.append(map(int,cin().split()))
    array.append([float('inf'),float('inf')])
    array.sort(key = lambda item: item[0])
    store,ans = MinHeap(),0
    for i in xrange(n+1):
        if len(store)==k and array[i][1]>store[0]:
            ans = max(ans,store.heappop()-array[i-1][0])
            store.heappush(array[i][1])
        elif len(store)<k:
            store.heappush(array[i][1])
    cout("%d\n"%ans)



