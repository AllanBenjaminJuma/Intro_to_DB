-- task_4.sql

-- Use the alx_book_store database explicitly.
USE alx_book_store;

SELECT
    COLUMN_NAME,
    COLUMN_TYPE
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE
    TABLE_SCHEMA = 'alx_book_store' AND TABLE_NAME = 'Books';