from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

root = Tk()
root.title("Namma Metro Fair Calculator")
root.geometry("700x350")
root.config(bg="Purple")
image1 = ImageTk.PhotoImage(Image.open("icon.jpg"))
root.iconphoto(False, image1)

title1 = Label(root, text = "                         Namma Metro Fair Calculator",font=("Arial", 20),bg="Purple", fg="White")
title1.grid(row=0, column=0, columnspan=3)

mylabel1 = Label(root, text = "        ",font=("Arial", 15),bg="Purple")
mylabel1.grid(row=1, column=0)

boarding_station_label = Label(root, text = "          Select the boarding station",font=("Arial", 15),bg="Purple", fg="White")
boarding_station_label.grid(row=2, column=0)

boarding_station = StringVar()
boarding_station.set("Nagasandra")
station_name = ["Nagasandra", "Dasarahalli", "Jalahalli", "Peenya Industry", "Peenya", "Goraguntepalya", "Yeshwanthpur", "Sandal Soap Factory", "Mahalakshmi", "Rajajinagar", "Mahakavi Kuvempu Road", "Srirampura", "Sampige Road", "Majestic", "Chikpete", "Krishna Rajendra Market", "National College", "Lalbagh Botanical Garden", "South End Circle", "Jayanagar", "Rashtreeya Vidyalaya Road", "Banashankari", "Jaya Prakash Nagar", "Yelachenahalli", "Konanakunte Cross", "Doddakallasandra", "Vajarahalli", "Thalaghattapura", "Silk Institute", "Kengeri", "Kengeri Bus Terminal", "Pattanagere", "Jnanabharathi", "Rajarajeshwari Nagar", "Nayandahalli", "Mysuru Road", "Deepanjali Nagara", "Attiguppe", "Vijayanagara", "Balagangadhara Natha Swamiji HOS", "Magadi Road", "City Railway Station", "Majestic","Sir M. Visveshwaraya Station", "Dr BR Ambedkar Vidhana Soudha", "Cubbon Park Sri Chamarajendra Park", "MG Road","Trinity", "Halasuru", "Indiranagara", "Swami Vivekananda Road", "Baiyappanahalli"]
boarding_station_dropdown_menu = OptionMenu(root, boarding_station, *station_name)
boarding_station_dropdown_menu.config(bg="Purple", fg="WHITE", height=2)
boarding_station_dropdown_menu.grid(row=2, column=1)

mylabel2 = Label(root, text = "    ",font=("Arial", 15),bg="Purple")
mylabel2.grid(row=3, column=0)

departure_station_label = Label(root, text = "          Select the departure station",font=("Arial", 15),bg="Purple", fg="White")
departure_station_label.grid(row=4, column=0)

departure_station = StringVar()
departure_station.set("Nagasandra")
departure_station_dropdown_menu = OptionMenu(root, departure_station, *station_name)
departure_station_dropdown_menu.config(bg="Purple", fg="WHITE", height=2)
departure_station_dropdown_menu.grid(row=4, column=1)

mylabel3 = Label(root, text = "    ",font=("Arial", 15),bg="Purple")
mylabel3.grid(row=5, column=0)

Green_line = ["Nagasandra", "Dasarahalli", "Jalahalli", "Peenya Industry", "Peenya", "Goraguntepalya", "Yeshwanthpur", "Sandal Soap Factory", "Mahalakshmi", "Rajajinagar","Mahakavi Kuvempu Road", "Srirampura","Sampige Road","Majestic","Chikpete","Krishna Rajendra Market","National College","Lalbagh Botanical Garden","South End Circle","Jayanagar","Rashtreeya Vidyalaya Road","Banashankari","Jaya Prakash Nagar","Yelachenahalli","Konanakunte Cross","Doddakallasandra","Vajarahalli","Thalaghattapura","Silk Institute"]
Purple_line = ["Kengeri","Kengeri Bus Terminal","Pattanagere","Jnanabharathi","Rajarajeshwari Nagar","Nayandahalli","Mysuru Road","Deepanjali Nagara","Attiguppe"," Vijayanagara","Balagangadhara Natha Swamiji HOS","Magadi Road","City Railway Station","Majestic","Sir M. Visveshwaraya Station","Dr BR Ambedkar Vidhana Soudha","Cubbon Park Sri Chamarajendra Park","MG Road","Trinity","Halasuru","Indiranagara","Swami Vivekananda Road","Baiyappanahalli"]

def check_me():
    global boarding_station
    global departure_station
    global Green_line
    global Purple_line
    global station_name
    new_window = Toplevel()
    new_window.geometry("500x350")
    new_window.config(bg="Purple")
    new_window.title("Namma Metro Fair Calculator")
    image1 = ImageTk.PhotoImage(Image.open("icon.jpg"))
    new_window.iconphoto(False, image1)
    title1 = Label(new_window, text = "            Namma Metro Fair Calculator",font=("Arial", 20),bg="Purple", fg="White")
    title1.grid(row=1, column=0, columnspan=3)

    if ((boarding_station.get() in Green_line and departure_station.get() in Green_line) or (boarding_station.get() in Purple_line and departure_station.get() in Purple_line)):
        no_of_stops = abs(station_name.index(boarding_station.get()) - station_name.index(departure_station.get())) - 1

    if (boarding_station.get() in Green_line and departure_station.get() in Purple_line):
        no_of_stops = abs( abs(Green_line.index("Majestic") - Green_line.index(boarding_station.get())) + abs(Purple_line.index("Majestic") - Purple_line.index(departure_station.get())) -1 )

    if (boarding_station.get() in Purple_line and departure_station.get() in Green_line):
        no_of_stops = abs( abs(Purple_line.index("Majestic") - Purple_line.index(boarding_station.get())) + abs(Green_line.index("Majestic") - Green_line.index(departure_station.get())) -1 )
    
    if no_of_stops == -1:
        response= messagebox.showwarning("Warning", "The boarding and departure station are the same")
        new_window.destroy()
    if no_of_stops == 0:
        price = 5
    if no_of_stops == 1:
        price = 9
    if no_of_stops == 2:
        price = 14
    if no_of_stops == 3:
        price = 18
    if no_of_stops > 3:
        price = 18 + (no_of_stops - 3)*2
    if departure_station.get() == "Majestic":
        price = price + 1
    
    mylabel6 = Label(new_window, text = "        ",font=("Arial", 15),bg="Purple")
    mylabel6.grid(row=2, column=0)

    boarding_station_label = Label(new_window, text = "          Boarding station : " + boarding_station.get(),font=("Arial", 15),bg="Purple", fg="White")
    boarding_station_label.grid(row=3, column=0)

    mylabel7 = Label(new_window, text = "    ",font=("Arial", 15),bg="Purple")
    mylabel7.grid(row=4, column=0)

    departure_station_label = Label(new_window, text = "          Departure station : " + departure_station.get(),font=("Arial", 15),bg="Purple", fg="White")
    departure_station_label.grid(row=5, column=0)

    mylabel8 = Label(new_window, text = "    ",font=("Arial", 15),bg="Purple")
    mylabel8.grid(row=6, column=0)

    no_of_stops_label = Label(new_window, text = "          No of Stops : " + str(no_of_stops),font=("Arial", 15),bg="Purple", fg="White")
    no_of_stops_label.grid(row=7, column=0)

    mylabel9 = Label(new_window, text = "    ",font=("Arial", 15),bg="Purple")
    mylabel9.grid(row=8, column=0)

    no_of_stops_label = Label(new_window, text = "          Price : " + str(price),font=("Arial", 15),bg="Purple", fg="White")
    no_of_stops_label.grid(row=9, column=0)

    mylabel9 = Label(new_window, text = "    ",font=("Arial", 15),bg="Purple")
    mylabel9.grid(row=10, column=0)

    Back_button = Button(new_window, text="Go Back", command=new_window.destroy, fg="Green", font=("Arial", 15))
    Back_button.grid(row=11, column=0)

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sukesh",
    database="namma_metro"
    )

    mycursor = mydb.cursor()

    sql_command = "INSERT INTO no_of_people (boarding_station, departure_station) VALUES (%s, %s)"
    sql_value = (boarding_station.get(), departure_station.get())
    mycursor.execute(sql_command, sql_value)

    mydb.commit()

def stats():
    stat_window = Toplevel()
    stat_window.geometry("500x350")
    stat_window.config(bg="Purple")
    stat_window.title("Namma Metro Fair Calculator")
    image1 = ImageTk.PhotoImage(Image.open("C:/Users/sukes/Downloads/images.png"))
    stat_window.iconphoto(False, image1)
    title1 = Label(stat_window, text = "            Namma Metro Fair Calculator",font=("Arial", 20),bg="Purple", fg="White")
    title1.grid(row=1, column=0, columnspan=3)

    mylabel9 = Label(stat_window, text = "    ",font=("Arial", 15),bg="Purple")
    mylabel9.grid(row=2, column=0)

    station_stat_label = Label(stat_window, text = "          Enter the station name: ",font=("Arial", 15),bg="Purple", fg="White")
    station_stat_label.grid(row=3, column=0)

    mylabel9 = Label(stat_window, text = "    ",font=("Arial", 15),bg="Purple")
    mylabel9.grid(row=4, column=0)

    station_name = ["All","Nagasandra", "Dasarahalli", "Jalahalli", "Peenya Industry", "Peenya", "Goraguntepalya", "Yeshwanthpur", "Sandal Soap Factory", "Mahalakshmi", "Rajajinagar", "Mahakavi Kuvempu Road", "Srirampura", "Sampige Road", "Majestic", "Chikpete", "Krishna Rajendra Market", "National College", "Lalbagh Botanical Garden", "South End Circle", "Jayanagar", "Rashtreeya Vidyalaya Road", "Banashankari", "Jaya Prakash Nagar", "Yelachenahalli", "Konanakunte Cross", "Doddakallasandra", "Vajarahalli", "Thalaghattapura", "Silk Institute", "Kengeri", "Kengeri Bus Terminal", "Pattanagere", "Jnanabharathi", "Rajarajeshwari Nagar", "Nayandahalli", "Mysuru Road", "Deepanjali Nagara", "Attiguppe", "Vijayanagara", "Balagangadhara Natha Swamiji HOS", "Magadi Road", "City Railway Station", "Majestic","Sir M. Visveshwaraya Station", "Dr BR Ambedkar Vidhana Soudha", "Cubbon Park Sri Chamarajendra Park", "MG Road","Trinity", "Halasuru", "Indiranagara", "Swami Vivekananda Road", "Baiyappanahalli"]

    station_stat = StringVar()
    station_stat.set("All")
    station_stat_dropdown_menu = OptionMenu(stat_window, station_stat, *station_name)
    station_stat_dropdown_menu.config(bg="Purple", fg="WHITE", height=2)
    station_stat_dropdown_menu.grid(row=3, column=1)

    mylabel5 = Label(stat_window, text = " ",font=("Arial", 15),bg="Purple")
    mylabel5.grid(row=5, column=0)

    def acquire_stats():
        acquire_stats_window = Toplevel()
        acquire_stats_window.geometry("500x350")
        acquire_stats_window.config(bg="Purple")
        acquire_stats_window.title("Namma Metro Fair Calculator")
        image1 = ImageTk.PhotoImage(Image.open("C:/Users/sukes/Downloads/images.png"))
        acquire_stats_window.iconphoto(False, image1)
        title1 = Label(acquire_stats_window, text = "            Namma Metro Fair Calculator",font=("Arial", 20),bg="Purple", fg="White")
        title1.grid(row=1, column=0, columnspan=3)

        if station_stat.get() == "All":

            def came_stats():
                came_stats_window = Toplevel()
                came_stats_window.geometry("500x350")
                came_stats_window.config(bg="Purple")
                came_stats_window.title("Namma Metro Fair Calculator")
                image1 = ImageTk.PhotoImage(Image.open("C:/Users/sukes/Downloads/images.png"))
                came_stats_window.iconphoto(False, image1)
                title1 = Label(came_stats_window, text = "            Namma Metro Fair Calculator",font=("Arial", 20),bg="Purple", fg="White")
                title1.grid(row=1, column=0, columnspan=3)

                mylabel9 = Label(came_stats_window, text = "    ",font=("Arial", 15),bg="Purple")
                mylabel9.grid(row=2, column=0)

                station_stat_label = Label(came_stats_window, text = "          No of people came to the station ",font=("Arial", 15),bg="Purple", fg="White")
                station_stat_label.grid(row=3, column=0)

                mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="sukesh",
                database="namma_metro"
                )

                mycursor = mydb.cursor()
                mycursor.execute("select departure_station, count(*) as count FROM no_of_people GROUP BY departure_station")

                i=0 
                for no_of_people in mycursor: 
                    for j in range(len(no_of_people)):
                        e = Entry(came_stats_window, width=20, fg='White', bg="Purple", font=("Arial", 15))
                        e.grid(row=i+4, column=j) 
                        e.insert(END, no_of_people[j])
                    i=i+1
            
            def left_stats():
                left_stats_window = Toplevel()
                left_stats_window.geometry("500x350")
                left_stats_window.config(bg="Purple")
                left_stats_window.title("Namma Metro Fair Calculator")
                image1 = ImageTk.PhotoImage(Image.open("C:/Users/sukes/Downloads/images.png"))
                left_stats_window.iconphoto(False, image1)
                title1 = Label(left_stats_window, text = "            Namma Metro Fair Calculator",font=("Arial", 20),bg="Purple", fg="White")
                title1.grid(row=1, column=0, columnspan=3)

                mylabel9 = Label(left_stats_window, text = "    ",font=("Arial", 15),bg="Purple")
                mylabel9.grid(row=2, column=0)

                station_stat_label = Label(left_stats_window, text = "          No of people left to the station ",font=("Arial", 15),bg="Purple", fg="White")
                station_stat_label.grid(row=3, column=0)

                mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="sukesh",
                database="namma_metro"
                )

                mycursor = mydb.cursor()
                mycursor.execute("select boarding_station, count(*) as count FROM no_of_people GROUP BY boarding_station")

                i=0 
                for no_of_people in mycursor: 
                    for j in range(len(no_of_people)):
                        e = Entry(left_stats_window, width=20, fg='White', bg="Purple", font=("Arial", 15))
                        e.grid(row=i+4, column=j) 
                        e.insert(END, no_of_people[j])
                    i=i+1

            mylabel9 = Label(acquire_stats_window, text = "    ",font=("Arial", 15),bg="Purple")
            mylabel9.grid(row=2, column=0)

            station_stat_label = Label(acquire_stats_window, text = "          No of people came to the station ",font=("Arial", 15),bg="Purple", fg="White")
            station_stat_label.grid(row=3, column=0)

            btn = Button(acquire_stats_window, text="Give Stats", command=came_stats, fg="Green", font=("Arial", 15))
            btn.grid(row=3, column=1)

            mylabel9 = Label(acquire_stats_window, text = "    ",font=("Arial", 15),bg="Purple")
            mylabel9.grid(row=4, column=0)

            station_stat_label = Label(acquire_stats_window, text = "          No of people left to the station ",font=("Arial", 15),bg="Purple", fg="White")
            station_stat_label.grid(row=5, column=0)

            btn = Button(acquire_stats_window, text="Give Stats", command=left_stats, fg="Green", font=("Arial", 15))
            btn.grid(row=5, column=1)
        
        if station_stat.get() != "All":
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sukesh",
            database="namma_metro"
            )

            mycursor = mydb.cursor()

            sql_command = "select count(departure_station) from no_of_people where departure_station = %s"
            sql_value = [station_stat.get()]
            mycursor.execute(sql_command, sql_value)

            i=0 
            for no_of_people in mycursor: 
                for j in range(len(no_of_people)):
                    demo_window = Toplevel()
                    e = Entry(demo_window, width=20, fg='White', bg="Purple", font=("Arial", 15))
                    e.grid(row=i+4, column=j) 
                    e.insert(END, no_of_people[j])
                    demo_window.destroy()
                i=i+1

            mylabel5 = Label(acquire_stats_window, text = " ",font=("Arial", 15),bg="Purple")
            mylabel5.grid(row=2, column=0)

            station_stat_label = Label(acquire_stats_window, text = "           No of people left to "+station_stat.get()+" are "+ str(no_of_people[0]),font=("Arial", 15),bg="Purple", fg="White")
            station_stat_label.grid(row=3, column=0)

            sql_command = "select count(boarding_station) from no_of_people where boarding_station = %s"
            sql_value = [station_stat.get()]
            mycursor.execute(sql_command, sql_value)

            i=0 
            for no_of_people in mycursor: 
                for j in range(len(no_of_people)):
                    demo_window = Toplevel()
                    e = Entry(demo_window, width=20, fg='White', bg="Purple", font=("Arial", 15))
                    e.grid(row=i+4, column=j) 
                    e.insert(END, no_of_people[j])
                    demo_window.destroy()
                i=i+1

            mylabel5 = Label(acquire_stats_window, text = " ",font=("Arial", 15),bg="Purple")
            mylabel5.grid(row=4, column=0)

            station_stat_label = Label(acquire_stats_window, text = "           No of people came to "+station_stat.get()+" are "+ str(no_of_people[0]),font=("Arial", 15),bg="Purple", fg="White")
            station_stat_label.grid(row=5, column=0)

            

    btn = Button(stat_window, text="Give Stats", command=acquire_stats, fg="Green", font=("Arial", 15))
    btn.grid(row=8, column=1)


mylabel5 = Label(root, text = " ",font=("Arial", 15),bg="Purple")
mylabel5.grid(row=5, column=0)

btn = Button(root, text="Results !!", command=check_me, fg="Green", font=("Arial", 15))
btn.grid(row=6, column=1)

mylabel5 = Label(root, text = " ",font=("Arial", 15),bg="Purple")
mylabel5.grid(row=7, column=0)

btn = Button(root, text="Stats", command=stats, fg="Green", font=("Arial", 15))
btn.grid(row=8, column=1)

root.mainloop()