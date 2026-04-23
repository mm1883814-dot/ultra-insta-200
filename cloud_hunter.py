import requests, random, os, time
from concurrent.futures import ThreadPoolExecutor

# بياناتك
TOKEN = "8712712886:AAFVD_aNqeRNcG_9Bjo2B5wel-KRMyJn4ME"
ID = "719829268"

def load_proxies():
    with open("proxies.txt", "r") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

all_proxies = load_proxies()
letters = "abcdefghijklmnopqrstuvwxyz0123456789._"

def generate_user():
    # توليد يوزر خماسي ذكي
    user = "".join(random.choice(letters) for _ in range(5))
    if user.startswith(('.', '_')) or user.endswith(('.', '_')) or ".." in user:
        return generate_user()
    return user

def check(user):
    proxy = random.choice(all_proxies)
    try:
        # المراقبة التي ستراها في المتصفح
        print(f"[*] Checking: {user} | Using Proxy: {proxy[:15]}...")
        url = f"https://www.instagram.com/{user}/"
        r = requests.get(url, proxies={"http": f"http://{proxy}", "https": f"http://{proxy}"}, timeout=2)
        if r.status_code == 404:
            requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                          json={"chat_id": ID, "text": f"✅ صيد سحابي بروكسي: @{user}"})
    except: pass

def start():
    # قوة 200 خيط في السحاب
    with ThreadPoolExecutor(max_workers=200) as executor:
        while True:
            executor.submit(check, generate_user())

if __name__ == "__main__":
    start()
