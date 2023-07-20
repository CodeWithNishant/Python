import pandas as pd
import sqlalchemy as sa

dbcon = sa.create_engine("mysql+mysqlconnector://root:nagar@localhost/important")

def input_data():

    date_l = []
    prog_lang_l = []
    time_l = []
    des_l = []

    date_input = input("Enter the date : ")
    language_input = input("Enter programming language(s) : ")
    time_input = float(input("Enter the time spent : "))
    desc_input = input("Enter a breif description : ")

    language_input = language_input.lower()
    desc_input = desc_input.lower()
    
    date_elig = False
    program_lang_elig = False
    time_elig = False    

#________________________________DATE ELIGIBILITY CHECK________________________________________________________

    l_date_elig = ['0','1','2','3','4','5','6','7','8','9','-']
    for i in range(len(date_input)):
        if date_input[i] in l_date_elig:
            continue
        else:
            break
    if i == len(date_input)-1:
        date_elig = True

# ______________________________PROGRAMMING LANGUAGE ELIGIBILTY CHECK_____________________________________________

    languages = ['nan','python','c++','java','javascript','ruby','kotlin','mysql','html','css','swift','c','c#']
    length_language_input = len(language_input.split())
    print(length_language_input)
    if length_language_input == 1:
        for i in range(len(language_input.split())):
            if language_input in languages:
                program_lang_elig = True
                continue
            else:
                break
    else:
        for i in range(len(language_input.split())):
            if language_input.split()[i] in languages:
                print(language_input.split()[i])
                continue
            else:
                i-=1
                break
        if i == len(language_input.split())-1:
            program_lang_elig = True

#_______________________________TIME SPENT ELIGIBILITY CHECK________________________________________________________

    if time_input>=3.0:
        print("The time looks suspicious !!")
        confirm = input("enter CONFIRM to confirm it : ")
        confirm = confirm.lower()
        if confirm == "confirm":
            time_elig = True
    else:
        time_elig=True

#_______________________________FINAL RESULT AFTER ELIGIBILITY CHECK_________________________________________________

    if date_elig == True and program_lang_elig == True and time_elig == True:
        print("\n\tThe inputs are eligible \n\t Now test it yourself to add it into database : ")
        print(date_input,language_input,time_input,desc_input)
        confirm_inputs = input("\n\twrite yes to enter or no to cancel : ")
        if confirm_inputs == 'yes' or confirm_inputs == 'y':
            date_l.append(date_input),prog_lang_l.append(language_input),time_l.append(time_input),des_l.append(desc_input)
            df1 = pd.DataFrame({"Date":date_l,"Language":prog_lang_l,"Time_spent":time_l,"Description":des_l})
            df1.to_sql("progress_report",dbcon,if_exists="append",index=False)
            print("\n\t\t\tSubmission Done")
        else:
            print("Inputs are discarded")
    else:
        print('Eligibility not accepted !')
        print("Date :",date_elig,"\nLanguage :",program_lang_elig,"\nTime :",time_elig)

def get_data():
    print("Here is the data for you : ")
    #df = pd.DataFrame({"Date":date_l,"Programming Language":prog_lang_l,"Time":time_l,"Description":des_l})
    show = pd.read_sql("select* from progress_report",dbcon)
    print(show)

def manual_code():
    print('\n\t\t\tIMPORTANT THINGS TO REMEMBER ! \nTHE TABLE NAME IS progress_report\nCOLUMNS :date\tlanguage\ttime_spent\tdescription\n')
    user_input = input("Enter the code : ")
    print("\nHere is the result")
    show = pd.read_sql(user_input,dbcon)
    print(show)

times_done=0
while True:
    print("\n\t1 to enter data\n\t2 to view it\n\t3 to exit\n\t4 to write manual sql code")
    start = input("\n\t\tEnter the command : ")
    if start == "1" or start == "enter data":
        input_data()
        times_done+=1
        while True:
            more = input("Want to enter more data (y or n) : ")
            if more == "y" or more == "1" or more == "enter data":
                input_data()
                times_done+=1
            else:
                break
    elif start == "2" or start == "view":
        get_data()
    elif start == "3" or start == "n":
        print("you have entered",times_done," rows")
        break
    elif start=="4" or start == "sql code":
        manual_code()
    else:
        print("Input is not defined")
        continue