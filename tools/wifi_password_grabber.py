import subprocess
import re
import os
import platform

def get_wifi_passwords():
    print("\n=== WiFi Password Grabber ===")
    
    if platform.system() == "Windows":
        try:
            # Windows Implementation
            profiles_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="ignore")
            profiles = re.findall(r"All User Profile\s*:\s*(.*)", profiles_data)
            
            if not profiles:
                print("[-] No WiFi profiles found.")
                return

            print(f"[+] Found {len(profiles)} profiles. Extracting passwords...\n")
            print(f"{'WiFi Name (SSID)':<30} | {'Password'}")
            print("-" * 50)

            for profile in profiles:
                profile = profile.strip()
                try:
                    profile_info = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8', errors="ignore")
                    password_match = re.search(r"Key Content\s*:\s*(.*)", profile_info)
                    
                    if password_match:
                        password = password_match.group(1)
                    else:
                        password = "[None / Open]"
                    
                    print(f"{profile:<30} | {password}")
                except subprocess.CalledProcessError:
                    print(f"{profile:<30} | [Error accessing profile]")

        except Exception as e:
            print(f"[-] An error occurred: {e}")

    elif os.path.exists("/data/misc/wifi/wpa_supplicant.conf"):
        # Android (Rooted) Implementation
        print("[*] Android system detected. Attempting to read wpa_supplicant.conf (Root required)...")
        try:
            with open("/data/misc/wifi/wpa_supplicant.conf", "r") as f:
                data = f.read()
                
            networks = re.findall(r'network={([^}]*)}', data, re.DOTALL)
            print(f"{'WiFi Name (SSID)':<30} | {'Password'}")
            print("-" * 50)
            
            for net in networks:
                ssid_match = re.search(r'ssid="(.*)"', net)
                psk_match = re.search(r'psk="(.*)"', net)
                
                if ssid_match:
                    ssid = ssid_match.group(1)
                    psk = psk_match.group(1) if psk_match else "[None / Open]"
                    print(f"{ssid:<30} | {psk}")
                    
        except PermissionError:
            print("[-] Permission Denied! You need Root access to read WiFi passwords on Android.")
            print("[-] Try running as root: 'su -c python tools/wifi_password_grabber.py'")
        except Exception as e:
             print(f"[-] An error occurred: {e}")
             
    else:
        print("[-] This tool is optimized for Windows or Rooted Android.")
        print("[-] On non-rooted Android/Termux, direct WiFi password access is restricted by the OS.")

if __name__ == "__main__":
    get_wifi_passwords()
    input("\nPress Enter to return to menu...")
