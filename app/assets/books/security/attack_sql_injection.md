# ATTACK BY SQL INJECTION


SELECT * FROM students WHERE studentId = " + studentId
SELECT * FROM students WHERE studentId = 117
SELECT * FROM students WHERE studentId = 117 OR 1=1;
                                             ↑↑↑↑↑↑
                                             XSS Attack

![](assets/books/security/assets/sql-injection-infographic.webp)                                             

## How to mitigate

- Parametrized requests
- Stored procedures