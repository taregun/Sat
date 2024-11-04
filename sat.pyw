import turtle 
from datetime import datetime
import winsound
import requests
import calendar

response = requests.get('https://ipinfo.io/json')
turtle.speed(0)
turtle.hideturtle()
turtle.penup()
turtle.goto(0, 0)
turtle.tracer(0)  
turtle.bgcolor("turquoise")
turtle.title("Sat")
screen=turtle.Screen()
screen.setup(width=1.0, height=1.0)

def draw_hour_markers():
    turtle.pensize(10)
    turtle.pencolor("BLACK") 
    for hour in range(12):
        angle = hour * 30
        turtle.penup()
        turtle.goto(0, 0)
        turtle.setheading(90 - angle) 
        turtle.forward(300) 
        turtle.pendown()
        turtle.forward(20)  
        turtle.penup()
        turtle.goto(0, 0)
        turtle.setheading(90 - angle)
        turtle.forward(260)  
        turtle.pendown()
        turtle.write(str(hour if hour != 0 else 12), align="center", font=("Comic Sans MS", 18, "normal"))
        turtle.penup()
        turtle.goto(0, 0)

def draw_second_markers():
    turtle.pensize(2) 
    turtle.pencolor("BLACK")  
    for second in range(60):  
        angle = second * 6 
        turtle.penup()
        turtle.goto(0, 0)
        turtle.setheading(90 - angle) 
        turtle.forward(310) 
        turtle.pendown()
        turtle.forward(10)  
        turtle.penup()
        turtle.goto(0, 0) 

def get_season(month):
    if month in [12, 1, 2]:
        return "Zima"
    elif month in [3, 4, 5]:
        return "Proljeće"
    elif month in [6, 7, 8]:
        return "Ljeto"
    elif month in [9, 10, 11]:
        return "Jesen"
    else:
        return "Nevažeći mjesec"
    

def time_until_new_year():
    now = datetime.now()
    new_year = datetime(now.year + 1, 1, 1)
    
    time_difference = new_year - now
    
    months = (new_year.year - now.year) * 12 + (new_year.month - now.month)
    days = time_difference.days
    total_seconds = time_difference.total_seconds()

    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)
 
    days_in_months = [31, 28 + (1 if (now.year % 4 == 0 and (now.year % 100 != 0 or now.year % 400 == 0)) else 0), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_hours = 0

    for month in range(now.month, 12):
        total_hours += days_in_months[month] * 24

    total_hours += days * 24
 
    total_hours += hours
    
    return total_hours, minutes, seconds



def draw_mini_calendar(year, month, current_day):
    turtle.penup()
    turtle.goto(500, 350) 
    turtle.pendown()
    turtle.pencolor("black")
    turtle.write(f"{months[month - 1]} {year}", align="center", font=("Comic Sans MS", 20, "bold")) 
    
    month_days = calendar.monthcalendar(year, month)
    day_labels = ["P", "U", "S", "Č", "P", "S", "N"]
    turtle.penup()
    for i, label in enumerate(day_labels):
        turtle.goto(500 + i * 40, 310) 
        turtle.write(label, align="center", font=("Comic Sans MS", 16, "bold"))  

    for week_num, week in enumerate(month_days):
        for day_num, day in enumerate(week):
            turtle.goto(500 + day_num * 40, 280 - week_num * 40)
            if day == 0:
                continue 
            if day == current_day:
                turtle.pencolor("red")  
            else:
                turtle.pencolor("black")
            turtle.write(day, align="center", font=("Comic Sans MS", 16, "normal")) 

previous_second = -1

while True:
    data = response.json()
    now = datetime.now() 
    turtle.clear()
    draw_hour_markers()
    draw_second_markers()
    year = now.year
    month = now.month
    day = now.day
    date=datetime(year,month,day)
    dayOfWeek=date.weekday()
    days=["Ponedjeljak","Utorak","Srijeda","Četvrtak","Petak","Subota","Nedjelja"]
    months=["Januar","Februar","Mart","April","Maj","Juni","Juli","Avgust","Septembar","Oktobar","Novembar","Decembar"]


    now = datetime.now()
    current_second = now.second
    if current_second != previous_second:
        winsound.Beep(1000, 20)
        previous_second = current_second
    HOUR = now.hour
    MINUTE = now.minute
    SECOND = (now.microsecond/1000000)+now.second
    newsec=int(SECOND)

    day_part=datetime.now()
    day_part=day_part.strftime("%p")
    if day_part=="AM":
        day_part="prije podne"
    else:
        day_part="poslije podne"
    
    secondDegres = (SECOND / 60) * 360
    minuteDegres = (MINUTE / 60) * 360 + (secondDegres / 60)
    hourDegres = (HOUR / 12) * 360 + (minuteDegres / 12)

    hours_to_new_year, minutes_to_new_year, seconds_to_new_year = time_until_new_year()

    date_str = f"{day:02d}.{month:02d}.{year}."
    turtle.goto(-80, 100)
    turtle.pencolor("black")
    turtle.write(date_str, font=("Comic Sans MS", 24, "normal"))

    date_str = f"{HOUR}.{MINUTE}.{int(SECOND)}."
    turtle.goto(-50, -100)
    turtle.pencolor("black")
    turtle.write(date_str, font=("Comic Sans MS", 24, "normal"))

    date_str = f"-Dan u sedmici: {days[dayOfWeek]}"
    turtle.goto(-780, 375)
    turtle.pencolor("black")
    turtle.write(date_str, font=("Comic Sans MS", 24, "normal"))

    date_str = f"-Dio dana: {day_part}"
    turtle.goto(-780, 325)
    turtle.pencolor("black")
    turtle.write(date_str, font=("Comic Sans MS", 24, "normal"))

    date_str = f"-Godišnje doba: {get_season(month)}"
    turtle.goto(-780, 275)
    turtle.pencolor("black")
    turtle.write(date_str, font=("Comic Sans MS", 24, "normal"))

    date_str = f"-Mjesec: {months[month - 1]}"
    turtle.goto(-780, 225)
    turtle.pencolor("black")
    turtle.write(date_str, font=("Comic Sans MS", 24, "normal"))

    turtle.goto(-780, 175)
    turtle.pencolor("black")
    turtle.write("-----------------------------", font=("Comic Sans MS", 24, "normal"))

    turtle.goto(-780, 125)
    turtle.pencolor("black")
    turtle.write("-Nova godina za:", font=("Comic Sans MS", 24, "normal"))

    turtle.goto(-780, 75)
    turtle.pencolor("black")
    turtle.write(f"  -{hours_to_new_year} sati,", font=("Comic Sans MS", 24, "normal"))

    turtle.goto(-780, 25)
    turtle.pencolor("black")
    turtle.write(f"  -{minutes_to_new_year} minuta,", font=("Comic Sans MS", 24, "normal"))

    turtle.goto(-780, -25)
    turtle.pencolor("black")
    turtle.write(f"  -{seconds_to_new_year+1} sekundi,", font=("Comic Sans MS", 24, "normal"))

    turtle.goto(-780, -75)
    turtle.pencolor("black")
    turtle.write("-----------------------------", font=("Comic Sans MS", 24, "normal"))

    date_str = f"-Vremenska zona:"
    turtle.goto(-780, -125)
    turtle.pencolor("black")
    turtle.write(date_str, font=("Comic Sans MS", 24, "normal"))

    date_str = f"  -{data['timezone']}"
    turtle.goto(-780, -175)
    turtle.pencolor("black")
    turtle.write(date_str, font=("Comic Sans MS", 24, "normal"))

    turtle.goto(-780, -225)
    turtle.pencolor("black")
    turtle.write("-----------------------------", font=("Comic Sans MS", 24, "normal"))

    date_str = f"-Entitet: "
    turtle.goto(-780, -275)
    turtle.pencolor("black")
    turtle.write(date_str, font=("Comic Sans MS", 24, "normal"))

    date_str = f"  -{data['region']}"
    turtle.goto(-780, -325)
    turtle.pencolor("black")
    turtle.write(date_str, font=("Comic Sans MS", 24, "normal"))


    date_str = f"{data['city']}"
    turtle.goto(-125, 325)
    turtle.pencolor("gray")
    turtle.write(date_str, font=("Comic Sans MS", 60, "normal"))
    turtle.goto(-130, 330)
    turtle.pencolor("black")
    turtle.write(date_str, font=("Comic Sans MS", 60, "normal"))

    draw_mini_calendar(year, month, day)

    date_str = f"{int(SECOND)}"
    turtle.goto(510, -340)
    turtle.pencolor("gray")
    turtle.write(date_str, font=("Comic Sans MS",150, "normal"))
    turtle.goto(500, -330)
    turtle.pencolor("black")
    turtle.write(date_str, font=("Comic Sans MS",150, "normal"))
    

    turtle.pencolor("black")
    turtle.pensize(10)
    turtle.penup()
    turtle.goto(0,0)
    turtle.setheading(90 - hourDegres)
    turtle.pendown()
    turtle.backward(50)
    turtle.pensize(5)
    turtle.forward(200)  
    turtle.penup()
    turtle.goto(0, -5)

    turtle.pencolor("BLACK")
    turtle.pensize(7)
    turtle.setheading(90 - minuteDegres)
    turtle.pendown()
    turtle.forward(250)  
    turtle.penup()
    turtle.goto(0,0)
    
    turtle.pencolor("RED")
    turtle.pensize(2)
    turtle.setheading(90 - secondDegres)
    turtle.pendown()
    turtle.forward(300) 
    turtle.forward(-380)
    turtle.pensize(6)
    turtle.goto(0,0)
    turtle.penup()
    turtle.goto(0, 0)

    turtle.update() 
    turtle.delay(1000)  