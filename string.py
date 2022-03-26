# Python program to convert a list to string
    
# def listToString(s): 
    
#     # initialize an empty string
#     str1 = "" 
    
#     # traverse in the string  
#     for ele in s: 
#         str1 += ele  
    
#     # return string  
#     return str1 
               
# # Driver code    
# s = ['My', 'name', 'is','Mahady']
# print(listToString(s)) 

# # Example 2---------------
# def listToString2(s2):  
#     # return string  
#     return (' '.join(map(str,s2)))
        
# s2 = ['I', 'want', 4, 'apples', 'and', 18, 'bananas'] # list need to convert in string first.        
# # Driver code    
# print(listToString2(s2)) 

# # Example 3---------------
# def listToString3(s3):  
#     # return string  
#     return (' '.join(s3))
        
# s3 = ['My', 'name', 'is','Mahady']  
# # Driver code    
# print(listToString3(s3)) 


# Example 4 (split)---------------
# def split(str):
#     return (str.split()) # split method convert in to a list
     
# # Driver code
# text = 'My name is Mahady'
# print(split(text))

# # Example 5 (split)---------------
# def split(text2):
#     return (text2.split())

# text2 = 'My, name, is, Mahady'
# print(text2.split(', ', -1))

# # Example 6 (split word)---------------
# def split(str):
#     return (list(str))
     
# # Driver code
# word = 'Mahady'
# print(split(word))

# # Other  Solution-----------
# def split2(str):
#     res = []
#     res[:] = str
#     return res
     
# text = 'Mahady'
# print(split2(text))


# # Example 7 (split word)---------------
# def split(word2):
#     myWord = ""
#     for char in word2:
#         if char != ' ':
#             print(char)
#             myWord += char   

#     return (list(myWord))
     
# # Driver code
# word2 = 'My name is mahady'
# print(split(word2))

# Example 8 (split word)---------------
# def split(word3):
#     myWord = ""
#     for char in word3:
#         if not(char == ' ' or char ==','):
#             print(char)
#             myWord += char

#     return (list(myWord))