from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://realpython.github.io/fake-jobs/"


def scrape_jobs():
    driver = webdriver.Chrome()
    try:
        driver.get(URL)

        # Wait up to 10 seconds for the job list to appear
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ResultsContainer"))
        )

        cards = driver.find_elements(By.CSS_SELECTOR, "div.card-content")

        jobs = []
        for card in cards:
            jobs.append({
                "title": card.find_element(By.CSS_SELECTOR, "h2.title").text,
                "company": card.find_element(By.CSS_SELECTOR, "h3.company").text,
                "location": card.find_element(By.CSS_SELECTOR, "p.location").text,
                "date": card.find_element(By.CSS_SELECTOR, "time").text,
            })
        return jobs
    finally:
        driver.quit()  # always close the browser, even if an error happens


if __name__ == "__main__":
    jobs = scrape_jobs()
    print("Jobs found:", len(jobs))
    for job in jobs[:3]:
        print(job)