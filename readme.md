# Introduction
The goal is to explore mining user query log for data discovery (i.e. How does user query table, which table are related to each other?)
I started with a open dataset from stackoverflow called *SENLIDB*, but ultimately I want to try to apply it on internal database.

# Dataset
https://github.com/johnthebrave/nlidb-datasets/blob/master/SENLIDB/train.json

I have been thinking a lot how can we communicate these information, or so called domain knowledge more efficiently. I am thinking whether *Analyzing user actual query log* could add more insight about the data.

For example, I may answer these questions if I could analyze SQL query logs
* How often is this table queried (and by who?)
* How is this table related to other tables? How are they usually joined together?
* What is the most common filtering condition added when people are querying this table?

# Contribution
So far, I only have rough ideas and need helps to get Open Dataset of user sql query logs. If you know such dataset exist, please email me @ mediumnok@gmail.com

Thanks!
