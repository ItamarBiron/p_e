##autor : itamar biron

def inRange(a):
    if(a>-1 and a<10):
        return 1
    return 0

def calc (a):
    count =0 
    for i1 in range (10):
        for i2 in range (10):
            for i3 in range (10):
                for i4 in range (10):
                     for i5 in range (10):
                          for i6 in range (10):
                               for i7 in range (10):
                                    for i8 in range (10):
                                         for i9 in range (10):
                                             x1= i1+i4+i7 -i6 -i8
                                             s = i1 +i2+i3+x1
                                             x2= s- i4 -i5 -i6
                                             x3= s -i7 -i8 -i9
                                             x4= s- i1-i5-i9
                                             x5= s-i3-i6-i9
                                             x6=s-i2-i5-i8
                                             x7=s-i1-i4-i7
                                             if(inRange(x1)and inRange(x2)and inRange(x3)and inRange(x4)and inRange(x5)and inRange(x6)and inRange(x7) ):
                                                 if(x1+x2+x3==i1+i5+i9 and i1+i5+i9== x5+x6+x7):
                                                     count = count +1

                                                    
                                 
                                        
            
    print count

calc(4)
print inRange(0)
