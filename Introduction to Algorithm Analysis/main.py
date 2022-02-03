class NewType(object):
    def __init__(self,dataInput1,dataInput2,dataInput3):
        self.data1 = dataInput1
        self.data2 = dataInput2
        self.data3 = dataInput3
    def printData(self):
        print("["+str(self.data1)+","+str(self.data2)+","+str(self.data3)+"]")


obj = NewType(5,7,1)
obj.printData()