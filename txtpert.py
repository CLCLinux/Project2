# TXTPERT from usa today paper
# Note: Limit 21 for nested statements for python
print  "Created by Julie Bell - 7-19-2013"
print  "jmwebstuff@yahoo.com"
print " "
print  "This is a computerized version of USA's txtpert puzzle. This only gives you " 
print "the possible words for the number combinations."
print " "
import os
import readline
import sys

# Build our dictionary of numbers and a list of associated values for that
# number.
txt={}	
txt[0] = [' ',' ',' ',' ']
txt[1] = [' ',' ',' ',' ']
txt[2] = ['a','b','c',' '] 
txt[3] = ['d','e','f',' ']
txt[4] = ['g','h','i',' '] 
txt[5] = ['j','k','l',' '] 
txt[6] = ['m','n','o',' ']
txt[7] = ['p','q','r','s']
txt[8] = ['t','u','v',' ']
txt[9] = ['w','x','y','z']

a1 = " "
a2 = " "
a3 = " " 
a4 = " "
a5 = " "
a6 = " "
a7 = " "
a8 = " "
a9 = " "
debug = 0 

# Check our values for dictionary listing
if debug == 1 :
	for i in range(2,10):
		print str(i) +  " is " + str(txt[i])

def GetNumber():
#	word= 5678
# word= 7227
#word= 2331
	#word = 86684
	word = raw_input("enter in a number 2 - 9  digits long: ")
	print word

# word length 2 thru 9 digits
	lword =len(str( word))
	if lword >9 or lword <2:
	 	print "Invalid number of digits must be between 2 and 9"
		sys.exit()

	sword=str(word)
	w0=sword.find("0")
	w1=sword.find("1")
	if w0 > 1 or w1 > 1:
		print "0 and 1 are invalid number - no combinations possible"
		sys.exit()

	if sword.isdigit() == False :
		print "Only digits 2 -9 are valid"
		sys.exit()

	if debug == 1 :
		print len(sword)
	return sword

# let's just get the listing for each letter in our word

def ListWord(sword):
	global debug
	xlen = len(sword)
	if debug == 1:
		print " "
		print " **** watch the below for our numbers in our string ****"
		print sword
		for i in range(0,xlen):
			print sword[i] 
			print int(sword[i])
			print txt[int(sword[i])]	

		print " "
		print '*** combining rows together ***'
	tTable=[]
	for i in range(0,xlen):
		A= txt[int(sword[i])]	
		tTable.append(A)
	if debug == 1:
		print tTable
		print " "
		print len(tTable)
 	return tTable 

def MakeTables(sword,tTable):  
	global a1,a2,a3,a4,a5,a6,a7,a8,a9
	a= tTable[0] 
	if debug == 1:
		print " "
		print "*** just one value from each list ***"
		print tTable[0]
		print a[0]

		print " "
	# for 4 letter word do this...
	# We can create a separate function for each lengh
	# of works 2 - 9
	# 
	
		print " "
		print "*** My list of combinations??? 4 letter word hard coded *** "

	res=""
	# Get the list of tables into it's own variable list 
	xlen= len(sword)
	a1 = tTable[0]
	a2 = tTable[1]
	if xlen < 3:
		return
	a3 = tTable[2]
	if xlen < 4:
		return
	a4 = tTable[3]
	if xlen < 5:
		return
	a5 = tTable[4]
	if xlen < 6:
		return
	a6 = tTable[5]
	if xlen < 7:
		return
	a7 = tTable[6]
	if xlen < 8:
		return
	a8 = tTable[7]
	if xlen < 9:
		return
	a9 = tTable[8]
	return 

def Letter2():
	global a1,a2,debug  
	final=[]
	for i in range(4):
		for j in range(4):
			res = a1[i] + a2[j] 
			final.append(res)
	return final

def Letter3():
	global a1,a2,a3,debug  
	final=[]
	for i in range(4):
		for j in range(4):
			for k in range(4):
					res = a1[i] + a2[j] + a3[k] 
					final.append(res)
					if debug == 1:
						print res
	if debug == 1:
		print final
		print len(final)
	return final
def Letter4():
	global a1,a2,a3,a4,debug  
	final=[]
	for i in range(4):
		for j in range(4):
			for k in range(4):
			      for l in range (4):
					res = a1[i] + a2[j] + a3[k] + a4[l]
					final.append(res)
					if debug == 1:
						print res
	if debug == 1:
		print final
		print len(final)
	return final

def Letter5():
	global a1,a2,a3,a4,a5,debug  
	final=[]
	for i in range(4):
	    for j in range(4):
		for k in range(4):
		    for l in range (4):
			for m in range(4):
				res = a1[i] + a2[j] + a3[k] + a4[l] + a5[m]
				final.append(res)
	return final
def Letter6():
	global a1,a2,a3,a4,a5,a6,debug  
	final=[]
	for i in range(4):
	    for j in range(4):
		for k in range(4):
		    for l in range (4):
			for m in range(4):
	                    for n in range(4):
				res = a1[i] + a2[j] + a3[k] + a4[l] + a5[m] +a6[n]
				final.append(res)
	return final
def Letter7():
	global a1,a2,a3,a4,a5,a6,a7,debug  
	final=[]
	for i in range(4):
	    for j in range(4):
		for k in range(4):
		    for l in range (4):
			for m in range(4):
	                    for n in range(4):
			        for o in range(4): 
				    res = a1[i] + a2[j] + a3[k] + a4[l] + a5[m] +a6[n] + a7[o]
				    final.append(res)
	return final
def Letter8():
	global a1,a2,a3,a4,a5,a6,a7,a8,debug  
	final=[]
	for i in range(4):
	    for j in range(4):
		for k in range(4):
		    for l in range (4):
			for m in range(4):
	                    for n in range(4):
			        for o in range(4): 
			            for p in range(4):	
				        res = a1[i] + a2[j] + a3[k] + a4[l] + a5[m] +a6[n] + a7[o] + a8[p]
				        final.append(res)
	return final
def Letter9():
	global a1,a2,a3,a4,a5,a6,a7,a8,a9,debug  
	final=[]
	for i in range(4):
	    for j in range(4):
		for k in range(4):
		    for l in range (4):
			for m in range(4):
	                    for n in range(4):
			        for o in range(4): 
			            for p in range(4):	
                                        for q in range(5):
				            res = a1[i] + a2[j] + a3[k] + a4[l] + a5[m] +a6[n] + a7[o] + a8[p] + a9[q]
				            final.append(res)
	return final


# we now have out list of all possible combinations 256
# now we have to remove all those with space at any spot but in the beginning??
# or any with a space ?? yes no spaces words ..

def FinishUp(sword,final):
	global debug 
	if debug == 1:
		print "*** sorted list ***"
		print " "
		final.sort()
		print final


# Now strip out all words that have a space in them.
		print "*** remaining word list ***"
		print " "
	temp=[]
	for i in range(len(final)):
		T1 = final[i]
		if T1.find(" ") == -1 :
		    temp.append(T1)

	if debug == 1:
		print temp
#
# Write out our list to a file so that we can check for bad list
# 
	f = open("txtpert.txt",'w')

	for i in range (len(temp)):
		s = temp[i] + "\n"
		f.write(s)

	f.close()

# Now we can get a list of words that are bad
# cat t1 | aspell list >badlist
# badlist - file   

	s="cat txtpert.txt |aspell list >badlist.txt"
	os.system(s)

# remove those badlist words from our array above to get out list of 
# valid words

	f = open("badlist.txt",'r')
	for word1 in f:
		word2= word1.split('\n')
		del1= temp.index(word2[0])
		temp.remove(word2[0])
		if debug == 1 :
			print word2[0] + " " + str(del1)
	f.close()

	print  " "
	print "*** Only our valid words from our list  ****"
	print sword + " has the following possible combinations :" 
	print  temp
	return 
#
#  The main program of stuff now that we have functions
#
while (1):
	sword = GetNumber()
	tTable = ListWord(sword)
	MakeTables(sword,tTable)
	xlen = len(sword)
	if xlen == 2:
		final = Letter2()
	if xlen == 3:
		final = Letter3()
	if xlen == 4 :
		final = Letter4()
	if xlen == 5 :
		final = Letter5()
	if xlen == 6 :
		final = Letter6()
	if xlen == 7 :
		final = Letter7()
	if xlen == 8 :
		final = Letter8()
	if xlen == 9 :
		final = Letter9()
	if len(final) > 0:
		 FinishUp(sword, final) 
