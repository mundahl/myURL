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
    return Title(home_title), Main(nav, Hr(), Div(cls="container")(H1("Coming soon!"), H6("(Welcome Man Law class of 2024 😋)"))), footer

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
                                    P("TODO IDEAS: Website welcome. Natural equilibrium of trading across seasons. Rip up the ESPN power index initial ranks. Rules. Fandom irrationality. Fanduel and draft kings are fracking fandom. Compare teams to thanksgiving dishes."),
                                    P("You read that right, johnmundahl.com! Instead of Medium or Google Drive, I figured I'd use a more long term (and vanity) website: my own. And if you're reading this, then I actually figured it out."),
                                    P("When in doubt, I'll force y'all to read the broken source code. I mean, I signed up for *writing* the recap, not making it accessible 😊"),
                                    P(""),
                                    P("Speaking of broken and long term thinking, I'm using this recap preface to wonder: How long until we're all trading away or for future draft picks to maximize championship odds?"),
                                    P("Like if you really want to win a championship, why don't you use 2025 to trade away your best players for tons of premium 2026 draft picks. Then before the 2026 trade deadline, trade out your best 2027 picks for the best players on non-playoff teams? Boom easy >50% championship in just three years of draft picks. Repeat in 2028-2030."),
                                    P(""),
                                    P("And if you don't use this future draft pick trading to condense 3 years or draft capital into 1 superteam, won't you be stuck in Viking purgatory: always solid, but never realistically going to win the championship?"),
                                    P(""),
                                    P("I don't want to be stuck in that purgatory. But I also would prefer to have an above average chance of being competitive and winning the championship every single year. That 'every single year' seems to be coming to an end. I too will eventually bend the knee to the future draft pick superteam gods. Will you?"),
                                    P(""),
                                    P("Said another way: have we seen our last Man Law champion that didn't benefit from (require?) future draft picks?"),
                                    P(""),
                                    P(""),
                                    

                                    H2("Kristian 7W beats Ruble 3W 149.12 to 75.8"),
                                    P(""),
                                    P(""),

                                    H2("Nihal 4W somehow beats Tim 4W 102.18 to 92.66"),
                                    P(""),
                                    P(""),

                                    H2("Joe 6W beats Chris 4W 125.7 to 109.66"),
                                    P(""),
                                    P(""),

                                    H2("Eshaan 5W beats Nathan 6W 124.72 to 100.36"),
                                    P(""),
                                    P(""),

                                    H2("Rob 9W beats Evan 8W 162.98 to 93.5"),
                                    P(""),
                                    P(""),

                                    H2("John 9W beats Clay 7W 105.66 to 102.98"),
                                    P(""),
                                    P(""),

                                    
                                   )), footer

serve()
