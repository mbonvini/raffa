from browser import document, window

paper = window.Raphael("left", "100%", "100%")
btn = document["run"]
btn_grid = document["grid"]
btn_next_example = document["next_example"]
btn_prev_example = document["prev_example"]
code_editor = window.editor

EX_1 = """# Ecco come disegnare un cerchio, se non si specifica niente il cerchio sarà rosso
cerchio()

# Ecco come disegnare un'atro cerchio in una posizione diversa
cerchio().x(200).y(200)

# Ecco come disegnare un cerchio verde
cerchio().x(400).y(300).colore("verde")

# Ecco come disegnare un cerchio giallo molto piccolo
cerchio().x(500).y(300).colore("giallo").raggio(10)

# Ecco come disegnare un cerchio azzurro molto grande
cerchio().x(600).y(400).colore("azzurro").raggio(100)

# Ecco come disegnare un cerchio con il bordo
cerchio().x(200).y(400).colore("blu").bordo(5, "azzurro")

# Ed un cerchio con il bordo piu grande
cerchio().x(300).y(500).colore("bianco").bordo(25, "rosso")"""

EX_2 = """# Ecco come disegnare un cerchio e farlo muovere
# dal punto (100, 200) fino a (500, 400) in 2 secondi.
(cerchio()
 .x(100)
 .y(200)
 .inizia_animazione()
 .x(500)
 .y(400)
 .durata(2)
 .parti())"""

EX_3 = """# Ecco come disegnare un cerchio e farlo muovere
# dal punto (100, 200) fino a (500, 400), e contemporaneamente
# cambiare il suo colore, il tutto in 2 secondi.
(cerchio()
 .x(100)
 .y(200)
 .inizia_animazione()
 .x(500)
 .y(400)
 .colore("blu")
 .durata(2)
 .parti())"""

EX_4 = """# Ecco come disegnare e far muovere contemporaneamente piu cerchi
(cerchio()
 .x(100)
 .y(200)
 .inizia_animazione()
 .x(500)
 .y(400)
 .colore("blu")
 .durata(2)
 .parti())

(cerchio()
 .colore("blu")
 .x(500)
 .y(200)
 .inizia_animazione()
 .x(100)
 .y(400)
 .colore("arancione")
 .durata(2)
 .parti())"""

EX_5 = """# Ecco come disegnare un sacco di cerchi che hanno
# dimensioni diverse
for i in range(100, 700, 100):
  cerchio().x(i).y(100).colore("viola").raggio(i/15)"""

EX_6 = """# Ecco come disegnare un cerchio e far scegliere al computer
# il suo colore. Continua a cliccare su "Disegna" e vedrai che
# continueranno a cambiare.
cerchio().x(200).y(100).colore(colore_magico())
cerchio().x(200).y(250).colore(colore_magico())
cerchio().x(200).y(400).colore(colore_magico())"""

EX_7 = """# Ecco un sacco di cerchi con colori casuali che si trasformano
# in una bandiera
for i in range(100, 700, 100):
    for j in range(100, 800, 100):
        (cerchio()
         .x(i)
         .y(j)
         .raggio(i/20 + j/20)
         .colore(colore_magico())
         .inizia_animazione()
         .colore("rosso" if j <= 300 else ("verde" if j >= 500 else "giallo"))
         .raggio(50)
         .durata(2)
         .parti(aspetta=1))"""

EX_8 = """# Ecco un sacco di cerchi con colori casuali che si trasformano
# in una bandiera
for i in range(100, 700, 100):
    for j in range(100, 700, 100):
        (cerchio()
         .x(i if i <= j else i + 50)
         .y(j if j <= i else j + 50)
         .raggio(10)
         .colore("grigio")
         .inizia_animazione()
         .colore("rosso" if i > j else ("verde" if i < j else "bianco"))
         .raggio(50)
         .x(i)
         .y(j)
         .durata(1)
         .parti(aspetta=1))"""

EX_9 = """# In questo esempio facciamo finta che i cerchi siano delle palline
#  e li facciamo scontrare
for i in range(100, 700, 100):
    (cerchio()
     .x(i)
     .y(100)
     .colore("azzurro")
     .raggio(40)
     .inizia_animazione()
     .x(i+20)
     .durata(0.1)
     .parti(aspetta=0.1 * i / 100))"""

EX_10 = """# Facciamo mouvere tutti i cerchi lungo linee diagonali
for i in range(100, 700, 100):
    (cerchio()
     .x(i)
     .y(100)
     .colore("azzurro")
     .raggio(40)
     .inizia_animazione()
     .x(600)
     .y(700 - i)
     .durata(2)
     .parti(aspetta=1))"""

EXAMPLES = [EX_1, EX_2, EX_3, EX_4, EX_5, EX_6, EX_7, EX_8, EX_9, EX_10]

ITA_COLORS_TO_CSS = {
    "verde chiaro": "#55efc4",
    "verde": "#00b894",
    "verde acqua": "#00cec9",
    "azzurro acqua": "#81ecec",
    "azzurro": "#74b9ff",
    "celeste": "#0984e3",
    "blu": "#0000CD",
    "lilla": "#a29bfe",
    "viola": "#6c5ce7",
    "giallo limone": "#ffeaa7",
    "giallo": "#fdcb6e",
    "rosa": "#fab1a0",
    "arancione": "#e17055",
    "rosso": "#d63031",
    "rosa caramella": "#fd79a8",
    "fucsia": "#e84393",
    "bianco": "white",
    "marrone": "#795548",
    "grigio chiaro": "#dfe6e9",
    "grigio": "#b2bec3",
    "grigio scuro": "#636e72",
    "nero": "#2d3436",
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


def is_element_visible(element):
    return element.node.style.display != "none"


def draw_grid():
    for i in range(100, 1000, 100):
        l = paper.path(f"M{i},20 v2000").attr(stroke_attr)
        t = paper.text(i, 10, f"x={i}")
        grid.append(l)
        grid.append(t)
    for i in range(100, 1000, 100):
        l = paper.path(f"M25,{i} h2000").attr(stroke_attr)
        t = paper.text(18, i, f"y={i}")
        grid.append(l)
        grid.append(t)


def colore_magico():
    return _colori[int(len(_colori) * (window.Math.random()))]


def colore(i):
    return _colori[i % len(_colori)]


class cerchio(object):

    def __init__(self, x=100, y=100, raggio=50):
        self._attrs = {
            "fill": "red",
            "stroke-width": 0,
            "stroke": "white"
        }
        self._is_animating = False
        self._duration = 1000
        self._repeat = None
        self._new_attrs = {}
        self.c = paper.circle(x, y, raggio).attr(self._attrs)
        return self

    def x(self, x):
        if not self._is_animating:
            self._attrs["cx"] = x
            self.c.attr(self._attrs)
        else:
            self._new_attrs["cx"] = x
        return self

    def y(self, y):
        if not self._is_animating:
            self._attrs["cy"] = y
            self.c.attr(self._attrs)
        else:
            self._new_attrs["cy"] = y
        return self

    def muovi_x(self, dx):
        return self

    def muovi_y(self, dy):
        return self

    def muovi_xy(self, dx, dy):
        return self

    def raggio(self, r):
        if not self._is_animating:
            self._attrs["r"] = r
            self.c.attr(self._attrs)
        else:
            self._new_attrs["r"] = r
        return self

    def colore(self, colore):
        if not self._is_animating:
            self._attrs["fill"] = ITA_COLORS_TO_CSS[colore.lower()]
            self.c.attr(self._attrs)
        else:
            self._new_attrs["fill"] = ITA_COLORS_TO_CSS[colore.lower()]
        return self

    def bordo(self, spessore, colore):
        if not self._is_animating:
            self._attrs["stroke"] = ITA_COLORS_TO_CSS[colore.lower()]
            self._attrs["stroke-width"] = spessore
            self.c.attr(self._attrs)
        else:
            self._new_attrs["stroke"] = ITA_COLORS_TO_CSS[colore.lower()]
            self._new_attrs["stroke-width"] = spessore
        return self

    def inizia_animazione(self):
        self._is_animating = True
        return self

    def durata(self, durata=1):
        self._duration = durata * 1000
        return self

    def ripeti(self, volte):
        self._repeat = volte
        return self

    def anima(self, aspetta=0):
        animation = window.Raphael.animation(
            self._new_attrs, self._duration, "ease-in-out")
        self.c.animate(animation.delay(aspetta * 1000).repeat(self._repeat))
        self._is_animating = False
        return self

    def parti(self, aspetta=0):
        return self.anima(aspetta)



def callback(ev):
    paper.clear()
    draw_grid()
    exec(code_editor.getValue())


def toggle_grid(ev):
    for x in grid:
        if is_element_visible(x):
            x.hide()
        else:
            x.show()

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


btn.bind("click", callback)
btn_grid.bind("click", toggle_grid)
btn_prev_example.bind("click", show_prev_example)
btn_next_example.bind("click", show_next_example)
show_example(None, increment=0, save=False)
