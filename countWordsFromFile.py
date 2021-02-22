def countWordsFromFile():
    fileName=input("Enter The File Name : ")
    fileNameOpen=open(fileName)
    fileData=fileNameOpen.read()
    splitFile=fileData.split()
    print(splitFile)
    count=0
    for i in splitFile:
        count=count+1
    print(count)
countWordsFromFile()
