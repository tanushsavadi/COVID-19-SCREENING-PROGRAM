symptoms= ["fever", "tiredness", "dry cough", "aches and pains", "nasal congestion", "runny nose", "sore throat", "diarrhoea"]
Pwithsymptoms=[]
Pwithoutsymptoms=[]
Choice=["yes", "no", "YES", "NO"]
c = ["yes", "YES"]
c1 = ["YES", "yes", "NO", "no"]
no = [1,2,3,4,5,6,7]
no2 = [1,2,3,4,5,6,7,8,9]
patients=[]
mildcond = []
risklevel = 0
seriouscond =[]
serious=0
mild=0
end=0
pcount=0
doc = []
def main ():
    end = 1
    while end == 1:
        risklevel=0
        symptotal=0
        pcount = 0
        serious=0
        mild=0
        doc = []
        print("*************************************************************************************************************")
        print("                                Welcome to the COVID-19 virtual screening program.")
        print("\n   You will now have to answer a series of questions, please answer carefully and truthfully!")
        print("*************************************************************************************************************")
        pname=str(input("\nEnter patient name : "))
        end1 = int(input("Enter 0 to terminate this program otherwise enter any other random number to continue: "))
        if end1 == 0:
            exit
        else:
            while len(pname) == 0:
                print("Insufficient characters or no characters were entered, please don't leave the field blank.")
                pname=str(input("\nEnter patient name : "))
            pnames = pname.split()
            if len(pname) > 1 :
                print("Welcome, " +str(pname))
            print("\nPlease chose your age category: \n 1.Under 18. \n 2.Between 18 and 65. \n 3.66 or older")
            choice1= int(input("Please enter 1,2 or 3 accordingly : "))
            while choice1 < 1 or choice1>3:
                print("Invalid input. Please enter 1,2 or 3 accordingly. ")
                choice1= int(input("Please enter 1,2 or 3 accordingly : "))
            if choice1==1:
                print("You have to be over the age of 18 to take this test")
                TRY= str(input("Do you want to try again? : "))
                if TRY in Choice:
                    return main()
            if choice1 == 2:
                risklevel+=3
            if choice1 == 3:
                risklevel+=5
            patients.append(pname)
            idno=int(input("\nPlease enter your ID number (Note : format for ID number should be a 7 digit number) : "))
            no1=len(str(abs(idno)))
            while no1 !=7:
                print("error")
                idno=int(input("\nPlease enter your ID number (Note : format for ID number should be a 7 digit number) : "))
                no1=len(str(abs(idno)))
            else:
                print("Your ID is accepted!")
                print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////") 
                choice=str(input("\nHave you noticed any of the following symptoms in the list?. Please enter yes or no(all caps or all lowercase)  : \n  \n 1.fever \n 2.tiredness \n 3.dry cough \n 4.aches and pains \n 5.nasal congestion \n 6.runny nose \n 7.sore throat \n 8.diarrhoea \n  \nYes or no? : "))
                while choice not in Choice:
                    print("Invalid input, Please enter yes or no(all caps or all lowercase)")
                    choice=str(input("Have you noticed any of the following symptoms in the list?. Please enter yes or no(all caps or all lowercase) \nYes or no? :  "))
                if choice == "yes" or "YES":
                    print("\nDo not worry, Please call 999 for further assistance and abide their suggestions. Avoid any contact with another person and please self-isolate yourself")
                    print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////") 
                if choice == "no" or "NO" or choice == "yes" or "YES":
                    print("\n\n*************************************************************************************************************")
                    print ("\nThe following list consists of the symptoms of COVID-19:  \n 1.fever \n 2.tiredness \n 3.dry cough \n 4.aches and pains \n 5.nasal congestion \n 6.runny nose \n 7.sore throat \n 8.diarrhoea \n ")
                    fever= str(input("\nDo you have fever?(Please enter yes or no(all caps or all lowercase) ) : "))
                    while fever not in Choice:
                        print("Invalid entry, please enter yes or no(all caps or all lowercase) ")
                        fever= str(input("Do you have fever?(Please enter yes or no(all caps or all lowercase) ) : "))
                    if fever in c:
                        risklevel+=5
                        symptotal+=1
                        seriouscond.append(pname)
                        Pwithsymptoms.append(pname)
                        serious +=1
                    else:
                        serious+=0
                        risklevel+=0
                        symptotal+=0
                    tiredness= str(input("\nDo you experience tiredness?(Please enter yes or no(all caps or all lowercase) ) : "))
                    while tiredness not in Choice:
                        print("Invalid entry, please enter yes or no(all caps or all lowercase)")
                        tiredness= str(input("Do you experience tiredness?(Please enter yes or no(all caps or all lowercase) ) : "))
                    if tiredness in c:
                        risklevel+=3
                        symptotal+=1
                        mildcond.append(pname)
                        Pwithsymptoms.append(pname)
                        mild+=1
                    else:
                        mild += 0
                        risklevel+=0
                        symptotal+=0
                    drycough = str(input("\nDo you have dry cough?(Please enter yes or no(all caps or all lowercase) ) : "))
                    while drycough not in Choice:
                        print("Invalid entry, please enter yes or no(all caps or all lowercase)")
                        drycough = str(input("Do you have dry cough?(Please enter yes or no(all caps or all lowercase) ) : "))
                    if drycough in c:
                        risklevel+=3
                        symptotal+=1
                        mildcond.append(pname)
                        Pwithsymptoms.append(pname)
                        mild += 1
                    else:
                        mild += 0
                        risklevel+=0
                        symptotal+=0
                    achesandpains= str(input("\nDo you experience aches and pains?(Please enter yes or no(all caps or all lowercase) ) : "))
                    while achesandpains not in Choice:
                        print("Invalid entry, please enter yes or no(all caps or all lowercase)")
                        achesandpains= str(input("Do you experience aches and pains?(Please enter yes or no(all caps or all lowercase) ) : "))
                    if achesandpains in c:
                        risklevel+=4
                        symptotal+=1
                        seriouscond.append(pname)
                        Pwithsymptoms.append(pname)
                        serious +=1
                    else:
                        serious +=1
                        risklevel+=0
                        symptotal+=0
                    nasalcongestion= str(input("\nDo you have nasal congestion?(Please enter yes or no(all caps or all lowercase) ) : "))
                    while nasalcongestion not in Choice:
                        print("Invalid entry, please enter yes or no(all caps or all lowercase)")
                        nasalcongestion= str(input("Do you have nasal congestion?(Please enter yes or no(all caps or all lowercase) ) : "))
                    if nasalcongestion in c:
                        risklevel+=2
                        symptotal+=1
                        mildcond.append(pname)
                        Pwithsymptoms.append(pname)
                        mild += 1
                    else:
                        mild += 0
                        risklevel+=0
                        symptotal+=0
                    runnynose= str(input("\nDo you have runny nose?(Please enter yes or no(all caps or all lowercase) ) : "))
                    while runnynose not in Choice:
                        print("Invalid entry, please enter yes or no(all caps or all lowercase)")
                        runnynose= str(input("Do you have runny nose?(Please enter yes or no(all caps or all lowercase) ) : "))
                    if runnynose in c:
                        risklevel+=2
                        symptotal+=1
                        mildcond.append(pname)
                        Pwithsymptoms.append(pname)
                        mild += 1
                    else:
                        mild += 0
                        risklevel+=0
                        symptotal+=0
                    sorethroat = str(input("\nDo you have a sore throat?(Please enter yes or no(all caps or all lowercase) ) : "))
                    while sorethroat not in Choice:
                        print("Invalid entry, please enter yes or no(all caps or all lowercase)")
                        sorethroat = str(input("Do you have a sore throat?(Please enter yes or no(all caps or all lowercase) ) : "))
                    if sorethroat in c:
                        risklevel+=3
                        symptotal+=1
                        mildcond.append(pname)
                        Pwithsymptoms.append(pname)
                        mild += 1
                    else:
                        mild += 0
                        risklevel+=0
                        symptotal+=0
                    diarrhoea = str(input("\nHave you been experiencing diarrhoea?(Please enter yes or no(all caps or all lowercase) ) : "))
                    while diarrhoea not in Choice:
                        print("Invalid entry, please enter yes or no(all caps or all lowercase)")
                        diarrhoea = str(input("Have you been experiencing diarrhoea?(Please enter yes or no(all caps or all lowercase) ) : "))
                    if diarrhoea in c:
                        risklevel+=5
                        symptotal+=1
                        seriouscond.append(pname)
                        Pwithsymptoms.append(pname)
                        serious +=1
                    else:
                        serious += 0
                        risklevel+=0
                        symptotal+=0
                    none= str(input("\nIf you didn't have any of the symptoms, that's great news, Keep up the good work on staying safe and keeping the community safe :) .\nPlease spread the word and tell everyone to stay home! \n\nEnter 'no' or 'NO' if you didn't have an experience with any of the symptoms or 'yes' or 'YES' if you did face one of these symptoms : "))
                    while none not in Choice:
                        print("\nInvalid entry, please enter yes or no(all caps or all lowercase)")
                        none= str(input("\nIf you didn't have any of the symptoms, that's great news, Keep up the good work on staying safe and keeping the community safe :) .\nPlease spread the word and tell everyone to stay home! \n\nEnter 'no' or 'NO' if you didn't have an experience with any of the symptoms or 'yes' or 'YES' if you did face one of these symptoms : "))
                    if none == "no" or "NO" :
                        risklevel+=0
                        symptotal+=0
                        Pwithoutsymptoms.append(pname)
                    else:
                        print("Do not worry, you will recover ")
                        print("\n\n*************************************************************************************************************")
                        print("\n\n======================================================================")
                    residence= "\nPlease chose where you reside from the following list (Enter an option like 1,2,3,4,5 or 6 accordingly) :\n\
        1. EUROPE\n\
        2. NORTH AMERICA\n\
        3. ASIA\n\
        4. SOUTH AMERICA\n\
        5. CENTRAL U.S.A\n\
        6. OCEANIA REGION\n\
        7. AFRICA\n Answer : "
                    residenceQ = int(input(residence))
                    while residenceQ not in no:
                        print("Error")
                        residenceQ = int(input("Please enter a number between 1 to 7 : "))
                    if residenceQ == 1:
                        risklevel += 5
                    if residenceQ == 2:
                        risklevel += 5
                    if residenceQ == 3:
                        risklevel += 4
                    if residenceQ == 4:
                        risklevel += 4
                    if residenceQ == 5:
                        risklevel += 5
                    if residenceQ == 6:
                        risklevel += 3
                    if residenceQ == 7:
                        risklevel += 4
                    travel = str(input("\nHave you travelled internationally? : "))
                    if travel == "yes" or "YES":
                        risklevel+=4
                        symptotal+=0
                    else:
                        risklevel +=0
                        symptotal +=0
                    if symptotal > 1 :
                        Pwithsymptoms.append(pname)
                    if symptotal == 0:
                        Pwithoutsymptoms.append(pname)
                    risklevel1 = risklevel/50*100
                    print("\nCalculating your results................")
                    print("Diagnosis complete!")
                    print("\n**************************************************************************************************************")
                    if risklevel > 20:
                        print("From the data collected using the questions you have answered here's what we have found.You have", +int(symptotal), "symptoms.", "You have a ", +int(risklevel1), "% of having COVID-19.\n\n ~Firstly do not worry or panic\n\n ~Secondly please wear gloves and face masks and practise other such sanitaztion routines to cut the curve of this spreading virus\n\n ~Thirdly Please remember to always follow 'social distancing' and to self-isolate yourself to prevent further spreading of this virus\n\n ~Lastly please adhere and stricly follow the government rules")
                        q = str(input("\nWould you like to get some information about the COVID-19 drive-through test centres?(only for UAE residents) : "))
                        while q not in c1:
                            print ("Error, enter yes or no")
                            q = str(input("Would you like to get some information about the COVID-19 drive-through test centres?(only for UAE residents) : "))
                        else:
                            import webbrowser
                            liveq = str(input("Do you live in the United Arab Emirates? : "))
                            cont = str(input("Do you want to continue? : "))
                            while cont in c:
                                if liveq in c:
                                    emirateslist = "\nWhich Emirate do you live in? : \n\
                                1. ABU DHABI\n\
                                2. DUBAI\n\
                                3. SHARJAH\n\
                                4. AJMAN\n\
                                5. UMM AL QUWAIN\n\
                                6. RAS AL KHAIMAH\n\
                                7. FUJAIRAH\nEnter your option(Enter a number between 1 to 7, respective to where you live or where you want to search for the centres) : "
                                    emirateslist1= int(input(emirateslist))
                                    while emirateslist1 not in no:
                                        print("Error")
                                        emirateslist1 = int(input("Please try again : ")) 
                                    if emirateslist1 == 1:
                                        testcentresauh = str(input("\nDo you want to view the list of COVID-19 drive-through test centres in Abu Dhabi? (Enter yes or no): "))
                                        while testcentresauh not in c1:
                                            print("Error")
                                            testcentresauh = str(input("\nDo you want to view the list of COVID-19 drive-through test centres in Abu Dhabi? (Enter yes or no): "))
                                        if testcentresauh in c:
                                            testcentreslist1 = "\nYou will now see a list of all available drive-through COVID-19 test centres in Abu Dhabi :\n\
                                1. Ghayathi, Al Dhafra\n\
                                2. Madinat Zayed, Al Dhafra\n\
                                3. Al Wathba\n\
                                4. Zayed Sports City\n\
                                5. Al Bahia\n\
                                6. Al Hili – Al Ain\n\
                                7. Asharej – Al Ain\n Please select an option between 1 to 7 to view the google maps location of any one of these locations : "
                                            location1 = int(input(testcentreslist1))
                                            while location1 not in no:
                                                print("error")
                                                location1 = int(input("Please try again : "))
                                            if location1 == 1:
                                                viewq = str(input("Do you wish to load the google maps for this loaction? : "))
                                                if viewq in c:
                                                    webbrowser.open("https://www.google.com/maps/place/23%C2%B050'16.1%22N+52%C2%B048'32.8%22E/@23.83781,52.809111,17z/data=!3m1!4b1!4m2!3m1!1s0x0:0x0")
                                            elif location1 == 2:
                                                viewq1 = str(input("Do you wish to load the google maps for this loaction? : "))
                                                if viewq1 in c:
                                                    webbrowser.open("https://www.google.com/maps/place/23%C2%B038'10.7%22N+53%C2%B042'30.7%22E/@23.636306,53.708532,17z/data=!3m1!4b1!4m2!3m1!1s0x0:0x0")
                                            elif location1 == 3:
                                                viewq2 = str(input("Do you wish to load the google maps for this loaction? : "))
                                                if viewq2 in c:
                                                    webbrowser.open("https://www.google.com/maps/place/24%C2%B013'20.2%22N+54%C2%B040'54.8%22E/@24.2225847,54.6784369,15.72z/data=!4m2!3m1!1s0x0:0x0")
                                            elif location1 == 4:
                                                viewq3 = str(input("Do you wish to load the google maps for this loaction? : "))
                                                if viewq3 in c:
                                                    webbrowser.open("https://www.google.com/maps/place/24%C2%B024'49.2%22N+54%C2%B027'13.8%22E/@24.413665,54.453839,17z/data=!3m1!4b1!4m2!3m1!1s0x0:0x0")
                                            elif location1 == 5:
                                                viewq4 = str(input("Do you wish to load the google maps for this loaction? : "))
                                                if viewq4 in c:
                                                    webbrowser.open("https://www.google.com/maps/place/24%C2%B032'06.8%22N+54%C2%B040'28.2%22E/@24.535229,54.674485,17z/data=!3m1!4b1!4m2!3m1!1s0x0:0x0")
                                            elif location1 == 6:
                                                viewq5 = str(input("Do you wish to load the google maps for this loaction? : "))
                                                if viewq5 in c:
                                                    webbrowser.open("https://www.google.com/maps/place/7HPQ8Q2J%2BF8/@24.3015194,55.7791108,15.75z/data=!4m5!3m4!1s0x0:0x0!8m2!3d24.3011875!4d55.7808125")
                                            elif location1 == 7:
                                                viewq6 = str(input("Do you wish to load the google maps for this loaction? : "))
                                                if viewq6 in c:
                                                    webbrowser.open("https://www.google.com/maps/place/''Asharij+-+Abu+Dhabi'/@24.2022584,55.6529182,13.88z/data=!4m5!3m4!1s0x3e8ab1e07aa3c4f5:0xc577693caf905c59!8m2!3d24.2010759!4d55.670834")
                                        cont = str(input("Do you want to continue? : "))
                                    elif emirateslist1 == 2:
                                        testcentresdxb = str(input("\nDo you want to view the list of COVID-19 drive-through test centres in Dubai? (Enter yes or no): "))
                                        while testcentresdxb not in c1:
                                            print("Error")
                                            testcentresdxb = str(input("\nDo you want to view the list of COVID-19 drive-through test centres in Dubai? (Enter yes or no): "))
                                        if testcentresdxb in c:
                                            testcentreslist2 = "\nYou will now see a list of all available drive-through COVID-19 test centres in Dubai :\n\
                            1. Al Khawaneej\n\
                            2. Port Rashid\ Mina Rashid\n\
                            3. Al Nasr Club, Oud Metha\n\
                            4. Dubai Festival City\n\
                            5. Al Qusais 2\n\
                            6. Silicon Oasis\n\
                            7. Discovery Gardens\n\
                            8. Al Warqa 1\n\
                            9. International City\n\Please select an option between 1 to 9 to view the google maps location of any one of these locations : "
                                            location2 = int(input(testcentreslist2))
                                            while location2 not in no2:
                                                print("Error")
                                                location2 = int(input("Please try again : "))
                                            if location2 == 1:
                                                view1 = str(input("Do you wish to load the google maps for this loaction? : "))
                                                if view1 in c:
                                                    webbrowser.open("https://www.google.com/maps/place/25%C2%B014'05.3%22N+55%C2%B028'28.9%22E/@25.234796,55.474681,17z/data=!3m1!4b1!4m2!3m1!1s0x0:0x0")
                                            elif location2 == 2:
                                                view2 = str(input("Do you wish to load the google maps for this loaction? : "))
                                                if view2 in c:
                                                    webbrowser.open("https://www.google.com/maps/place/25%C2%B015'15.1%22N+55%C2%B016'51.8%22E/@25.254198,55.281054,17z/data=!3m1!4b1!4m2!3m1!1s0x0:0x0")
                                            elif location2 == 3:
                                                view3 = str(input("Do you wish to load the google maps for this loaction? : "))
                                                if view3 in c :
                                                    webbrowser.open("https://www.google.com/maps/place/AL+Nasr+Club/@25.2411884,55.3109154,17z/data=!3m1!4b1!4m5!3m4!1s0x3e5f42d398202755:0x8d359f3666389beb!8m2!3d25.2411884!4d55.3109154")
                                            elif location2 == 4:
                                                view4 = str(input("Do you wish to load the google maps for this loaction? : "))
                                                if view4 in c:
                                                    webbrowser.open("https://www.google.com/maps/place/Dubai+Festival+City+Mall/@25.2219515,55.3527943,17z/data=!3m1!4b1!4m5!3m4!1s0x3e5f5d778cffffff:0xf49b6296189d22d5!8m2!3d25.2219515!4d55.3527943")
                                            elif location2 == 5:
                                                view5 = str(input("Do you wish to load the google maps for this loaction? : "))
                                                if view5 in c:
                                                    webbrowser.open("https://www.google.com/maps/place/Manazel+Deira+-+Al+Nahda+road+8+B+St+-+Dubai/@25.2672851,55.3798815,15.88z/data=!4m5!3m4!1s0x3e5f5c355b35a375:0xc0f16155043508fe!8m2!3d25.267325!4d55.3814257")
                                            elif location2 == 6:
                                                view6 = str(input("Do you wish to load the google maps for this loaction? : "))
                                                if view6 in c:
                                                    webbrowser.open("https://www.google.com/maps/place/Lynx+Tower/@25.1098801,55.3775451,17z/data=!3m1!4b1!4m5!3m4!1s0x3e5f644332d72d47:0x2d4cbd4d86172769!8m2!3d25.1098801!4d55.3775451")
                                            elif location2 == 7:
                                                view7 = str(input("Do you wish to load the google maps for this loaction? : "))
                                                if view7 in c:
                                                    webbrowser.open("https://www.google.com/maps/place/6+-+Dubai/@25.048985,55.1287676,17z/data=!4m5!3m4!1s0x3e5f1336b3d36eb1:0x42edbd60275da9!8m2!3d25.0499473!4d55.1311601")
                                            elif location2 == 8:
                                                view8 = str(input("Do you wish to load the google maps for this loaction? : "))
                                                if view8 in c:
                                                    webbrowser.open("https://www.google.com/maps/place/Al+Mushroom+Building+3/@25.1960708,55.3756212,13.24z/data=!4m15!1m9!4m8!1m3!2m2!1d55.3946474!2d25.1925186!1m3!2m2!1d55.4054646!2d25.1920691!3m4!1s0x3e5f61a68ea68fc7:0xe859063827bd7926!8m2!3d25.1920691!4d55.4054646")
                                            elif location2 == 9:
                                                view9 = str(input("Do you wish to load the google maps for this loaction? : "))
                                                if view9 in c:
                                                    webbrowser.open("https://www.google.com/maps/dir//25.167881,55.397612/@25.1642872,55.3903532,14z")
                                        cont = str(input("Do you want to continue? : "))
                                    elif emirateslist1 == 3:
                                        testcentresshrjh = str(input("\nDo you want to view the list of COVID-19 drive-through test centre(s) in Sharjah? (Enter yes or no): "))
                                        while testcentresshrjh not in c1:
                                            print("error")
                                            testcentresshrjh = str(input("\nDo you want to view the list of COVID-19 drive-through test centre(s) in Sharjah? (Enter yes or no): "))
                                        if testcentresshrjh in c:
                                            testcentreslist3 = "\nYou will now see a list of all available drive-through COVID-19 test centre(s) in Sharjah :\n\
                                1. Sharjah Golf and Shooting club\nPlease select an option to view the google maps location for this location : "
                                            location3 = int(input(testcentreslist3))
                                            while location3 != 1:
                                                print("Error")
                                                location3 = int(input("Please try again : "))
                                            else:
                                                views1 = str(input("Do you wish to load the google maps for this loaction? : "))
                                                if views1 in c:
                                                    webbrowser.open("https://www.google.com/maps/place/National+Screening+Center-Sharjah+%D9%85%D8%B1%D9%83%D8%B2+%D8%A7%D9%84%D9%85%D8%B3%D8%AD+%D8%A7%D9%84%D9%88%D8%B7%D9%86%D9%8A-%D8%A7%D9%84%D8%B4%D8%A7%D8%B1%D9%82%D8%A9%E2%80%AD/@25.3511709,55.4840677,14.64z/data=!4m5!3m4!1s0x3e5f595345384641:0x83f7fd744c35e147!8m2!3d25.3543221!4d55.4889096")
                                        cont = str(input("Do you want to continue? : "))
                                    elif emirateslist1 == 4:
                                        testcentresajman = str(input("\nDo you want to view the list of COVID-19 drive-through test centre(s) in Ajman? (Enter yes or no): "))
                                        while testcentresajman not in c1:
                                            print("Error")
                                            testcentresajman = str(input("\nDo you want to view the list of COVID-19 drive-through test centre(s) in Ajman? (Enter yes or no): "))
                                        if testcentresajman in c:
                                            testcentreslist4 ="\nYou will now see a list of all available drive-through COVID-19 test centre(s) in Ajman :\n\
                                1. Al Jerf 2- Ajman\nPlease select an option to view the google maps location for this location : "
                                            location4 = int(input(testcentreslist4))
                                            while location4 != 1:
                                                print("Error")
                                                location4 = int(input("Please try again : "))
                                            else:
                                                View1 = str(input("Do you wish to load the google maps for this loaction? : "))
                                                if View1 in c:
                                                    webbrowser.open("https://www.google.com/maps/place/7HQQCF3J%2BGV/@25.4038125,55.4821875,17z/data=!3m1!4b1!4m5!3m4!1s0x0:0x0!8m2!3d25.4038125!4d55.4821875")
                                        cont = str(input("Do you want to continue? : "))
                                    elif emirateslist1 == 5:
                                        testcentreUAQ = str(input("\nDo you want to view the list of COVID-19 drive-through test centre(s) in Umm Al Quwain? (Enter yes or no): "))
                                        while testcentreUAQ not in c1:
                                            print("Error")
                                            testcentreUAQ = str(input("\nDo you want to view the list of COVID-19 drive-through test centres in Umm Al Quwain? (Enter yes or no): "))
                                        if testcentreUAQ in c:
                                            testcentreslist5 ="\nYou will now see a list of all available drive-through COVID-19 test centre(s) in Umm Al Quwain :\n\
                                1. Sheikh Khalifa Hall - Umm Al Quawain\nPlease select an option to view the google maps location for this location : "
                                            location5 = int(input(testcentreslist5))
                                            while location5 != 1:
                                                print("Error")
                                                location5 = int(input("Please try again : "))
                                            else:
                                                View2 = str(input("Do you wish to load the google maps for this loaction? : "))
                                                if View2 in c:
                                                    webbrowser.open("https://www.google.com/maps/place/National+Screening+Center-Umm+Al+Quwain+%D9%85%D8%B1%D9%83%D8%B2+%D8%A7%D9%84%D9%85%D8%B3%D8%AD+%D8%A7%D9%84%D8%B5%D8%AD%D9%8A-%D8%A3%D9%85+%D8%A7%D9%84%D9%82%D9%8A%D9%88%D9%8A%D9%86%E2%80%AD/@25.5062209,55.5923237,15.89z/data=!4m5!3m4!1s0x3ef5fb840cd08899:0x91dd48518af25039!8m2!3d25.5073136!4d55.5965441?hl=en-GB")
                                        cont = str(input("Do you want to continue? : "))
                                    elif emirateslist1 == 6:
                                        testcentreRAK = str(input("\nDo you want to view the list of COVID-19 drive-through test centre(s) in Ras Al Khaimah? (Enter yes or no): "))
                                        while testcentreRAK not in c1:
                                            print("Error")
                                            testcentreRAK = str(input("\nDo you want to view the list of COVID-19 drive-through test centre(s) in Ras Al Khaimah? (Enter yes or no): "))
                                        if testcentreRAK in c:
                                            testcentreslist6 ="\nYou will now see a list of all available drive-through COVID-19 test centre(s) in Ras Al Khaimah:\n\
                                1. Dafan Al Khor\nPlease select an option to view the google maps location for this location : "
                                            location6 = int(input(testcentreslist6))
                                            while location6 != 1:
                                                print("Error")
                                                location6 = int(input("Please try again : "))
                                            else:
                                                View3 = str(input("Do you wish to load the google maps for this loaction? : "))
                                                if View3 in c:
                                                    webbrowser.open("https://www.google.com/maps/place/National+Screening+Center-Ras+Al+Khaimah+%D9%85%D8%B1%D9%83%D8%B2+%D8%A7%D9%84%D9%85%D8%B3%D8%AD+%D8%A7%D9%84%D8%B5%D8%AD%D9%8A-%D8%B1%D8%A3%D8%B3+%D8%A7%D9%84%D8%AE%D9%8A%D9%85%D8%A9%E2%80%AD/@25.7714241,55.9269558,15.02z/data=!4m5!3m4!1s0x0:0xdff72fc2dcc899ab!8m2!3d25.7728101!4d55.9342899?hl=en-GB")
                                        cont = str(input("Do you want to continue? : "))
                                    elif emirateslist1 == 7:
                                        testcentreFujairah = str(input("\nDo you want to view the list of COVID-19 drive-through test centre(s) in Fujairah? (Enter yes or no): "))
                                        while testcentreFujairah not in c1:
                                            print("Error")
                                            testcentreFujairah = str(input("\nDo you want to view the list of COVID-19 drive-through test centre(s) in Fujairah? (Enter yes or no): "))
                                        if testcentreFujairah in c:
                                            testcentreslist7 ="\nYou will now see a list of all available drive-through COVID-19 test centre(s) in Fujairah:\n\
                                1. Fujairah Hospital area\nPlease select an option to view the google maps location for this location : "
                                            location7 = int(input(testcentreslist7))
                                            while location7 != 1:
                                                print("Error")
                                                location7 = int(input("Please try again : "))
                                            else:
                                                View4 = str(input("Do you wish to load the google maps for this loaction? : "))
                                                if View4 in c:
                                                    webbrowser.open("https://www.google.com/maps/place/7HQR48JC%2BJ5/@25.1315625,56.3204375,17z/data=!3m1!4b1!4m5!3m4!1s0x0:0x0!8m2!3d25.1315625!4d56.3204375")
                                        cont = str(input("Do you want to continue? : "))
                            else:
                                exit
                    else:
                        print("Geart job, the probability that you are having COVID-19 is", +int(risklevel1), "and you have", +int(symptotal), "symptoms.\n\nPlease continue your ongoing efforts on keeping you and the people around you safe by staying home and never forgetting to practise 'social distancing'! " )
            print("\n\n----------------------------------------------------------------------------------------------------------------------------------------")
            patient2 = str(input("\nIs there another patient that needs to use this program for diagnosis? : "))
            while patient2 not in Choice:
                print("Invalid entry, please enter yes or no(all caps or all lowercase)")
                patient2 = str(input("Is there another patient that needs to use this program for diagnosis? : "))
            if patient2 in c:
                return main()
            else:
                login= str(input("\nAre you a doctor? : "))
                docname = str(input("Please enter your name Doctor : "))
                doc.append(docname)
                if login not in c:
                    return main()
                else:
                    password= input("Enter your password (You only get 3 tries or else program ends!): ")
                    while password != "access54321" and pcount != 3:
                        print("\nPassword is incorrect!")
                        password= input("Enter your password: ")
                        pcount +=1
                    if pcount ==3:
                        exit                        
                    else:
                        print("\nAccess granted, Welcome Doctor ", (doc))
                    print("You can currently access", +len(patients), "record(s)")
                    find = str(input("Do you wish to find a record? : "))
                    while find in c:
                        searchtype = "\nYou can search by either :\n\
        1. Name\n\
        2. Condition level\nEnter your choice (1 or 2) : " 
                        searchtype1 = int(input(searchtype))
                        if searchtype1 == 1:
                            x = 1
                            while x == 1:
                                for count in range (1):
                                    search2 = str(input("\nPlease enter the patient name you are looking for : "))
                                    if search2 not in (patients):
                                        print("'",search2,"'", ", was not found in database or isn't a valid name, please enter the name as it was entered")
                                    else:
                                        for i in range (len(patients)):
                                            if patients [i] == search2:
                                                print("\nPatient name: ", (patients[i]))
                                                x = 0
                            print("\nNumber of symptoms: ",+int(symptotal))
                            print("\nProbability of having COVID-19: ",+int(risklevel1))
                            if serious > 0:
                                print("\nCondition level: Serious")
                            else:
                                print("\nCondition level: Mild")
                            find = str(input("\nDo you wish to find a record? : "))
                        else:
                            opt = "\nChoose option : \n\
        1.Mild conditions\n\
        2. Serious conditions\n Enter your choice (1 or 2) : "
                            opt1 = int(input(opt))
                            if opt == 1:
                                if len(mildcond) == 0:
                                    print("There are no patients with mild conditions!")
                                else:
                                    print("\nName of patient: "+str(mildcond[i]))
                            else:
                                if len(seriouscond) == 0:
                                    print("There are no patients with mild conditions!")
                                else:
                                    print("Name of patient: "+str(seriouscond[i]))
                            find = str(input("Do you wish to find a record? : "))
            print("\n\n----------------------------------------------------------------------------------------------------------------------------------------")
main()









                              
