############################################################################
#																		   #
# Measurement Science Laboratory 2014 (Y1 Chemistry)					   #
# Python script to get a dark count from  an Adafruit ADC connected 	   #
# to a Rasp Pi GPIO    													   #
# Lab Co-ordinator: joshua.edel@imperial.ac.uk							   #
#																		   #
############################################################################

from Adafruit_ADS1x15 import ADS1x15
import numpy as np
import sys

filename = sys.argv[1]

############# Settings for the AdaFruit ADC Module #########################
#																		   #
# Fixed sps (8 16 32 64 128 250 475 860)								   #
# pga (6144 4096 2048 1024 0512 0256)								       #
# Do not edit the other options unless you know what you're doing          #
#															               #
############################################################################

sps = 250
datapoints = int(time1*sps) 
pga = 6144
ADS1115 = 0x01
ADS1015 = 0x00
period = 1.00/sps
adc = ADS1x15(ic=ADS1015)

######################## Log the data from the chip ########################
 
def logdata():
	data = []
	adc.startContinuousDifferentialConversion(0,1,pga,sps)
	startTime = time.time()
	t1 = startTime
	t2 = t1
	for x in range(0,datapoints):
		data.append(adc.getLastConversionResults())
		while(t2-t1 < period):
			t2 = time.time()
		t1 += period
	return(data)

############################ Collect dark count ############################

dataSamples = logdata()
darkcout = np.mean(dataSamples)
str_t = "%f" %(darkcount)
f = open(filename, 'w')
f.write(str_t)
f.close



