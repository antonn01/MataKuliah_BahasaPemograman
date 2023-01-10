# Parent class
class Hewan:  
    def bicara(self):  
        print("Hewan berbicara")  
         
# Child class mewarisi dari class Hewan
class Kucing(Hewan):
    def meaow(self):  
        print("meaow....meaow....meaow..!!!") 
 
k = Kucing()
k.meaow()
k.bicara()
 
