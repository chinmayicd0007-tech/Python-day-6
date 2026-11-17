text = " My name is \"Chinmayi"
print(text) 

s1 = ""
res = bool(s1)
print(res)

s1 = "Python"
s2 = "Python"
print(s1, id(s1))
print(s2, id(s2))
print(s1, id(s2))
print(s1 == s2)

s1 = "hello"
print(s1, id(s1))
s1 = s1 + "world"
print(s1, id(s1))