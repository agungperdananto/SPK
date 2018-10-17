import numpy as np

#Input

print('Jumlah data: ')
qty = int(input())
data = []
print('INPUT DATA:')
for i in range(qty):
	 data_ = input().strip().split(' ')
	 data.append(data_)
print('INPUT BOBOT(harus sesuai dengan jumlah kolom):')
bobot = input().strip().split(' ')
bobot = [int(x) for x in bobot]  # into integer
data = np.array(data).astype(float)

print('INPUT ATTRIBUT(harus sesuai dengan jumlah kolom):')
print('0 = cost, dan 1 = benefit')
attr = input().strip().split(' ')
attr = [int(x) for x in attr]  # into integer

#proses
#normalisasi bobot
bobot_=[]
for x in bobot:
    x_=x/np.sum(bobot)
    bobot_.append(x_)
bobot_
bobot_ = [round(x,2) for x in bobot_]
bobot = bobot_

def normalisasi(data):
    x, y = data.shape
    data_normal=[]
    for i in range(x):
        data_=[]
        for j in range(y):

            if attr[j] == 0:
                r = round(np.min(data[:,j])/data[i,j],2)
    #             print(data[i,j], "min:", np.min(data[:,j]))

            else:
                r = round(data[i,j]/np.max(data[:,j]),2)
    #             print(data[i,j],"max:", np.max(data[:,j]))

            data_.append(r)
    #     print(data_)
        data_normal.append(data_)
    data_normal = np.array(data_normal).astype(float)
#     print(data_normal)
    return data_normal
R = normalisasi(data)  

def final(R):
    x, y = R.shape
    hasil=[]
    for i in range(x):
        z_=0
        for j in range(y):
            z = R[i,j]*bobot[j]
            z_ += z
        hasil.append(round(z_,2))
    return hasil

hasil = final(R)



#output
print('DATA: ',data)
print('BOBOT: ', bobot)
print('ATTRIBUT: ', attr)

x=1
winner = np.max(hasil)
for i in hasil:
    print('A>',x,':', i,end='')
    if i >= winner:
        print(' ==> winner')
    else:
        print("")
    x+=1

