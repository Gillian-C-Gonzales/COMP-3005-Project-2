import psycopg2
from  psycopg2 import Error
import os

def member_menu():
    information = []
    print("Profile Login")
    email = input("Email:")
    password = input("Passowrd:")

    information.append(email)
    information.append(password)

    return information
    



def trainer_menu():
    information = []
    print("Trainer Login")
    email = input("Name:")

    information.append(email)

    return information

def admin_menu():
    information = []
    print("Admin Login")
    email = input("Email:")
    password = input("Passowrd:")

    information.append(email)
    information.append(password)

    return information

def registeration(heading):
    os.system('cls')
    information = []
    print(heading)
    print("Name:")
    name = input()
    print("Gender:")
    gender = input()
    print("Age:")
    age = input()
    print("Email:")
    email = input()
    print("Password:")
    password = input()
    print("Freeday(M/T/W/TH/F):")
    freeday = input()

    information.append(name)
    information.append(gender)
    information.append(age)
    information.append(email)
    information.append(password)
    information.append(freeday)
    return information



def starting():
    print("Welcome to the Health and Fitness Club Management System")
    print("Choose which type of user you are 1-5\n"
          "1: Member\n"
          "2: Trainer\n"
          "3: Admin\n"
          "4: New member/register\n"
          "0: Exit\n")
    type_of_user = int(input())
    while (type_of_user > 4 and type_of_user < -1):
        os.system('cls')
        print("Invalid input try again")
        print("Choose which type of user you are 1-5\n"
            "1: Member\n"
            "2: Trainer\n"
            "3: Admin\n"
            "4: New member/register\n"
            "0: Exit\n")
        type_of_user = int(input())


    if (type_of_user == 1):
        member_login = [1,member_menu()]
        return member_login
    elif (type_of_user == 2):
        trainer_login = [2,trainer_menu()]
        return trainer_login
    elif (type_of_user == 3):
        admin_login = [3,admin_menu()]
        return admin_login
    elif (type_of_user == 4):
        new_member = [4,registeration("Registration process type in the following information:")]
        return new_member
    elif (type_of_user == 0):
        return [0,0]
    else:
        print("Type of user error (line 31)")





if (__name__ == "__main__"):
    # try:
        connection = psycopg2.connect(database = "COMP-3005_Project_2", 
                                      user="postgres",
                                      host="localhost",
                                      password="654RfghYT",
                                      port = 5432)
        
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(),"\n")
        curr = connection.cursor()
        returning = [1,0]

        while (returning[0] != 0):
            returning = starting()

            if returning[0] == 1:
                print("member edit")
                curr.execute("Select email from member")
                emails = curr.fetchall()
                count = 0
                for email in emails:
                    count+=1
                    if email[0] == returning[1][0]:
                        print('pass')
                        curr.execute("Select password from member where email = %s",(email))
                        password = curr.fetchall()
                        print(password[0])
                        if password[0][0] == returning[1][1]:
                            print("Login Successful")
                            profile_input = 1
                            while (profile_input != 0):
                                os.system('cls')
                                print("Select one of the options to edit your profile\n"
                                    "1: Edit personal information\n"
                                    "2: Edit Fitnesss goals\n"
                                    "3: Edit Health metrics\n"
                                    "4: Display Routines, Fitness Acheivements, Health Stats\n"
                                    "5: Schedule Managment")
                                profile_input = int(input())
                                curr.execute("Select MID from member where email = %s",(email))
                                mid = curr.fetchall()
                                if (profile_input == 1):
                                    edited_information = registeration("Type in new information")
                                    curr.execute("UPDATE member Set name = %s, gender = %s, age = %s, email = %s, password = %s, free_day = %s where MID = %s",
                                                (edited_information[0],edited_information[1],edited_information[2],edited_information[3],edited_information[4],edited_information[5], mid[0][0]))
                                    connection.commit()
                                elif(profile_input == 2):
                                    print("New fitness goal")
                                    print("Type new goal:")
                                    edited_goal = input()
                                    print("Type in by what date")
                                    edited_time = input()
                                    curr.execute("UPDATE fitness_goals Set goal = %s, time = %s where MID = %s",
                                                (edited_goal,edited_time, mid[0]))
                                    connection.commit()
                                elif(profile_input == 3):
                                    print("New health metrics")
                                    print("Type new date:")
                                    edited_date = input()
                                    print("Type new weight")
                                    edited_weight = input()
                                    print("Type new BFP")
                                    edited_BFP = input()
                                    curr.execute("UPDATE fitness_metrics Set date = %s, weight = %s, BFP = %s where MID = %s",
                                                (edited_date,edited_weight,edited_BFP, mid[0][0]))
                                    connection.commit()
                                elif(profile_input == 4):
                                    print(mid)
                                    curr.execute("Select exercise_name from routine where mid = %s",(mid[0]))
                                    member_routine = curr.fetchall()
                                    print(member_routine)
                                    print("Routine: " + member_routine[0][0])
                                    curr.execute("Select acheivement from fitness_acheivements where mid = %s",(mid[0]))
                                    member_achievement = curr.fetchall()
                                    print("Acheivement: " + member_achievement[0][0])
                                    curr.execute("Select weight, BFP from fitness_metrics where mid = %s",(mid[0]))
                                    member_health_metrics = curr.fetchall()
                                    print("Weight" + str(member_health_metrics[0][0]))
                                    print("BFP" + str(member_health_metrics[0][1]))
                                    input()
                                elif(profile_input == 5):
                                    print("Schedule a group fitness actvity(1) or personal training session(2)?")
                                    session_type = int(input())
                                    print(mid)
                                    curr.execute("Select free_day from member where mid = %s",(mid[0]))
                                    member_free_day = curr.fetchall()
                                    if (session_type == 2):
                                        print("Availiable Trainers")
                                        curr.execute("Select name from trainer where free_day = %s",(member_free_day))
                                        trainer_free = curr.fetchall()
                                        print(trainer_free)
                                        print("Select trainer by index (starting from 0)")
                                        select_trainer = int(input())
                                        selected_trainer = trainer_free[select_trainer]
                                        curr.execute("Select TID from trainer where name = %s",(selected_trainer))
                                        tid = curr.fetchall()
                                        print("Type in a timestamp for a training session")
                                        selected_time = input()
                                        curr.execute("Insert into training_session(MID, TID, scheduled_time)"
                                                     "Values(%s,%s,%s)",(mid[0],tid[0],selected_time))
                                        input("Training Session successful")
                                        connection.commit()
                                    elif (session_type == 1):
                                        print("Availiable Group Activities")
                                        curr.execute("Select name from group_fitness where dayslot = %s",(member_free_day))
                                        group_free = curr.fetchall()
                                        print("Select group by index (starting from 0)")
                                        select_group = int(input())
                                        selected_group = group_free[select_group]
                                        curr.execute("Select signupcount from group_fitness where name = %s",(selected_group))
                                        count = curr.fetchall()
                                        count += 1
                                        curr.execute("UPDATE group_fitness Set signupcount = %s where name = %s",
                                                (count,selected_group))
                                        connection.commit()
                                elif(profile_input == 0):
                                    break
                                else:
                                    print("Invalid input try again")
                        else: 
                            print("Password fail")
                if count == len(emails):
                    print("Email not valid")
            elif returning[0]== 2:
                print("trainer edit")
                trainer_input = 1
                while (trainer_input != 0):
                    os.system('cls')
                    print("Select one of the options to edit your profile\n"
                        "1: Edit schedule\n"
                        "2: View members\n"
                        "0: Exit")
                    print(type(returning[1][0]))
                    curr.execute("Select TID from trainer where name = {0}".format(returning[1][0]))
                    tid = curr.fetchall()
                    if trainer_input == 1:
                        print("Type in new day of the week(M,T,W,TH,F)")
                        new_day = input()
                        curr.execute("UPDATE trainer Set free_day = %s where TID = %s",
                                (new_day, tid[0][0]))
                        connection.commit()
                    elif trainer_input == 2:
                        print("All memebers assigned")
                        curr.execute("Select MID from training_session where TID = %s",(tid[0][0]))
                        all_members = curr.fetchall()
                        input()
                    elif trainer_input == 0:
                        break
            elif returning[0] == 3:
                print("admin edit")
                admin_input = 1
                while admin_input != 0:
                    os.system('cls')
                    print("Select one of the options to edit your profile\n"
                        "1: Manage Room Bookings\n"
                        "2: Equipment Maintence\n"
                        "3: Class Schedule Update\n"
                        "4: Billing\n"
                        "0: Exit")
                    admin_input = int(input())
                    if (admin_input == 1):
                        print("All rooms")
                        curr.execute("Select room_number from room_booking")
                        rooms = curr.fetchall()
                        print(rooms)
                        print("Which room would u like to edit (index start from 0)")
                        select_room = int(input())
                        selected_room = rooms[select_room]
                        print("Choose a day for the room's avaliablility(M,T,W,TH,F)")
                        room_day = input()
                        curr.execute("UPDATE room_booking Set dayslot = %s where room_number = %s",
                                (room_day, selected_room))
                        connection.commit()
                    elif (admin_input == 2):
                        print("Viewing all equipment")
                        curr.execute("Select equipment,last_day_checked from gym_equipment")
                        equipment =  curr.fetchall()
                        print(equipment)
                        input()
                    elif (admin_input == 3):
                        print("Viewing all classes")
                        curr.execute("Select activity from group_fitness")
                        gym_class = curr.fetchall()
                        print(gym_class)
                        print("Which activity would you like to update(index start from 0)")
                        select_class = int(input())
                        selected_class = gym_class[select_class]
                        print("New activity name?")
                        new_activity = input()
                        curr.execute("UPDATE group_fitness Set activity = %s where activity = %s",
                                (new_activity, selected_class))
                        connection.commit()
                    elif (admin_input == 4):
                        print("Adding new billing")
                        print("Input credit card infomation")
                        credit_card = input()
                        print("Success: Charged $50")
                        input()
            elif returning[0] == 4:
                print("new memeber edit ")
                curr.execute("Insert into member(name, gender, age, email, password, goal_value, free_day)" 
                            "Values(%s,%s,%s,%s,%s,%s, NULL)",
                            (returning[1][0],returning[1][1],returning[1][2],returning[1][3],returning[1][4], returning[1][5]))
                connection.commit()
                curr.execute("Select MID from member where email = %s",(returning[1][3]))
                mid = curr.fetchall()
                print(mid)
                input()
                curr.execute("Insert into fitness_metrics(date, weight, BFP, MID)" 
                            "Values('2002-04-22', 0 ,0 , %s )",(mid[0]))
                curr.execute("Insert into fitness_goals(goal, time, MID)" 
                            "Values('None','2025-04-22' , %s )",(mid))
                curr.execute("Insert into fitness_acheivements(acheivement, time, MID)" 
                            "Values('None', '2002-04-22', %s )",(mid))
                curr.execute("Insert into routine(exercise_name, duration, MID)" 
                            "Values('None', '00:00:00', %s )",(mid))
                connection.commit()
            elif returning[0] == 0:
                curr.close()
                connection.close()
                input("Program End, Press enter to finish")



    # except (Exception, Error) as error:
    #     print("Error while connecting to PostgreSQL",error)
