import sqlite3
import pytz
import os
from datetime import datetime

# Detect environment (Streamlit Cloud uses STREAMLIT_RUNTIME env var)
IS_CLOUD = os.getenv("STREAMLIT_RUNTIME") is not None

# ✅ Set DB path based on environment
if IS_CLOUD:
    DB_PATH = "/tmp/emovera.db"  # Writable in cloud
else:
    DB_PATH = "./data/data.db"   # Local storage

# ✅ Create data folder locally if missing
if not IS_CLOUD and not os.path.exists("data"):
    os.makedirs("data")

# ✅ Connect to DB safely
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
c = conn.cursor()

IST = pytz.timezone('Asia/Kolkata')  # Indian Standard Time


# ==========================
# ✅ TABLE CREATION FUNCTIONS
# ==========================

def create_page_visited_table():
    c.execute('CREATE TABLE IF NOT EXISTS pageTrackTable(pagename TEXT, timeOfvisit TIMESTAMP)')
    conn.commit()

def create_emotionclf_table():
    c.execute('CREATE TABLE IF NOT EXISTS emotionclfTable(rawtext TEXT, prediction TEXT, probability NUMBER, timeOfvisit TIMESTAMP)')
    conn.commit()


# ==========================
# ✅ DATA INSERTION FUNCTIONS
# ==========================

def add_page_visited_details(pagename, timeOfvisit=None):
    """Log page visit with timestamp"""
    if timeOfvisit is None:
        timeOfvisit = datetime.now(IST).strftime("%Y-%m-%d %H:%M:%S")
    else:
        timeOfvisit = timeOfvisit.astimezone(IST).strftime("%Y-%m-%d %H:%M:%S")

    c.execute('INSERT INTO pageTrackTable(pagename, timeOfvisit) VALUES (?,?)', (pagename, timeOfvisit))
    conn.commit()


def add_prediction_details(rawtext, prediction, probability, timeOfvisit=None):
    """Log prediction info"""
    if timeOfvisit is None:
        timeOfvisit = datetime.now(IST).strftime("%Y-%m-%d %H:%M:%S")
    else:
        timeOfvisit = timeOfvisit.astimezone(IST).strftime("%Y-%m-%d %H:%M:%S")

    c.execute('INSERT INTO emotionclfTable(rawtext, prediction, probability, timeOfvisit) VALUES (?,?,?,?)',
              (rawtext, prediction, probability, timeOfvisit))
    conn.commit()


# ==========================
# ✅ VIEW FUNCTIONS
# ==========================

def view_all_page_visited_details():
    c.execute('SELECT * FROM pageTrackTable')
    return c.fetchall()

def view_all_prediction_details():
    c.execute('SELECT * FROM emotionclfTable')
    return c.fetchall()
