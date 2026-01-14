#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa
Usage: ./5-filter_cities.py mysql_user mysql_password database_name state_name
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    # Execute ONE query only (SQL injection safe)
    cursor.execute(
        """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """,
        (sys.argv[4],)
    )

    cities = cursor.fetchall()

    # Print cities in one line separated by comma
    print(", ".join(city[0] for city in cities))

    cursor.close()
    db.close()
