import os
import sys
import hashlib
import time

# === Anti-Theft Protection ===


if os.path.basename(os.getcwd()) != "ETCHERO-MULTITOOL-V3":
    sys.exit("🚫 Unauthorized clone detected. Exiting...")

if os.path.basename(__file__) != "ETCHERO.py":
    sys.exit("⚠️ Cloning or Renaming Detected. Exiting...")

def _check_security(k):
    # SHA-256 hash of "ETCHERO123"
    # Splitting the hash to prevent simple string searches
    part1 = "f1ff0437bd4176d28c6f4c294e1f8ff"
    part2 = "71e6459ee0e75bb93e7ee0debc01c95e5"
    target = part1 + part2
    
    hashed_input = hashlib.sha256(k.encode()).hexdigest()
    return hashed_input == target

key = input("🔑 Enter unlock key: ")

print("Verifying key...")
time.sleep(1.5) # Fake delay for security theater

if not _check_security(key):
    sys.exit("❌ Wrong key. Access denied.")

BRAND = "by ABDULHAMEED AMIN"
if BRAND not in "by ABDULHAMEED AMIN":
    sys.exit("🚫 Branding removed. Tool crashed.")

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""\033[1;32m
███████╗████████╗░█████╗░██╗░░██╗███████╗██████╗░░█████╗░
██╔════╝╚══██╔══╝██╔══██╗██║░░██║██╔════╝██╔══██╗██╔══██╗
█████╗░░░░░██║░░░██║░░╚═╝███████║█████╗░░██████╔╝██║░░██║
██╔══╝░░░░░██║░░░██║░░██╗██╔══██║██╔══╝░░██╔══██╗██║░░██║
███████╗░░░██║░░░╚█████╔╝██║░░██║███████╗██║░░██║╚█████╔╝
╚══════╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░╚════╝░
\033[0m
      ETCHERO MULTITOOL v3.0 - by ABDULHAMEED AMIN
""")

def menu():
    print("""
[1] Spam Link Tester
[2] WhatsApp Toolkit
[3] Telegram Bot Notifier
[4] Fake Virus Scanner
[5] Website Header Viewer
[6] Google Dorker
[7] Directory Bruteforcer
[8] Link Shortener
[9] System Info Tool
[10] Update Checker
[11] SMS Bomber
[12] IP Tracker
[13] Password Generator
[14] Email Verifier
[15] Network Scanner
[16] Port Scanner
[17] Whois Lookup
[18] Subdomain Finder
[19] DNS Lookup
[20] GeoIP Locator
[21] WiFi Password Grabber
[22] Image Metadata Extractor
[23] Hash Generator & Identifier
[24] PassGAN (AI Password Gen)
[0] Exit
""")

def run_tool(choice):
    if choice == '0':
        exit()
    try:
        tool_map = {
            str(i): f"python tools/{name}.py" for i, name in enumerate([
                "spam_tester",
                "whatsapp_toolkit",
                "telegram_bot_notifier",
                "fake_virus_scanner",
                "website_header_viewer",
                "google_dorker",
                "directory_bruteforcer",
                "link_shortener",
                "system_info_tool",
                "update_checker",
                "sms_bomber",
                "ip_tracker",
                "password_generator",
                "email_verifier",
                "network_scanner",
                "port_scanner",
                "whois_lookup",
                "subdomain_finder",
                "dns_lookup",
                "geoip_locator",
                "wifi_password_grabber",
                "image_metadata_extractor",
                "hash_tool",
                "passgan"
            ], 1)
        }
        os.system(tool_map[choice])
    except KeyError:
        print("Invalid option!")

if __name__ == "__main__":
    banner()
    while True:
        menu()
        choice = input("Select an option: ")
        run_tool(choice)
