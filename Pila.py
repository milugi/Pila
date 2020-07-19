from tda_pila import Pila, pilaint, pilastring, barrido_pila, pila_vacia, apilar, desapilar, cima, tamanio_pila, ordenar
import random

pila = Pila()
p = Pila()

pila_n = Pila()
pilaint(pila_n, 5)
print('Pila de numeros enteros')
barrido_pila(pila_n)
print('')

pila_car = Pila()
pilastring(pila_car, 5)
print('Pila de caracteres')
barrido_pila(pila_car)
print('')

#1

def cont_ocurrencias(pila, oc):
    c = 0
    aux = 0
    pila_auxiliar = Pila()
    while not pila_vacia(pila):
        aux = desapilar(pila)
        if oc == aux:
            c +=1
        apilar(pila_auxiliar, aux)
    while not pila_vacia (pila_auxiliar):
        if c == 0:
            print('No existe el elemento ingresado en la pila')
        else:
            print('La cantidad de ocurrencias en la pila es de ' + str(c))

#2

def pila_par(pila):
    paux = Pila()
    aux = 0
    while not pila_vacia(pila):
        aux = desapilar(pila)
        if aux % 2 == 0:
            apilar (paux, aux)
    while not pila_vacia(paux):
        apilar(pila,desapilar(paux))
    print('La pila con numeros pares es: ') 
    barrido_pila(pila)

#3

def remplazar (pila, oc):
    c = 0
    aux = 0
    paux = Pila()
    while not pila_vacia(pila):
        aux = desapilar(pila)
        if oc == aux:
            c += 1
            aux == input('Ingrese una caracter para reemplazar  ')
        apilar(paux, aux)
    while not pila_vacia (paux):
        apilar(pila, desapilar(paux))
    if c == 0:
        print('El elemento no se encuentra en la pila')

#ej4

def invertir_pila(pila):
    pila_auxiliar = Pila()
    while not pila_vacia(pila):
        apilar(pila_auxiliar, desapilar(pila))
    print('La pila invertida es: ')
    barrido_pila(pila_auxiliar)

#ej5

def palindromo(palabra):
    pila = Pila()
    aux = len(palabra)
    palabra_auxiliar = ''
    for i in range (0, aux):
        c = palabra[i]
        apilar(pila, c)
    while not pila_vacia(pila):
        palabra_auxiliar= palabra_auxiliar + desapilar(pila)
    if palabra == palabra_auxiliar:
        print('es palindromo')

#ej6

def inversa (palabra):
    pila = Pila()
    aux = len (palabra)
    palabra_auxiliar = ''
    for i in range (0, aux):
        c = palabra[i]
        apilar(pila, c)
    while not pila_vacia(pila):
        palabra_auxiliar = palabra_auxiliar + desapilar(pila)
    print(palabra_auxiliar)

#7

def iesimo (pila, pos):
    paux = Pila()
    for i in range (0, pos):
        apilar(paux, desapilar(pila))
    desapilar(pila)
    while not pila_vacia(paux):
        apilar(pila, desapilar(paux))

#ej8

p = Pila()
pila_copa = Pila()
pila_oro = Pila()
pila_basto = Pila()
pila_espada = Pila()
cartas = ['Copa', 'Oro', 'Basto', 'Espada']

def naipes(p, pila_basto, pila_copa, pila_espada, pila_oro, cartas):
    for i in range(1,40):
        n = random.randint(1,13)
        cartas = random.choice (cartas)
        apilar(p,[n,cartas])
    while not pila_vacia(p):
        aux = desapilar(p)
        if aux[1] == "Oro":
            apilar(pila_oro, aux)
        if aux[1] == "Espada":
            apilar(pila_espada, aux)
        if aux[1] == "Basto":
            apilar(pila_basto, aux)
        if aux[1] == "Copa":
            apilar(pila_copa, aux)

    barrido_pila(pila_oro)
    print("Mazo de Espada: ")
    barrido_pila(pila_espada)
    print("Mazo de Basto: ")
    barrido_pila(pila_basto)
    print("Mazo de Copa: ")
    barrido_pila(pila_copa)
    print("Mazo de Oro: ")

pila_copa = ordenar(pila_copa)
print("Mazo de Copa ordenado: ")
barrido_pila(pila_copa)

#9

def ej_factorial(n):
    pila = Pila()
    aux = 1
    for i in range (1, n + 1):
        apilar(pila, i)
    while not pila_vacia(pila):
        aux  = aux * desapilar(pila)
    print('Factorial del numero ingresado: ', str(aux))

#10 ''inserta en la iesima posicion''

def insertar_atenea():
    pila = Pila()
    pila_dioses = ['Hades', 'Artemisa', 'Apolo', 'Zeus','Ares', 'Hebe', 'Heracles', 'Dionisio']
    pila_aux = Pila()
    pos = 2
    for i in range (0,9):
        apilar(pila, pila_dioses[i])
    print('Pila de dioses griegos: ')
    barrido_pila(pila)
    if tamanio_pila(pila) > (pos + 1):
        i = 0
        while i < pos:
            m = desapilar(pila)
            apilar(pila_aux, m)
            i += 1
        m = apilar(pila, 'Atenea')
        while not pila_vacia(pila_aux):
            apilar(pila, desapilar(pila_aux))
        barrido_pila(pila)
        print('Atenea se inserto en la posicion ', pos)

#Ej11

def cant_vocale(pila):
    cont = 0
    while not pila_vacia:
        m = desapilar(pila)
        if m == 'A' or m == 'a' or m == 'E' or m == 'e' or m == 'I' or m == 'i' or m == 'O' or m == 'o' or m == 'U' or m == 'u':
            cont += 1
    print('La cantidad de vocales en la pila es : ', cont)

#ej12

def buscar_personajes():
    pila = Pila()
    pila_auxiliar = Pila()
    Leia_Organa = False
    Boba_Fett = False
    personajes_sw = ['Leia Organa','Yoda', 'Palpatine','C-3po', 'Darth Maul', 'Darth Vader', 'Luke Skywalker','Chewbacca']
    for i in range (0,9):
        star_w = random.choice(personajes_sw)
        apilar(pila, star_w)
    while not pila_vacia(pila):
        m = desapilar(pila)
        if m == 'Leia Organa':
            apilar(pila_auxiliar, m)
            Leia_Organa = True
        if m == 'Boba Fett':
            apilar(pila_auxiliar,m)
            Boba_Fett = True
    while not pila_vacia (pila_auxiliar):
        apilar(pila, desapilar(pila_auxiliar))
    if Leia_Organa == True:
        print('Leia Organa existe en la pila de personajes')
    if Boba_Fett == True :
        print ('Boba Fett existe en la pila de personajes')

#Ej 13

def ordenar_pila():
    pila = Pila ()
    pila_auxiliar = Pila()
    while not pila_vacia(pila):
        dato = random.randint(1,50)
        if not pila_vacia (pila):
            while not pila_vacia(pila) and cima(pila)>= dato:
                apilar(pila_auxiliar, desapilar(pila))
            apilar(pila, dato)
            while not pila_vacia(pila_auxiliar):
                apilar(pila,desapilar(pila_auxiliar))
            barrido_pila(pila)

#ej14

def ord_quicksort(vec, pri, ult):
    pila = Pila()
    apilar(pila, [pri, ult])
    datos = []
    while not pila_vacia(pila):
        datos = desapilar(pila)
        i = datos[0]
        j = datos[1] - 1
        pivot = datos[1]
        while i < j:
            while vec[i] <= vec[pivot] and i < j:
                i += 1
            while vec[j] > vec[pivot] and i < j:
                j -= 1
            if i <= j:
                vec[i], vec[j] = vec[j], vec[i]
        if vec[pivot] < vec[i]:
            vec[pivot], vec[i] = vec[i], vec[pivot]
        if datos[0] < j:
            apilar(pila, [datos[0], j])
        if datos[1] > i:
            apilar(pila, [i+1, datos[1]])

#ej15

def interseccion_personajes():
    pila_5 = Pila()
    pila_7 = Pila()
    pila_aux = Pila()
    e5 = ['Luke Skywalker', 'Lando Calrissian', 'Yoda', 'Chewbacca',
           'Emperador Palpatine', 'C3PO']
    e7 = ['Rey', 'Finn', 'Luke Skywalker', 'Kylo Ren', 'Chewbacca',
           'C3PO']
    for i in range(0, len(e5)):
        apilar(pila_5, e5[i])
        apilar(pila_7, e7[i])
    print('Episodio V: The empire strikes back')
    barrido_pila(pila_5)
    print('Episodio VII: The force awakens')
    barrido_pila(pila_7)
    while not pila_vacia(pila_5):
        m = desapilar(pila_5)
        while not pila_vacia(pila_7):
            y = desapilar(pila_7)
            if(m == y):
                print('El personaje ' + str(m) + ' se encuentra en ambos episodios')
            apilar(pila_aux, y)
        while(not pila_vacia(pila_aux)):
            y = desapilar(pila_aux)
            apilar(pila_7, y)


# EJ 16
def contar():
    p_voc = Pila()
    p_con = Pila()
    po = Pila()
    parrafo = 'Los hombres no son nada, los principios lo son todo.'
    numeros = '0123456789'
    vocales = 'aeiouAEIOU'
    consonantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    print(parrafo)
    for dato in parrafo:
        if dato in vocales:
            apilar(p_voc, dato)
        elif dato in consonantes:
            apilar(p_con, dato)
        else:
            apilar(po, dato)

    # A) B) y D)
    voc, cons, o, eb, n = 0, 0, 0, 0, 0
    while not pila_vacia(p_voc):
        desapilar(p_voc)
        voc += 1
    while not pila_vacia(p_con):
        desapilar(p_con)
        cons += 1
    while not pila_vacia(po):
        m = desapilar(po)
        o += 1
        if m == ' ':
            eb += 1
        elif m in numeros:
            n += 1
    print('Cantidad de vocales:', voc)
    print('Cantidad de consonantes:', cons)
    print('Cantidad de otros caracteres:', o)
    print('Cantidad de espacios en blanco:', eb)
    print('Cantidad de numeros:', n)

    # C)
    total = voc + cons + o
    print('Porcentaje de vocales:', round(voc * 100 / total, 2), '%')
    print('Porcentaje de consonantes:', round(cons * 100 / total, 2), '%')

    # E)
    if voc == o:
        print('Igual cantidad de vocales y otros caracteres')
    else:
        print('Cantidades distintas de vocales y otros caracteres')

    # F)
    z = False
    while not pila_vacia(p_con):
        dato = desapilar(p_con)
        if dato == 'z':
            z = True
    if z:
        print('Existen letras Z en el parrafo')

# EJ 17
def objetos():
    pila = Pila()
    objetos = ['computadora', 'vaso', 'mesa', 'silla', ' helado', ' canasta', 'piza', 'tv']
    for i in range(0, len(objetos)):
        pes = random.randint(1, 8)
        apilar(pila, [pes, objetos[i]])
    print('La pila de objetos(en kg.) es : ')
    barrido_pila(pila)
    pila = ordenar(pila)
    print('La pila de objetos ordenados por peso es:')
    barrido_pila(pila)

# EJ 18
def peliculas():
    '''Pila de peliculas y sus datos'''
    pila = Pila()
    c = 0
    titulo = ['Reservoir Dogs', 'Bohemian Rhapsody',
              'Doctor Strange', 'Avengers: Infinity War',
              'Guardianes de la galaxia']
    estudio = ['Marvel Studios', 'Artisan Entertainment', 'GK Films',
               'Marvel Studios', 'Marvel Studios', 'Marvel Studios']
    anio = ['1992', '2018', '2016', '2018', '2014']
    for i in range(0, 6):
        title, studio, year = titulo[i], estudio[i], anio[i]
        apilar(pila, [title, studio, year])
    print('Peliculas:')
    barrido_pila(pila)
    while not pila_vacia(pila):
        dato = desapilar(pila)
        if dato[2] == '2014':
            print(str(dato[0]) + ' fue estrenada en 2014')
        if dato[2] == '2018':
            c += 1
        if dato[1] == 'Marvel Studios' and str(dato[2]) == '2018':
            print(str(dato[0]) + ' fue producida por Marvel en el año 2018')
    print('Se estrenaron', c, 'peliculas en 2018')


# EJ 19
def robot():
    pila = Pila()
    pila_aux = Pila()
    movimientos = ['norte', 'sur', 'este', 'oeste', 'noreste', 'sureste', 'noroeste', 'suroeste']
    for i in range(1, random.randint(0, 20)):
        apilar(pila, random.choice(movimientos))
    print('Los pasos realizados por el robot son:')
    barrido_pila(pila)
    while not pila_vacia(pila):
        m = desapilar(pila)
        if m == 'norte':
            apilar(pila_aux, 'sur')
        if m == 'sur':
            apilar(pila_aux, 'norte')
        if m == 'este':
            apilar(pila_aux, 'oeste')
        if m == 'oeste':
            apilar(pila_aux, 'este')
        if m == 'norte':
            apilar(pila_aux, 'sur')
        if m == 'noreste':
            apilar(pila_aux, 'suroeste')
        if m == 'noroeste':
            apilar(pila_aux, 'sureste')
        if m == 'sureste':
            apilar(pila_aux, 'noroeste')
        if m == 'suroeste':
            apilar(pila_aux, 'noreste')
    while not pila_vacia(pila_aux):
        apilar(pila, desapilar(pila_aux))
    print('Pasos en reversa para volver a punto de partida:')
    barrido_pila(pila)
    print('El robot realiza', tamanio_pila(pila), 'movimientos en ida')
    print('El robot realiza', tamanio_pila(pila), 'movimientos en vuelta')
    print('El robot realiza', tamanio_pila(pila) * 2, 'movimientos en total')


# EJ 20
def fibonacci(n):
    pila = Pila()
    apilar(pila, 0)
    if n == 1:
        apilar(pila, 1)
    elif n > 1:
        apilar(pila, 1)
        while tamanio_pila(pila) <= n:
            d1 = desapilar(pila)
            d2 = cima(pila)
            s = d1 + d2
            apilar(pila, d1)
            apilar(pila, s)
    barrido_pila(pila)

# EJ 21
def temperaturas(pila):
    pila = Pila()
    pila_aux = Pila()
    t_max = cima(pila)
    t_min = cima(pila)
    t_med = 0
    v_mayores = 0
    v_menores = 0
    print('Temperaturas registradas en el mes:')
    barrido_pila(pila)
    while not pila_vacia(pila):
        dato = desapilar(pila)
        t_med += dato
        if dato < t_min:
            t_min = dato
        if dato > t_max:
            t_max = dato
        apilar(pila_aux, dato)
    grado = tamanio_pila(pila_aux)
    t_med = t_med / grado
    while not pila_vacia(pila_aux):
        dato = desapilar(pila_aux)
        if dato >= t_med:
            v_mayores += 1
        else:
            v_menores += 1
    print('Temperatura minima:', t_min, '°')
    print('Temperatura maxima :', t_max, '°')
    print('El rango de temperatura media:', round(t_med, 2), '°')
    print('Temperaturas mayores e iguales a la media:', v_mayores, '°')
    print('Temperaturas menores a la media:', v_menores, '°')


# EJ 22
def marvel():
    pila = Pila()
    pila1 = Pila()
    pila2 = Pila()
    personaje = ['Iron Man', 'Heimdall', 'J.A.R.V.I.S', 'Doctor Strange',
                 'Groot', 'Thor Odinson', 'Rocket Raccoon', 'Black Widow']
    apariciones = [7, 4, 5, 1, 2, 5, 2, 5]
    for i in range(0, len(personaje)):
        apilar(pila, [personaje[i], apariciones[i]])
    print('Pila de personajes y sus apariciones en Marvel')
    barrido_pila(pila)
    while not pila_vacia(pila):
        dato = desapilar(pila)
        if dato[0] == 'Black Widow':
            print(str(dato[0]) + ' participo en ' + str(dato[1]) + ' peliculas')
        if dato[1] >= 5:
            print('Personaje que articipo en 5 o mas peliculas: ' + str([dato[0], dato[1]]))
        cad = dato[0]
        if cad[0] == 'C' or cad[0] == 'D' or cad[0] == 'G':
            print('Personajes que empiezan con la letra C, D o G: ' + dato[0])
        apilar(pila1, dato)
    barrido_pila(pila1)
    rr, gt = 1, 1
    while not pila_vacia(pila1):
        m = desapilar(pila1)
        if m[0] == 'Rocket Raccoon':
            print('Rocket Raccoon se encuentra en la posicion', rr)
        else:
            rr += 1
        apilar(pila2, m)
        while not pila_vacia(pila2):
            y = desapilar(pila2)
            if y[0] == 'Groot':
                print('Groot se encuentra en la posicion', gt)
            else:
                gt += 1


