import pyfiglet


def render_art(name: str):
    ascii_banner = pyfiglet.figlet_format(name)
    print(ascii_banner)


if __name__ == "__main__":
    render_art("AI DEV 2026")
