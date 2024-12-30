
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random




# Initialize lists for storing scraped data
Image_Source = []
Product_name = []
Total_Rating = []
Total_reviews = []
Total_features = []
Total_price = []
Total_real_price = []
Total_discount = []

def scrape_page(driver):



    # Find all containers
    containers = driver.find_elements(By.CLASS_NAME, "tUxRFH")

    for container in containers:
        # Image Source
        try:
            image = container.find_element(By.CSS_SELECTOR, "img.DByuf4")
            img_src = image.get_attribute("src")
        except:
            img_src = "NA"
        Image_Source.append(img_src)

        # Product Name
        try:
            product_name = container.find_element(By.CLASS_NAME, "KzDlHZ")
            product = product_name.text
        except:
            product = "NA"
        Product_name.append(product)

        # Rating
        try:
            product_rating = container.find_element(By.CLASS_NAME, "XQDdHH")
            rating = product_rating.text
        except:
            rating = "NA"
        Total_Rating.append(rating)

        # Reviews
        try:
            product_reviews = container.find_element(By.CLASS_NAME, "Wphh3N")
            review = product_reviews.text
        except:
            review = "NA"
        Total_reviews.append(review)

        # Features 

        try:
            product_feature = container.find_element(By.CLASS_NAME , "G4BRas")
            feature = product_feature.text
        except:
            feature = "NA"
        Total_features.append(feature)

        # Price
        try:
            product_price = container.find_element(By.CLASS_NAME, "Nx9bqj")
            price = product_price.text
        except:
            price = "NA"
        Total_price.append(price)

        try:
            actual_price = container.find_element(By.CLASS_NAME, "yRaY8j")
            acc_price = actual_price.text
        except:
            acc_price = "NA"
        Total_real_price.append(acc_price)

        # Discount
        try:
            discount = container.find_element(By.CLASS_NAME, "UkUFwK")
            discount_text = discount.text
        except:
            discount_text = "NA"
        Total_discount.append(discount_text)




def click_next_page(driver, wait):
    try:
        # Locate the "Next" link with class name '_9QVEpD' and span text "Next"
        next_button = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@class='_9QVEpD']/span[text()='Next']/..")))

        # Scroll into view of the "Next" button
        ActionChains(driver).move_to_element(next_button).perform()

        # Click on the "Next" button
        next_button.click()

        print("Clicked on the 'Next' button successfully.")
        return True
    except Exception as e:
        print(f"No more 'Next' button found or an error occurred: ")
        return False

def setup():
    # Initialize the webdriver 
    driver = webdriver.Chrome()

    # Open the target webpage
    driver.get("https://www.flipkart.com/search?q=iphone+16+pro&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=iphone+16+pro%7CMobiles&requestId=aceb49d6-6685-4d74-ac26-fdb7d5d9a81f&as-backfill=on&page=1")
    driver.maximize_window()
    return driver





def main():

    driver = setup()

    wait = WebDriverWait(driver, 10)

    try:
        while True:
            # Scrape data from the current page
            scrape_page(driver)

            # Click the "Next" button to go to the next page
            if not click_next_page(driver, wait):
                print("Scraping completed or no more pages available.")
                break

            # Wait for the next page to load
            time.sleep(random.uniform(2, 4))

    finally:
        driver.quit()


        df = pd.DataFrame({"Product Names": Product_name ,"Ratings": Total_Rating , 
                           "Reviews": Total_reviews , "Features": Total_features,"Prices": Total_price,
                           "Actual Prices": Total_real_price , "Discounts": Total_discount , "Image Sources": Image_Source})
        df.to_csv("scraped_data.csv", index=False)
        print("Data saved to scraped_data.csv")

if __name__ == "__main__":
    main()
