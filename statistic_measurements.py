import os
from collections import OrderedDict
from collections import defaultdict
import sys
from math import log10
import numpy as np
from scipy import stats
import collections
#import statistics


hex_vals = defaultdict()

myKey = -1	

for line in open("hex_vals.txt", "r"):
	if len(line.split()) == 0:
		continue
	if not line[0:2] == "0x":
		myKey = line.split()[1]
		continue
	if myKey in hex_vals:
		hex_vals[ myKey ].append( line.split()[0] )
	else:
		hex_vals[ myKey ] = []
		hex_vals[ myKey ].append( line.split()[0] )

hex_vals = OrderedDict(sorted(hex_vals.items()))
signal_strength = defaultdict()
s_s = defaultdict()
ss_all_vals = defaultdict()

count = 0
for key in hex_vals:
	signal_strength[key] = []
	s_s[key] = 0
	ss_all_vals[key] = []
	for elem in hex_vals[key]:
		q = ( int(elem,0) >> 4 ) * 2
		i = ( int(elem,0) & int("0x0F",0) ) * 2
		q = int(q)**2
		i = int(i)**2	
		if i+q == 0:
			print key, "\t", elem, "\tuh-oh"
			continue
		# raw_input("")
		SS = 10 *log10( (i+q) )
		print type(SS)
		print SS
		s_s[key] += SS
		ss_all_vals[key].append( SS )
		count +=1
		signal_strength[key].append(SS)
	if not count==0:
		s_s[key] /= count
	count = 0

outfile = open("avg_signal_strength.txt", "w")
#s_s = OrderedDict(sorted(s_s.keys()))

for key in s_s:
	outfile.write("\n" + str(key))
	outfile.write("\t" + str(s_s[key]))


outfile.close() #close prev file

outfile = open("iterations_signal_strength.txt", "w")
ss_all_vals = OrderedDict(sorted(ss_all_vals.items()))
for key in ss_all_vals:
	for val in ss_all_vals[key]:
		outfile.write("\n" + str(key))
		outfile.write("\t" + str(val))
outfile.close()

outfile = open("std_dev_signal_strength.txt", "w")
for key in ss_all_vals:
		#standard_dev = statistics.stdev(ss_all_vals[key])
		yee = np.array(ss_all_vals[key])
		standard_dev = np.std(yee)
		outfile.write("\n" + str(key))
		outfile.write("\t"+ str(standard_dev))
outfile.close()

outfile = open("mode.txt", "w")
for key in ss_all_vals:
		#standard_dev = statistics.stdev(ss_all_vals[key])
		yee = (ss_all_vals[key])
		f = (stats.mode(yee)[0])
		outfile.write("\n" + str(key))
		outfile.write("\t" + str(f))
outfile.close()


#filter out all readings not within the standard deviation#
#1.find standard deviation and median and store them in dict
st = defaultdict()
median = defaultdict()
mode = defaultdict()

for key in ss_all_vals:
	yee = np.array(ss_all_vals[key])
	mod = stats.mode(yee)
	m = np.array(ss_all_vals[key])
	standard_dev = np.std(yee)
	me = np.median(m)
	st[key]= standard_dev
	median[key] = me
	mode[key] = mod

#print ss_all_vals
#2. find all data values within this stand dev(filter) and store them in dict
gucci= defaultdict()
for key in s_s:
	gucci[key] = []
	upper = median[key] + st[key]
	lower = median[key] - st[key]
	for val in ss_all_vals[key]:
		if (val <= upper):
			if (val >= lower):
				gucci[key].append(val)

gucci2= defaultdict()
for key in s_s:
	gucci2[key] = []
	#print mode[key][0]
	upper = mode[key][0] + st[key]
	lower = mode[key][0] - st[key]
	for val in ss_all_vals[key]:
		if (val <= upper):
			if (val >= lower):
				gucci2[key].append(val)

#3. Use new data to find new avg and store in dict
avg = defaultdict()
for key in gucci:
	avg[key] = []
	#print "\n",gucci[key]
	avg[key].append(np.average(gucci[key]))

avg2 = defaultdict()
for key in gucci2:
	avg2[key] = []
	#print "\n",gucci[key]
	avg2[key].append(np.average(gucci2[key]))

	'''for val in gucci[key]:
		gucci[key] += gucci[key][val]
		county +=1
	gucci[key]/= county
	county = 0'''

#output that information into a text file
outfile = open("median_avg.txt","w")
od = collections.OrderedDict(sorted(avg.items()))
for key in od:
	f = float(avg[key][0])
	outfile.write("\n" + str(key))
	outfile.write("\t" + str(f))
outfile.close()

outfile = open("mode_avg.txt","w")
od2 = collections.OrderedDict(sorted(avg2.items()))
for key in od2:
	f = float(avg2[key][0])
	outfile.write("\n" + str(key))
	outfile.write("\t" + str(f))
outfile.close()

outfile = open("median.txt","w")
for key in median:
	outfile.write("\n" + str(key))
	outfile.write("\t" + str(median[key]))
outfile.close()
