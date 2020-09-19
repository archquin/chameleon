#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 02:12:01 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 20:13:02 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 07:56:08 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 02:56:35 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 23:58:12 2020

@author: fadewell
"""

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
c1 = c2 = c3 = c4 = cx1 = cx2 = cy1 = cy2 = 0
c = d = 0
dimensions = 0
Fs = []
while ensemble <1 :
    white = '-2'   ######## white <---->Green, Cream           1
    Yellow = '-5'   ####-2,-3,-4,----> Yellow==k @ k = 0 ======> 4 White
    Blue = '-7'      ##### -3,-4,-5 ---->Blue == j @ j = -1
    Somon = '5'    ##### 1,3,4,5 -----> Somon = k @ k = 0
    Pink = '-6'      ###### 2,3,4 ----> Pink = ij @ ij = 0
    Green= '-4'      ##### 1,-1,-2,-3 ----> Green = j @ j = 2
    black = '-5' ##### -2,-3,-4 -----> black == i == ij@ ij = 0
    Tree = '2'  #### i 3x
    Cream = '2'  ######## 3,4,5-------> is white too 2
    
    print('How many entities?')
    b = input()
    b = int(b)
    mines = b
    
    print('what value of entity?')
    a = input()
    a = int(a)
    er = a
    
    OfY = OfX = 0
    while dimensions < mines:
       
      #  Somon = str(-int(Green))
    #    Blue = str( int(Green)+1 )     ##### -3,-4,-5 ---->Blue == j @ j = -1
        qqrrr22 = qrcode.make(Cream)
        qqrrr22.save('r000partEnQtities000r.png')
        iiim0g0mgg111 = cv2.imread("r000partEnQtities000r.png")
        gggrreeeeyy0 = cv2.cvtColor(iiim0g0mgg111, cv2.COLOR_XYZ2RGB)
        cream, bbox, straight_qrcode = detector.detectAndDecode(iiim0g0mgg111)

        Cream = int(cream)
        d = 0
        while Cream > 0:
            
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
                
               
                
                qqrrr22 = qrcode.make(black)
                qqrrr22.save('r000partEntities000r.png')
                iiim00mgg111 = cv2.imread("r000partEntities000r.png")
                ggrreeeeyy0 = cv2.cvtColor(iiim00mgg111, cv2.COLOR_HSV2RGB)
                Black, bbox, straight_qrcode = detector.detectAndDecode(iiim00mgg111)
                i = 3
                if OfX != 0 and OfY != 0:
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
                                                
                                                if (OfX == x and OfY == y and OfX == z and OfY == w and ((a == 'M' or c == 'M')  and  b !='¬H' and d!='M') ):#and c == '¬E') ):
                                                 #   print('Somon',Somon)
                                                    if Nn == 1 and ((c1 == '¬M'  or c1 == '0' ))  and Somon == 5  :
                                                    #    print(x+1,'x',y+1,'y')
                                                        print(z+1,'ix',w+1,'iy')
                                                        FS=[x+1,y+1]
                                                        plt.imshow(cWhite)
                                                        plt.show()
                                             
                                                    elif Nn==2 and ((c2 == '¬M'  or c2 == '0' ))  and Somon == 4 :
                                                      #  print(x+1,'x',y-1,'y')
                                                        print(z+1,'ix',w-1,'iy')
                                                        FS=[x+1,y-1]
                                                        plt.imshow(cWhite)
                                                        plt.show()
                                          
                                                    elif Nn==3  and ((c3 == '¬M'  or c3 == '0' ))  and Somon == 3 :
                                                      #  print(x-1,'x',y-1,'y')
                                                        print(z-1,'ix',w-1,'iy')
                                                        FS=[x-1,y-1]
                                                        plt.imshow(cWhite)
                                                        plt.show()
                                                      
                                                    elif Nn==4  and ((c4 == '¬M'  or c4 == '0'))  and Somon == 2 :
                                                      #  print(x-1,'x',y+1,'y')   
                                                        print(z-1,'ix',w+1,'iy')
                                                        FS=[x-1,y+1]
                                                        plt.imshow(cWhite)
                                                        plt.show()
                                                    
                                                    
                                                    
                           
                                        Yellow = int(Yellow)
                                        
                                        if  k != Yellow:
                                            Yellow +=1
                                            col = [x,w]
                                            qr6 = qrcode.make(col)
                                            qr6.save('Yellow.png')
                                            aYellow = cv2.imread("Yellow.png")
                                            cYellow = cv2.cvtColor(aYellow, cv2.COLOR_BGR2GRAY)
                                            data, bbox, straight_qrcode = detector.detectAndDecode(aYellow)
  
                                        if k == Yellow or c != 'M':                                               

                                            Yellow = yellow
                                      #      print(Yellow)
                                            k = int(somon)
                                            if (OfX == z and OfY == y and OfX == x) and OfY == w+1 and ((a == 'M' or c == 'M')  and  ((cx2 == '¬M'  or cx2 == '0' )) and b !='¬H' and d!='M' and Somon == 5)  :
                                              #  print(Somon,'Somon')
                                               # print('Same column (X coordinates)')
                                                #print(x,'x',y,'y',z,'z',w,'w',i,'i')
                                                print(x,'x',w,'y')
                                                plt.imshow(cYellow)
                                                plt.show()
                                            #    qx3 = '¬E'
                                            if (OfX == z and OfY == y and OfX == x) and OfY == w-1 and ((a == 'M' or c == 'M') and ((cx1 == '¬M' or cx1 == '0'))  and b !='¬H' and d!='M' and Somon == 1)  :
                                                print(Somon,'Somon')
                                               # print('Same column (X coordinates)')
                                             #   print(x,'x',y,'y',z,'z',w,'w',i,'i')
                                                print(x,'x',w,'y')
                                                plt.imshow(cYellow)
                                                plt.show()
                                                plt.show()
                                             #   qx4 = '¬E'
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
                                       
                                    if j == Blue or c != 'M':
                                        Blue = blue
                                        
                                        j = int(Cream)
                                        jk = j
                                        
                                        if ( OfX == x and OfY == y ) and OfX == z+1  and ((a == 'M' or c == 'M') and  ((cy2 == '¬M' or cy2 == '0'))  and b !='¬H' and d!='M' and Somon == 5):# and b != '¬E':
                                  
                                            print(z,'x',y,'y')
                                            plt.imshow(cBlue)
                                            plt.show()
                                        elif ( OfX == x and OfY == y ) and  OfX == z-1 and ((a == 'M' or c == 'M') and ((cy1 == '¬M' or cy1 == '0'))  and b !='¬H' and d!='M' and Somon == 1 ):# and b != '¬E':
                                     #       print('Same row (Y coordinates)')
                                            print(Somon,'Somon')
                                         #   print(x,'x',y,'y',z,'z',w,'w',i,'i')
                                            print(z,'x',y,'y')
                                            plt.imshow(cBlue)
                                            plt.show()
                                      #      qx2 = '¬E'
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
                                   if  b != '¬H' and c == 'M' and d!='M':
                                           a = 'M'
                                           black = -1
                                  
                                   
                                   
                                           
                                         
                                if k == i :
                                    if ( OfX == x and OfY == y and (a != '¬M' and (a!='M' or b != '¬H')) and c == 'M' ) :
                                       FS=[x,y,(a)]
                                 
                                       if Somon == 5 and b != '¬H' and ((c1 == 'M' or c1 == '0' )):
                                           print(x+1,'x',y+1,'y')
                                           plt.imshow(ggreyy)
                                           plt.show()
                                        
                                       elif Somon==4 and b != '¬H' and ((c2 == 'M' or c2 == '0')) :
                                           print(x+1,'x',y-1,'y')
                                           plt.imshow(ggreyy)
                                           plt.show()
                                    
                                       elif Somon==3 and b != '¬H' and ((c3 == 'M' or c3 == '0' )):
                                           print(x-1,'x',y-1,'y')
                                           plt.imshow(ggreyy)
                                           plt.show()
                                        
                                       elif Somon==2 and b != '¬H' and ((c4 == 'M'  or c4 == '0' )):
                                           print(x-1,'x',y+1,'y')   
                                           plt.imshow(ggreyy)
                                           plt.show()
                                     
                                       elif Somon == 1 and b != '¬H':
                                           print(x,'x',y,'y')   
                                          
                                         
                                           
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
                               
                              
                               if ( OfX == x and  OfY == y and OfY != 0 and OfX!=0) and ((cx1 == 'M' or cx1 == '0'))  and b !='¬H'  and c == 'M' and d!='M':
                                  print(x,'x',y+1,'y') ###=='
                                  plt.imshow(cPink)
                                  plt.show()
                              
                               if ( OfX == x and  OfY == y+1 and OfY != 0 and OfX!=0) and ((cx2 == 'M' or cx2 == '0'))   and b !='¬H'  and c == 'M' and d!='M':
                                  print(x,'x',y,'y') 
                                  plt.imshow(cPink)
                                  plt.show()
                                
                            
                            if ij == Pink or c != 'M': 
                          #      print('here')
                                ij = 101
                                
                            
                            
                            
                                   
                 
                        Pink = pink
                        
                  
                  
                        
                        if ji!=j:
                            
                            qr6 = qrcode.make(OfX)
                            qr6.save('Green.png')
                            aGreen = cv2.imread("Green.png")
                            cGreen = cv2.cvtColor(aGreen, cv2.COLOR_BGR2HLS)
                            data, bbox, straight_qrcode = detector.detectAndDecode(aGreen)
                            if OfX == x and OfY != 0 and OfX!=0 and ((cy1 == 'M' or cy1 == '0'))  and b !='¬H' and c == 'M' and d!='M':
                                print(x+1,'x',OfY,'y')
                                plt.imshow(cGreen)
                                plt.show()
                              
                        
                            if  OfX == x+1 and OfY != 0 and OfX!=0 and ((cy2 == 'M' or cy2 == '0')) and b !='¬H'  and c == 'M' and d!='M':
                                print(x,'x',OfY,'y')
                                plt.imshow(cGreen)
                                plt.show()
                              
                                      
                            Green = int(Green)
                            Green +=1
                        
                
                        if ji==j :
                            j = kj
                            j -=1
                            kj = j
                           # 
                         #   
                        
                        ij = ijk
                       # i = int(black)
                    #j = ij
                    Green = int(green)
                 

                    
              
                    black = int(black)  
                    print('loading a',a)
                    if ij != black:####black
                        qr6 = qrcode.make(KiJ)
                        qr6.save('IceBlueWhite.png')
                        anWhite = cv2.imread("IceBlueWhite.png")
                        ccWhite = cv2.cvtColor(anWhite, cv2.COLOR_RGB2XYZ)
                        data, bbox, straight_qrcode = detector.detectAndDecode(anWhite)
                        plt.imshow(ccWhite)
                        if  OfX != 0 and OfY != 0 :
                           
                            if black == -5 and a != 'M' :
                                print(OfX+1,'x',OfY+1,'y')
                                plt.imshow(ggrreeeyy0)
                                plt.show() 
                                print(' Enter Value, M , ¬M')
                                c1 = input ()  
                               
                            elif black==-4 and  a != 'M' :
                                print(OfX+1,'x',OfY-1,'y')
                                plt.imshow(ggrreeeyy0)
                                plt.show() 
                                print(' Enter Value, M , ¬M')
                                c2 = input ()  
                              
                            elif black==-3 and a != 'M'  :
                                print(OfX-1,'x',OfY-1,'y')
                                plt.imshow(ggrreeeyy0)
                                plt.show() 
                                print(' Enter Value, M , ¬M')
                                c3 = input ()  
                               
                            elif black==-2 and  a != 'M'  :
                                print(OfX-1,'x',OfY+1,'y')   
                                plt.imshow(ggrreeeyy0)
                                plt.show() 
                                print(' Enter Value, M , ¬M')
                                c4 = input ()  
                               
                            elif black == -1 :
                                b = 'H'
                                if a == 'M':
                                    d = '¬M'
                                    OfX = OfY = 0
                                    a = er
                                    c = '¬M'
                                  
                                    
                        black +=1
                        
           
                            
                    
                    if black == ij or b == '¬H':
                        ij= 101
                        i = ij
                        black = Black
                        
   
                
             #   print(i,'i',ij,'ij',ijk,'ijk')
             #   
                  
               # Tree -= 1
                if jik != i:
                    i = ikj     
                    i += 1
                    ikj = i
                 #   print('Entities',i)
                   # Mines -= 1
                    if OfX != 0 and OfY == 0:
                        plt.imshow(ggrreeeeyy0)
                        plt.show() 
                        print('which y has ')
                        OfY = input()
                        OfY = int(OfY)
                        print(' Enter Value, M , ¬M')
                        cx2 = input()
                        print(OfX,'x', OfY-1,'y')
                    elif OfX != 0 and OfY != 0 and b !='¬H':
                        plt.imshow(ggrreeeeyy0)
                        plt.show() 
                        print(' Enter Value, M , ¬M')
                        cx1 = input()
                        print(OfX,'x', OfY+1,'y')
                    

                if jik ==i:
                    i = int(Tree)
                    
                   # Tree-=1
            Tree = tree
  

            
            
            if OfX == 0:
                plt.imshow(gggrreeeeyy0)
                plt.show()
                print('which x has ')
                OfX = input()
                OfX = int(OfX)
                print(' Enter Value, M , ¬M')
                cy2 = input()
                print(OfX-1,'x')
             
            elif OfX != 0:
                if b != '¬H':
                    plt.imshow(gggrreeeeyy0)
                    plt.show()
                    print(' Enter Value, M , ¬M')
                    cy1 = input()
                    print(OfX+1,'x')
                elif b =='¬H':
                    print('QR Cream QR')
                    c = 0
                    a = er
                    b  = mines
                    OfX = OfY = 0
                    
            Cream -= 1
        Cream = cream
     #   print(' Enter Value, M , ¬M')    
        c = 'M'
        dimensions += 1

    ensemble += 1
