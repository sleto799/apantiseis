def triad(arr):
  arr = sorted(arr)
  for i, p in enumerate(arr):
   l, u = 0, len(arr)-1
   while l < i < u:
     ok = p + arr[l] + arr[u]
     if ok > 0:
      u-= 1
     elif ok < 0:
      l+= 1
     else:
      yield arr[l], p, arr[u]
      l+= 1
      u-= 1					
print("\n")
print " The combinations of triads consisting of 30 numbers randomly selected between (-30,30) whose sum equals to 0 are the following: "
print("\n")
if __name__ == '__main__':    
  from random import randint
  li = list(set(randint(-30, 30) for _ in range(30)))
  for t in triad(li):
    print t