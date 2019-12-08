plan = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
p = ["x","o"]
t = 0
def kordinat(x,y):
  return plan[x + (y*7)]
game = True
pw = [0,0]
while game:
  for i in range(0,6):
    gfx = "|".join(plan[((5-i)*7):(7+((5-i)*7))])
    print("|"+gfx+"|")
  print("----------------")
  print(" 1 2 3 4 5 6 7")
  for e in range(0,2):
    for x in range(0,7):
      for y in range(0,3):
        if kordinat(x,y) == p[e]and kordinat(x,(y+1)) == p[e] and kordinat(x,(y+2)) == p[e] and kordinat(x,(y+3)) == p[e]:
          pw[e] = 1
    for x in range(0,4):
      for y in range(0,6):
        if plan[x+y*7] == p[e] and plan[x+1+y*7] == p[e] and plan[x+2+y*7] == p[e] and plan[x+3+y*7] == p[e]:
          pw[e] = 1
      for y in range(0,3):
        if plan[x+y*7] == p[e] and plan[x+1+(y+1)*7] == p[e] and plan[x+2+(y+2)*7] == p[e] and plan[x+3+(y+3)*7] == p[e]:
          pw[e] = 1
        if plan[6-x+y*7] == p[e] and plan[5-x+(y+1)*7] == p[e] and plan[4-x+(y+2)*7] == p[e] and plan[3-x+(y+3)*7] == p[e]:
          pw[e] = 1
  for i in range(0,2):
    if pw[i] == 1:
      game = False
  full = True
  for i in range(0,42):
    if plan[i] == " ":
      full = False
  if full:
    game = False
  tur = True
  if game:
    while tur:
      print("spelare",(t+1))
      drag = input()
      if drag == "1":
        for i in range(0,6):
          if plan[i*7+0] == " " and tur:
            plan[i*7+0] = p[t]
            tur = False
      if drag == "2":
        for i in range(0,6):
          if plan[i*7+1] == " " and tur:
            plan[i*7+1] = p[t]
            tur = False
      if drag == "3":
        for i in range(0,6):
          if plan[i*7+2] == " " and tur:
            plan[i*7+2] = p[t]
            tur = False
      if drag == "4":
        for i in range(0,6):
          if plan[i*7+3] == " " and tur:
            plan[i*7+3] = p[t]
            tur = False
      if drag == "5":
        for i in range(0,6):
          if plan[i*7+4] == " " and tur:
            plan[i*7+4] = p[t]
            tur = False
      if drag == "6":
        for i in range(0,6):
          if plan[i*7+5] == " " and tur:
            plan[i*7+5] = p[t]
            tur = False
      if drag == "7":
        for i in range(0,6):
          if plan[i*7+6] == " " and tur:
            plan[i*7+6] = p[t]
            tur = False
  if t == 0:
    t = 1
  else:
    t = 0    
for i in range(0,2):
  if pw[i] == 1:
    print("Spelare",(i+1),"har vunnit")
    for i in range(0,10):
      print(" ")
drag = input()
