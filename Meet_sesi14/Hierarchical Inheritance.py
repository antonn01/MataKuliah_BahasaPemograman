# Class utama 
class Parent: 
      def fungsi1(self): 
            print("Fungsi pada parent class.") 
   
# class 1 turunan 
class Child1(Parent): 
      def fungsi2(self): 
            print("Fungsi pada child 1.") 
   
# class 2 turunan
class Child2(Parent): 
      def fungsi3(self): 
            print("Fungsi pada child 2.") 
 
object1 = Child1() 
object2 = Child2() 
 
object1.fungsi1() 
object1.fungsi2()  
 
object2.fungsi1() 
object2.fungsi3()