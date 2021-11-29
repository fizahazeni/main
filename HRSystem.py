#Python code created in 2021 for Programming module to create a HR System

from datetime import datetime
import pandas as pd
accounts=pd.read_csv("HR System.csv")

#list
raceopt=["Chinese","Malay","Indian","Eurasian","Others"]
maritalopt=["Single","Married","Widowed","Divorced"]
deptopt=["HR","Finance","Information Technology","Compliance"]
roleopt=["Team Manager","Staff"]
citizenopt=["Singaporean","Permanent Resident","Foreigner"]
region_options=["North","Central","East","West","North-East"]
area_options=[["Lim Chu Kang","Sembawang","Woodlands","Yishun","Kranji"],
              ["Downtown","Outram","Sentosa","Orchard","Newton","Bukit Timah","Novena","Thomson","Bishan","Bukit Merah","Marine Parade","Toa Payoh"],
              ["Bedok", "Changi","Paya Lebar","Pasir Ris","Tampines"],
              ["Bukit Batok", "Bukit Panjang","Boon Lay","Choa Chu Kang","Clementi","Jurong West","Jurong East","Tuas","Pasir Laba","West Coast"],
              ["Ang Mo Kio","Hougang","Punggol","Seletar","Sengkang","Serangoon"]]
team_managers =[["Shanon Lee", "Adeline Yeo" ,"Tasha Goh"],["Daniel Chew","Paul Hwee"],["Jonathan Lee" ,"Cherie Goh"],["Rachel Quek","Bob Low"]]
start_options=["Create Account","Login"]
hroptions=["Update New Information","Edit Existing Information","Reset Password","Removal of Account","Leave Approval","Handling My Leave","Bonus System","Exit System"]
empoptions=["View your Info","Handling My Leave","Exit System"]
manoptions=["View your Info","View your Team Structure","Handling My Leave","Rewards System","Exit System"]
status=["Full Time","Part Time","Contract"]
grades=["A","B","C","D","E","F"]
bonus_spread=[0.15,0.10,0.075,0.05,0.25,0]
check=["Yes","No"]



#FUNCTIONS
#Employer ID
def generate_id():
    global accounts
    accounts.loc[accounts.username == user_input,"Emp_ID"] = accounts.shape[0] + 1

#username& password creation
def acc_creation():
    while True:
        global accounts
        accepted = False
        global user_input
        user_input = input("Enter a username with at least 8 characters.")
        if " " in user_input:
            print("No spaces allowed.")
            continue
        elif len(user_input) >= 8:
            for id, row in accounts.iterrows():
                if row["username"] == user_input:
                        accepted = True
        else:
            print("Length not 8 characters")
            continue
            
        if accepted:
            print("Username exist")
            continue 
        else:
            break
        

    while True:
        accepted = False
        password_input = input("Enter a password with at least 8 characters and at least 1 special character.")
        if " " in user_input:
            print("No spaces allowed.")
            continue
        elif len(password_input) >= 8:
            for char in password_input:
                if char in "~!@#$%^&*()_+`-=[]\{}|;':,./<>?":
                    accounts=accounts.append({"username":user_input, "password":password_input}, ignore_index=True)
                    accepted = True
                    break 
        else:
            print("Password not 8 characters")
            continue
    
        if accepted:
            return accounts
        
        else:
            print("Password require special character")
            continue
            
#generate questions 
def qnfunc(topic,options,start,end):
    while True:
        print("Please enter " + topic)
        try:
            for i in options:
                print("[" + str(options.index(i)+1) + "]" + str(i))
            global qn
            qn=int(input("Please enter numbers included only."))
        except ValueError:
            continue
        if qn in range(start,end):
            global x
            x= options[qn-1]
            break
        else:
            continue

#question           
def question(topic):
    while True:
        print("Please enter " + topic)
        try:
            global qn
            qn=input("Please enter accordingly.")
            break
        except ValueError:
            continue
            
#question of integer values       
def intquestion(topic):
    while True:
        print("Please enter " + topic)
        try:
            global qn
            qn=int(input("Please enter accordingly."))
            break
        except ValueError:
            continue
            
#acc login
def acc_login():
    while True:
        global user_login
        accepted = False   
        user_login = input("What is your username:")
        password_login = input("Enter password:")
        for id, row in accounts.iterrows():
            if row["username"] == user_login and row["password"] == password_login:
                print("Login Successful")
                accepted = True

        if accepted:
            break
        else: 
            print("Wrong username or password")
            continue

#leave management 
def leaveapp():
    while True:
        global accounts
        leave_number = 14
        try:
            start = datetime.strptime(input("Starting date of leave: (ddmmyyyy)"), "%d%m%Y")
            end = datetime.strptime(input("Ending date of leave: (ddmmyyyy)"), "%d%m%Y")
        except ValueError:
            print("Please enter in ddmmyyy format")
            continue
    
        daydiff = end.weekday() - start.weekday()
        weekdays = ((end-start).days - daydiff) / 7 * 5 + min(daydiff,5) - (max(end.weekday() - 4, 0) % 5)
        
        print("You have applied for ", weekdays, " days of leave")
        if weekdays > leave_number:
            print("Insufficient leave.\nYou have only ", leave_number ," days of leave left")
            continue
        elif start <= datetime.today() or weekdays<=0:
            print("Incorrect dates entered. Please check the dates entered. Weekends or dates past today are not accepted.")
            continue
        
        else:
            print("Application successful.\nYou have ", leave_number - weekdays," days of leave left") 
       
        accounts.loc[accounts[accounts["username"] == user_login].index[0], "No of Leaves"] = leave_number - weekdays
        accounts.loc[accounts[accounts["username"] == user_login].index[0], "Leave Dates"] = str(start.date())+" to "+ str(end.date())
        accounts.loc[accounts[accounts["username"] == user_login].index[0], "Leave Status"] = "Pending"
        accounts
        break

#find value according to the username       
def find_user(user_input,column_name,value):
    accounts.loc[accounts[accounts.username== user_input].index[0],column_name] = value
    
def performance():    
    team= team_data["Name"]
    for member in team:
        print("Name: ", member)
        while True:  
            grading=input("Enter Grade from A to F ")
            if grading.upper() in grades:
                accounts.loc[accounts[accounts["Name"] == member].index[0],"Performance"] = grading.upper()
                break
            else:
                print("Please enter letters from A-F only")
                print("Name: ", member)
                
#retrieve username
def userqn(qn):
    while True:
            accepted = False
            global usrname
            usrname= input(qn)
            for i in accounts.username:
                if i in usrname:
                    accepted=True
                    break
            if accepted:
                break


#HR
def hr_function():
    while True:
        qnfunc("what you would like to do.",hroptions,1,len(hroptions)+1)

        if qn==1:
            userqn("Please enter the username of the employee.")
            qnfunc("status of the employee.",status,1,len(status)+1)
            find_user(usrname,"Status",x)
            intquestion("salary of the employee.")
            find_user(usrname,"Salary",qn)
            print("New information has been added successfully.")
            continue

        elif qn==2:
            userqn("Please enter the username of the employee.")
            qnfunc("which column value you would like to edit.",list(accounts.columns),1,len(accounts.columns)+1)
            question("the new value.")
            find_user(usrname,x,qn)
            print("Changes have been performed successfully.")
            continue

        elif qn==3:
            userqn("Please enter the username of the employee.")
            question("new password.")
            find_user(usrname,"password",qn)
            continue

        elif qn==4:
            userqn("Please enter the username of the employee.")
            indexNames = accounts[ accounts["username"] == usrname ].index
            qnfunc("whether you are sure to delete the account?",check,1,len(check)+1)
            if qn==1:
                accounts.drop(indexNames , inplace=True)
                print("Account with the username "" + usrname + "" has been removed successfully.")
                continue
            elif qn==2:
                continue

        elif qn==5:
            for id, row in accounts.iterrows():
                if row["Leave Status"] == "Pending":
                    pending = accounts[accounts["Leave Status"] == "Pending"]
                    for id, row in pending.iterrows():
                        print("Name: " + str(row["Name"]) + " No. of Leaves: " + str(row["No of Leaves"]) +"Leave Dates: " + str(row["Leave Dates"]))
                        hr_approval = int(input("Select the following action \n[1]Approve \n[2]Reject"))
                        if hr_approval==1:
                            accounts.loc[accounts[accounts["Name"] == row["Name"]].index[0], "Leave Status"] = "Approved"
                            pending.drop(pending.index, inplace=True)
                            continue
                        elif hr_approval==2:
                            accounts.loc[accounts[accounts["Name"] == row["Name"]].index[0], "Leave Status"] = "Not Approved"
                            pending.drop(pending.index, inplace=True)
                            continue
            else:
                print("No leave request to be approved.")
                continue
            
                          
        elif qn==6:
            leaveapp()
            continue
            
        elif qn==7:            
            for id, row in accounts.iterrows():
                for i in range(0,len(grades)-1):
                    if accounts.loc[id,"Performance"]==grades[i]:
                        accounts.loc[id,"Bonus"] = accounts.loc[id,"Salary"] * bonus_spread[i]
                        continue
            print(accounts[["Emp_ID","username","Bonus"]])
            print("Bonus has been successfully calculated.") 
            
        elif qn==8:
            print("Thank you! Goodbye~")
            accounts.to_csv("HR System.csv", index=False)
            break
        
        
#Employee
def emp_function():
    while True:
        qnfunc("what you would like to do.",empoptions,1,len(empoptions)+1)
        
        if qn==1:
            own_data= accounts[accounts["username"] == user_login]
            print(own_data)
            continue
        elif qn==2:
            leaveapp()
            continue
        if qn==3:
            print("Thank you! Goodbye~")
            accounts.to_csv("HR System.csv", index=False)
            break
        
        
#Team Manager
def man_function():
    while True:
        qnfunc("what you would like to do.",manoptions,1,len(manoptions)+1)
        if qn==1:
            own_data= accounts[accounts["username"] == user_login]
            print(own_data)
            continue

        elif qn==2:
            global team_data
            team_data=accounts[accounts["Team Manager"] == accounts.loc[accounts[accounts.username== user_login].index[0],"Name"]]
            print(team_data.filter(items=["Name","Race","Department","Citizenship","Managerial Role","Team Manager","No of Leaves","Leave Dates","Leave Status"]))
            continue
        elif qn==3:
            leaveapp()
            continue
        elif qn==4:
            performance()
            continue
        elif qn==5:
            print("Thank you! Goodbye~")
            accounts.to_csv("HR System.csv", index=False)
            break
        
        
#Main function of System
def main():        
    while True:
        print("Welcome to our HR System!")
        qnfunc("whether you are creating an account or logging in.",start_options,1,len(start_options)+1)
    
        if qn==1:
            acc_creation()
            generate_id()
            employee_name = input("Enter your full name.")
            find_user(user_input,"Name",employee_name)
    
            #Race
            qnfunc("your race.",raceopt,1,len(raceopt)+1)
            find_user(user_input,"Race",x)
    
            #Marital Status
            qnfunc("your Marital Status.",maritalopt,1,len(maritalopt)+1)
            find_user(user_input,"Marital Status",x)
    
            #Department
            qnfunc("the department you would like to join.",deptopt,1,len(deptopt)+1)
            find_user(user_input,"Department",x)
    
            #Citizenship
            qnfunc("Citizenship Status.",citizenopt,1,len(citizenopt)+1)
            find_user(user_input,"Citizenship",x)
    
            #Region
            qnfunc("number corresponding to region.",region_options,1,len(region_options)+1)
            find_user(user_input,"Region",x)
    
            #Area
            qnfunc("number corresponding to area.",area_options[qn-1],1,len(area_options[qn-1])+1)
            find_user(user_input,"Area",x)
    
            #Role
            qnfunc("your managerial role.",roleopt,1,len(roleopt)+1)
            find_user(user_input,"Managerial Role",x)
    
            #Team Manager
            if x=="Staff":
                qnfunc("your Team Manager's name.",team_managers[qn-1],1,len(team_managers[qn-1])+1)
                find_user(user_input,"Team Manager",x)
            elif x=="Team Manager":
                find_user(user_input,"Team Manager","Pending Team Managers")
    
            print("You have successfully created an account. You can now login.")
            accounts.to_csv("HR System.csv", index=False)
            continue
    
    
        elif qn==2:
            acc_login()
            if accounts.loc[accounts[accounts.username == user_login].index[0], "Department"]=="HR":
                hr_function()
            elif accounts.loc[accounts[accounts.username== user_login].index[0], "Managerial Role"]=="Team Manager":
                man_function()
            else:
                emp_function()
            break
        
        
if __name__ == "__main__":
    main()
