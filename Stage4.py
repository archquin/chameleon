#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 14:49:58 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 22:40:09 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 18:05:00 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 06:48:45 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 18:01:00 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 19:23:50 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 03:53:09 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 21:43:19 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 22:03:31 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 17:12:42 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 05:50:58 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 18:52:12 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 21:58:01 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 17:36:26 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 15:12:14 2020

@author: fadewell
"""

#import math
import qrcode
#import pyqrcode
#import pandas as pd
#import numpy as np
#from pandas import D
import matplotlib.pyplot as plt
import cv2 as cv2
detector = cv2.QRCodeDetector()

#import pandas as pd
#import
ensemble = 0
ijk = 0
KiJ=JiK = 0
q1=q2=q3=q4=0
qx1=qx2=qx3=qx4=0
c = 0
dimensions = 0
Fs = []
while ensemble <1 :
    white = '-2'   ######## white <---->Green, Cream           1
    Yellow = '-5'   ####-2,-3,-4,----> Yellow==k @ k = 0 ======> 4 White
    Blue = '-7'      ##### -3,-4,-5 ---->Blue == j @ j = -1
    Somon = '5'    ##### 1,3,4,5 -----> Somon = k @ k = 0
    Pink = '-6'      ###### 2,3,4 ----> Pink = ij @ ij = 0
    Green= '-4'      ##### 1,-1,-2,-3 ----> Green = j @ j = 2
    black = '-2' ##### -2,-3,-4 -----> black == i == ij@ ij = 0
    Tree = '1'  #### i 3x
    Cream = '2'  ######## 3,4,5-------> is white too 2
    print('How many entities?')
    b = input()
    b = int(b)
    Tree = str(int(b))  
    while dimensions < 1:
       
      #  Somon = str(-int(Green))
    #    Blue = str( int(Green)+1 )     ##### -3,-4,-5 ---->Blue == j @ j = -1
        qqrrr22 = qrcode.make(Cream)
        qqrrr22.save('r000partEnQtities000r.png')
        iiim0g0mgg111 = cv2.imread("r000partEnQtities000r.png")
        gggrreeeeyy0 = cv2.cvtColor(iiim0g0mgg111, cv2.COLOR_XYZ2RGB)
        cream, bbox, straight_qrcode = detector.detectAndDecode(iiim0g0mgg111)
     #   print('how many mines?')
      #  b = input()
      #  b = int(b)
      #   
        yaw = 1
        while yaw > 0:
            
            i = 0
            ikj = i
            qr2 = qrcode.make(Tree)
            qr2.save('partEntities00.png')
            img111 = cv2.imread("partEntities00.png")
            greyyyy = cv2.cvtColor(img111, cv2.COLOR_BGR2RGB)
            tree, bbox, straight_qrcode = detector.detectAndDecode(img111)
            Tree = int(Tree)   
            jik = int(Tree)           
            Mines = int(Tree)       
            bb = Mines
            while i < Tree:

                j = 2
                print('which y has ')
                OfY = input()
                OfY = int(OfY)
                   #    b = input()
                    #    b = int(b)
                print('which x has ')
                OfX = input()
                OfX = int(OfX)
                print('what value of entity?')
                a = input()
                a = int(a)
                aa = int(a)
                black = str(-int(a)) 
                qqrrr22 = qrcode.make(black)
                qqrrr22.save('r000partEntities000r.png')
                iiim00mgg111 = cv2.imread("r000partEntities000r.png")
                ggrreeeeyy0 = cv2.cvtColor(iiim00mgg111, cv2.COLOR_HSV2RGB)
                Black, bbox, straight_qrcode = detector.detectAndDecode(iiim00mgg111)
                i = 0
                ij = 0
                
                while i < j :
               #     i = ij
           
                    qqrr22 = qrcode.make(Green)
                    qqrr22.save('000partEntities000.png')
                    iiim0mgg111 = cv2.imread("000partEntities000.png")
                    ggrreeeyy0 = cv2.cvtColor(iiim0mgg111, cv2.COLOR_RGB2XYZ)
                    green, bbox, straight_qrcode = detector.detectAndDecode(iiim0mgg111)
                    
                    Cream = int(Cream)
                    j = 2
                    kj = j
                    k = 0
                    ijk = ij
                    ji = int(Green)
                    Green = int(Green)
                    x = 0
                 
                   
                    while j > Green :## i<j
                       # ij = ijk
                        #i = ij
                        qr22 = qrcode.make(Pink)
                        qr22.save('00partEntities00.png')
                        iiimmgg111 = cv2.imread("00partEntities00.png")
                        ggrreeeyy = cv2.cvtColor(iiimmgg111, cv2.COLOR_BGR2HLS)
                        pink, bbox, straight_qrcode = detector.detectAndDecode(iiimmgg111)
                        
                        jk = 2
                        ###i = 0 or 
                        ij = 0
                        ik = k
                        JiK = 0
                        
                        y = 0
                        x += 1
                       
              #          print('a: from 1 to 4')
                       #
                     #   i=ij#############################################
                        while ij < jk:
                            y+=1
                           # b = input()
                            
                           
                            k = 0
                            ik = k
                            ki = k
                            qr22 = qrcode.make(Somon)
                            qr22.save('0partEntities0.png')
                            iiimg111 = cv2.imread("0partEntities0.png")
                            ggreeyy = cv2.cvtColor(iiimg111, cv2.COLOR_BGR2Luv)
                            somon, bbox, straight_qrcode = detector.detectAndDecode(iiimg111)
                            i = int(Somon)
                            
                            Somon = int(Somon)
                            z = 0
                            while  k  < Somon :###### X KiJ X
                                z+=1
                                
                                 ### -2
                                qqr2 = qrcode.make(Blue)
                                qqr2.save('0partEntities.png')
                                iimg11 = cv2.imread("0partEntities.png")
                                ggreyy = cv2.cvtColor(iimg11, cv2.COLOR_BGR2LAB)
                                blue, bbox, straight_qrcode = detector.detectAndDecode(iimg11)
                                w = 0
                              #  j = 5
                                if OfX == x and OfY == y:
                                    j = -1
                                while j < k:
                                    Nn=0  
                                    w +=1
                                    k = 4
                                    if OfX == x:
                                        k=-1
                                    qr1 = qrcode.make(Yellow)
                                    qr1.save('partEntities.png')
                                    img11 = cv2.imread("partEntities.png")
                                    greyy = cv2.cvtColor(img11, cv2.COLOR_BGR2HSV)
                                    yellow, bbox, straight_qrcode = detector.detectAndDecode(img11)
                                    
                                  #  Yellow = yellow
                                    while k <  i:
                                        
                                        qr = qrcode.make(white)
                                        qr.save('partEntities0.png')
                                        img1 = cv2.imread("partEntities0.png")
                                        greyyy = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
                                        White, bbox, straight_qrcode = detector.detectAndDecode(img1)
                                        ik = 0
                                        Nn+=1
                                        white = int(white) ### white == jk , -6
                                        jk = 2
                                      #  KiJ = 0
                                        
                                        while ik < jk:
                 
                                            white = int(white)
                                            if ik != white:
                                                white+= 1
                                                qr6 = qrcode.make(Fs)
                                                qr6.save('White.png')
                                                aWhite = cv2.imread("White.png")
                                                cWhite = cv2.cvtColor(aWhite, cv2.COLOR_BGR2RGB)
                                                data, bbox, straight_qrcode = detector.detectAndDecode(aWhite)
                               
                                        
                                            if  ik == white:
                                                white = White
                                                ik = 3
                                                
                                                if (OfX == x and OfY == y and OfX == z and OfY == w and (a == 'M' and  b == '¬H') ):#and c == '¬E') ):
                                                 #   print('Somon',Somon)
                                                    if Nn == 1 and q1 == 'E' and Somon == 5  :
                                                    #    print(x+1,'x',y+1,'y')
                                                        print(z+1,'ix',w+1,'iy')
                                                        FS=[x+1,y+1]
                                                        plt.imshow(cWhite)
                                                        plt.show()
                                                       # Fs.append(FS)
                                                    elif Nn==2 and q2 == 'E' and Somon == 4 :
                                                      #  print(x+1,'x',y-1,'y')
                                                        print(z+1,'ix',w-1,'iy')
                                                        FS=[x+1,y-1]
                                                        plt.imshow(cWhite)
                                                        plt.show()
                                                     #   Fs.append(FS)
                                                    elif Nn==3  and q3 == 'E' and Somon == 3 :
                                                      #  print(x-1,'x',y-1,'y')
                                                        print(z-1,'ix',w-1,'iy')
                                                        FS=[x-1,y-1]
                                                        plt.imshow(cWhite)
                                                        plt.show()
                                                    #    Fs.append(FS)
                                                    elif Nn==4  and q4 == 'E' and Somon == 2 :
                                                      #  print(x-1,'x',y+1,'y')   
                                                        print(z-1,'ix',w+1,'iy')
                                                        FS=[x-1,y+1]
                                                        plt.imshow(cWhite)
                                                        plt.show()
                                                      #  Fs.append(FS)
                                                    
                                                    
                           
                                        Yellow = int(Yellow)
                                        
                                        if  k != Yellow:
                                            Yellow +=1
                                            col = [x,w]
                                            qr6 = qrcode.make(col)
                                            qr6.save('Yellow.png')
                                            aYellow = cv2.imread("Yellow.png")
                                            cYellow = cv2.cvtColor(aYellow, cv2.COLOR_BGR2GRAY)
                                            data, bbox, straight_qrcode = detector.detectAndDecode(aYellow)
  
                                        if k == Yellow :                                               

                                            Yellow = yellow
                                      #      print(Yellow)
                                            k = int(somon)
                                            if (OfX == z and OfY == y and OfX == x) and OfY == w+1 and (a == 'M' and  b == '¬H' and qx3=='E' and Somon == 5)  :
                                              #  print(Somon,'Somon')
                                               # print('Same column (X coordinates)')
                                                #print(x,'x',y,'y',z,'z',w,'w',i,'i')
                                                print(x,'x',w,'y')
                                                plt.imshow(cYellow)
                                                plt.show()
                                            if (OfX == z and OfY == y and OfX == x) and OfY == w-1 and (a == 'M' and  b == '¬H' and qx4 =='E' and Somon == 1)  :
                                                print(Somon,'Somon')
                                               # print('Same column (X coordinates)')
                                             #   print(x,'x',y,'y',z,'z',w,'w',i,'i')
                                                print(x,'x',w,'y')
                                                plt.imshow(cYellow)
                                                plt.show()
                                                plt.show()
                                      #      if (OfX == z and OfY == y and OfX == x) and OfY == w and (a == 'M' and  b == '¬H' and qx4 =='E' and Somon == 1)  :
                                         #       print(Somon,'Somon')
                                               # print('Same column (X coordinates)')
                                             #   print(x,'x',y,'y',z,'z',w,'w',i,'i')
                                          #      print(x,'x',w,'y')
                                         #       plt.imshow(cYellow)
                                          #      plt.show()
                            
                                    Blue = int(Blue)
                     
                                    if j != Blue:  #### blue -2
                                       # j -= 1
                                        row =[z,y]
                                        qr6 = qrcode.make(row)
                                        qr6.save('Blue.png')
                                        aBlue = cv2.imread("Blue.png")
                                        cBlue = cv2.cvtColor(aBlue, cv2.COLOR_BGR2HSV)
                                        data, bbox, straight_qrcode = detector.detectAndDecode(aBlue)
                                        Blue +=1
                                   #  
                                       
                                    if j == Blue:
                                        Blue = blue
                                        
                                        j = int(Cream)
                                        jk = j
                                        
                                        if ( OfX == x and OfY == y ) and OfX == z+1  and (a == 'M' and  b == '¬H' and qx1 == 'E' and Somon == 5):# and b != '¬E':
                                     #       print('Same row (Y coordinates)')
                                          #  print(Somon,'Somon')
                                         #   print(x,'x',y,'y',z,'z',w,'w',i,'i')
                                            print(z,'x',y,'y')
                                            plt.imshow(cBlue)
                                            plt.show()
                                        elif ( OfX == x and OfY == y ) and  OfX == z-1 and (a == 'M' and  b == '¬H' and qx2=='E' and Somon == 1 ):# and b != '¬E':
                                     #       print('Same row (Y coordinates)')
                                            print(Somon,'Somon')
                                         #   print(x,'x',y,'y',z,'z',w,'w',i,'i')
                                            print(z,'x',y,'y')
                                            plt.imshow(cBlue)
                                            plt.show()
                                      #  elif ( OfX == x and OfY == y ) and  OfX == z and (a == 'M' and  b == '¬H' and qx2=='E' and Somon == 1 ):# and b != '¬E':
                                     #       print('Same row (Y coordinates)')
                                       #     print(Somon,'Somon')
                                        # #   print(x,'x',y,'y',z,'z',w,'w',i,'i')
                                         #   print(z,'x',y,'y')
                                          #  plt.imshow(cBlue)
                                           # plt.show()
                                           
                                            
                                    
                                    
                                    k = ki

                                if k != i :
                                   i -= 1
                                   if ( OfX == x and OfY == y and  (a =='M' or a =='¬M') and ((b == '¬W' and c == '¬E') or (c == 'E' and b == 'W') or (b == '¬W' and c == 'E') or (c == '¬E' and b == 'W'))) :
                                       print(i,'i')
                                       if ( OfX == x and OfY == y and  z== int(somon)-1) :
                                           print(z,'z')
                                           plt.imshow(ggreyy)
                                           plt.show()
                                           print(' Enter a Value () to change square or [M] V [¬M]')
                                           a = input()
                                           a = str(a)
                            
                                           if a != '¬M' and a!='M': 
                                               a = int(a)
                                               print('which y has ')
                                               OfY = input()
                                               OfY = int(OfY)
                                               print('which x has ')
                                               OfX = input()
                                               OfX = int(OfX)
                                               x  = OfX -1
                                               
                                               Green = green
                                         
                                if k == i :
                                    if ( OfX == x and OfY == y and (a != '¬M' and a!='M' or b != 'H') ) :
                                       FS=[x,y,(a)]
                                    #   Fs.append(FS)
                                    #   c = a
                                 #      print(x,'x',y,'y')
                                       
                                       if Somon == 5 and b != '¬H':
                                           print(x+1,'x',y+1,'y')
                                           plt.imshow(ggreyy)
                                           plt.show()
                                           if b != '¬H':
                                               print(' Enter Value, E , ¬E')
                                               q1 = input()
                                       elif Somon==4 and b != '¬H':
                                           print(x+1,'x',y-1,'y')
                                           plt.imshow(ggreyy)
                                           plt.show()
                                           if b != '¬H':
                                               print(' Enter Value, E , ¬E')
                                               q2 = input()
                                       elif Somon==3 and b != '¬H':
                                           print(x-1,'x',y-1,'y')
                                           plt.imshow(ggreyy)
                                           plt.show()
                                           if b != '¬H':
                                               print(' Enter Value, E , ¬E')
                                               q3 = input()
                                       elif Somon==2 and b != '¬H':
                                           print(x-1,'x',y+1,'y')   
                                           plt.imshow(ggreyy)
                                           plt.show()
                                           if b != '¬H':
                                               print(' Enter Value, E , ¬E')
                                               q4 = input()
                                       elif Somon == 1 and b != '¬H':
                                           print(x,'x',y,'y')   
                                           print(' Enter a Value () to change square or [M] V [¬M]')
                                           a = input()
                                           a = str(a)
                                          # a = int(a)
                                           if a != '¬M' and a!='M': 
                                               a = int(a)
                                               print('which y has ')
                                               OfY = input()
                                               OfY = int(OfY)
                                               print('which x has ')
                                               OfX = input()
                                               OfX = int(OfX)
                                               x  = OfX -1
                                               b = int(Tree)
                                               Green = green
                                           Somon = k
                                    Somon -=1
                                    if Somon!= i:
                                      # print(w)
                                       i = int(somon)
                                       z = 0
                                
                            Somon = somon
                           
                            
                           
                            
                            
                            i = ij   
                            Pink = int(Pink)
                            if ij != Pink:
                               Pink+=1
                               qr6 = qrcode.make(OfY)
                               qr6.save('Pink.png')
                               aPink= cv2.imread("Pink.png")
                               cPink = cv2.cvtColor(aPink, cv2.COLOR_BGR2Luv)
                               data, bbox, straight_qrcode = detector.detectAndDecode(aPink)
                               
                            #   print('False')
                               
                              
                               if ( OfX == x and  OfY == y ) :
                                  print(x,'x',y+1,'y') ###=='
                                  plt.imshow(cPink)
                                  plt.show()
                                  if b != '¬H':
                                      print(' Enter Value, E , ¬E')
                                      qx4 = input()
                               if ( OfX == x and  OfY == y+1):
                                  print(x,'x',y,'y') 
                                  plt.imshow(cPink)
                                  plt.show()
                                  if b != '¬H':
                                      print(' Enter Value, E , ¬E')
                                      qx3 = input()
                            
                            if ij == Pink: 
                          #      print('here')
                                ij = 101
                                
                            
                            
                            
                                   
                 
                        Pink = pink
                        
                  
                  
                        
                        if ji!=j:
                            
                            qr6 = qrcode.make(OfX)
                            qr6.save('Green.png')
                            aGreen = cv2.imread("Green.png")
                            cGreen = cv2.cvtColor(aGreen, cv2.COLOR_BGR2HLS)
                            data, bbox, straight_qrcode = detector.detectAndDecode(aGreen)
                            if OfX == x:
                                print(x+1,'x',OfY,'y')
                                plt.imshow(cGreen)
                                plt.show()
                                if b != '¬H':
                                      print(' Enter Value, E , ¬E')
                                      qx2 = input()
                            if  OfX == x+1:
                                print(x,'x',OfY,'y')
                                plt.imshow(cGreen)
                                plt.show()
                                if b != '¬H':
                                      print(' Enter Value, E , ¬E')
                                      qx1 = input()
                                
                                    #k = int(green)
                            Green = int(Green)
                            Green +=1
               #         if a == 0:
                #                print('How many mines would then be?')
                 #               b = input()
                  #              b = int(b)
                   #             black = str(-int(b))
                
                        if ji==j:
                            j = kj
                            j -=1
                            kj = j
                           # 
                         #   
                        
                        ij = ijk
                        i = int(black)
                    #j = ij
                    Green = int(green)
                 #   plt.imshow(ggrreeeyy0)
                   # plt.show() 
                    
                        
                    print('a',a)
                    if ij != i:####black
                        qr6 = qrcode.make(Fs)
                        qr6.save('IceBlueWhite.png')
                        anWhite = cv2.imread("IceBlueWhite.png")
                        ccWhite = cv2.cvtColor(anWhite, cv2.COLOR_RGB2XYZ)
                        data, bbox, straight_qrcode = detector.detectAndDecode(anWhite)
                        plt.imshow(ccWhite)
                        if a == '¬M':
                            plt.imshow(ggrreeeyy0)
                            plt.show() 
                            if ij != i:
                                b = int(Tree)
                                ij= i
                          #  ij-= 1
                        if a == 'M':
                            plt.imshow(ggrreeeyy0)
                            plt.show() 
                            print(' Enter Value, M , ¬M')
                            c = input()
                            if c != 'M':
                                print(' Enter Value, H , ¬H')
                                b = input()
                            if c == 'M':
                                ij= 101
                                i = ij
                                b = int(Tree)
                                print(c,'c',i,'i',j,'j')
                                black = Black
                            
                    
                    if ij == i and a == '¬M' or b == 'H':
                        ij= 101
                        i = ij
                        b = int(Tree)
                        black = Black
                                           #x  = OfX -1
                                           #Green = green
                        #    if ij != i:
                         #       ij-= 1
                          #  if ij == i:
                           #     ij +=1
                    
                 
               
                            
                        
                    
                
                print(i,'i',ij,'ij',ijk,'ijk')
                
                  
               # Tree -= 1
                if jik != i:
                    i = ikj     
                    i += 1
                    ikj = i
                    Mines -= 1
                    print('Entities',Mines)
                    plt.imshow(ggrreeeeyy0)
                    plt.show() 
                    
                   # if jik == i:
                       # i = -Tree
                if jik ==i:
                    i = int(Tree)
                    
                   # Tree-=1
                ### I  
            Tree = tree
  

            print('QR Cream QR')
            
            plt.imshow(gggrreeeeyy0)
            plt.show()   
            yaw -= 1

        dimensions += 1

    ensemble += 1
