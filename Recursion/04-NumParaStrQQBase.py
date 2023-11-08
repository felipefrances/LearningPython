def deNumParaStr(n, base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return deNumParaStr(n // base, base) + convertString[n % base]

print(deNumParaStr(985, 16))
