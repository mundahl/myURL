from fasthtml.common import *

app, rt = fast_app()

@rt('/')
def get():
    return Html(
        Head(
            Title('Custom Page'),
            Meta(charset="utf-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1"),
            Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@latest/css/pico.min.css"),
            Link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css"),
            Style(
                '''
                body { font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; }
                .navbar {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    padding: 10px;
                    width: 100%;
                    box-sizing: border-box;
                    border-bottom: 1px solid #ccc;
                }

                .nav-right {
                    display: flex;
                    justify-content: flex-end;
                    gap: 15px;
                }

                .hamburger-menu {
                    display: none; /* Hide hamburger menu by default */
                    font-size: 1.5em;
                    cursor: pointer;
                }

                /* Hide the normal menu and show the hamburger on small screens */
                @media (max-width: 768px) {
                    .nav-right {
                        display: none;
                    }
                    .hamburger-menu {
                        display: block;
                    }
                }

                /* Dropdown menu styling */
                .dropdown-menu {
                    display: none;
                    flex-direction: column;
                    gap: 10px;
                    position: absolute;
                    background-color: white;
                    padding: 10px;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                    top: 50px; /* Adjust according to your navbar height */
                    right: 10px;
                }

                .dropdown-menu.show {
                    display: flex;
                }

                .nav-left { 
                    color: #333; 
                    text-decoration: none; 
                    padding: 5px 10px; 
                    font-size: 200%; /* 100% larger than default */
                    font-weight: bold;
                }

                .nav-link { 
                    color: #333; 
                    text-decoration: none; 
                    padding: 5px 10px; 
                }
                .nav-link:hover { 
                    background-color: #ddd; 
                }
                .profile-img { 
                    width: 150px; 
                    height: 150px; 
                    border-radius: 50%; 
                    object-fit: cover; 
                }
                .page-container { 
                    display: flex; 
                    justify-content: space-between; 
                    max-width: 1000px; 
                    margin: 0 auto; 
                }
                .content-section { 
                    flex-grow: 1; 
                    padding-left: 20px; 
                }
                '''
            )
        ),
        Body(
            Nav(
                Div("John Mundahl", _class="nav-left"),
                Div(
                    A('Home', href="/", _class="nav-link"),
                    A('Articles', href="/articles", _class="nav-link"),
                    A('Podcast Notes', href="/podnotes", _class="nav-link"),
                    A('Contact', href="/contact", _class="nav-link"),
                    _class="nav-right"
                ),
                _class="navbar"
            )
        )
    )

serve()
