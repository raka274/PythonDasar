import turtle

# Setup Layar
s = turtle.Screen()
s.bgcolor("white")
t = turtle.Turtle()
t.speed(3)
t.pensize(2)

def pindah(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def perisai_luar():
    """Menggambar bingkai segi lima biru"""
    pindah(-70, 50)
    t.color("#003399") # Biru Tua
    t.begin_fill()
    t.forward(140)  # Atas
    
    t.right(45)
    t.forward(100)  # Kanan atas
    t.right(90)
    t.forward(100)  # Kanan bawah (menuju lancip)
    # Membuat sudut bawah lancip
    curr_pos = t.pos()
    t.goto(0, -120) 
    t.goto(curr_pos[0]*-1, curr_pos[1])
    t.goto(-70, 50)
    t.end_fill()

def roda_gerigi():
    """Simbol teknik/industri"""
    pindah(0, -30)
    t.color("white")
    t.pensize(4)
    # Lingkaran tengah
    t.circle(40)
    
    # Gerigi sederhana
    for i in range(12):
        t.penup()
        t.circle(40, 30)
        t.pendown()
        t.forward(10)
        t.backward(10)

def buku_terbuka():
    """Simbol pendidikan di tengah"""
    pindah(-30, 0)
    t.color("yellow")
    t.begin_fill()
    # Sayap kiri
    t.setheading(160)
    t.forward(40)
    t.right(70)
    t.forward(30)
    t.right(110)
    t.forward(40)
    # Sayap kanan
    t.setheading(20)
    t.forward(40)
    t.left(70)
    t.forward(30)
    t.left(110)
    t.forward(40)
    t.end_fill()

def tulisan():
    pindah(0, -160)
    t.color("black")aadawsa 
    t.write("PRESTASI PRIMA", align="center", font=("Arial", 14, "bold"))

# Eksekusi Gambar
perisai_luar()
roda_gerigi()
buku_terbuka()
tulisan()

t.hideturtle()
turtle.done()