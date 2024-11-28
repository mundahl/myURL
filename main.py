from fasthtml.common import *
from datetime import datetime

home_title = 'Mundahl Makes Moves'

nav = Nav()(
    Div(cls="container")(
        Div(cls="grid")(
            H1(A("John Mundahl", href="/", 
                 style="text-decoration: none; color: inherit; font-family: 'Garamond', 'Palatino', serif;", 
                 onmouseover="this.style.color='#01659A';", 
                 onmouseout="this.style.color='inherit';")),
            Div(cls="grid")(
                A("Jottings", cls="outline", style="--pico-border-color:transparent", href="/jottings", role="button" ),
                A("Makings", cls="outline", style="--pico-border-color:transparent", href="/makings", role="button"),
                A("Man Law", cls="outline", style="--pico-border-color:transparent", href="/manlaw24", role="button"),
                A("Join Me?", href="/joinme", role="button")))))


current_year = str(datetime.now().year)
footer = Footer(style="text-align: center;")(
    P(f"© John Mundahl, {current_year} | Your ceiling is much higher | This site built by ", A("me", href="https://github.com/mundahl/myURL"))
)


jot_title = "Mundahl's Jottings"



make_title = "Mundahl's Makings"


joinme_title = "Join Mundahl"


manlaw24_title = "Man Law 2024 Recap"



app,rt = fast_app()

@app.get("/")
def homepage():
    return Title(home_title), Main(nav, Hr(), Div(cls="container")(H1("Coming soon!"), H6("(What's up Carson!)"))), footer

@app.get("/jottings")
def jottings_page():
    return Title(jot_title), Main(nav, Hr(), Div(cls="container")(H1("Jottings"), P("Coming soon."))), footer

@app.get("/makings")
def makings_page():
    return Title(make_title), Main(nav, Hr(), Div(cls="container")(H1("Makings"), P("Under construction."))), footer

@app.get("/joinme")
def joinme_page():
    return Title(joinme_title), Main(nav, Hr(), Div(cls="container")
                                   (H1(A("Message Me", href="mailto:john.mundahl@gmail.com")), 
                                    P("Self-expression is powerful. Every bit attracts better-matched people who I'd love to interact with."),
                                    P("That's probably you. So message me. Or accept stasis."),
                                    P("Email me at firstname.lastname@gmail.com"))
                                   ), footer

@app.get("/manlaw24")
def manlaw24_page():
    return Title(manlaw24_title), Main(nav, Hr(), Div(cls="container") 
                                   (H1("Man Law 2024 Recap - Week 12"), 
                                    P("TODO IDEAS: Website welcome. Natural equilibrium of trading across seasons. Rip up the ESPN power index initial ranks. Rules. Fandom irrationality. Fanduel and draft kings are fracking fandom. Compare teams to thanksgiving dishes.")
                                   )), footer

serve()
