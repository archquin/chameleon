#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 05:22:24 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 00:23:08 2020

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
import numpy as np
#from pandas import D
import matplotlib.pyplot as plt
import cv2 as cv2
detector = cv2.QRCodeDetector()
from itertools import combinations
#import pandas as pd
#import
ensemble = 0
ijk = 0
KiJ=JiK=Nn = 0
q1=q2=q3=q4=0
qx1=qx2=qx3=qx4=0
c1 = c2 = c3 = c4 = cx1 = cx2 = cy1 = cy2 = 0
cc1=cc2=cc3=cc4=cc5=cc6=cc7=cc8=0
c = d = e = f =0
dimensions = 0
bb = []
cc = []
aa = []
while ensemble <1 :
    white = '0'   ######## white <---->Green, Cream           1
    Yellow = '-11'   ####-2,-3,-4,----> Yellow==k @ k = 0 ======> 4 White
    Blue = '-2'      ##### -3,-4,-5 ---->Blue == j @ j = -1
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
         #   bb = Mines
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
                                    j = -1 # int(blue)-len(aa)
                                    
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
                                        ik = 2
                                        
                                        white = int(white) ### white == jk , -6
                                        jk = 3
                                      #  KiJ = 0
                                        
                                        while ik < jk:
                 
                                            white = int(white)
                                            if ik != white:
                                                ik-= 1
                                                qr6 = qrcode.make(1111)
                                                qr6.save('White.png')
                                                aWhite = cv2.imread("White.png")
                                                cWhite = cv2.cvtColor(aWhite, cv2.COLOR_BGR2RGB)
                                                data, bbox, straight_qrcode = detector.detectAndDecode(aWhite)
                                                if  f == 'H':
                                                    print(Nn,'Nn',ik,'ik')
                                                    print(aa[Nn][ik])
                                                    plt.imshow(cWhite)
                                                    plt.show()
                                                
                                            if  ik == white:
                                                white = White
                                                ik = 3
                                                
                                                
                                                    
                                                    
                           
                                        Yellow = int(Yellow)
                                        
                                        
                                        if  k != Yellow:
                                            Yellow +=1
                                            col = [x,w]
                                            qr6 = qrcode.make(col)
                                            qr6.save('Yellow.png')
                                            aYellow = cv2.imread("Yellow.png")
                                            cYellow = cv2.cvtColor(aYellow, cv2.COLOR_BGR2GRAY)
                                            data, bbox, straight_qrcode = detector.detectAndDecode(aYellow)
                                            if f == 'H':
                                                Nn+=1
                                                plt.imshow(cYellow)
                                                plt.show()
                                                if Nn == 10:
                                                    f = '¬H'
                                            
                                        if k == Yellow or c != 'M'  :                                               

                                            Yellow = yellow
                                      #      print(Yellow)
                                            k = int(somon)
                                            
                                 
                                    Blue = int(Blue)
                     
                                    if j != Blue:  #### blue -2
                                        j -= 1
                                        
                                        row =[z,y]
                                        qr6 = qrcode.make(row)
                                        qr6.save('Blue.png')
                                        aBlue = cv2.imread("Blue.png")
                                        cBlue = cv2.cvtColor(aBlue, cv2.COLOR_BGR2HSV)
                                        data, bbox, straight_qrcode = detector.detectAndDecode(aBlue)
                                        #if (OfX == x and OfY == y and OfX == z and OfY == w and ((a == 'M' or c == 'M')  and  b !='¬H' and d!='M' and f == 'H') ):
                                           # jj+=1
                                       
                                    if j == Blue or c != 'M':
                                        Blue = blue
                                        
                                        j = int(somon)
                                        jk = j
                                        
                                       
                              
                                           
                                            
                                    
                                    
                                    k = ki

                                if k != i :
                                   i -= 1
                                   if  b != '¬H' and c == 'M' and d!='M' and f != 'H':
                                           a = 'M'
                                          # print(f,'f')
                                           black = -2
                                   elif  b != '¬H' and c == 'M' and d!='M' and f == 'H' or f == '¬H':
                                           a = 'M'
                                         #  print(f,'f')
                                           black = -1           
                                  
                                   
                                   
                                           
                                         
                                if k == i :
                                    if ( OfX == x and OfY == y and (a != '¬M' and (a!='M' or b != '¬H')) and c == 'M' and f != 'H' and f != '¬H') :
                                       FS=[x,y,(a)]
                                       
                                       if Somon == 5 and b != '¬H' and c1 == 'M':
                                           print(x+1,'x',y+1,'y')
                                           plt.imshow(ggreyy)
                                           plt.show()
                                           cc3 = (x+1,y+1)
                                           cc.append(cc3)
                                      
                                       elif Somon==4 and b != '¬H' and c2 == 'M':
                                           print(x+1,'x',y-1,'y')
                                           plt.imshow(ggreyy)
                                           plt.show()
                                           cc4 = (x+1,y-1)
                                           cc.append(cc4)
                                    
                                       elif Somon==3 and b != '¬H' and c3 == 'M':
                                           print(x-1,'x',y-1,'y')
                                           plt.imshow(ggreyy)
                                           plt.show()
                                           cc5 = (x-1,y-1)
                                           cc.append(cc5)
                                         
                                       elif Somon==2 and b != '¬H' and c4 == 'M':
                                           print(x-1,'x',y+1,'y')   
                                           plt.imshow(ggreyy)
                                           plt.show()
                                           cc6 = (x-1,y+1)
                                           cc.append(cc6)
                                      
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
                               
                              
                               if ( OfX == x and  OfY == y and OfY != 0 and OfX!=0) and cx1 == 'M' and b !='¬H'  and c == 'M' and d!='M' and f != 'H' and f != '¬H':
                                  print(x,'x',y+1,'y','1111') ###=='
                                  plt.imshow(cPink)
                                  plt.show()
                                  cc7 = (x,y+1)
                                  cc.append(cc7)
                             
                               if ( OfX == x and  OfY == y+1 and OfY != 0 and OfX!=0) and cx2 == 'M' and b !='¬H'  and c == 'M' and d!='M' and f != 'H' and f != '¬H':
                                  print(x,'x',y,'y') 
                                  plt.imshow(cPink)
                                  plt.show()
                                  cc2=(x,y)
                                  cc.append(cc2)
                              
                            
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
                            if OfX == x and OfY != 0 and OfX!=0 and cy1 == 'M' and b !='¬H' and c == 'M' and d!='M' and f != 'H' and f != '¬H':
                                print(x+1,'x',OfY,'y', '1111')
                                plt.imshow(cGreen)
                                plt.show()
                                cc8 = (x+1,OfY)
                                cc.append(cc8)
                                 
                      
                        
                            if  OfX == x+1 and OfY != 0 and OfX!=0 and cy2 == 'M' and b !='¬H'  and c == 'M' and d!='M' and f != 'H' and f != '¬H':
                                print(x,'x',OfY,'y')
                                plt.imshow(cGreen)
                                plt.show()
                                cc1 = (x,OfY)
                                cc.append(cc1)
                              
                            Green = int(Green)
                            Green +=1
                        
                
                        if ji==j or Nn == 10:
                            j = kj
                            j -=1
                            kj = j
                           # 
                         #   
                        
                        ij = ijk
                       # i = int(black)
                    #j = ij
                    Green = int(green)
                    if  OfY != 0 and OfX!=0 and  b !='¬H'  and c == 'M' and d!='M' and f != '¬H':#and f == 'H':      
                        #cc = (cc1, cc2, cc3,cc4,cc5,cc6,cc7,cc8)
                       # cc.remove(0)
                        comb = combinations(cc, er) 
                        print(i,'i',z,'z')
                        f = 'H'
                       # bb.append(cc)
                        for e in list(comb): 
                            print (e) 
                            e = list(e)
                            aa.append(e)
                    
              
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
                                bb.append([OfX+1,OfY+1])
                            elif black==-4 and  a != 'M' :
                                print(OfX+1,'x',OfY-1,'y')
                                plt.imshow(ggrreeeyy0)
                                plt.show() 
                                print(' Enter Value, M , ¬M')
                                c2 = input ()  
                                bb.append([OfX+1,OfY-1])
                            elif black==-3 and a != 'M'  :
                                print(OfX-1,'x',OfY-1,'y')
                                plt.imshow(ggrreeeyy0)
                                plt.show() 
                                print(' Enter Value, M , ¬M')
                                c3 = input ()  
                                bb.append([OfX-1,OfY-1])
                            elif black==-2 and  a != 'M' and f != 'H'  :
                                print(OfX-1,'x',OfY+1,'y')   
                                plt.imshow(ggrreeeyy0)
                                plt.show() 
                                print(' Enter Value, M , ¬M')
                                c4 = input ()  
                                bb.append([OfX-1,OfY+1])
                            elif black == -1 :
                                b = 'H'
                                if a == 'M':
                                    d = '¬M'
                                    OfX = OfY = 0
                                    a = er
                                    c = '¬M'
                                  
                                    
                        black +=1
                        
           
                            
                    
                    if black == ij or f == '¬H':
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
                        bb.append([OfX,OfY-1])
                    elif OfX != 0 and OfY != 0 and b !='¬H':
                        plt.imshow(ggrreeeeyy0)
                        plt.show() 
                        print(' Enter Value, M , ¬M')
                        cx1 = input()
                        print(OfX,'x', OfY+1,'y')
                        bb.append([OfX,OfY+1])
                        

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
                bb.append(OfX-1)
            elif OfX != 0:
                if b != '¬H':
                    plt.imshow(gggrreeeeyy0)
                    plt.show()
                    print(' Enter Value, M , ¬M')
                    cy1 = input()
                    print(OfX+1,'x')
                    bb.append(OfX+1)
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
