<h2>  Employees Earning More Than Their Managers</h2><hr><div style="user-select: auto;"><p style="user-select: auto;">Table: <code style="user-select: auto;">Employee</code></p>

<pre style="user-select: auto;">+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| salary      | int     |
| managerId   | int     |
+-------------+---------+
id is the primary key column for this table.
Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.
</pre>

<p style="user-select: auto;">&nbsp;</p>

<p style="user-select: auto;">Write an SQL query to find the employees who earn more than their managers.</p>

<p style="user-select: auto;">Return the result table in <strong style="user-select: auto;">any order</strong>.</p>

<p style="user-select: auto;">The query result format is in the following example.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> 
Employee table:
+----+-------+--------+-----------+
| id | name  | salary | managerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | Null      |
| 4  | Max   | 90000  | Null      |
+----+-------+--------+-----------+
<strong style="user-select: auto;">Output:</strong> 
+----------+
| Employee |
+----------+
| Joe      |
+----------+
<strong style="user-select: auto;">Explanation:</strong> Joe is the only employee who earns more than his manager.
</pre>
</div>