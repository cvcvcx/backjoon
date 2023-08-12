-- 코드를 입력하세요
SELECT CATEGORY, SUM(SALES) AS TOTAL_SALES
FROM BOOK as b
JOIN BOOK_SALES as bs ON b.BOOK_ID = bs.BOOK_ID
WHERE YEAR(SALES_DATE) = 2022 AND MONTH(SALES_DATE) = 1
GROUP BY CATEGORY
ORDER BY CATEGORY