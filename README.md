# Olympic-Database


A full-stack web application for managing Olympic **country** and **game (sport)** records, built with **Python Flask** and **PostgreSQL**. Supports full CRUD operations (Create, Read, Update, Delete) along with custom SQL queries, through a simple server-rendered HTML interface.

---



##  Project Overview

This project models a simple **Olympic Games database** with two core entities:

- **Country** — `countryname`, `year`
- **Game** — `gamename`, `yearadded`, `yearremoved`, `year`

The Flask app exposes routes to insert, view, update, and delete records for both entities directly against a PostgreSQL database, along with two pre-built custom queries for reporting.



##  Database Schema

**`country` table**
| Column | Description |
|---|---|
| `countryname` | Name of the participating country |
| `year` | Year of participation |

**`game` table**
| Column | Description |
|---|---|
| `gamename` | Name of the sport/game |
| `yearadded` | Year the game was added to the Olympics |
| `yearremoved` | Year the game was removed (if applicable) |
| `year` | Reference Olympic year |

See the `er diagram/` folder for the full Entity-Relationship diagrams used to design this schema.

---

## Getting Started

### Prerequisites
- Python 3.x
- PostgreSQL installed and running locally

### 1. Install dependencies
```bash
pip install flask psycopg2
```

### 2. Set up the database
Create a PostgreSQL database named `olympicdata2`, then create the two tables:

```sql
CREATE DATABASE olympicdata2;

CREATE TABLE country (
    countryname VARCHAR(100),
    year INT
);

CREATE TABLE game (
    gamename VARCHAR(100),
    yearadded INT,
    yearremoved INT,
    year INT
);
```

### 3. Configure the database connection
By default, `main.py` connects using:
```python
host="localhost"
database="olympicdata2"
user="postgres"
password="admin"
```
Update these credentials in `main.py` to match your local PostgreSQL setup.

### 4. Run the app
```bash
cd project
python main.py
```
The app will start in debug mode. Visit **http://127.0.0.1:5000/** in your browser.

---

