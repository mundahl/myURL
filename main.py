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
                                    P("Speaking of broken and long term thinking, I'm using this recap preface to wonder: How long until we're all trading away -- or for -- future draft picks to maximize championship odds?"),
                                    P("Like if you really want to win a championship, why don't you use 2025 to trade away your best players for tons of premium 2026 draft picks. Then before the 2026 trade deadline, cash in your best 2027 picks for the best players on non-playoff teams? Boom easy >50% championship in just three years of draft picks. Repeat in 2028-2030."),
                                    P(""),
                                    P("And if you don't use this future draft pick trading to condense 3 years or draft capital into 1 superteam, won't you be stuck in Viking purgatory: always solid, but never realistically going to win the championship?"),
                                    P(""),
                                    P("I don't want to be stuck in that purgatory. But I also would prefer to have an above average chance of being competitive and winning the championship every single year. That 'every single year' seems to be coming to an end. I too will eventually bend the knee to the future draft pick superteam gods. Will you?"),
                                    P(""),
                                    P("Said another way: have we seen our last Man Law champion that didn't benefit from (require?) future draft picks?"),
                                    P(""),
                                    P(""),
                                    

                                    H2("Kristian 7W beats Ruble 3W 149.12 to 75.8"),
                                    P("Ranking 5th on the SNICKERS power ranks, Kristian seems to have accepted the Vikings ~solid~ purgatory. He'll make the playoffs (or miss it tragically) but without Rashee Rice or future draft pick reinforcements, does he have a chance of winning the 'ship?"),
                                    P("Starting and STILL 12th on the SNICKERS power ranks, Ruble has rejected purgatory and looks to be using his extra 2nd (or 4th), 3rd, 7th, and 9th draft picks to start a 2025 super team. If Ruble's team is indeed strong next year, any bets on how much 2026 draft capital he'll sacrifice to boost championship odds?"),

                                    H2("Nihal 4W somehow beats Tim 4W 102.18 to 92.66"),
                                    P("Starting and STILL 11th on the SNICKERS power ranks, Nihal successfully rejected purgatory last year by trading his 2024 6th for De'Von Achane and eeking out a championship win! This year he's reseting and has an extra 3rd (or 5th), 4th, and 10th for next year. Maybe he and Ruble will be the Yankees-Dodgers of next year."),
                                    P("Tim has slid to 9th in the power ranks. He's in a funny position as a 'franchise'. He hasn't done much (any?) future draft pick trading, but he'll miss his second playoff in a row. Not sure if Tim is too nice or perfectly rational to lean on future draft picks to shovel him out of his hole."),

                                    H2("Joe 6W beats Chris 4W 125.7 to 109.66"),
                                    P("Joe's team did an impressive march from 10th to 6th in the power ranks. If it weren't for injuries, I'd expect his championship chances to be much higher. Why? He had an extra 6th this year and added Bucky Irving at the deadlin. But instead, the truest Vikings fan will likely accept the truest Vikings outcome: purgatory."),
                                    P("Chris may have slipped to 10th in the SNICKERS power ranks and not traded for any future draft picks, BUT he's no stranger to the trade. We all saw Chris losing this round of musical chairs since no trading partners were left at the deadline. Also, Chris did lose his 4th and 10th rounders in 2025 to gain JK Dobbins and Nick Chubb. I cryptically commented 🐑🪒 by which I predicted that Chris got 'fleeced'. Turned out right 😕 Also! Chris likely enabled the first champion to benefit from the future draft picks trade: In 2021, Chris traded his 4th rounder for Elijah Mitchell at the deadline. The partner softened the pick to a 5th rounder, drafted Mahomes (when he was great), and marched to the championship: Me 😈"),

                                    H2("Eshaan 5W beats Nathan 6W 124.72 to 100.36"),
                                    P("Eshaan has slipped from 2nd to 8th in the power ranks and showed the - or at least my - main downside to the strategy of future draft pick superteams: time. Trading players takes time. Coordinating, hangling, committing, communicating etc. It's surely more work than Esh would like to put into this. Maybe there's a better way."),
                                    P("Starting 4th but slipping to 7th, Nathan's franchise seems to be following both Kristian and Eshaan. He savvily traded only a 9th for Chase Brown, but he'll either make or tragically miss the playoffs. Sounds like purgatory, no? Well, maybe not quite - or at least that's not the intention: In addition to the Chase Brown trade, Guggs invests time in scheming up trades throughout the season! Early on, he inquired about two of my RBs. I saw it a few days later (too late?) and forgot to respond. Sorry Guggs!"),

                                    H2("Rob 9W beats Evan 8W 162.98 to 93.5"),
                                    P("Futures trades need someone to benefit now. These two teams are *the* two teams swinging for the superteam fences. Maybe championship preview?"),
                                    P("Rob has climbed up 6 spots to 1st overall. He's only made 5 roster changes, but two of those were for studs Lamar Jackson and AJ Brown. (Love the conditional arrangement btw.) "),
                                    P("Evan has climbed up 4 spots to 2nd overall. He's ran a juggernaught of a team all season and doubled down to get DK Metcalf for a 3rd and Cooper Kupp for a 7th. Despite 2nd in the power ranks, I'm probably most scared to maybe play him in the playoffs."),

                                    H2("John 9W beats Clay 7W 105.66 to 102.98"),
                                    P("John has climbed up 6 spots to 3rd overall. He has 9Wins, but does he have a snowball's chance in hell to beat Rob or Evan? His last two wins have been by <3pts each. He claims it'd be super fun to be the last 'natural champion, but that seems unlikely..."),
                                    P("Clay got to start the season with the #1 overall power rank and has slipped to 4th. He would have crushed John if half his team wasn't on bye. But does it matter? He won back-to-back championships during the pandemic and both (?) were without future draft picks I think. Kudos! Coast into the playoffs, give it a go, and most likely: pack it up and plan your next push."),

                                    
                                   )), footer

serve()
