class treenode:
    def __init__(self,val,left,right):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    st=[]
    res=[]
    while root or st:
        while root:
            st.append(root)
            root=root.left
        root = st.pop()
            res.append(root.val)

            root = root.right
        
        return res 
