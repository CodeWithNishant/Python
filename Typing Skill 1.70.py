import time
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

difficulty_lvl = []
wpm_l = []

def main():
    incorrect_alphabets =  []
    print("""                               Typing Master version-1.70""")

    correct_l = []
    incorrect_l = []

    text1 = "A computer is an electronic machine that runs on electricity and it understands only binary language that is the language \n of zeros and ones"
    text2 = "The programming language is a tool to talk with the computer and to say it to do a specific task, there are many \n programming languages available but python  is the most popular nowadays"
    text3 = "The minimum energy needed by an electron to come out from a metal surface is called the work function of the metal. \n Energy required for electron emission from the metal surface can be supplied by suitable heating."
    text4 = "The existance of discrete energy levels in an atom was directly verified in 1914 by James Frank and Gustav Hertz. \n They studied the spectrum of mercury vapour when electrons having different kinetic energies passed through the vapours."
    text5 = "We would first define the wavefront: when we drop a small stone on a calm pool of water, waves spread out of the \n point of impact. Every point on the surface starts oscillating with time."
    text6 = "Einstein showed from his theory of special relativity that it is necessary to treat mass as another form of energy. \n Before the advent of this theory of special relativity it was presumed that mass and erergy were conserved separatively in a reaction."  
    text7 = "The atomic mass of O found from mass spectroscopy experiments is seen to be 15.99493u. Substracting the mass of 8 \n electrons(8x0.00055u) from this, we get the experiment mass of O nucleus to be 15.99053u"
    text8 = "Consider a thin p-type silicon (p-Si) semiconductor wafer. By adding precisely a small quantity of pentavalent impurity, \n part of the p-Si wafer can be converted into n-Si. There are several processes by which a semiconductor can be formed."
    text9 = "Iitially, diffusion current is large and drift current is small. As the diffusion process continues, the space-charge \n regions on either side of the junction extend, thus increasing the elctric field strength and hence drift current."

    texts_easy = [text1,text2,text3]
    texts_medium = [text4,text5,text6]
    texts_hard = [text7,text8,text9]
    texts = {"Easy":texts_easy,"Medium":texts_medium,"Hard":texts_hard}

    text_lvl = input("\nSelect Difficulty Level (easy/medium/hard) :")

    if text_lvl == "easy" or text_lvl == "e":
        text_range = texts["Easy"]
    elif text_lvl == "medium" or text_lvl == "m":
        text_range = texts["Medium"]
    elif text_lvl == "hard" or text_lvl == "h":
        text_range = texts["Hard"]
    else:
        text_range = texts["Easy"]
        print("\nThe Option That You Have Chosen Is Invalid ; Easy Text Will Be Chosen By Default")
        text_lvl = "easy"

    text_chosen = random.choice(text_range)

    def wpm(w,tt,tl):
        if w==0:
            print("\nYou have not typed anything !!")
        else:
            wpm = np.round(w/tt*60)
            edited_wpm = np.round(wpm*(1-(error/w)))
            print("Words per minute :",wpm)
            print("\nYou have done :",error,"errors \n Error percentage :",np.round((error/w)*100),"%","\n Edited typing speed is :",edited_wpm)
            if edited_wpm <20:
                print(edited_wpm," is a BELOW AVERAGE typing speed")
            elif edited_wpm>=20 and edited_wpm <30:
                print(edited_wpm," is an AVERAGE typing speed")
            elif edited_wpm>=30 and edited_wpm <40:
                print(edited_wpm," is GOOD tpying speed")
            elif edited_wpm>=40 and edited_wpm<50:
                print(edited_wpm," is a VERY GOOD typing speed")
            else:
                print("This program shows that your typing speed is greater than 50!")
            difficulty_lvl.append(tl)
            wpm_l.append(edited_wpm)

    def show_mistake(c,inc):
        mistake_df = pd.DataFrame({"Correct ":c,"Incorrect ":inc})
        print("\n",mistake_df)

        for i in range(len(c)):
            if inc[i] != "<EMPTY>":
                for k in inc[i]:
                    if k not in c[i]:
                        incorrect_alphabets.append(k)
            else:
                incorrect_alphabets.append("<NOTHING TYPED>")

        l1 = []
        l2 = []
        for i in incorrect_alphabets:
            if i not in l1:
                frequency = incorrect_alphabets.count(i)
                l1.append(i)
                l2.append(frequency)
        print("\n\t\t\t\t\tWrong Alphabets")
        wrong_alpha_df = pd.DataFrame({"Alphabets":l1,"Frequency":l2})
        print(wrong_alpha_df)

    print("\n")
    print(text_chosen)
    print("\n")
    start_now = input("Write \'start\' to start typing or Write \'change\' to change the text :")
    if start_now == "start" or start_now == "1":
        text = text_chosen.split()
        print("\n\t\t\t\tStart typing in 2 seconds")
        time.sleep(2)
        time_taken_run = time.perf_counter()
        text_entered = input("\t\t Start typing from here : \n\n")
        time_taken_type = time.perf_counter()
    elif start_now == "change" or start_now == "2":
        if text_lvl == "easy":
            if text_chosen == text1:
                text_chosen = texts["easy"[random.choice([text2,text3])]]
            elif text_chosen == text2:
                text_chosen = texts["easy"[random.choice([text1,text3])]]
            else:
                text_chosen = texts["easy"[random.choice([text2,text1])]]
        elif text_lvl == "medium":
            if text_chosen == text4:
                text_chosen = medium[random.choice([text5,text6])]
            elif text_chosen == text5:
                text_chosen = medium[random.choice([text4,text6])]
            else:
                text_chosen = medium[random.choice([text4,text5])]
        else:
            if text_chosen == text7:
                text_chosen = hard[random.choice([text8,text9])]
            elif text_chosen == text8:
                text_chosen = hard[random.choice([text7,text9])]
            else:
                text_chosen = hard[random.choice([text7,text8])]
        text = text_chosen.split()
        print("\n\t\t\t\tStart typing in 2 seconds")
        time.sleep(2)
        time_taken_run = time.perf_counter()
        text_entered = input("\t\t Start typing from here : \n\n")
        time_taken_type = time.perf_counter()

    text_entered = text_entered.split()
    time_taken_actual = np.round(time_taken_type-time_taken_run)
    print("\nTime Taken :",time_taken_actual,"seconds")

    if len(text)<=len(text_entered):
        r_l = text
    elif len(text)>len(text_entered):
        r_l = text_entered

    for i in range(len(r_l)):
        if text_entered[i] != text[i] and len(text)>len(text_entered):
            if text_entered[i] == text[i+1]:
                text_entered.insert(i,"<EMPTY>")

    error = 0
    for i in range(len(r_l)):
        if text[i]!=text_entered[i]:
            if text_entered[i] == "<EMPTY>":
                correct_l.append(text[i])
                incorrect_l.append(text_entered[i])
            else:
                correct_l.append(text[i])
                incorrect_l.append(text_entered[i])
                error+=1

    wpm(len(text_entered),time_taken_actual,text_lvl)
    show_mistake(correct_l,incorrect_l)

def show_texts():
    text1 = "A computer is an electronic machine that runs on electricity and it understands only binary language that is the language of zeros and ones"
    text2 = "The programming language is a tool to talk with the computer and to say it to do a specific task, there are many programming languages available but python is the most popular nowadays"
    text3 = "The miniumum energy needed by an electron to come out from a metal surface is called the work function of the metal. Energy required for electron emission from the metal surface can be supplied by suitable heating."
    text4 = "The existance of discrete energy levels in an atom was directly verified in 1914 by James Frank and Gustav Hertz. They studied the spectrum of mercury vapour when electrons having different kinetic energies passed through the vapours."
    text5 = "We would first define the wavefront: when we drop a small stone on a calm pool of water, waves spread out of the point of impact. Every point on the surface starts oscillating with time."
    text6 = "Einstein showed from his theory of special relativity that it is necessary to treat mass as another form of energy. Before the advent of this theory of special relativity it was presumed that mass and erergy were conserved separatively in a reaction."  
    text7 = "The atomic mass of O found from mass spectroscopy experiments is seen to be 15.99493u. Substracting the mass of 8 electrons(8x0.00055u) from this, we get the experiment mass of O nucleus to be 15.99053u"
    text8 = "Consider a thin p-type silicon (p-Si) semiconductor wafer. By adding precisely a small quantity of pentavalent impurity, part of the p-Si wafer can be converted into n-Si. There are several processes by which a semiconductor can be formed."
    text9 = "Iitially, diffusion current is large and drift current is small. As the diffusion process continues, the space-charge regions on either side of the junction extend, thus increasing the elctric field strength and hence drift current."

    print("\n\t\t\t\t\tEasy Texts")
    print("1.",text1)
    print("2.",text2)
    print("3.",text3)
    print("\n\t\t\t\t\tMedium Texts")
    print("1.",text4)
    print("2.",text5)
    print("3.",text6)
    print("\n\t\t\t\t\tHard Texts")
    print("1.",text7)
    print("2.",text8)
    print("3.",text9)
    time.sleep(5)

def about():
    print("\n\t\t\t\t\tTyping Skill version 1.70")
    time.sleep(2)
    print("\t\t\t\tThis program is developed by :")
    time.sleep(3)
    print("\t\t\t\t\t\tNishant Nagar")
    time.sleep(2)
    print("\n\t\t\tThis program is capable of choosing texts from categories easy, medium, hard")
    time.sleep(5)
    print("\t\t,and calculate the typing speed of the user, counts the mistakes and show the edited typing speed")
    time.sleep(5)
    print("\t\t,the mistaken words are also showed with the correct spelling, and at the last, alphabets with")
    time.sleep(5)
    print("\t\t\trepetive mistakes are showed.")
    time.sleep(3)
    print("\n\tThis program is still under heavy development, new feature are being developed by the coder, hope you enjoy")
    time.sleep(5)
    print("\n\t\t\t\t\tTHANK YOU  -- Developer")

def end_it():
    if len(wpm_l) != 0:
        print("\n\t\t\tYOUR PERFORMANCE")
        dict_final = {"Difficulty ":difficulty_lvl,"Typing Speed":wpm_l}
        dataframe = pd.DataFrame(dict_final)
        print(dataframe)
    else:
        print("You have not given any test !")

def performance():
    time.sleep(1)
    print("\n\t\t\t\t\tPERFORMANCE")
    print("You have given ",len(wpm_l)," tests")
    average_speed = np.average(wpm_l)
    print("Average typing speed : ",average_speed)
    ask_show = input("Do you want a graph to show your performance (y or n) :")

    if ask_show == "y" or ask_show == "yes":
        if len(wpm_l) == 0:
            print("You have not done any typing test yet, return after giving tests.")
        elif len(wpm_l) == 1:
            print("You currently have done 1 writing test, to show a graph you atleast need to give 2 tests.")
        else:
            x_axis = np.arange(1,len(wpm_l)+1)
            plt.plot(x_axis,wpm_l)
            plt.xlabel("Test Number")
            plt.ylabel("WPM")
            plt.title("Performance in word per minute")
            plt.show()

while True:
    print("\n\t\t\t\t\tTYPING SKILL 1.50")
    print("\n\t\t\t\t\t1. Start Typing Test")
    print("\n\t\t\t\t\t2. Show Texts")
    print("\n\t\t\t\t\t3. About")
    print("\n\t\t\t\t\t4. Exit")
    print("\n\t\t\t\t\t5. Performance")
    start = input("\n\t\t\t\t\t Choose your action :")
    if start == "1" or start == "type" or start == "start":
        main()
    elif start == "2" or start == "texts":
        show_texts()
    elif start == "3" or start == "about":
        about()
    elif start == "n" or start == "no" or start == "exit" or start == "quit" or start == "4":
        rusure = input("\n\t\t\t\tAre you sure you want to exit ? ")
        if rusure == "yes" or rusure == "y" or rusure == "1":
            end_it()
            print("Exiting program !")
            break
        else:
            continue

    elif start == "5":
        performance()
    else:
        print("\n\t\t\t\t\tThe option chosen is not defined !!")
        continue






