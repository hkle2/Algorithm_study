SELECT
    CASE
        WHEN id % 2 = 1 AND id != total_num THEN id + 1
        WHEN id % 2 = 0 THEN id - 1
        ELSE id
    END AS id, student
FROM
    (SELECT id, student, COUNT(*) OVER() AS total_num
    FROM Seat) AS A
ORDER BY id;