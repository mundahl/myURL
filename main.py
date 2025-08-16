from fasthtml.common import *
from fasthtml.components import Article, Aside, Span, Ul, Li
from datetime import datetime
import base64
from pathlib import Path
import markdown
import re
from typing import Optional
import os

home_title = 'Mundahl Makes Moves'

_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="100%" height="100%" fill="#01659A"/><text x="50%" y="50%" font-family="Garamond, Palatino, serif" font-weight="700" font-size="34" fill="#fff" text-anchor="middle" dominant-baseline="middle">JM</text></svg>'''
_favicon_data = base64.b64encode(_svg.encode('utf-8')).decode('ascii')
favicon = Link(rel="icon", href=f"data:image/svg+xml;base64,{_favicon_data}")

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

category_colors = {
    "note": "#01659A",
    "essay": "#546E7A",
    "link": "#00897B"
}

def get_category_span(category):
    if not category: return ""
    color = category_colors.get(category.lower(), "#607D8B")
    return Span(category, style=f"background-color: {color}; color: white; padding: 2px 8px; border-radius: 4px; font-size: 0.75em; margin-left: 8px; vertical-align: middle;")


def get_jottings():
    jottings_dir = Path("jottings")
    if not jottings_dir.is_dir():
        return []
    # Sort by filename, newest first, assuming YYYY-MM-DD.md format
    md_files = sorted(jottings_dir.glob("*.md"), key=lambda p: p.name, reverse=True)
    jottings = []
    for md_file in md_files:
        lines = md_file.read_text(encoding='utf-8').splitlines()
        
        metadata = {}
        content_start_index = 0
        for i, line in enumerate(lines):
            if re.match(r"^\w+:", line):
                key, value = line.split(":", 1)
                metadata[key.strip()] = value.strip()
            else:
                content_start_index = i
                break
        else: # if all lines are metadata
            content_start_index = len(lines)

        # trim blank lines between metadata and content
        while content_start_index < len(lines) and not lines[content_start_index].strip():
            content_start_index += 1

        content = '\n'.join(lines[content_start_index:])
        
        # title is first H1
        title_match = re.search(r"^#\s+(.*)", content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else md_file.stem.replace('-', ' ').title()
        date_str = md_file.stem if re.match(r"^\d{4}-\d{2}-\d{2}$", md_file.stem) else None
        
        jottings.append({
            "path": md_file,
            "title": title,
            "content": content,
            "slug": metadata.get("slug"),
            "category": metadata.get("category"),
            "date": date_str,
        })
    return jottings

@app.get("/")
def homepage():
    md_path = Path("johnmundahl/hello.md")
    style_home = Style("""
.hello-md-content img { width: 30%; height: auto; display: block; margin: 1rem auto; }
""")
    if md_path.is_file():
        md = markdown.Markdown(extensions=['fenced_code'])
        content_html = md.convert(md_path.read_text(encoding='utf-8'))
        main = Main(nav, Hr(), Div(cls="container")(Div(cls="hello-md-content")(Article(NotStr(content_html)))))
    else:
        main = Main(nav, Hr(), Div(cls="container")(H1("Welcome"), P("Could not find johnmundahl/hello.md")))
    return Title(home_title), favicon, style_home, main, footer

@app.get("/jottings")
@app.get("/jottings/{slug}")
def jottings_page(slug: Optional[str] = None):
    all_jottings = get_jottings()
    if not all_jottings:
        return Title(jot_title), favicon, Main(nav, Hr(), Div(cls="container")(H1("Jottings"), P("No jottings yet."))), footer

    if slug:
        selected_jotting_list = [j for j in all_jottings if j['slug'] == slug]
        selected_jotting = selected_jotting_list[0] if selected_jotting_list else all_jottings[0]
    else:
        selected_jotting = all_jottings[0]

    md = markdown.Markdown(extensions=['fenced_code'])
    content_html = md.convert(selected_jotting['content'])

    sidebar_links = Ul(*[
        Li(
            A(j['title'], href=f"/jottings/{j['slug']}"),
            Span(j['date'], style="color: #777; font-size: 0.8em; margin-left: 8px; margin-right: 8px;") if j.get('date') else "",
            get_category_span(j['category'])
        )
        for j in all_jottings if j['slug']
    ])

    main_content = Article(
        NotStr(content_html)
    )

    page_layout = Div(cls="grid", style="grid-template-columns: 3fr 1fr; gap: 2rem;")(
        main_content,
        Aside(H4("Jottings"), sidebar_links)
    )

    return Title(f"{selected_jotting['title']} - {jot_title}"), favicon, Main(nav, Hr(), Div(cls="container")(page_layout)), footer

@app.get("/makings")
def makings_page():
    return Title(make_title), favicon, Main(nav, Hr(), Div(cls="container")(H1("Makings"), P("Under construction."))), footer

@app.get("/joinme")
def joinme_page():
    return Title(joinme_title), favicon, Main(nav, Hr(), Div(cls="container")
                                   (H1(A("Message Me", href="mailto:john.mundahl@gmail.com")), 
                                    P("Self-expression is powerful. Every bit attracts better-matched people who I'd love to interact with."),
                                    P("That's probably you. So message me. Or accept stasis."),
                                    P("Email me at firstname.lastname@gmail.com"))
                                   ), footer

serve()
