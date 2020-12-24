from browser import document, window

paper = window.Raphael("left", "100%", "100%")
document["shape_info"].innerHTML = ""
btn = document["run"]
btn_grid = document["grid"]
btn_next_example = document["next_example"]
btn_prev_example = document["prev_example"]
code_editor = window.editor
window.show_grid = True


EX_1 = """# Ecco come disegnare un cerchio, se non si specifica niente il cerchio sarà rosso
cerchio()

# Ecco come disegnare un'atro cerchio in una posizione diversa
cerchio().x(200).y(200)

# Ecco come disegnare un cerchio verde
cerchio().x(400).y(300).colore(verde)

# Ecco come disegnare un cerchio giallo molto piccolo
cerchio().x(500).y(300).colore(giallo).raggio(10)

# Ecco come disegnare un cerchio azzurro molto grande
cerchio().x(600).y(400).colore(azzurro).raggio(100)

# Ecco come disegnare un cerchio con il bordo
cerchio().x(200).y(400).colore(blu).bordo(5, azzurro)

# Ed un cerchio con il bordo piu grande
cerchio().x(300).y(500).colore(bianco).bordo(25, rosso)

# Ed una stella con bordo bianco
stella(x=300, y=100, raggio=70).bordo(5, bianco)

# Ed un quadrato con bordo arancione
quadrato(x=400, y=150, lato=70).bordo(5, arancione)

# Ed un triangolo con bordo verde smeraldo
triangolo(x=500, y=200, lato=70).bordo(5, verde_smeraldo)
"""

EX_2 = """# Ecco come disegnare un cerchio e farlo muovere
# dal punto (100, 200) fino a (500, 400) in 2 secondi.
(cerchio()
 .x(100)
 .y(200)
 .aggiungi_animazione(durata=2)
 .x(500)
 .y(400)
 .parti())"""

EX_3 = """# Ecco come disegnare un cerchio e farlo muovere
# dal punto (100, 200) fino a (500, 400), e contemporaneamente
# cambiare il suo colore, il tutto in 2 secondi.
(cerchio()
 .posizione(x=100, y=200)
 .aggiungi_animazione(durata=2)
 .posizione(x=500, y=400)
 .colore(blu)
 .parti())"""

EX_4 = """# Ecco come disegnare e far muovere contemporaneamente piu cerchi
(cerchio()
 .posizione(x=100, y=200)
 .aggiungi_animazione(durata=2)
 .posizione(x=500, y=400)
 .colore(blu)
 .parti())

(cerchio()
 .colore(blu)
 .posizione(x=500, y=200)
 .aggiungi_animazione(durata=2)
 .posizione(x=100, y=400)
 .colore(arancione)
 .parti())"""

EX_5 = """# Ecco come disegnare un cerchio blu con raggio di dimensioni 100
# e farlo diventare un quadrato di dimensioni 200 con un bordo rosso
(cerchio()
 .colore(blu)
 .posizione(x=350, y=350)
 .raggio(100)
 .aggiungi_animazione(durata=2)
 .cambia_forma(QUADRATO)
 .colore(arancione)
 .bordo(10, rosso)
 .lato(200)
 .parti())"""

EX_6 = """# Ecco come disegnare un cerchio e farlo muovere
# dal punto (100, 200) fino a (500, 400) in 2 secondi.
c = cerchio()
c.posizione(x=100, y=200)
c.colore(rosso)
c.raggio(50)

c.aggiungi_animazione()
c.posizione(x=100, y=400)
c.cambia_forma(STELLA)
c.colore(celeste)
c.lato(100)

c.aggiungi_animazione()
c.posizione(x=500, y=400)
c.cambia_forma(QUADRATO)
c.colore(verde)
c.lato(100)

c.aggiungi_animazione()
c.posizione(x=500, y=200)
c.cambia_forma(TRIANGOLO)
c.colore(giallo)

c.aggiungi_animazione()
c.posizione(x=100, y=200)
c.cambia_forma(CERCHIO)
c.raggio(50)
c.colore(rosso)

c.parti()"""

EX_7 = """# Ecco come disegnare un sacco di cerchi che hanno
# dimensioni diverse
for i in conta(da=100, aggiungi=100, fino=700):
  cerchio().x(i).y(100).colore(viola).raggio(i / 15)"""

EX_8 = """# Ecco come disegnare un cerchio e far scegliere al computer
# il suo colore. Continua a cliccare su "Disegna" e vedrai che
# continueranno a cambiare.
cerchio().posizione(x=200, y=100).colore(colore_magico())
cerchio().posizione(x=200, y=250).colore(colore_magico())
cerchio().posizione(x=200, y=400).colore(colore_magico())"""

EX_9 = """# Ecco un sacco di cerchi con colori casuali che si trasformano
# in una bandiera
for i in conta(da=100, aggiungi=100, fino=700):
    for j in conta(da=100, aggiungi=100, fino=700):
        (quadrato()
         .x(i if i <= j else i + 50)
         .y(j if j <= i else j + 50)
         .lato(10)
         .colore(grigio)
         .aggiungi_animazione(durata=1)
         .colore(rosso if i > j else (verde if i < j else bianco))
         .lato(90)
         .posizione(x=i, y=j)
         .parti(aspetta=1))"""

EX_10 = """# In questo esempio facciamo finta che i cerchi siano delle palline
#  e li facciamo scontrare
for i in conta(da=100, aggiungi=100, fino=700):
    (cerchio()
     .posizione(x=i, y=100)
     .colore(colore_magico(blu))
     .raggio(40)
     .aggiungi_animazione(durata=0.1)
     .x(i+20)
     .parti(aspetta=0.1 * i / 100))"""

EX_11 = """# Facciamo mouvere tutti i cerchi lungo linee diagonali
for i in conta(da=100, aggiungi=100, fino=700):
    (triangolo()
     .posizione(x=i, y=100)
     .colore(colore_magico(blu))
     .lato(80)
     .aggiungi_animazione(durata=2)
     .posizione(x=600, y=700 - i)
     .ruota(90)
     .parti(aspetta=1))"""

EX_12 = """# Disegnamo un cerchio fatto da tanti cerchi
for angolo in range(0, 360, 10):
    (cerchio()
     .posizione(x=350, y=350)
     .raggio(5)
     .colore(grigio)
     .aggiungi_animazione(durata=2)
     .x(350 + 250 * cos(angolo))
     .y(350 + 250 * sin(angolo))
     .raggio(20)
     .colore(colore_magico(verde))
     .parti(aspetta=1)
    )"""

EX_13 = """# Disegnamo una spirale
for angolo in range(0, 4 * 360, 10):
    (cerchio()
     .posizione(x=350, y=350)
     .raggio(1)
     .colore(grigio)
     .aggiungi_animazione(durata=2)
     .x(350 + (angolo / 4.0 / 360.0) * 300 * cos(angolo))
     .y(350 + (angolo / 4.0 / 360.0) * 300 * sin(angolo))
     .raggio(1 + (angolo / 4.0 / 360.0) * 20)
     .colore(colore_magico("viola"))
     .parti(aspetta=1)
    )"""

EX_14 = """# Disegnamo dei fiori di vari colori

# Prima decidiamo dove posizionarli
posizioni_e_colori = [[(200, 200), verde],
                      [(200, 500), rosso],
                      [(350, 350), viola],
                      [(500, 200), blu],
                      [(500, 500), rosa]]

# Ora disegnamo i nostri cinque fiori
for centro, colore in posizioni_e_colori:
    x0, y0 = centro
    for angolo in range(0, 360, 30):
        # Aggiungiamo i petali
        (cerchio()
         .posizione(x=x0, y=y0)
         .raggio(5)
         .colore(grigio)
         .aggiungi_animazione(durata=2)
         .x(x0 + 75 * cos(angolo))
         .y(y0 + 75 * sin(angolo))
         .raggio(30)
         .colore(colore_magico(colore))
         .parti(aspetta=1))

        # Un cerchio in ogni centro
        (cerchio()
         .posizione(x=x0, y=y0)
         .colore(girasole)
         .aggiungi_animazione(durata=2)
         .raggio(50)
         .parti(aspetta=1))"""

EX_15 = """# Quattro forme,  un cerchio, una stella, un quadrato ed un
# triangolo. Queste forme decisono di scambiarsi di posto, ed ogni volta
# che lo fanno si trasformarno nel loro vicino...
posizioni = [(200, 200), (200, 400), (500, 400), (500, 200)]
forme = [CERCHIO, STELLA, QUADRATO, TRIANGOLO]
colori = [rosso, celeste, verde, giallo]

oggetti = [forma(x=x, y=y, forma=f).colore(c) for (x, y), f, c
           in zip(posizioni, forme, colori)]

indice = lambda x: x % 4

for i, oggetto in enumerate(oggetti):
    (oggetto
     .aggiungi_animazione(durata=2)
     .posizione(*posizioni[indice(i + 1)])
     .colore(colori[indice(i + 1)])
     .cambia_forma(forme[indice(i + 1)])
     .aggiungi_animazione(durata=2)
     .posizione(*posizioni[indice(i + 2)])
     .colore(colori[indice(i + 2)])
     .cambia_forma(forme[indice(i + 2)])
     .aggiungi_animazione(durata=2)
     .posizione(*posizioni[indice(i + 3)])
     .colore(colori[indice(i + 3)])
     .cambia_forma(forme[indice(i + 3)])
     .aggiungi_animazione(durata=2)
     .posizione(*posizioni[indice(i + 4)])
     .colore(colori[indice(i + 4)])
     .cambia_forma(forme[indice(i + 4)])
     .parti())"""

EX_16 = """# Questa è la storia di quattro quadrati che si uniscono per formare un fiore.
dt = 1.0

(quadrato(x=200, y=200)
 .colore(rosso)
 .aggiungi_animazione(durata=dt)
 .posizione(x=300, y=300)
 .aggiungi_animazione(durata=dt)
 .ruota(45)
 .aggiungi_animazione(durata=dt)
 .lato(100 * SQRT2)
 .aggiungi_animazione(durata=dt)
 .posizione(x=300, y=250)
 .ruota(0)
 .aggiungi_animazione(durata=dt)
 .posizione(x=300, y=400 - 50*SQRT2)
 .aggiungi_animazione(durata=dt)
 .posizione(x=400 - 50*SQRT2, y=400 - 50*SQRT2)
 .aggiungi_animazione(durata=dt)
 .posizione(x=400, y=400)
 .ruota(0)
 .lato(200)
 .parti())

(quadrato(x=600, y=200)
 .colore(celeste)
 .aggiungi_animazione(durata=dt)
 .posizione(x=500, y=300)
 .aggiungi_animazione(durata=dt)
 .ruota(45)
 .aggiungi_animazione(durata=dt)
 .lato(100 * SQRT2)
 .aggiungi_animazione(durata=dt)
 .posizione(x=500, y=250)
 .ruota(0)
 .aggiungi_animazione(durata=dt)
 .posizione(x=500, y=400 - 50*SQRT2)
 .aggiungi_animazione(durata=dt)
 .posizione(x=400 + 50*SQRT2, y=400 - 50*SQRT2)
 .aggiungi_animazione(durata=dt)
 .posizione(x=400, y=400)
 .ruota(45)
 .parti())

(quadrato(x=600, y=600)
 .colore(verde)
 .aggiungi_animazione(durata=dt)
 .posizione(x=500, y=500)
 .aggiungi_animazione(durata=dt)
 .ruota(45)
 .aggiungi_animazione(durata=dt)
 .lato(100 * SQRT2)
 .aggiungi_animazione(durata=dt)
 .posizione(x=500, y=550)
 .ruota(0)
 .aggiungi_animazione(durata=dt)
 .posizione(x=500, y=400 + 50*SQRT2)
 .aggiungi_animazione(durata=dt)
 .posizione(x=400 + 50*SQRT2, y=400 + 50*SQRT2)
 .aggiungi_animazione(durata=dt)
 .posizione(x=400, y=400)
 .ruota(0)
 .lato(100)
 .parti())

(quadrato(x=200, y=600)
 .colore(giallo)
 .aggiungi_animazione(durata=dt)
 .posizione(x=300, y=500)
 .aggiungi_animazione(durata=dt)
 .ruota(45)
 .aggiungi_animazione(durata=dt)
 .lato(100 * SQRT2)
 .aggiungi_animazione(durata=dt)
 .posizione(x=300, y=550)
 .ruota(0)
 .aggiungi_animazione(durata=dt)
 .posizione(x=300, y=400 + 50*SQRT2)
 .aggiungi_animazione(durata=dt)
 .posizione(x=400 - 50*SQRT2, y=400 + 50*SQRT2)
 .aggiungi_animazione(durata=dt)
 .posizione(x=400, y=400)
 .ruota(45)
 .lato(100*SQRT2/2)
 .parti())"""

EX_17 = """# Ecco come disegnare una stella a sei punte che contiene al suo interno
# altre stelle a sei punte.
a = 550

for i in range(9):
    if i % 3 == 0:
        c = giallo
    elif i % 3 == 1:
        c = giallo_limone
    else:
        c = carota

    (triangolo(x=400, y=350)
    .lato(a)
    .colore(c)
    .ruota(90 if i % 2 else 0))

    (triangolo(x=400, y=350)
    .lato(a)
    .colore(c)
    .ruota(-90 if i % 2 else 180))

    a = a * SQRT3 / 3"""

EX_18 = """# Degli esagoni che si trasformano in stelle
centro_x, centro_y = 350, 380
lato = 65


def esagono_tipo_a(cx, cy, lato, aspetta=1, durata=2):
    d = lato * SQRT3 / 6
    b = d * SQRT3 / 2
    (triangolo(x=cx, y=cy - 2 * d, lato=lato)
    .ruota(180)
    .colore(verde)
    .aggiungi_animazione(durata=durata)
    .posizione(x=cx, y=cy - 4 * d)
    .ruota(120)
    .parti(aspetta=aspetta))

    (triangolo(x=cx + 2 * b, y=cy - d, lato=lato)
    .ruota(0)
    .colore(verde_chiaro)
    .aggiungi_animazione(durata=durata)
    .posizione(x=cx + 4 * b, y=cy - 2 * d)
    .ruota(-60)
    .parti(aspetta=aspetta))

    (triangolo(x=cx + 2 * b, y=cy + d, lato=lato)
    .ruota(180)
    .colore(verde_smeraldo)
    .aggiungi_animazione(durata=durata)
    .posizione(x=cx + 4 * b, y=cy + 2 * d)
    .ruota(240)
    .parti(aspetta=aspetta))

    (triangolo(x=cx, y=cy + 2 * d, lato=lato)
    .ruota(0)
    .colore(verde)
    .aggiungi_animazione(durata=durata)
    .posizione(x=cx, y=cy+4*d)
    .ruota(-60)
    .parti(aspetta=aspetta))

    (triangolo(x=cx - 2 * b, y=cy + d, lato=lato)
    .ruota(-60)
    .colore(verde_chiaro)
    .aggiungi_animazione(durata=durata)
    .posizione(x=cx - 4 * b, y=cy + 2 * d)
    .ruota(240)
    .parti(aspetta=aspetta))

    (triangolo(x=cx - 2*b, y=cy - d, lato=lato)
    .ruota(0)
    .colore(verde_smeraldo)
    .aggiungi_animazione(durata=durata)
    .posizione(x=cx - 4*b, y=cy - 2*d)
    .ruota(60)
    .parti(aspetta=aspetta))


def esagono_tipo_b(cx, cy, lato, aspetta=1, durata=2):
    # sinistra
    (triangolo(x=cx - lato / SQRT3, y=cy, lato=lato)
    .ruota(-30)
    .colore(giallo)
    .aggiungi_animazione(durata=durata)
    .posizione(x=cx - 2 * lato / SQRT3, y=cy)
    .ruota(30)
    .parti(aspetta=aspetta))

    # destra
    (triangolo(x=cx + lato / SQRT3, y=cy, lato=lato)
    .ruota(30)
    .colore(giallo)
    .aggiungi_animazione(durata=durata)
    .posizione(x=cx + 2*lato / SQRT3, y=cy)
    .ruota(-30)
    .parti(aspetta=aspetta))

    # alto-destra
    (triangolo(x=cx + lato / SQRT3 / 2, y=cy - lato / 2, lato=lato)
    .ruota(-30)
    .colore(giallo_limone)
    .aggiungi_animazione(durata=durata)
    .posizione(x=cx + lato / SQRT3, y=cy - lato)
    .ruota(30)
    .parti(aspetta=aspetta))

    # alto-sinistra
    (triangolo(x=cx - lato / SQRT3 / 2, y=cy - lato /2, lato=lato)
    .ruota(30)
    .colore(girasole)
    .aggiungi_animazione(durata=durata)
    .posizione(x=cx - lato / SQRT3, y=cy - lato)
    .ruota(-30)
    .parti(aspetta=aspetta))

    # basso-destra
    (triangolo(x=cx + lato / SQRT3 / 2, y=cy + lato / 2, lato=lato)
    .ruota(-30)
    .colore(giallo_limone)
    .aggiungi_animazione(durata=durata)
    .posizione(x=cx + lato / SQRT3, y=cy + lato)
    .ruota(30)
    .parti(aspetta=aspetta))

    # basso-sinistra
    (triangolo(x=cx - lato / SQRT3 / 2, y=cy + lato /2, lato=lato)
    .ruota(30)
    .colore(girasole)
    .aggiungi_animazione(durata=durata)
    .posizione(x=cx - lato / SQRT3, y=cy + lato)
    .ruota(-30)
    .parti(aspetta=aspetta))


esagono_tipo_a(centro_x, centro_y, lato * SQRT3 * SQRT3, aspetta=7, durata=1)
esagono_tipo_b(centro_x, centro_y, lato * SQRT3, aspetta=6, durata=1)
esagono_tipo_a(centro_x, centro_y, lato, aspetta=5, durata=1)
esagono_tipo_b(centro_x, centro_y, lato / SQRT3, aspetta=4, durata=1)
esagono_tipo_a(centro_x, centro_y, lato / SQRT3 / SQRT3, aspetta=3, durata=1)
esagono_tipo_b(centro_x, centro_y, lato / SQRT3 / SQRT3 / SQRT3, aspetta=2, durata=1)
"""

EX_19 = """# Queste esempio mostra come si può creare un effetto 3d con delle
# forme geometriche.
l = 100
cx = 350
cy = 300
distanza = 200

# parete sinistra
triangolo(x=cx - l * SQRT3 / 6, y=cy + l/2, lato=l).colore(verde).ruota(-30)
# pavimento
triangolo(x=cx, y=cy+l, lato=l).colore(verde).ruota(30)
# cerchio
(cerchio(x=cx + l * SQRT3 / 6 - distanza * SQRT3/2, y=cy + l/2 + distanza/2)
 .raggio(l * 0.5)
 .colore(rosso)
 .aggiungi_animazione(durata=2)
 .posizione(x=cx+l*SQRT3/6, y=cy+l/2)
 .colore(melograno)
 .parti())

# parete destra
triangolo(x=cx + l * SQRT3 / 3, y=cy+l, lato=l).colore(verde_smeraldo).ruota(-30)
triangolo(x=cx + l * SQRT3 / 2, y=cy+l/2, lato=l).colore(verde_smeraldo).ruota(30)
# tetto
triangolo(x=cx, y=cy, lato=l).colore(verde_chiaro).ruota(30)
triangolo(x=cx + l * SQRT3 / 3, y=cy, lato=l).colore(verde_chiaro).ruota(-30)
"""

EXAMPLES = [EX_1, EX_2, EX_3, EX_4, EX_5, EX_6, EX_7, EX_8, EX_9,
            EX_10, EX_11, EX_12, EX_13, EX_14, EX_15, EX_16, EX_17,
            EX_18, EX_19]

ITA_COLORS_TO_CSS = {
    "verde_chiaro": "#55efc4",
    "verde": "#00b894",
    "verde_acqua": "#00cec9",
    "verde_smeraldo": "#2ecc71",
    "azzurro_acqua": "#81ecec",
    "azzurro": "#74b9ff",
    "celeste": "#0984e3",
    "blu": "#0000CD",
    "lilla": "#a29bfe",
    "viola": "#6c5ce7",
    "giallo_limone": "#ffeaa7",
    "giallo": "#fdcb6e",
    "girasole": "#f1c40f",
    "rosa": "#fab1a0",
    "arancione": "#e17055",
    "carota": "#e67e22",
    "zucca": "#d35400",
    "melograno": "#c0392b",
    "rosso": "#d63031",
    "rosa_caramella": "#fd79a8",
    "fucsia": "#e84393",
    "bianco": "white",
    "marrone": "#795548",
    "grigio_chiaro": "#dfe6e9",
    "grigio": "#b2bec3",
    "grigio_scuro": "#636e72",
    "cemento": "#95a5a6",
    "argento": "#bdc3c7",
    "nero": "#000000",
}

HEX_COLOR_TO_ITA = {v.lower(): k.lower() for k, v in ITA_COLORS_TO_CSS.items()}

translate_color = lambda hex_color: HEX_COLOR_TO_ITA.get(hex_color.lower(), hex_color)

giallo = "giallo"
verde_chiaro = "verde_chiaro"
verde = "verde"
verde_acqua = "verde_acqua"
verde_smeraldo = "verde_smeraldo"
azzurro_acqua = "azzurro_acqua"
azzurro = "azzurro"
celeste = "celeste"
blu = "blu"
lilla = "lilla"
viola = "viola"
giallo_limone = "giallo_limone"
giallo = "giallo"
girasole = "girasole"
rosa = "rosa"
arancione = "arancione"
carota = "carota"
zucca = "zucca"
melograno = "melograno"
rosso = "rosso"
rosa_caramella = "rosa_caramella"
fucsia = "fucsia"
bianco = "bianco"
marrone = "marrone"
grigio_chiaro = "grigio_chiaro"
grigio = "grigio"
grigio_scuro = "grigio_scuro"
cemento = "cemento"
argento = "argento"
nero = "nero"

COLOR_PALETTES = {
    "rosso": ["#C91F37", "#C91F37", "#9D2933", "#CF000F", "#E68364",
              "#F22613", "#CF3A24", "#C3272B", "#8F1D21", "#D24D57"],
    "verde": ["#7A942E", "#8DB255", "#5B8930", "#6B9362", "#407A52", "#006442",
              "#87D37C", "#26A65B", "#26C281", "#049372", "#2ABB9B", "#16A085",
              "#36D7B7", "#03A678", "#4DAF7C"],
    "rosa": ["#F08F90", "#F47983", "#DB5A6B", "#C93756", "#FCC9B9",
             "#FFB3A7", "#F62459", "#F58F84"],
    "giallo": ["#D9B611", "#F3C13A", "#F7CA18", "#E2B13C", "#A17917", "#F5D76E",
               "#F4D03F", "#FFA400", "#E08A1E", "#FFB61E", "#FAA945", "#FFA631",
               "#FFB94E", "#E29C45", "#F9690E", "#CA6924", "#F5AB35"],
    "blu": ["#4D8FAC", "#4D8FAC", "#22A7F0", "#19B5FE", "#59ABE3", "#48929B",
            "#317589", "#89C4F4", "#4B77BE", "#1F4788", "#003171", "#044F67",
            "#264348"],
    "viola": ["#875F9A", "#5D3F6A", "#89729E", "#763568", "#8D608C",
              "#A87CA0", "#5B3256", "#BF55EC", "#8E44AD", "#9B59B6",
              "#BE90D4"],
    "grigio": ["#BFBFBF", "#F2F1EF", "#BDC3C7", "#ECF0F1", "#D2D7D3",
               "#757D75", "#EEEEEE", "#ABB7B7", "#6C7A89", "#95A5A6"]
}

_colori = list(ITA_COLORS_TO_CSS.keys())

_COLORI = list(ITA_COLORS_TO_CSS.keys())

_colori_text = [
    f'<span style="color:{ITA_COLORS_TO_CSS[c]}">{c}</span>' for c in _colori
    if c != "bianco"]
_colori_text += ['e <span style="color:white; background-color:#2d3436"> bianco</span>']

stroke_attr = {"stroke": 1,
               "stroke": "#FFFFFF",
               "stroke-dasharray": "--",
               "stroke-width": 0.5}
grid = []
window.current_example = 0
window.show_grid = True
document["colors_list"].innerHTML = f"""Ecco i colori disponibili: {', '.join(_colori_text)}."""

# Trigonometric functions
PI = 2.0 * window.Math.asin(1)
SQRT2 = window.Math.sqrt(2)
SQRT3 = window.Math.sqrt(3)
sin = lambda x: window.Math.sin(x * PI / 180.0)
cos = lambda x: window.Math.cos(x * PI / 180.0)

# Constants
STELLA = "stella"
QUADRATO =  "quadrato"
CERCHIO = "cerchio"
TRIANGOLO = "triangolo"

_default_color = {
    STELLA: ITA_COLORS_TO_CSS[giallo],
    QUADRATO: ITA_COLORS_TO_CSS[blu],
    CERCHIO: ITA_COLORS_TO_CSS[rosso],
    TRIANGOLO: ITA_COLORS_TO_CSS[verde],
}

def is_element_visible(element):
    return element.node.style.display != "none"


def draw_grid():
    for i in range(100, 1000, 100):
        l = paper.path(f"M{i},20 v2000").attr(stroke_attr)
        t = paper.text(i, 10, f"x={i}")
        if not window.show_grid:
            l.hide()
            t.hide()
        grid.append(l)
        grid.append(t)
    for i in range(100, 1000, 100):
        l = paper.path(f"M25,{i} h2000").attr(stroke_attr)
        t = paper.text(18, i, f"y={i}")
        if not window.show_grid:
            l.hide()
            t.hide()
        grid.append(l)
        grid.append(t)


def colore_magico(filtro=None):
    if filtro is None or filtro not in COLOR_PALETTES:
        return _colori[int(len(_colori) * (window.Math.random()))]
    else:
        n = len(COLOR_PALETTES[filtro])
        return COLOR_PALETTES[filtro][int(n * (window.Math.random()))]


def colore(i):
    return _colori[i % len(_colori)]


def _star_path(x, y, radius, angle=0.0):
    # Reference: https://mathworld.wolfram.com/Pentagram.html
    a = 0.381966
    b = 0.236068
    r = 0.16246
    R = 0.200811
    rho = 0.525731
    X = 0.309017
    Y = 0.224514
    scale = radius / rho

    x1, y1 = x, y - rho * scale
    x2, y2 = x + (b / 2) * scale, y - r * scale
    x3, y3 = x + (a + b / 2) * scale, y - r * scale
    x4, y4 = x + (a + b / 2 - X) * scale, y - r * scale + Y * scale
    x5, y5 = x + X * scale, y + (R + Y) * scale
    x6, y6 = x, y + R * scale
    x7, y7 = x - X * scale, y + (R + Y) * scale
    x8, y8 = x - (a + b/2 - X) * scale, y - r * scale + Y * scale
    x9, y9 = x - (a + b/2) * scale, y - r * scale
    x10, y10 = x - b / 2 * scale, y - r * scale

    x1, y1 = rotate(x1, y1, x, y, angle)
    x2, y2 = rotate(x2, y2, x, y, angle)
    x3, y3 = rotate(x3, y3, x, y, angle)
    x4, y4 = rotate(x4, y4, x, y, angle)
    x5, y5 = rotate(x5, y5, x, y, angle)
    x6, y6 = rotate(x6, y6, x, y, angle)
    x7, y7 = rotate(x7, y7, x, y, angle)
    x8, y8 = rotate(x8, y8, x, y, angle)
    x9, y9 = rotate(x9, y9, x, y, angle)
    x10, y10 = rotate(x10, y10, x, y, angle)

    path = f"M {x1} {y1} " # Top
    path += f"L {x2} {y2} "
    path += f"L {x3} {y3} " # Top right
    path += f"L {x4} {y4} "
    path += f"L {x5} {y5} " # Down right
    path += f"L {x6} {y6} " # Down center
    path += f"L {x7} {y7} " # Down left
    path += f"L {x8} {y8} "
    path += f"L {x9} {y9} " # Top left
    path += f"L {x10} {y10} "
    path += f"L {x1} {y1} " # Top
    return path


def _square_path(x, y, length, angle=0.0):
    x1, y1 = x - length / 2, y - length / 2
    x2, y2 = x + length / 2, y - length / 2
    x3, y3 = x + length / 2, y + length / 2
    x4, y4 = x - length / 2, y + length / 2
    x1, y1 = rotate(x1, y1, x, y, angle)
    x2, y2 = rotate(x2, y2, x, y, angle)
    x3, y3 = rotate(x3, y3, x, y, angle)
    x4, y4 = rotate(x4, y4, x, y, angle)
    path = f"M {x1} {y1} "
    path += f"L {x2} {y2} "
    path += f"L {x3} {y3} "
    path += f"L {x4} {y4} "
    path += f"L {x1} {y1} "
    return path


def _circle_path(x, y, radius):
    path = f"M {x - radius}, {y} "
    path += f"a {radius},{radius} 0 1,1 {radius * 2},0 "
    path += f"a {radius},{radius} 0 1,1 -{radius * 2},0 "
    return path


def _triangle_path(x, y, length, angle=0.0):
    x1, y1 = x, y - length * 1.736 * 2 / 6
    x2, y2 = x + length / 2, y + length * 1.732 / 6
    x3, y3 = x - length / 2, y + length * 1.732 / 6
    x1, y1 = rotate(x1, y1, x, y, angle)
    x2, y2 = rotate(x2, y2, x, y, angle)
    x3, y3 = rotate(x3, y3, x, y, angle)
    path = f"M {x1} {y1} "
    path += f"L {x2} {y2} "
    path += f"L {x3} {y3} "
    path += f"L {x1} {y1} "
    return path


def rotate(x, y, x_center, y_center, angle):
    new_x = ((x - x_center) * window.Math.cos(angle * PI / 180.0)
             - (y - y_center) * window.Math.sin(angle * PI / 180.0) + x_center)
    new_y = ((x - x_center) * window.Math.sin(angle * PI / 180.0)
             + (y - y_center) * window.Math.cos(angle * PI / 180.0) + y_center)
    return (new_x, new_y)


def _path_function(x, y, size, forma, angolo=0.0):
    if forma == STELLA:
        return _star_path(x, y, size, angolo)
    elif forma == QUADRATO:
        return _square_path(x, y, size, angolo)
    elif forma == CERCHIO:
        return _circle_path(x, y, size)
    elif forma == TRIANGOLO:
        return _triangle_path(x, y, size, angolo)
    else:
        print(f"Wrong path: {forma}")
        return _circle_path(x, y, size)


class forma(object):

    def __init__(self, x=100, y=100, dimensione=50, forma="stella"):
        self._x = x
        self._y = y
        self._forma = forma
        self._angolo = 0.0
        self._dimensione = dimensione
        self._show_info = False
        path = _path_function(self._x, self._y, self._dimensione, self._forma)
        self._attrs = {
            "fill": _default_color.get(forma, rosso),
            "stroke-width": 0,
            "stroke": "white",
            "path": path,
            "stroke-linecap": "round",
            "stroke-linejoin": "round",
        }
        self._durations = []
        self._new_attrs = []
        self.s = paper.path(path).attr(self._attrs)
        self.s.click(self._on_click)
        self.s.mouseout(self._on_mouseout)
        return self

    def _on_mouseout(self, event, *args, **kwargs):
        document["shape_info"].innerHTML = ""
        self._show_info = False

    def _description(self):
        description = f"<b>{self._forma.capitalize()}</b>"
        description += f"<br/>&#8227; posizione x = {self._x:.1f}"
        description += f"<br/>&#8227; posizione y = {self._y:.1f}"
        description += f"<br/>&#8227; colore = {translate_color(self._attrs['fill'])}"
        description += f"<br/>&#8227; angolo = {self._angolo}"
        description += f"<br/>&#8227; dimensione = {self._dimensione:.1f}"
        if self._attrs["stroke-width"]:
            description += f"<br/>&#8227; dimensione bordo = {self._attrs['stroke-width']}"
            description += f"<br/>&#8227; colore bordo = {translate_color(self._attrs['stroke'])}"
        return description

    def  _on_click(self, event, *args, **kwargs):
        if self._show_info:
            return self._on_mouseout(event)
        document["shape_info"].innerHTML = self._description()
        self._show_info = True

    def _is_animating(self):
        return len(self._new_attrs) > 0

    def _update_path(self):
        path = _path_function(self._x, self._y, self._dimensione, self._forma, self._angolo)
        if not self._is_animating():
            self._attrs["path"] = path
            self.s.attr(self._attrs)
        else:
            self._new_attrs[-1]["path"] = path

    def posizione(self, x, y):
        return self.xy(x, y)

    def xy(self, x, y):
        self._x = x
        self._y = y
        self._update_path()
        return self

    def x(self, x):
        self._x = x
        self._update_path()
        return self

    def y(self, y):
        self._y = y
        self._update_path()
        return self

    def cambia_forma(self, forma):
        self._forma = forma
        self._update_path()
        return self

    def ruota(self, angolo):
        self._angolo = angolo
        self._update_path()
        return self

    def dimensione(self, d):
        self._dimensione = d
        self._update_path()
        return self

    def lato(self, l):
        self.dimensione(l)
        return self

    def raggio(self, r):
        self.dimensione(r)
        return self

    def colore(self, colore):
        if not self._is_animating():
            if colore in ITA_COLORS_TO_CSS:
                self._attrs["fill"] = ITA_COLORS_TO_CSS[colore.lower()]
            else:
                self._attrs["fill"] = colore
            self.s.attr(self._attrs)
        else:
            if colore in ITA_COLORS_TO_CSS:
                self._new_attrs[-1]["fill"] = ITA_COLORS_TO_CSS[colore.lower()]
            else:
                self._new_attrs[-1]["fill"] = colore
        return self

    def bordo(self, spessore, colore):
        if not self._is_animating():
            self._attrs["stroke"] = ITA_COLORS_TO_CSS[colore.lower()]
            self._attrs["stroke-width"] = spessore
            self.s.attr(self._attrs)
        else:
            self._new_attrs[-1]["stroke"] = ITA_COLORS_TO_CSS[colore.lower()]
            self._new_attrs[-1]["stroke-width"] = spessore
        return self

    def aggiungi_animazione(self, durata=1):
        self._new_attrs.append({})
        self._durations.append(durata * 1000)
        return self

    def _callback(self):
        if self._new_attrs:
            new_attrs = self._new_attrs.pop(0)
            duration = self._durations.pop(0)
            animation = window.Raphael.animation(
                new_attrs, duration, "ease-in-out", self._callback)
            self.s.animate(animation.delay(0).repeat(None))

    def anima(self, aspetta=0):
        if self._new_attrs:
            new_attrs = self._new_attrs.pop(0)
            duration = self._durations.pop(0)
            animation = window.Raphael.animation(
                new_attrs, duration, "ease-in-out", self._callback)
            self.s.animate(animation.delay(aspetta * 1000).repeat(None))
        return self

    def parti(self, aspetta=0):
        return self.anima(aspetta)


class quadrato(forma):

    def __init__(self, x=100, y=100, lato=50):
        super(quadrato, self).__init__(x, y, lato, forma=QUADRATO)
        return self

    def _description(self):
        description = f"<b>{self._forma.capitalize()}</b>"
        description += f"<br/>&#8227; posizione x = {self._x:.1f}"
        description += f"<br/>&#8227; posizione y = {self._y:.1f}"
        description += f"<br/>&#8227; colore = {translate_color(self._attrs['fill'])}"
        if self._angolo != 0.0:
            description += f"<br/>&#8227; angolo = {self._angolo:.1f}"
        description += f"<br/>&#8227; lato = {self._dimensione:.1f}"
        if self._attrs["stroke-width"]:
            description += f"<br/>&#8227; dimensione bordo = {self._attrs['stroke-width']}"
            description += f"<br/>&#8227; colore bordo = {translate_color(self._attrs['stroke'])}"
        return description

class stella(forma):

    def __init__(self, x=100, y=100, raggio=50):
        super(stella, self).__init__(x, y, raggio, forma=STELLA)
        return self

    def _description(self):
        description = f"<b>{self._forma.capitalize()}</b>"
        description += f"<br/>&#8227; posizione x = {self._x:.1f}"
        description += f"<br/>&#8227; posizione y = {self._y:.1f}"
        description += f"<br/>&#8227; colore = {translate_color(self._attrs['fill'])}"
        if self._angolo != 0.0:
            description += f"<br/>&#8227; angolo = {self._angolo:.1f}"
        description += f"<br/>&#8227; lato = {self._dimensione:.1f}"
        if self._attrs["stroke-width"]:
            description += f"<br/>&#8227; dimensione bordo = {self._attrs['stroke-width']}"
            description += f"<br/>&#8227; colore bordo = {translate_color(self._attrs['stroke'])}"
        return description

class cerchio(forma):

    def __init__(self, x=100, y=100, raggio=50):
        super(cerchio, self).__init__(x, y, raggio, forma=CERCHIO)
        return self

    def _description(self):
        description = f"<b>{self._forma.capitalize()}</b>"
        description += f"<br/>&#8227; posizione x = {self._x:.1f}"
        description += f"<br/>&#8227; posizione y = {self._y:.1f}"
        description += f"<br/>&#8227; colore = {translate_color(self._attrs['fill'])}"
        description += f"<br/>&#8227; raggio = {self._dimensione:.1f}"
        if self._attrs["stroke-width"]:
            description += f"<br/>&#8227; dimensione bordo = {self._attrs['stroke-width']}"
            description += f"<br/>&#8227; colore bordo = {translate_color(self._attrs['stroke'])}"
        return description

class triangolo(forma):

    def __init__(self, x=100, y=100, lato=50):
        super(triangolo, self).__init__(x, y, lato, forma=TRIANGOLO)
        return self

    def _description(self):
        description = f"<b>{self._forma.capitalize()}</b>"
        description += f"<br/>&#8227; posizione x = {self._x:.1f}"
        description += f"<br/>&#8227; posizione y = {self._y:.1f}"
        description += f"<br/>&#8227; colore = {translate_color(self._attrs['fill'])}"
        if self._angolo != 0.0:
            description += f"<br/>&#8227; angolo = {self._angolo:.1f}"
        description += f"<br/>&#8227; lato = {self._dimensione:.1f}"
        if self._attrs["stroke-width"]:
            description += f"<br/>&#8227; dimensione bordo = {self._attrs['stroke-width']}"
            description += f"<br/>&#8227; colore bordo = {translate_color(self._attrs['stroke'])}"
        return description

def callback(ev):
    paper.clear()
    draw_grid()
    if code_editor.getSelectedText():
        code_to_execute = code_editor.getSelectedText()
    else:
        code_to_execute = code_editor.getValue()
    exec(code_to_execute)


def toggle_grid(ev):
    for x in grid:
        if is_element_visible(x):
            x.hide()
        else:
            x.show()
    window.show_grid = not window.show_grid
    print("now is", window.show_grid)


def show_example(ev, increment=0, save=True):
    # Update the existing exercise
    if save:
        EXAMPLES[window.current_example] = code_editor.getValue()

    # Show the new one and update the counter
    window.current_example += increment
    if window.current_example >= len(EXAMPLES):
        window.current_example = 0
    elif window.current_example < 0:
        window.current_example = len(EXAMPLES) - 1

    code_editor.setValue(EXAMPLES[window.current_example])
    code_editor.clearSelection();
    callback(ev)


def show_next_example(ev):
    show_example(ev, increment=1, save=True)


def show_prev_example(ev):
    show_example(ev, increment=-1, save=True)


def call_draw_callback(editor, *args, **kwargs):
    callback(None)


def conta(da=0, aggiungi=1, fino=10):
    return range(da, fino, aggiungi)


btn.bind("click", callback)
btn_grid.bind("click", toggle_grid)
btn_prev_example.bind("click", show_prev_example)
btn_next_example.bind("click", show_next_example)
show_example(None, increment=0, save=False)
code_editor.commands.addCommand({
    "name": 'execute',
    "bindKey": {"win": "Ctrl-Enter",  "mac": "Command-Enter"},
    "exec": call_draw_callback,
    "readOnly": True
})
