class node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def areidentical(root1,root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    return (root1.val==root2.val and areidentical(root1.left,root2.left) and areidentical(root1.right,root2.right))

def issubtree(t,s):
    if s is None:
        return True
    if t is None:
        return False
    if (areidentical(t,s)):
        return True
    return issubtree(t.left,s) or issubtree(t.right,s)
def insert_t(arr,root,i,n):
    if i<n:
        temp=node(arr[i])
        root=temp
        root.left=insert_t(arr,root.left,2*i+1,n)
        root.right=insert_t(arr,root.right,2*i+2,n)
    return root
def tree():
    values=input("enter the values")
    arr=list(map(int,values.split()))
    n=len(arr)
    return insert_t(arr,None,0,n)
print("t tree")
t=tree()
print("s tree")
s=tree()
result=issubtree(t,s)
if result:
    print("s is subtree of t")
else:
    print("s is not sub tree of t")
    


    
