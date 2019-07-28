class OlympicMedal():
    def __init__(self,name='',golden=0,silver=0,bronze=0):
        self.name=name
        self.golden=golden
        self.silver=silver
        self.bronze=bronze
        self.medal=['',0,0,0]
        self.sum=[self.name,self.golden+self.silver+self.bronze]
    def UpdateMedal(self):
        self.medal[0]=self.name
        self.medal[1]=self.golden
        self.medal[2]=self.silver
        self.medal[3]=self.bronze
        self.sum[1]=self.golden+self.silver+self.bronze
    def addMedal(self,medal,num):
        if medal=='golden':
            self.golden+=num
        elif medal=='silver':
            self.silver+=num
        else:
            self.bronze+=num
        self.UpdateMedal()
    def ShowMedal(self):
        self.UpdateMedal()
        print('golden is %d \n'%self.golden)
        print('silver is %d \n'%self.silver)
        print('bronze is %d \n'%self.bronze)
    def MedalSum(self):
        self.UpdateMedal()
        print('The sum of %s\'s medal is %d'%(self.sum[0],self.sum[1]))

china=OlympicMedal('china',10,10,10)
china.ShowMedal()
china.addMedal('golden',1)
china.ShowMedal()
china.MedalSum()
russia=OlympicMedal('russia',6,6,6)
russia.ShowMedal()
russia.addMedal('silver',2)
russia.ShowMedal()
russia.MedalSum()
usa=OlympicMedal('usa',5,5,5)
usa.ShowMedal()
usa.MedalSum()
french=OlympicMedal('french',6,4,3)
french.ShowMedal()
french.MedalSum()
sumList=sorted([china.sum,russia.sum,usa.sum,french.sum],key=lambda a: a[1],reverse=True)
goldenList=sorted([china.medal,russia.medal,usa.medal,french.medal],key=lambda a: a[1],reverse=True)
print(sumList)
print(goldenList)