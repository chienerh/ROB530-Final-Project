#!/usr/bin/env python
# plot collected position/orientation data from lego loam
import matplotlib.pyplot as plt
import sys
import math
print sys.argv
if len(sys.argv)==2:
	if sys.argv[1].endswith('txt'):
		filename=sys.argv[1]
	else:
		print 'Need txt file'
		sys.exit(1)
else:
	print 'Need to specify txt file'
	sys.exit(1)

file=open(filename,"r")
alldata=file.readlines()

xCood=[]
yCood=[]
count=0
for line in alldata:
	count+=1
	if count%3==1:
		xCood.append(-float(line))
	if count%3==2:
		yCood.append(float(line))
'''
file=open('GPS-RTK-20180719.txt',"r")
alldata=file.readlines()
gtx=[]
gty=[]
for line in alldata:
	inline=line.split(" ")
	#print inline
	gtx.append(float(inline[0]))
	gty.append(float(inline[1]))
'''
fig=plt.figure()
plt.plot(xCood,yCood)
#plt.plot(gtx,gty)
#plt.xlim(-500, 800) 
#plt.ylim(-900, 400)
plt.show()