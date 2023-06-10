# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        #in order traversal 
        def rserialize(root, treeSerialized): 
            if root is None: 
                treeSerialized += 'null'
            else: 
                treeSerialized = treeSerialized + '{' +   '"root"' +   ':' + str(root.val) +  ',' +  '"left"'+   ':' + self.serialize(root.left)  +','+  '"right"' +  ':'+ self.serialize(root.right) +'}'
            return treeSerialized
        return rserialize(root, '')
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        print(data)
        dictionary = json.loads(data)
        print(dictionary)
        def rdeserialize(aDictionary): 
            if aDictionary == None: 
                return None

            root =  TreeNode(aDictionary['root'])
            
            root.left  = rdeserialize(aDictionary["left"])
            root.right = rdeserialize(aDictionary["right"])
            return root
        
        root = rdeserialize(dictionary)
        return root
            
        
        
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))