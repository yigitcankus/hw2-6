import numpy as np
"""
1'den 200'ye kadar olan çift sayılardan oluşan 10 X 10'luk bir dizi oluşturun. 
arange() fonksiyonu yardımcı olabilir.
"""
cift_sayilar = np.arange(0,200,2).reshape(10,10)

print(cift_sayilar)

#############

"""
kenar(5,7) --> array([[1., 1., 1., 1., 1., 1., 1.],
                       [1., 0., 0., 0., 0., 0., 1.],
                       [1., 0., 0., 0., 0., 0., 1.],
                       [1., 0., 0., 0., 0., 0., 1.],
                       [1., 1., 1., 1., 1., 1., 1.]])
"""


row = int(input("enter row number:"))
column = int(input("enter column number:"))

for i in range(row):
    for j in range(column):
        if i == 0 or i == row-1:
            print("1 ", end="")
        else:
            if j == 0 or j == column-1:
                print("1 ", end="")
            else:
                print("0 ",end="")
    print("\n")