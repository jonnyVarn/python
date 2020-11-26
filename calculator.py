
class calculator():
    
    def meaningless(summa):
        returner="not much"
        if int(summa)>=1 and int(summa) < 50:
            returner="Less then fifty"

        if int(summa)==50:
            returner="Fifty"

        if int(summa)>50 and int(summa)<100:
            returner="Almosta a hundred"

        if int(summa)==100:
            returner="Spot on!"

        if int(summa) > 100:
            returner="Missed the spot!"
        return returner

    def pluss(tal1, tal2):
        summa=int(tal1) + int(tal2)
        calculator.meaningless(summa)
        return summa
    
    def minus(tal1, tal2):
        summa=int(tal1)-int(tal2)
        return summa

    def times(tal1, tal2):
        summa=int(tal1)*int(tal2)
        return summa

    def division(tal1, tal2):
        summa=int(tal1)/int(tal2)
        return summa

def main_menu():
    print("-----------------------------------------------")
    print("            The super calculator               ")
    print("         options are */+- or q for quit        ")
    print("-----------------------------------------------")

    
    

#print(pluss(1, 1))
#print(minus(1,1))
#print(times(1,1))
#print(division(1,1))
#add a comment 
running="run"
main_menu()
cal=calculator
while running !="q":
      
    running=input()

    if running=="+":
        tal1=input("first number")
        tal2=input("second number")
        print("-----------------------------------------------")
        print(tal1 + " + " + tal2)
        print("===============================================")
        print(cal.pluss(tal1, tal2))
        print(cal.meaningless(int(tal1) + int(tal2)))
        
     
    if running=="-":
        tal1=input("first number")
        tal2=input("second number")
        print("-----------------------------------------------")
        print(tal1 + "-" + tal2)
        print("===============================================")
        print(cal.minus(tal1, tal2))
        print(cal.meaningless(int(tal1) - int(tal2)))

    if running=="/":
        tal1=input("first number")
        tal2=input("second number")
        print("-----------------------------------------------")
        print(tal1 + "/" + tal2)
        print("===============================================")
        print(cal.division(int(tal1), int(tal2)))
        print(cal.meaningless(int(tal1) / int(tal2)))

    if running=="*":
        tal1=input("first number")
        tal2=input("second number")
        print("-----------------------------------------------")
        print(cal.times(int(tal1), int(tal2)))
        print(cal.meaningless(int(tal1) * int(tal2)))

    
    if running != "q" or running != "+" or running != "-" or running != "*" or running != "/":
       main_menu()
      