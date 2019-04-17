Consider this solution: 

-  sort the array on basis of first value
-  initialize a min heap
-  iterate over the array
    - if the size of the heap is K and array[i].second > heap.front
        - value = heap.pop()
        - ans = max(ans,value- array[i].first)
        - push array[i].second into heap
    - else if size of heap < K
        - push array[i].second into heap
-  print ans
