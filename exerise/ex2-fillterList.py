nums = [1,6,6,3,6,2,10,2,100]
remove_num = 6

def myfilter( n ):
    return n !=6


tmplist = filter( myfilter ,nums)
newlist = list(tmplist)
newlist.sort()
print(newlist)

tmplist = filter( lambda n: n!=6  ,nums)
newlist = list(tmplist)
newlist.sort()
print(newlist)
print( sorted(set(newlist))  )

