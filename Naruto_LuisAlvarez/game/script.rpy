# You can place the script of your game in this file.
# - Puedes colocar el 'script' de tu juego en este archivo.

# Declare images below this line, using the image statement.
# - Declara imágenes bajo esta línea, usando 'image' como
#   en el ejemplo.
# eg. image eileen happy = "eileen_happy.png"
image bg kono1 = "images/kono1.jpg"
image bg kono2 = "images/kono2.png"
image bg tro = "images/tronco.jpg"
image bg kak4 = "images/kak4.jpg"
image bg nar1 = "images/nar1.png"
image bg sasu1 = "images/sasu1.png"
image bg kak1 = "images/kak2.png"
image bg nar2 = "images/nar2.png"
image bg sasu2 = "images/sasu2.png"
image bg kak2 = "images/kaka2.png"
image bg nar3 = "images/nar3.png"
image bg sasu3 = "images/sasu3.png"
image bg kak3 = "images/kaka3.png"
image bg kak5 = "images/kaka7.png"
# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el 
#   ejemplo.
define n = Character("Naruto")
define s = Character("Sasuke")
define k = Character("Kakashi")
define x = Character("Narrador")
# The game starts here.
# - El juego comienza aquí.
label start:
    play music "images/kana.ogg"
    scene bg kono1
    x "Hola, yo soy el narrador, les contare la historia sobre la batalla de Naruto y Sasuke contra Kakashi"
    x"Sasuke y Naruto se encontaron en algun sitio de Konoka"
    show nar1
    n"Hey, Sasuke"
    show sasu1 at right
    s"Naruto"
    n"¿Como estas?"
    s"Eso no es de tu incumbencia"
    n"Hey, vamos a entrenar con Kakashi-sensei!!!"
    s"Con Kakashi?"
    n"Si!!!
    Hace tiempo no entrenamos con el
    ¿Quieres ir?"
    s"ah(Suspiro), Ok vamos"
    hide nar1
    hide sasu1
    scene bg kono2
    show kak1
    show nar1 at left
    show sasu1 at right
    n"Hey, ahi esta Kakashi-sensei"
    s"..."
    k"oh, hola"
    hide nar1
    show nar2 at left
    n"basta de formalidades"
    n"Queremos luchar contra ti"
    k"oh, creo que no me aceptaras un no"
    hide kak1
    show kak2
    k"OK,empecemos!!"
    hide sasu1
    show sasu2 at right
    s"Naruto, preparate"
    n"SI!!"
    s"Yo atacare primero, preparate"
    n"Vamos!!!"
    s"Preparate, Kakashi"
    k"(Tendre que tener cuidado, estos dos habran ideado un plan"
    hide sasu2
    hide nar2
    hide kak2
    show sasu3
    s"CHIDORI"
    hide sasu3
    show kak4
    k"ugh!!!"
    show sasu2 at right
    hide kak6
    scene bg tro
    s"desaparecio"
    scene bg kono2
    show kak3 at right
    s"Esta atras de mi, (lo que me esperaba)"
    s"Ahora Naruto"
    k"¿¿QUE??"
    show nar3 at left
    n"RASENGAN"
    hide nar3
    hide kak2
    hide kak3
    show kak4
    k"ugh!!!"
    n"Le di!!"
    hide kak4
    show kak5
    k"Estoy muy feliz de progreso, Naruto-Sasuke"
    
    stop music 
    return
    
    
    
        
