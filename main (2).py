import time
import turtle

while True:
  total_seconds=round(time.time())
  current_second=round(total_seconds%60)
                    
  current_minute=round((total_seconds//60)%60)
  #current_minute
  current_hour=round(total_seconds//3600)%12
  est_hour=round((current_hour-4)%12)

  time.sleep(1)

 


  #calculate times
  
  
  #Draw clock circle and format turtle
  t = turtle
  t.hideturtle()
  t.pensize(10)
  t.speed(100)
  t.penup()
  t.goto(0, 0)
  t.setheading(0)
  t.pendown()
  t.circle(50)
  t.left(90)
  t.penup()
  t.forward(50)
  t.pendown()
  #Draw hour hand
  t.right(30*est_hour)
  t.pensize(5)
  t.forward(30)
  t.back(30)
  t.left(30*est_hour)
          
  t.pencolor("black")
  #Draw minute hand
  t.right(6*est_hour)
  t.pensize(3)
  t.forward(40)
  t.back(40)
  t.left(6*current_minute)

  #Draw second hand
  t.pensize(1)
  t.pencolor("red")
  t.right(6*current_second)
  t.forward(40)
  t.back(40)
  t.left(6 * current_second)
          
  #Print time
  t.penup()
  t.goto(-20, -20)
  t.pencolor("black")
  #Uncomment the lines below once you define the time variables.
  turtle.write(str(est_hour) + ":"+ str(current_minute) + ":"+ str(current_second))
  time.sleep(1)
  turtle.clear()
 