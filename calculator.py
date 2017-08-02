count=1
print("Dev:Logan")
print("V1.1.1")
print("")
print("Dev Note:")
print("There are a few problems with this calculator and you have to adsume there is the units squared and cubed if you are finding the volume/area/surface area.")
print("Also, I cannot for the life of me get the area of the circle function working. Will get that in later updates.")
print('We plan to add in the future a formula section to see all the formulas and to get formulas with square roots like the quadratic formula.')
print("")
print('To use the addition funcion type "add". To use the subtracton function type "sub".')
print('To use the multiplucation function type "multi". To use the division function type "div".')
print('To use the expodental function type "exp". To find the area of a rectangle/square type "arec".')
print('To find the area of a triangle type "atri". To find the area of a circle using the radius type "acir".')
print('To find the area of a trapizoid type "atrap". To find to volume of a sphere type "vsph".')
print('To find the volume of a rectangular prisim/cube type "vrec". To find the volume of a cone type "vcone".')
print('To find the volume of a cylinder type "vcyl". To find the surface area of a rectangular prisim type "sarec"')
print('To find the surface area of a cylinder type "sacyl". To find the surface area of a sphere type "sasph"')
print('To find the perimiter of a square/rectangle type "prec". To find the circumference of a cirle type "pcir".')
while count< 10:
  fun= input('')
  if fun == "add":
    print("")
    print('What is the first number do you want to add?')
    a= int(input(''))
    print('What is the second number you want to add?')
    b= int(input(''))
    c=a+b
    print(c)
  if fun == "sub":
    print("")
    print('What is the first number do you want to subtract?')
    a= int(input(''))
    print('What is the second number you want to subtract?')
    b= int(input(''))
    c=a-b
    print(c)
  if fun == "multi":
    print("")
    print('What is the first number do you want to multipulie?')
    a= int(input(''))
    print('What is the second number you want to multipulie?')
    b= int(input(''))
    c=a*b
    print(c)
  if fun == "div":
    print("")
    print('What is the first number do you want to divide?')
    a= int(input(''))
    print('What is the second number you want to divide?')
    b= int(input(''))
    c=a/b
    print(c)
  if fun == "exp":
    print("")
    print('What is the base number?')
    a= int(input(''))
    print('To the power of...')
    b= int(input(''))
    c=a**b
    print(c)
  if fun == "arec":
    print("")
    print('What is the length?')
    a= int(input(''))
    print('What is the width?')
    b= int(input(''))
    c=a*b
    print(c)
  if fun == "atri":
    print("")
    print('What is the base?')
    a= int(input(''))
    print('What is the hight?')
    b= int(input(''))
    c=(a+b)/2
    print(c)
  if fun == "atrap":
    print("")
    print('What is the base1?')
    a= int(input(''))
    print('What is the base2?')
    b= int(input(''))
    print('What is the hight?')
    d=int(input(''))
    c=((a+b)/2)*d
  if fun == "vsph":
    print("")
    print('What is the radius?')
    a= int(input(''))
    c=1.333333333*3.141592653*(a**3)
    print(c)
  if fun == "vrec":
    print("")
    print('What is the length?')
    a= int(input(''))
    print('What is the width?')
    b= int(input(''))
    print('What is the hieght?')
    d= int(input(''))
    c=a*b*d
    print(c)
  if fun == "vcone":
    print("")
    print('What is the radius?')
    a= int(input(''))
    print('What is the height?')
    b= int(input(''))
    c=3.141592653*(a**2)*(b/3)
    print(c)
  if fun == "vcyl":
    print("")
    print('What is the radius?')
    a= int(input(''))
    print('What is the height?')
    b= int(input(''))
    c=3.141592653*(a**2)*b
    print(c)
  if fun == "sarec":
    print("")
    print('What is the length?')
    l= int(input(''))
    print('What is the width?')
    w= int(input(''))
    print('What is the hieght?')
    h= int(input(''))
    c=2*(w*l+h*l+h*w)
    print(c)
  if fun == "sacyl":
    print("")
    print('What is the radius?')
    r= int(input(''))
    print('What is the height?')
    h= int(input(''))
    c=3.141592653*r*h+2*3.141592653*(r**2)
  if fun == "sasph":
    print("")
    print('What is the radius?')
    a= int(input(''))
    c=4*3.141592653*(a**2)
    print(c)
  if fun == "prec":
    print("")
    print('What is the length??')
    a= int(input(''))
    print('What is the width??')
    b= int(input(''))
    c=2*a+2*b
    print(c)
  if fun == "pcir":
    print("")
    print('What is the radius?')
    a= int(input(''))
    c=2*3.141592653*a
    print(c)
  if fun == "Young man":
    print('')
    print('There is no need to feel down')
    young=input('')
    if young == 'I say young man':
      print('')
      print('Pick yourself off the ground')
      young1=input('')
      if young1 == 'I said young man':
        print('')
        print("'cause you're in a new town")
        print("There's no need to be unhappy.")
  else:
    print('')