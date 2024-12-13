pens_id = []
pens_name=[]
pens_age=[]
pens_type=[]

def add_pensioner(pensioner_id, name, age, pension_type):
        if pensioner_id in pens_id:
                print("pensioner already exist")
        else:
                if age>40:
                        pens_id.append(pensioner_id)
                        pens_name.append(name)
                        pens_age.append(age)
                        pens_type.append(pension_type)
                        print("pensioner added succesfully")
                else:
                        print("no age")
        
PENSION_RATES = {'c': 10000,'d': 5000,'n': 2000}

def calculate_pension(pensioner_id, pension_type):
    if(pensioner_id)in pens_id:
        if (pension_type)in PENSION_RATES:
            pension_amount = PENSION_RATES[pension_type]
            print(pension_amount)
        else:
            print("Invalid pension type")
    else:
        print("Pensioner not found")

def display_pension_details(pensioner_id):
       if pensioner_id in pens_id:
               print("pensioner_id\tpensioner_name\tpensioner_age\tpension_type")
               pos=pens_id.index(pensioner_id)
               print(" %d\t\t\t%s\t\t%d\t\t%s"%(pens_id[pos],pens_name[pos],pens_age[pos],pens_type[pos]))
       else:
           print("invalid id")

def all_pensioner_details():
    
    if len(pens_id)==0:
        print("list is empty")
    else:
        print("pensioner_id\tpensioner_name\tpensioner_age\tpension_type")
        for i in range(len(pens_id)):
            print(" %d\t\t\t%s\t\t%d\t\t%s"%(pens_id[i],pens_name[i],pens_age[i],pens_type[i]))
            
while True:
    print("1.add pensioner 2.calculate pension 3.pensioner details 4.display all 5.exit")
    ch=int(input("enter ur choice: "))
    if ch==1:
        pensioner_id=int(input("enter pensioner id: "))
        name=input("enter pensioner name: ")
        age=int(input("enter pensioner age: "))
        pension_type=input("enter typr: ")
        add_pensioner(pensioner_id, name, age, pension_type)
    elif ch==2:
        pensioner_id=int(input("enter pensioner id: "))
        pension_type=input("enter typr: ")
        calculate_pension(pensioner_id, pension_type)
    elif ch==3:
        pensioner_id=int(input("enter pensioner id: "))
        display_pension_details(pensioner_id)
    elif ch==4:
        all_pensioner_details()
    elif ch==5:
        break