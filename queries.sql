-- 1. Total postings stored
SELECT COUNT(*) FROM postings;

-- 2. New postings added on each scrape day
SELECT scraped_date, COUNT(*) AS new_postings
FROM postings
GROUP BY scraped_date
ORDER BY scraped_date;

-- 3. Postings per posting date
SELECT date, COUNT(*) AS total
FROM postings
GROUP BY date
ORDER BY date;

-- 4. Top 5 companies by number of postings
SELECT company, COUNT(*) AS total
FROM postings
GROUP BY company
ORDER BY total DESC
LIMIT 5;

-- 5. How many titles mention "python"
SELECT COUNT(*) FROM postings
WHERE LOWER(title) LIKE '%python%';