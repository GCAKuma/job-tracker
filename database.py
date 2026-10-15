import sqlite3
from scraper import scrape_jobs
from cleaner import clean_jobs

DB_NAME = "jobs.db"


def create_table(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS postings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            company TEXT NOT NULL,
            location TEXT,
            date TEXT NOT NULL,
            scraped_date TEXT NOT NULL,
            UNIQUE (title, company, location, date)
        )
    """)


def save_jobs(df):
    conn = sqlite3.connect(DB_NAME)
    create_table(conn)

    before = conn.execute("SELECT COUNT(*) FROM postings").fetchone()[0]

    for row in df.itertuples(index=False):
        conn.execute(
            "INSERT OR IGNORE INTO postings "
            "(title, company, location, date, scraped_date) "
            "VALUES (?, ?, ?, ?, ?)",
            (row.title, row.company, row.location, row.date, row.scraped_date),
        )
    conn.commit()

    after = conn.execute("SELECT COUNT(*) FROM postings").fetchone()[0]
    conn.close()
    return after - before


if __name__ == "__main__":
    jobs = scrape_jobs()
    df = clean_jobs(jobs)
    new_count = save_jobs(df)
    print("Scraped:", len(df))
    print("New postings saved:", new_count)