#!/usr/bin/python
# {}.py - A program to calculate Mahalanobis distance
# More on the pandas library: https://pandas.pydata.org
# More on the NumPy package: https://www.numpy.org/

import sys
import math
import os
import numpy as np
import pandas as pd
from scipy import linalg
from scipy.stats.distributions import chi2

def isNumber(num):
	try:
		float(num)
		return True
	except ValueError:
		return False 	


def mahalanobis(x, data, covariance):
	
	# Calculate mean value of dataset
	mu = np.mean(data)
	
	x_minus_mu = x - mu
		
	# Calculate covariance and information matrix
	if not covariance:
		covariance = np.cov(data.values.T)
	information = linalg.inv(covariance)
	
	# Mahalanobis distance
	md = np.dot( np.dot(x_minus_mu, information), x_minus_mu.T)
	
	return md.diagonal()
	
def main():
	bound = ''.ljust(40, '*')
	start = ' [ STARTED ] '.center(40, '*')
	end = ' [ FINISHED ] '.center(40, '*')
	print(bound + '\n' + start + '\n' + bound)
	
	fileName = 'lesson7_mahal_diamonds.csv'
	
	if fileName == 'lesson7_mahal_dataset_0.csv':
		# Read data
		# Taken from https://jamesmccaffrey.wordpress.com/2017/11/09/example-of-calculating-the-mahalanobis-distance/
		# We assumed that the three variables are independent
		data = pd.read_csv(fileName)
		data.head()
		test = pd.DataFrame([[66, 640, 44], [69, 595, 38]], columns=list(['height','score','age']))
	elif fileName == 'lesson7_mahal_diamonds.csv':
		# Read data
		# Taken from https://www.machinelearningplus.com/statistics/mahalanobis-distance/
		data = pd.read_csv(fileName).iloc[:, [0,4,6]]
		data.head()	
		test = data[['carat', 'depth', 'price']].head(5)
	else:
		sys.exit('[ERROR]: File not found!')
		
	# Mahalanobis distance
	test['mahalanobis'] = mahalanobis(test, data, None)	
	test.head()
	
	# Probability (1-p) with which we are certain that, when the 
	# squared Mahalanobis distance is greater than the critical 
	# value (cv) associated with this probability and the proper DOF,
	# then the test vector (tv) is an outlier 
	p = 0.001
	dof = 3
	cv = chi2.ppf(1-p, dof)
	
	outlier = []
	critical_value = []
	for i in range(len(test['mahalanobis'])):
		critical_value.append(cv)
		if test['mahalanobis'][i] > cv:
			outlier.append('true')
		else:
			outlier.append('false')
	
	test['critical-value'] = np.asarray(critical_value)
	test['p_value'] = 1 - chi2.cdf(test['mahalanobis'], dof)
	test['outlier'] = np.asarray(outlier)
	print(test)
	
	print(bound + '\n' + end + '\n' + bound)
		
	return 0
	
if __name__ == '__main__':
	sys.exit(main())