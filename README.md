# Udacity-fsnd-log-analysis-frist-project
Udacity Full Stack NanoDegree Log Analysis Project

### Project Description
>This is the reporting tool project that asks you questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1 % of requests lead to errors?
and prints out reports (in plain text) based on the data in the database. This reporting tool is a Python3 program connecting PostgreSQL databse using the psycopg2 module.
  
#### Setting up and running the database:

  1. usee `vagrant up` and `vagrant ssh` to up and run vagrant 

  2. Load the data in local database using the command:
  
  ```
    psql -d news -f newsdata.sql
  ```
  3. Use `psql` to connect to vagrant postgreSQL.
  
  4. Use `\c news` to connect to news Database.
  
### Running the queries:
  Run Reporting Tool.py using this command inside your vagrant box:
  ```
    $ python3 /vagrant/Reporting\ Tool.py 
  ```
