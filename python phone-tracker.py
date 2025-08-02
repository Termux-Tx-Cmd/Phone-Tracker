#!/usr/bin/env python3

import os
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import webbrowser

# ---------- 🔥 BANNER ---------- #
def banner():
    os.system("clear")
    print("\033[1;32m" + "="*60)
    print("███╗░░░███╗░█████╗░██╗██╗░░░██╗███╗░░░███╗  ████████╗██╗░░██╗".center(60))
    print("████╗░████║██╔══██╗██║██║░░░██║████╗░████║  ╚══██╔══╝╚██╗██╔╝".center(60))
    print("██╔████╔██║██║░░██║██║██║░░░██║██╔████╔██║  ░░░██║░░░░╚███╔╝░".center(60))
    print("██║╚██╔╝██║██║░░██║██║██║░░░██║██║╚██╔╝██║  ░░░██║░░░░██╔██╗░".center(60))
    print("██║░╚═╝░██║╚█████╔╝██║╚██████╔╝██║░╚═╝░██║  ░░░██║░░░██╔╝╚██╗".center(60))
    print("╚═╝░░░░░╚═╝░╚════╝░╚═╝░╚═════╝░╚═╝░░░░░╚═╝  ░░░╚═╝░░░╚═╝░░╚═╝".center(60))
    print("\033[1;33m" + "-"*60)
    print("📲 Termux Tx Cmd | Developer: Mahim".center(60))
    print("-"*60 + "\033[0m")

# ---------- 🌐 AUTO OPEN PAGE ---------- #
def open_page():
    webbrowser.open("https://www.facebook.com/share/16JmHprSe1/")

# ---------- 📞 MAIN TOOL ---------- #
def main():
    banner()
    open_page()

    try:
        number = input("\033[1;36m🔢 Enter phone number with country code (e.g. +8801XXXXXXXXX): \033[0m")
        parsed = phonenumbers.parse(number)

        location = geocoder.description_for_number(parsed, 'en')
        sim = carrier.name_for_number(parsed, 'en')
        zone = timezone.time_zones_for_number(parsed)
        map_link = f"https://www.google.com/maps/search/{location}"

        print("\n\033[1;35m📍 Location :\033[0m", location)
        print("\033[1;34m📡 Carrier  :\033[0m", sim)
        print("\033[1;32m🕓 Timezone :\033[0m", zone)
        print("\033[1;36m🌐 Map Link :\033[0m", map_link)

    except:
        print("\n\033[1;31m❌ Invalid number format! Please try again.\033[0m")

if __name__ == "__main__":
    main()
