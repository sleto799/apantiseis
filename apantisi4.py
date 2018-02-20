ar_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]	   
def conv(ar):
 rom = ''
 while ar > 0:
     for i, r in ar_map:
         while ar >= i:
             rom += r
             ar -= i
 return rom
print("\n")
ar= input("Please select the integer(number) you would like to convert to roman numerals: ")
print("\n")
print "In roman numerals ",ar," is :",conv(ar)