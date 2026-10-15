import pandas as pd
from datetime import date
from scraper import scrape_jobs


def clean_jobs(jobs):
    df = pd.DataFrame(jobs)

    # 1. Trim extra spaces from the text columns
    for col in ["title", "company", "location"]:
        df[col] = df[col].str.strip()

    # 2. Turn the date text into real dates (bad ones become empty)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # 3. Drop rows missing important values
    df = df.dropna(subset=["title", "company", "date"])

    # 4. Remove duplicate postings
    df = df.drop_duplicates(subset=["title", "company", "location", "date"])

    # 5. Store the date as plain text like 2021-04-08 (easy for SQLite)
    df["date"] = df["date"].dt.strftime("%Y-%m-%d")

    # 6. Record the day we scraped it, to count "new postings" later
    df["scraped_date"] = date.today().isoformat()

    return df


if __name__ == "__main__":
    raw = scrape_jobs()
    clean = clean_jobs(raw)
    print("Before cleaning:", len(raw))
    print("After cleaning:", len(clean))
    print(clean.head())