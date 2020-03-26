1. 用一条SQL 语句 查询出每门课都大于80 分的学生姓名

name course grade
张三 语文 81
张三 数学 75
李四 语文 76
李四 数学 90
王五 语文 81
王五 数学 100
王五 英语 90

> select name from table_name group by name having min(grade)>80;

《sql必知必会》总结
https://www.cnblogs.com/lgjbky/p/9469291.html