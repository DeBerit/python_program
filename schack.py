# pjäser:
vit = ["B", "T", "S", "L", "D", "K", "*"]
svart = ["b", "t", "s", "l", "d", "k", "*"]
bräde = [] # kordinatsystemet
hot = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # information om punkter i kordinatsystem
tur = 0
game = True
vitvinst = False
svartvinst = False
for i in range(0, 64): # Blankt kordinatsystem
    bräde.append(" ")


def kordinatbli(bli, x, y): # Kordinaten blir en sak
    global bräde
    bräde[x + (y * 8)] = bli


def kordinatär(x, y):# Vad är på på kordinaten
    return bräde[x + (y * 8)]


def hotad(x, y): 
    if hot[x + (y * 8)] != 0:
        return True
    else:
        return False


def snäll(spelare, x, y):
    if spelare == 1:
        for i in range(0, 6):
            if svart[i] == kordinatär(x, y):
                return True
    if spelare == 0:
        for i in range(0, 6):
            if vit[i] == kordinatär(x, y):
                return True


def tom(x, y):
    if kordinatär(x, y) == " ":
        return True


def pjäshitta(pjäs, spelare, x, y):
    if spelare == 0:
        pjäs = pjäs.upper()
    if kordinatär(x, y) == pjäs:
        return True
    else:
        return False


def hota(x, y):
    global hot
    global tur
    if (x + (y * 8)) >= 0 and (x + (y * 8)) < 64:
        if not snäll(tur, x, y):
            hot[x + (8 * y)] == 1
            return True
        else:
            return False
    else:
        return False


def raklinje(x, y, fx, fy): # jajhsajjdhs
    loop = True
    while loop:
        x = x + fx
        y = y + fy
        if tom(x, y):
            if not hota(x, y):
                loop = False
        else:
            hota(x, y)
            loop = False


def gå(pjäsx, pjäsy, målx, måly):
    if kordinatär == "*":
        if tur == 0:
            kordinatbli(" ", målx, måly - 1)
        if tur == 1:
            kordinatbli(" ", målx, måly + 1)
    kordinatbli(kordinatär(pjäsx, pjäsy), målx, måly)
    kordinatbli(" ", pjäsx, pjäsy)


def fårgå(spelare, pjäsx, pjäsy, målx, måly):
    if hotad(målx, måly) and not snäll(spelare, målx, måly):
        gå(pjäsx, pjäsy, målx, måly)
        return True


def drag(promt):
    a = input(promt)
    if a == "1" or a == "a":
        return 0
    elif a == "2" or a == "b":
        return 1
    elif a == "3" or a == "c":
        return 2
    elif a == "4" or a == "d":
        return 3
    elif a == "5" or a == "e":
        return 4
    elif a == "6" or a == "f":
        return 5
    elif a == "7" or a == "g":
        return 6
    elif a == "8" or a == "h":
        return 7
    else:
        return "NEJ"


def springare(x, y):
    hota(x + 2, y + 1)
    hota(x + 1, y + 2)
    hota(x - 2, y + 1)
    hota(x - 1, y + 2)
    hota(x + 2, y - 1)
    hota(x + 1, y - 2)
    hota(x - 2, y - 1)
    hota(x - 1, y - 2)


def löpare(x, y):
    raklinje(x, y, 1, 1)
    raklinje(x, y, -1, 1)
    raklinje(x, y, 1, -1)
    raklinje(x, y, -1, -1)


def torn(x, y):
    raklinje(x, y, 1, 0)
    raklinje(x, y, 0, 1)
    raklinje(x, y, -1, 0)
    raklinje(x, y, 0, -1)


def bondegå(x, y):
    pass


def bondehota(x, y):
    pass


def dam(x, y):
    torn(x, y)
    löpare(x, y)


def kung(x, y):
    hota(x+1, y+1)
    hota(x+1, y-1)
    hota(x-1, y+1)
    hota(x-1, y-1)
    hota(x+1, y)
    hota(x-1, y)
    hota(x, y+1)
    hota(x, y-1)


while game:
    for y in range(0, 8):
        gfx = " | ".join(bräde[8 * y:8 + (8 * y)])
        print("| " + gfx + " |")
        print("---------------------------------")
    for i in range(0, 64):
        hot[i] = 0
    turklar = False
    rörd = False
    while not turklar:
        pjäsx = drag("x")
        pjäsy = drag("y")
        # drag 
        if pjäshitta("s", tur, pjäsx, pjäsy):
            springare(pjäsx, pjäsy)
            for i in range(0, 64):
                if hot[i] != 0:
                    rörd = True
            while rörd:
                målx = drag("x")
                måly = drag("y")
                if fårgå(tur, pjäsx, pjäsy, målx, måly):
                    rörd = False
                    turklar = True
        if pjäshitta("l", tur, pjäsx, pjäsy):
            löpare(pjäsx, pjäsy)
            for i in range(0, 64):
                if hot[i] != 0:
                    rörd = True
            while rörd:
                målx = drag("x")
                måly = drag("y")
                if fårgå(tur, pjäsx, pjäsy, målx, måly):
                    rörd = False
                    turklar = True
        if pjäshitta("t", tur, pjäsx, pjäsy):
            torn(pjäsx, pjäsy)
            for i in range(0, 64):
                if hot[i] != 0:
                    rörd = True
            while rörd:
                målx = drag("x")
                måly = drag("y")
                if fårgå(tur, pjäsx, pjäsy, målx, måly):
                    rörd = False
                    turklar = True
        if pjäshitta("d", tur, pjäsx, pjäsy):
            dam(pjäsx, pjäsy)
            for i in range(0, 64):
                if hot[i] != 0:
                    rörd = True
            while rörd:
                målx = drag("x")
                måly = drag("y")
                if fårgå(tur, pjäsx, pjäsy, målx, måly):
                    rörd = False
                    turklar = True
        if pjäshitta("b", tur, pjäsx, pjäsy):
            bondegå(pjäsx, pjäsy)
            for i in range(0, 64):
                if hot[i] != 0:
                    rörd = True
            while rörd:
                målx = drag("x")
                måly = drag("y")
                if fårgå(tur, pjäsx, pjäsy, målx, måly):
                    rörd = False
                    turklar = True