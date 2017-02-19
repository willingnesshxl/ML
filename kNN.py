# -*- coding: utf-8 -*-
from numpy import *
import operator

def createDataSet():
	group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group,labels


def classify0(inX, dataSet, labels, k):
	dataSetsize = dataSet.shape[0]
	diffMat = tile(inX, (dataSetsize,1))-dataSet #
	sqDiffMat = diffMat **2
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances**0.5
	sortedDistIndicies = distances.argsort() 
	# argsort()返回原数组按照索引值排列后由小到大的索引值 
	# 如 x = np.array([3, 1, 2]) np.argsort(x) array([1, 2, 0]) 即最小的在x[1]，中间的在x[2]，最大的在x[0]
	# sortedDistIndicies 返回到当前点距离从小到大的点的索引
	classCount = {}
	for i in range(3):
		voteIlabel = labels[sortedDistIndicies[i]]
		# print voteIlabel
		classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
		# print classCount[voteIlabel]
	sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
	return sortedClassCount[0][0]

def file2atrix(filename):
	fr = open(filename)
	arrayOLines = fr.readlines()
	numberOfLines = len(arrayOLines)
	returnMat = zeros((numberOfLines,3))
	classLabelVector = []
	index = 0
	for line in arrayOLines:
		line = line.strip()
		listFromLine = line.split('\t')
		returnMat[index,:] = listFromLine[0:3]
		classLabelVector.append(int(listFromLine[-1]))
		index += 1
	return returnMat,classLabelVector


def autoNorm(dataSet):
	minVals = dataSet.min(0)
	maxVals = dataSet.max(0)
	ranges  maxVals - minVals
	normDataSet = zeros(shape(dataSet))
	m = dataSet.shape[0]
	normDataSet = dataSet - tile(minVals,(m,1))
	normDataSet = normDataSet/tile(ranges,(m,1))
	return normDataSet,ranges,minValsßßß





group,labels = createDataSet()
res = classify0([0,0],group,labels,3)
print res