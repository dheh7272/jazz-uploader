import os
import asyncio
import nest_asyncio
from playwright.async_api import async_playwright

# Nest asyncio for handling event loops
nest_asyncio.apply()

async def run_bot():
    # Aapka number GitHub Secrets se uthayega
    jazz_number = os.environ.get("JAZZ_NUMBER")
    
    if not jazz_number:
        print("Ghalati: JAZZ_NUMBER nahi mila. Please Settings mein Secret add karein.")
        return

    async with async_playwright() as p:
        print("Bot shuru ho raha hai...")
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        try:
            # JazzDrive ya login page par jana
            print(f"Logging in with: {jazz_number}")
            await page.goto("https://jazzdrive.com.pk/login") # Yahan apni asli URL check kar lein
            
            # Login ka baki code jo aapne pehle banaya tha wo yahan aayega
            # Filhal ye bot ko login ki koshish dikhayega
            
            print("Bot kamyabi se chal raha hai!")
            
        except Exception as e:
            print(f"Error aaya: {e}")
        
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(run_bot())
