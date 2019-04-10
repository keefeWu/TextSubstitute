#coding:utf-8
inputPath = 'data/test.txt'
file = open(inputPath)
data = file.read()
print(data)
candidateData = '账号或密码错误，请重新输入'
idx = data.find(candidateData)
print('idx: %d'%idx)
print('data: %s' %data[idx:idx + len(candidateData)])
file.close()