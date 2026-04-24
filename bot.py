import os
import asyncio
import requests
from playwright.async_api import async_playwright

# GitHub Secrets se information uthana
TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
JAZZ_NUM = os.environ.get("JAZZ_NUMBER")

def send_to_telegram(text):
    # Sukuna Bot aapko message bhejay ga
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}"
    requests.get(url)

def get_otp_from_telegram():
    # Ye aapke reply ka wait karega
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    last_id = -1
    print("Sukuna is waiting for OTP on Telegram...")
    while True:
        try:
            data = requests.get(url).json()
            if data["result"]:
                msg = data["result"][-1]
                if msg["update_id"] > last_id:
                    text = msg["message"]["text"]
                    if text.isdigit():
                        return text
        except:
            pass
        asyncio.sleep(2)

async def run_bot():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        try:
            print("Opening JazzDrive...")
            await page.goto("https://jazzdrive.com.pk/login")
            
            # Entering Number
            await page.fill("input[type='tel']", JAZZ_NUM)
            await page.click("button[type='submit']")
            
            # Sending message to you
            send_to_telegram(f"Kareem bhai, Sukuna is ready! JazzDrive ne OTP bheja hai. Jaldi se yahan OTP likh kar send karein:")
            
            # Waiting for your reply on Telegram
            otp = get_otp_from_telegram()
            
            # Entering OTP
            await page.fill("input[name='otp']", otp)
            await page.click("button#login-btn")
            
            send_to_telegram("Sukuna says: Login Successful! ✅")
            
        except Exception as e:
            send_to_telegram(f"Error: {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(run_bot())
