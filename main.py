#coding:utf-8
import json
import os
def generateOutputData(data, idx, keyName):
	preData = data[:idx]
	nextData = data[idx + len(candidateData):]
	preDataSeg = preData.split()
	nextDataSeg = nextData.split()

	#if in comment
	leftCommentIdx = preData.rfind('/*') 
	rightCommentIdx = preData.rfind('*/')
	if leftCommentIdx > rightCommentIdx:
		return data 

	if preDataSeg[-1][-1] == "'" and nextDataSeg[0][0] == "'":
		substituteStr =  "this.$t('%s')"%keyName
		preIdx = preData.rfind("'")
		nextIdx = nextData.find("'")
		preData = data[:preIdx]
		nextData = nextData[nextIdx+1:]
		data = preData + substituteStr + nextData 
	elif preDataSeg[-1][-1] == "\"" and nextDataSeg[0][0] == "\"":
		preIdxLabel = preData.rfind('label')
		preIdxPlaceholder = preData.rfind('placeholder')
		preIdx = max(preIdxLabel, preIdxPlaceholder)
		substituteStr =  "$t('%s')"%keyName
		preData = preData[:preIdx] + ":" + preData[preIdx:idx]
		data = preData + substituteStr + nextData 
	else:
		substituteStr =  "{{ $t('%s') }}"%keyName
		data = preData + substituteStr + nextData 
	return data


def loadFiles(path):
	files = os.listdir(path)
	return files

def createFolder(folder_name):
	if not os.path.exists(folder_name):
		os.mkdir(folder_name)

def get_key (dict, value):
	return [k for k, v in dict.items() if v == value]

def getSortedMapKey(keyMap):
	valueList = []
	for keyName in keyMap:
		valueList.append(keyMap[keyName])
	valueList.sort(key=lambda x:len(x))
	sortedKeyList = []
	valueList.reverse()
	print(valueList)
	for value in valueList:
		sortedKeyList.append(get_key(keyMap, value))
	return sortedKeyList

inputFolder = 'data/'
outputFolder = 'output/'
createFolder(outputFolder)
jsonPath = 'json/cn.json'
jsonFile = open(jsonPath,encoding = 'utf-8')
jsonData = jsonFile.read()
keyMap = json.loads(jsonData)
sortedKeyList = getSortedMapKey(keyMap)

inputFiles = loadFiles(inputFolder)
for FileName in inputFiles:
	inputPath = os.path.join(inputFolder, FileName)
	inputFile = open(inputPath,encoding = 'utf-8')

	outputPath = os.path.join(outputFolder, FileName)
	outputFile = open(outputPath, 'w', encoding = 'utf-8')

	data = inputFile.read()

	for keyNameList in sortedKeyList:
		keyName = keyNameList[0]
		candidateData = keyMap[keyName]
		print('candidate: %s key: %s'%(candidateData, keyName))
			
		# find the idx
		start = 0
		idx = 0
		while(idx != -1):
			idx = data.find(candidateData, start)
			print('idx: %d'%idx)
			if idx == -1:
				continue
			start = idx + 1
			print('data: %s' %data[idx:idx + len(candidateData)])

			# substitute
			data = generateOutputData(data, idx, keyName)
	print('output:%s'%data)
	outputFile.write(data)
	inputFile.close()
	outputFile.close()