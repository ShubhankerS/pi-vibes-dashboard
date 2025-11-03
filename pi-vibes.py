from modules import system_info, weather, quote, ascii_art
from rich.console import Console
from rich.panel import Panel

console = Console()

def main():
    console.clear()
    console.rule("[bold yellow]🌞  PI-VIBES DASHBOARD  🌞")

    # System Info
    sysinfo = system_info.get_info()
    console.print(Panel(sysinfo, title="🖥️  System Info"))

    # Weather
    weather_info = weather.get_weather()
    console.print(Panel(weather_info, title="🌦️  Weather"))

    # Quote
    quote_text = quote.get_quote()
    console.print(Panel(quote_text, title="🧠  Quote of the Moment"))

    # ASCII Mood
    art = ascii_art.get_random_art()
    console.print(Panel(art, title="🌱  Today's Vibe"))

if __name__ == "__main__":
    main()
