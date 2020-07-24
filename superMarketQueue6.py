def queue_time(customers, n):
    tills = [0]*n
    #print(tills)
    for i in customers:
      tills[0] += i
      #print(tills)
      tills.sort()
    return max(tills)

print(queue_time([5,3,2,6],3))