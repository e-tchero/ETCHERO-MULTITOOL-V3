import random
import sys
import os
import time

try:
    from colorama import Fore, init
    init(autoreset=True)
except ImportError:
    # Fallback if colorama is not installed
    class Fore:
        GREEN = ""
        RED = ""
        YELLOW = ""
        CYAN = ""
        WHITE = ""
    def init(**kwargs): pass

# Embedded mini-dataset (Top common passwords + patterns for "training" simulation)
# In a real scenario, this would load from a large rockyou.txt
DEFAULT_TRAINING_DATA = [
    "123456", "password", "12345678", "qwerty", "123456789", "12345", "1234567", "111111", "123123", "987654321",
    "iloveyou", "admin", "1234567890", "monkey", "dragon", "123321", "password123", "sunshine", "princess",
    "charlie", "donald", "shadow", "master", "football", "baseball", "michael", "jennifer", "superman",
    "letmein", "yamaha", "michelle", "daniel", "jessica", "justin", "battery", "camera", "hacker", "trustno1",
    "killer", "system", "matrix", "cisco", "ninja", "pirate", "security", "linux", "python", "google",
    "facebook", "twitter", "instagram", "snapchat", "youtube", "netflix", "spotify", "amazon", "apple",
    "samsung", "huawei", "xiaomi", "oneplus", "nokia", "sony", "nintendo", "xbox", "playstation", "fortnite",
    "minecraft", "roblox", "pokemon", "pikachu", "naruto", "goku", "luffy", "zoro", "nami", "sasuke", "sakura",
    "kakashi", "itachi", "madara", "obito", "hinata", "minato", "jiraiya", "tsunade", "orochimaru", "gaara",
    "rocklee", "shikamaru", "ino", "choji", "neji", "tenten", "kiba", "shino", "kankuro", "temari",
    "supersecret", "canttouchthis", "tryharder", "youwontguess", "correcthorsebatterystaple"
]

class MarkovPassGAN:
    def __init__(self, order=2):
        self.order = order
        self.chain = {}
        self.starts = []

    def train(self, passwords):
        """Builds the Markov chain from a list of passwords."""
        print(f"{Fore.YELLOW}[*] Training model on {len(passwords)} samples...")
        for p in passwords:
            if len(p) < self.order:
                continue
            
            # Record valid starting sequences
            self.starts.append(p[:self.order])
            
            # Build chain
            for i in range(len(p) - self.order):
                gram = p[i:i+self.order]
                next_char = p[i+self.order]
                
                if gram not in self.chain:
                    self.chain[gram] = []
                self.chain[gram].append(next_char)
        
        print(f"{Fore.GREEN}[+] Training complete. Learned {len(self.chain)} patterns.")

    def generate(self, max_length=12):
        """Generates a password using the trained model."""
        if not self.chain:
            return "Error: Model not trained"
        
        current_gram = random.choice(self.starts)
        password = current_gram
        
        while len(password) < max_length:
            if current_gram not in self.chain:
                break
            
            next_char = random.choice(self.chain[current_gram])
            password += next_char
            current_gram = password[-self.order:]
            
        return password

def banner():
    print(rf"""{Fore.CYAN}
    ____                   ____  ___    _   __
   / __ \____ ____________/ __ \/   |  / | / /
  / /_/ / __ `/ ___/ ___/ / / / /| | /  |/ / 
 / ____/ /_/ (__  |__  ) /_/ / ___ |/ /|  /  
/_/    \__,_/____/____/\____/_/  |_/_/ |_/   
                                             
      {Fore.WHITE}AI-Powered Password Generator (Markov Chain)
    """)

def main():
    banner()
    
    print(f"{Fore.YELLOW}[1] Use Built-in Dataset (Lite Mode)")
    print(f"{Fore.YELLOW}[2] Train on Custom Wordlist (Advanced)")
    
    choice = input(f"\n{Fore.GREEN}Select option: ")
    
    passwords = []
    
    if choice == '2':
        path = input(f"{Fore.YELLOW}Enter path to wordlist (e.g., rockyou.txt): ").strip('"')
        if os.path.exists(path):
            try:
                with open(path, 'r', encoding='latin-1') as f:
                    passwords = [line.strip() for line in f if line.strip()]
            except Exception as e:
                print(f"{Fore.RED}[!] Error reading file: {e}")
                return
        else:
            print(f"{Fore.RED}[!] File not found. Using built-in dataset.")
            passwords = DEFAULT_TRAINING_DATA
    else:
        passwords = DEFAULT_TRAINING_DATA

    # Initialize and Train
    gan = MarkovPassGAN(order=2) # 2-gram Markov Chain
    gan.train(passwords)
    
    while True:
        try:
            count = int(input(f"\n{Fore.YELLOW}How many passwords to generate? (0 to exit): "))
            if count == 0:
                break
            
            length = int(input(f"{Fore.YELLOW}Max length per password (default 12): ") or 12)
            
            print(f"\n{Fore.CYAN}--- Generated Passwords ---")
            for _ in range(count):
                pw = gan.generate(length)
                print(f"{Fore.WHITE}{pw}")
            print(f"{Fore.CYAN}---------------------------")
            
        except ValueError:
            print(f"{Fore.RED}[!] Invalid input")

if __name__ == "__main__":
    main()
