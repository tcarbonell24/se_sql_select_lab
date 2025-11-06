# STEP 1A
# Import SQL Library and Pandas
import pandas as pd
import sqlite3

# STEP 1B
# Connect to the database
conn = sqlite3.connect('data.sqlite')

#answer = pd.read_sql("""SELECT * FROM employees""", conn)

#print(answer)


# STEP 2
# Replace None with your code
df_first_five = pd.read_sql("""SELECT employeeNumber, lastName FROM employees LIMIT 5""", conn)
print(df_first_five)

# STEP 3
# Replace None with your code
df_five_reverse = pd.read_sql("""SELECT lastName, employeeNumber FROM employees LIMIT 5""", conn)
print(df_five_reverse)

# STEP 4
# Replace None with your code
df_alias = pd.read_sql("""SELECT lastName, employeeNumber AS ID FROM employees LIMIT 5""", conn)
print(df_alias)

# STEP 5
# Replace None with your code
df_executive = pd.read_sql("""
                           SELECT *,
                           CASE
                                WHEN jobTitle = "President"
                                OR jobTitle LIKE '%VP%'
                                THEN "Executive"
                                ELSE "Not Executive"
                            END AS role
                            FROM employees
                            """, conn)
print(df_executive)

# STEP 6
# Replace None with your code
df_name_length = pd.read_sql("""SELECT LENGTH(lastName) AS name_length FROM employees""", conn)
print(df_name_length)

# STEP 7
# Replace None with your code
df_short_title = pd.read_sql("""SELECT SUBSTRING(jobTitle, 1, 2) FROM employees""", conn)
print(df_short_title)

# STEP 8
# Replace None with your code
sum_total_price = pd.read_sql("""SELECT SUM(ROUND(priceEach * quantityOrdered)) FROM orderDetails""", conn)
print(sum_total_price)

# STEP 9
# Replace None with your code
df_day_month_year = pd.read_sql("""
                                SELECT orderDate, 
                                SUBSTRING(orderDate, 9 ,2) as day
                                FROM orders
                                """, conn)
print(df_day_month_year)




# STEP 1A
# Import SQL Library and Pandas
import pandas as pd
import sqlite3

# STEP 1B
# Connect to the database
conn = sqlite3.connect('data.sqlite')


# answer = pd.read_sql("""SELECT * FROM employees""", conn)

# print(answer)

# STEP 2
# Replace None with your code
df_first_five = pd.read_sql("""SELECT employeeNumber, lastName FROM employees""", conn)
# print(df_first_five)

# STEP 3
# Replace None with your code
df_five_reverse = pd.read_sql("""SELECT lastName, employeeNumber FROM employees""", conn)
# print(df_five_reverse)

# STEP 4
# Replace None with your code
df_alias = pd.read_sql("""SELECT lastName, employeeNumber AS ID FROM employees""", conn)
# print(df_alias)

# STEP 5
# Replace None with your code
df_executive = pd.read_sql("""
    SELECT *,
    CASE
      WHEN jobTitle = "President"
      OR jobTitle LIKE '%VP%'
      THEN "Executive"
      WHEN jobTitle LIKE '%Manager%'
      THEN "Management"
      ELSE "Not Executive"
    END AS role                       
    FROM employees
""", conn)
# print(df_executive)

# STEP 6
# Replace None with your code
df_name_length = pd.read_sql("""SELECT LENGTH(lastName) as name_length FROM employees""", conn)
# print(df_name_length)

# STEP 7
# Replace None with your code
df_short_title = pd.read_sql("""SELECT SUBSTRING(jobTitle, 1, 2) as short_title FROM employees""", conn)
# print(df_short_title)

# STEP 8
# Replace None with your code
sum_total_price = pd.read_sql("""SELECT ROUND(priceEach * quantityOrdered) as orderTotal FROM orderDetails""", conn).sum()
# print(sum_total_price)

# STEP 9
# Replace None with your code
df_day_month_year = pd.read_sql("""
    SELECT orderDate,
    SUBSTRING(orderDate, 9, 2) AS day,
    SUBSTRING(orderDate, 6, 2) AS month,
    SUBSTRING(orderDate, 1, 4) AS year
    FROM orders
""", conn)
print(df_day_month_year)
