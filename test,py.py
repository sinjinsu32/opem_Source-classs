def findMax(a, b, c)
if a>b:
    biggest=a
else:
     biggest=b
  if c>biggest:
      biggest=c
      
    
    return biggset

a = int(input("첫 번째 숫자 입력 : "))
b = int(input("두 번째 숫자 입력 ; "))
c = int(input("세 번째 숫자 입력 : "))
        
 biggest= findMax(a, b, c)

 print(a, b, c, "중 가장 큰수는 ", biggest, "입니다")       
