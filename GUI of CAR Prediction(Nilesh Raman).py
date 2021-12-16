#----------------------------NILESH RAMAN ------------------------------------
#---------------------------DAV UNIVERSITY-------------------------------------
#-----------------------GUI OF CAR PREDICTION---------------------------------



#-------------------------Loading all Moduels---------------------------------

import pandas as pd
import numpy as np
from tkinter import *
from tkinter import ttk
from joblib import load
from tkinter import messagebox


win=Tk()
#------------------Creating Geometry,Title,Bg color---------------------------
win.geometry("1450x750")
win.title("WELCOME TO CAR SELLING PRICE PREDICTION!")
win.config(bg="black")


year=StringVar()
drivenkm=StringVar()
fue=StringVar()
fue.set("Petrol")
seller=StringVar()
seller.set("Individual")
trans=StringVar()
trans.set("Manual")
owner=StringVar()
owner.set("First Owner")
mileage=StringVar()
engine=StringVar()
power=StringVar()
seat=StringVar()
seat.set("5")


def func():
#------------Loading file /data------------------
    la=load("fuel.joblib")
    lb=load("seller_type.joblib")
    lt=load("transmission.joblib")
    lo=load("owner.joblib")
    sc=load("scaling.joblib")
    reg=load("regressor.joblib")
    
#--------------------------------Making Dictonary-----------------------------   
    try:
        dfn=pd.DataFrame({"Year":int(year.get()),"Driven_Kilometers":int(drivenkm.get()),
                         "Fuel_Type":[str(fue.get())],
                         "Seller_Type":[str(seller.get())],
                         "Transmission":[str(trans.get())],"Owners":[str(owner.get())],
                         "Mileage":[float(mileage.get())],"Engine":[int(engine.get())],
                         "Power":[float(power.get())],"Seat":[float(seat.get())]})        
        
        dfn["Fuel_Type"]=la.transform(dfn["Fuel_Type"])
        dfn["Seller_Type"]=lb.transform(dfn["Seller_Type"])
        dfn["Transmission"]=lt.transform(dfn["Transmission"])
        dfn["Owners"]=lo.transform(dfn["Owners"])
        dfn=sc.transform(dfn)
    
        output_var=("THE APPROXIMATED PRICE OF THIS CAR IS : ₹{} ".format(int(reg.predict(dfn))))
        output_screen_label.config(text=output_var,font=("Century",20),fg="White",bg="black")
        
    except:
        messagebox.showerror('Empty Fields','All Fields Are Mandatory !',icon = 'warning')
    
   
#-------------------------Creating Exit Button--------------------------------------  
def ExitApplication():
    
    box= messagebox.askquestion ('Exit Application','Are you sure you want to exit the application ?',icon = 'warning')
    if box== 'yes':
        
        win.destroy()       
exit_button = Button(win, text="EXIT",bd = '7',bg="white",font=("Arial",10),command=ExitApplication)
exit_button.place(x=1300,y=700)
    


#------------------------Creating Heading---------------------------------------
heading=Label(win,text="C A R    P R I C E    P R E D I C T I O N",fg="White",bg="black",font=("aesthetica",40)).place(x=350,y=40)



#----------------creating Entries and Lables for Data Input-------------------

l_year=Label(win,text="Model Year",font=("Disengaged",25),fg="White",bg="black").place(x=130,y=200)
e_year=Entry(win,textvariable=year,width=40,bg="white").place(x=420,y=205,height=23)


l_drivenkm=Label(win,text="Driven KMs",font=("Disengaged",25),fg="White",bg="black").place(x=130,y=305)
e_drivenkm=Entry(win,textvariable=drivenkm,width=40,bg="white").place(x=420,y=310,height=23)


l_fuel=Label(win,text="Fuel Type",font=("Disengaged",25),fg="White",bg="black").place(x=820,y=200)
com_fuel=ttk.Combobox(win,textvariable=fue,values=["Diesel","Petrol","CNG","LPG"]).place(x=1150,y=205,height=23)


l_seller=Label(win,text="Seller Type",font=("Disengaged",25),fg="White",bg="black").place(x=820,y=300)
com_seller=ttk.Combobox(win,textvariable=seller,values=["Individual","Dealer","Trustmark Dealer"]).place(x=1150,y=305,height="23")


l_trans=Label(win,text="Transmission type",font=("Disengaged",20),bg="black",fg="white").place(x=820,y=600)
com_trans=ttk.Combobox(win,textvariable=trans,values=["Manual" ,"Automatic"]).place(x=1150,y=605,height=23)


l_owner=Label(win,text="Owner",font=("Disengaged",25),fg="White",bg="black").place(x=820,y=400)
com_owner=ttk.Combobox(win,textvariable=owner,values=["First Owner","Second Owner" ,"Third Owner" ,"Fourth & Above Owner" ,"Test Drive Car"]).place(x=1150,y=400,height=23)


l_mileage=Label(win,text="Mileage",font=("Disengaged",20),fg="White",bg="black").place(x=130,y=605)
l_mileage=Label(win,text="(KmpL)(km/kg)",font=("arial",13),fg="White",bg="black").place(x=260,y=610)
e_mileage=Entry(win,textvariable=mileage,width=40,bg="white").place(x=420,y=610,height="23")


l_engine=Label(win,text="Engine (CC)",font=("Disengaged",25),fg="White",bg="black").place(x=130,y=405)
e_engine=Entry(win,textvariable=engine,width=40,bg="white").place(x=420,y=410,height=23)


l_power=Label(win,text="Max Power",font=("Disengaged",25),fg="White",bg="black").place(x=130,y=505)
l_power=Label(win,text="(BHP)",font=("Disengaged",13),fg="White",bg="black").place(x=220,y=550)
e_power=Entry(win,textvariable=power,width=40,bg="white").place(x=420,y=510,height=23)


l_seat=Label(win,text="Total Seats",font=("Disengaged",20),fg="White",bg="black").place(x=820,y=500)
com_seat=ttk.Combobox(win,textvariable=seat,values=["2","4","5","6","7","8",'9',"10","14"]).place(x=1150,y=505,height=23)

l_nilesh=Label(win,text="© NILESH RAMAN",font=("arial",10),fg="White",bg="black").place(x=25,y=720)





#---------------------------------Creating Submit Button-------------------------------------
submit=Button(win,text="SUBMIT", bd = '7',fg="black",bg="white",command=func)
submit.place(x=1228,y=700) 


output_screen_label=Label(win)
output_screen_label.place(x=300,y=690)  

win.mainloop()



