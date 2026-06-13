#importing libraries 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import pandas as pd


def track_price():

    url = input("Enter Amazon Product URL: ").strip()

    driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))

    driver.get(url)
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    title = soup.find("title")

    if title:
        print("\nProduct Title:")
        print(title.text)
    else:
        print("Title not found")

    price = soup.find("span", class_="a-price-whole")

    if price:
        current_price = ''.join(ch for ch in price.text
        if ch.isdigit()
)
    else:
        print("Price not found")

    print("\nPrice:")
    print(current_price)

    data = pd.DataFrame([
        {
            "Product": title.text,
            "Price": current_price
        }
    ])

    try:
        old_data = pd.read_csv("prices.csv",names=["Product", "Price"])

        if len(old_data) > 0:   
            last_price = float(str(old_data.iloc[-1]["Price"]).replace(",", "").strip())

        current_price_int = int(current_price)

        #displaying changes (if any) or just current data
        print(f"\nLast Price: {last_price}")
        print(f"Current Price: {current_price_int}")

        #Price change decoding(dropped/increased/unchanged) 
        if current_price_int < last_price:
            status = "\nPRICE DROPPED! 🔥"
            print(status)

        elif current_price_int > last_price:
            status = "\nPrice Increased 📈"
            print(status)

        else:
            status = "\nPrice Unchanged ➖"
            print(status)

    except Exception as e:
        print("Comparison Error:", e)

    data.to_csv("prices.csv", mode="a", header=False, index=False)

    #confirmation for task done 
    print("\nSaved to prices.csv")
    
    driver.quit()

def get_product_info(url):

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    driver.get(url)
    time.sleep(2)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    title = soup.find("title")

    if title:
        product_title = title.text
    else:
        product_title = "Title Not Found"

    price = soup.find("span", class_="a-price-whole")

    if price:
        current_price = ''.join(
            ch for ch in price.text
            if ch.isdigit()
        )
    else:
        current_price = "0"

    # Default status
    status = "First Record 🆕"

    try:

        old_data = pd.read_csv(
            "prices.csv",
            names=["Product", "Price"]
        )

        if len(old_data) > 0:

            last_price = float(
                str(old_data.iloc[-1]["Price"])
                .replace(",", "")
                .replace(".", "")
                .strip()
            )

            current_price_int = int(current_price)

            if current_price_int < last_price:
                status = "PRICE DROPPED! 🔥"

            elif current_price_int > last_price:
                status = "Price Increased 📈"

            else:
                status = "Price Unchanged ➖"

    except Exception:
        pass

    # Save latest price
    data = pd.DataFrame([
        {
            "Product": product_title,
            "Price": current_price
        }
    ])

    data.to_csv(
        "prices.csv",
        mode="a",
        header=False,
        index=False
    )

    driver.quit()

    return product_title, current_price, status

#https://www.amazon.in/dp/B0F7Y54PJX