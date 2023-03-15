def isRotated(s1, s2):
  if len(s1)!=len(s2):
    return False
  s=(s1+s1)
  if s2 in s:
    return True
  else:
    return False


s1=input()
s2=input()
print(isRotated(s1, s2))