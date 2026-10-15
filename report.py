import sqlite3

DB_NAME = "jobs.db"

# Skills to look for in job titles
SKILLS = ["python", "engineer", "developer", "manager", "analyst", "designer"]


def run_report():
    conn = sqlite3.connect(DB_NAME)

    total = conn.execute("SELECT COUNT(*) FROM postings").fetchone()[0]
    print("=== JOB POSTING REPORT ===")
    print("Total postings stored:", total)

    print("\nNew postings per scrape day:")
    rows = conn.execute(
        "SELECT scraped_date, COUNT(*) FROM postings "
        "GROUP BY scraped_date ORDER BY scraped_date"
    ).fetchall()
    for day, count in rows:
        print(" ", day, "->", count)

    print("\nTop 5 companies:")
    rows = conn.execute(
        "SELECT company, COUNT(*) AS total FROM postings "
        "GROUP BY company ORDER BY total DESC LIMIT 5"
    ).fetchall()
    for company, count in rows:
        print(" ", company, "->", count)

    print("\nKeywords in job titles:")
    results = []
    for skill in SKILLS:
        count = conn.execute(
            "SELECT COUNT(*) FROM postings WHERE LOWER(title) LIKE ?",
            ("%" + skill + "%",),
        ).fetchone()[0]
        results.append((skill, count))
    results.sort(key=lambda item: item[1], reverse=True)
    for skill, count in results:
        print(" ", skill, "->", count)

    conn.close()


if __name__ == "__main__":
    run_report()