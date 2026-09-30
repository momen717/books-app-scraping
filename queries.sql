-- Create the books table
CREATE TABLE books (
    title TEXT NOT NULL,
    price REAL NOT NULL,
    rating INTEGER NOT NULL,
    in_stock BOOLEAN NOT NULL,
    url TEXT NOT NULL
);

--  Average price for each rating
SELECT
    rating,
    ROUND(AVG(price), 2) AS average_price
FROM books
GROUP BY rating
ORDER BY rating;

--  The 5 most expensive books rated 4 or 5
SELECT
    title,
    price,
    rating,
    in_stock,
    url
FROM books
WHERE rating IN (4, 5)
ORDER BY price DESC
LIMIT 5;

--  How many books are out of stock, per rating
SELECT
    rating,
    COUNT(*) AS out_of_stock_count
FROM books
WHERE in_stock = 0
GROUP BY rating
ORDER BY rating;
