#coding:utf-8
import json
def generateOutputData(keyName):
	return "{{ $t('%s') }}"%keyName
inputPath = 'data/test.txt'
outputPath = 'data/out.txt'
jsonPath = 'data/cn.json'
inputFile = open(inputPath,encoding = 'utf-8')
outputFile = open(outputPath, 'w', encoding = 'utf-8')
jsonFile = open(jsonPath)
jsonData = jsonFile.read()
keyMap = json.loads(jsonData)
data = inputFile.read()
for keyName in keyMap:
	candidateData = keyMap[keyName]
	print('candidate: %s key: %s'%(candidateData, keyName))
		
	# find the idx
	idx = data.find(candidateData)
	print('idx: %d'%idx)
	if idx == -1:
		continue
	print('data: %s' %data[idx:idx + len(candidateData)])

	# substitute
	data = data[:idx]+ generateOutputData(keyName) + data[idx + len(candidateData):]
print('output:%s'%data)
outputFile.write(data)
inputFile.close()
outputFile.close()