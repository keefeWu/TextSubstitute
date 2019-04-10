#coding:utf-8
def generateOutputData(keyName):
	return "{{ $t('%s') }}"%keyName
inputPath = 'data/test.txt'
file = open(inputPath)
data = file.read()
print(data)
candidateData = '账号或密码错误，请重新输入'
keyName = 'account_password_error_please_input_again'
mould = "{{ $t('the_account_cannot_be_null') }}"
# find the idx
idx = data.find(candidateData)
print('idx: %d'%idx)
print('data: %s' %data[idx:idx + len(candidateData)])
# substitute
outputData = data[:idx]+ generateOutputData(keyName) + data[idx + len(candidateData):]
print('output:%s'%outputData)

file.close()