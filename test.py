#number = int(input('напишите число '))
#if number % 2:
    #print('не четное')
#else:
    #print('четное')





t = int(input('введите температуру'))
if t > 20 and t < 31:
    print('надень понаму')
elif t > 10 and t < 21:
    print('надень кепку')
elif t > 0 and t < 11:
    print('надень рубашку')
elif t < 0 and t > -11:
    print('надень свитер')
elif t < -12:
    print('надень куртку')    
else:
    print('станься дома')
