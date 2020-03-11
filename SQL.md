## 数据库管理系统（DBMS）

SQL（发音为字母S-Q-L 或sequel）是Structured Query Language（结构化查询语言）的缩写。
SQL 是一种专门用来与数据库沟通的语言。

schema(模式)，可以用来描述表的信息，也可以用来描述整个数据库和其中数据表的关系。

* distinct 关键字作用于所有的列，而不仅仅是跟在其后的那一列

* 如果想在多个列上进行降序排序，必须对每一列指定DESC 关键字。
> SELECT * FROM Customers
 ORDER BY Country ASC, CustomerName DESC;
 
* SQL（像多数语言一样）在处理OR 操作符前，优先处理AND 操作符

* IN 操作符一般比一组OR 操作符执行得更快

* 视图是虚拟的表，它不包括任何列或者数据，包含的是一个查询。用于SQL语句的重用，

### Syntax

* INSERT INTO Syntax
> INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);

* UPDATE Syntax
> UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;

* DELETE Syntax
> DELETE FROM table_name WHERE condition;

* SELECT TOP Syntax
> SELECT column_name(s)
FROM table_name
WHERE condition
LIMIT number;

* Functions: MIN(), MAX(), COUNT(), AVG(), SUM()
> SELECT MIN(column_name)
FROM table_name
WHERE condition;

* The SQL LIKE Operator
The LIKE operator is used in a WHERE clause to search for a specified pattern in a column.

There are two wildcards often used in conjunction with the LIKE operator:

`%` - The percent sign represents zero, one, or multiple characters

`_` - The underscore represents a single character
> SELECT column1, column2, ...
FROM table_name
WHERE columnN (NOT) LIKE pattern;

* IN Syntax
> SELECT column_name(s)
FROM table_name
WHERE column_name (NOT) IN (value1, value2, ...);

* BETWEEN Syntax
> SELECT column_name(s)
FROM table_name
WHERE column_name (NOT) BETWEEN value1 AND value2;

* 使用函数Concat拼接
> SELECT Concat(vend_name, ' (', vend_country, ')') as vend_title
FROM Vendors
ORDER BY vend_name;

* SQL JOIN
A JOIN clause is used to combine rows from two or more tables, based on a related column between them.

Different Types of SQL JOINs
Here are the different types of the JOINs in SQL:

(INNER) JOIN: Returns records that have matching values in both tables
LEFT (OUTER) JOIN: Returns all records from the left table, and the matched records from the right table
RIGHT (OUTER) JOIN: Returns all records from the right table, and the matched records from the left table
FULL (OUTER) JOIN: Returns all records when there is a match in either left or right table

* UNION Syntax
> SELECT column_name(s) FROM table1
UNION (ALL)
SELECT column_name(s) FROM table2;

* GROUP BY Syntax
> SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
ORDER BY column_name(s);

GROUP BY 子句必须出现在WHERE 子句之后，ORDER BY 子句之前。

* HAVING Clause
The HAVING clause was added to SQL because the WHERE keyword could not be used with aggregate functions.

>SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
HAVING condition
ORDER BY column_name(s);

WHERE 在数据分组前进行过滤，HAVING 在数据分组后进行过滤
> SELECT vend_id, COUNT(*) AS num_prods
FROM Products
WHERE prod_price >= 4
GROUP BY vend_id
HAVING COUNT(*) >= 2;
ORDER BY num_prods;

* SELECT INTO Syntax
Copy all columns into a new table:

> SELECT *
INTO newtable [IN externaldb]
FROM oldtable
WHERE condition;

Tip: SELECT INTO can also be used to create a new, empty table using the schema of another. Just add a WHERE clause that causes the query to return no data:

> SELECT * INTO newtable
FROM oldtable
WHERE 1 = 0;

* INSERT INTO SELECT Syntax
> INSERT INTO table2 (column1, column2, column3, ...)
SELECT column1, column2, column3, ...
FROM table1
WHERE condition;

* SQL NULL Functions

The MySQL IFNULL() function lets you return an alternative value if an expression is NULL:

### What is a Stored Procedure?
A stored procedure is a prepared SQL code that you can save, so the code can be reused over and over again.

So if you have an SQL query that you write over and over again, save it as a stored procedure, and then just call it to execute it.

You can also pass parameters to a stored procedure, so that the stored procedure can act based on the parameter value(s) that is passed.

Stored Procedure Syntax
CREATE PROCEDURE procedure_name
AS
sql_statement
GO;
Execute a Stored Procedure
EXEC procedure_name;

Stored Procedure With Multiple Parameters
Setting up multiple parameters is very easy. Just list each parameter and the data type separated by a comma as shown below.

The following SQL statement creates a stored procedure that selects Customers from a particular City with a particular PostalCode from the "Customers" table:

Example
CREATE PROCEDURE SelectAllCustomers @City nvarchar(30), @PostalCode nvarchar(10)
AS
SELECT * FROM Customers WHERE City = @City AND PostalCode = @PostalCode
GO;
Execute the stored procedure above as follows:

Example
EXEC SelectAllCustomers @City = "London", @PostalCode = "WA1 1DP";


### The SQL BACKUP DATABASE Statement

The BACKUP DATABASE statement is used in SQL Server to create a full back up of an existing SQL database.

Syntax
> BACKUP DATABASE databasename
TO DISK = 'filepath';

### SQL Constraints
SQL constraints are used to specify rules for the data in a table.

Constraints are used to limit the type of data that can go into a table. This ensures the accuracy and reliability of the data in the table. If there is any violation between the constraint and the data action, the action is aborted.

Constraints can be column level or table level. Column level constraints apply to a column, and table level constraints apply to the whole table.

The following constraints are commonly used in SQL:

NOT NULL - Ensures that a column cannot have a NULL value
UNIQUE - Ensures that all values in a column are different
PRIMARY KEY - A combination of a NOT NULL and UNIQUE. Uniquely identifies each row in a table
FOREIGN KEY - Uniquely identifies a row/record in another table
CHECK - Ensures that all values in a column satisfies a specific condition
DEFAULT - Sets a default value for a column when no value is specified
INDEX - Used to create and retrieve data from the database very quickly

* Use the TRUNCATE statement to delete all data inside a table.

> TRUNCATE TABLE
 Persons;
 
* CREATE/DROP UNIQUE INDEX Syntax
Creates a unique index on a table. Duplicate values are not allowed:

>CREATE UNIQUE INDEX index_name
ON table_name (column1, column2, ...);

>ALTER TABLE table_name
DROP INDEX index_name;

### SQL CREATE VIEW Statement
In SQL, a view is a virtual table based on the result-set of an SQL statement.

A view contains rows and columns, just like a real table. The fields in a view are fields from one or more real tables in the database.

You can add SQL functions, WHERE, and JOIN statements to a view and present the data as if the data were coming from one single table.

> CREATE VIEW Syntax
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;

### SQL Updating a View
A view can be updated with the CREATE OR REPLACE VIEW command.

> SQL CREATE OR REPLACE VIEW Syntax
CREATE OR REPLACE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;

### SQL DROP VIEW Syntax
> DROP VIEW view_name;


## REF
[w3schools](https://www.w3schools.com/sql/default.asp)