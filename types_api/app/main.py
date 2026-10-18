
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()

















import os
from typing import List, Any, Dict

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import mysql.connector
from mysql.connector import Error as MySQLError

app = FastAPI(title="Types API", version="1.0.0", description="Serves the /Types endpoint from MariaDB")

# CORS (open; tighten in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---- DB CONFIG (override via env in docker-compose) ----
DB_HOST = os.getenv("DB_HOST", "mariadb")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USER", "myuser")
DB_PASS = os.getenv("DB_PASS", "mypassword")
DB_NAME = os.getenv("DB_NAME", "mydatabase")
DB_TABLE_TYPES = os.getenv("DB_TABLE_TYPES", "Types")  # exact case matters on Linux
DB_TABLE_COUNTRIES = os.getenv("DB_TABLE_COUNTRIES", "Countries")  # exact case matters on Linux
DB_TABLE_CITIES = os.getenv("DB_TABLE_CITIES", "Cities")  # exact case matters on Linux
DB_TABLE_PLACES = os.getenv("DB_TABLE_PLACES", "Places")  # exact case matters on Linux
DB_TABLE_DATA = os.getenv("DB_TABLE_DATA", "Data")  # exact case matters on Linux
DB_TABLE_TOOLS = os.getenv("DB_TABLE_TOOLS", "Tools")  # exact case matters on Linux

def get_conn():
    return mysql.connector.connect(
        host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASS, database=DB_NAME
    )



def fetch_types(limit: int = 2000, offset: int = 0) -> List[Dict[str, Any]]:
    # NOTE: use backticks around the table name in case-insensitive/odd names
    query = f"SELECT * FROM `{DB_TABLE_TYPES}` LIMIT %s OFFSET %s"
    conn = get_conn()
    try:
        cur = conn.cursor(dictionary=True)
        # ensure safe ints for LIMIT/OFFSET
        lim = max(0, int(limit))
        off = max(0, int(offset))
        cur.execute(query, (lim, off))
        rows = cur.fetchall()
        return rows
    except MySQLError as e:
        raise
    finally:
        try:
            cur.close()
        except Exception:
            pass
        conn.close()
# You asked for '/Types'. We'll also provide lowercase alias '/types' for convenience.
@app.get("/Types")
@app.get("/types")
def read_types(limit: int = 100, offset: int = 0):
    try:
        rows = fetch_types(limit=limit, offset=offset)
        # FastAPI encodes Decimals and datetimes; no custom serializer needed
        return JSONResponse(content=rows)
    except MySQLError as e:
        raise HTTPException(status_code=500, detail=f"MySQL error: {e.msg}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))






def fetch_countries(limit: int = 200, offset: int = 0) -> List[Dict[str, Any]]:
    # NOTE: use backticks around the table name in case-insensitive/odd names
    query = f"SELECT * FROM `{DB_TABLE_COUNTRIES}` LIMIT %s OFFSET %s"
    conn = get_conn()
    try:
        cur = conn.cursor(dictionary=True)
        # ensure safe ints for LIMIT/OFFSET
        lim = max(0, int(limit))
        off = max(0, int(offset))
        cur.execute(query, (lim, off))
        rows = cur.fetchall()
        return rows
    except MySQLError as e:
        raise
    finally:
        try:
            cur.close()
        except Exception:
            pass
        conn.close()
# You asked for '/Types'. We'll also provide lowercase alias '/types' for convenience.
@app.get("/Countries")
@app.get("/countries")
def read_types(limit: int = 200, offset: int = 0):
    try:
        rows = fetch_countries(limit=limit, offset=offset)
        # FastAPI encodes Decimals and datetimes; no custom serializer needed
        return JSONResponse(content=rows)
    except MySQLError as e:
        raise HTTPException(status_code=500, detail=f"MySQL error: {e.msg}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




def fetch_Cities(limit: int = 2000, offset: int = 0) -> List[Dict[str, Any]]:
    # NOTE: use backticks around the table name in case-insensitive/odd names
    query = f"SELECT * FROM `{DB_TABLE_CITIES}` LIMIT %s OFFSET %s"
    conn = get_conn()
    try:
        cur = conn.cursor(dictionary=True)
        # ensure safe ints for LIMIT/OFFSET
        lim = max(0, int(limit))
        off = max(0, int(offset))
        cur.execute(query, (lim, off))
        rows = cur.fetchall()
        return rows
    except MySQLError as e:
        raise
    finally:
        try:
            cur.close()
        except Exception:
            pass
        conn.close()
# You asked for '/Cities'. We'll also provide lowercase alias '/types' for convenience.
@app.get("/cities")
@app.get("/Cities")
def read_Cities(limit: int = 2000, offset: int = 0):
    try:
        rows = fetch_Cities(limit=limit, offset=offset)
        # FastAPI encodes Decimals and datetimes; no custom serializer needed
        return JSONResponse(content=rows)
    except MySQLError as e:
        raise HTTPException(status_code=500, detail=f"MySQL error: {e.msg}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))






def fetch_places(limit: int = 4000, offset: int = 0) -> List[Dict[str, Any]]:
    # NOTE: use backticks around the table name in case-insensitive/odd names
    query = f"SELECT * FROM `{DB_TABLE_PLACES}` LIMIT %s OFFSET %s"
    conn = get_conn()
    try:
        cur = conn.cursor(dictionary=True)
        # ensure safe ints for LIMIT/OFFSET
        lim = max(0, int(limit))
        off = max(0, int(offset))
        cur.execute(query, (lim, off))
        rows = cur.fetchall()
        return rows
    except MySQLError as e:
        raise
    finally:
        try:
            cur.close()
        except Exception:
            pass
        conn.close()
# You asked for '/Types'. We'll also provide lowercase alias '/types' for convenience.
@app.get("/Places")
@app.get("/places")
def read_places(limit: int = 8000, offset: int = 0):
    try:
        rows = fetch_places(limit=limit, offset=offset)
        # FastAPI encodes Decimals and datetimes; no custom serializer needed
        return JSONResponse(content=rows)
    except MySQLError as e:
        raise HTTPException(status_code=500, detail=f"MySQL error: {e.msg}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))





def fetch_data(limit: int = 60000, offset: int = 0) -> List[Dict[str, Any]]:
    # NOTE: use backticks around the table name in case-insensitive/odd names
    query = f"SELECT * FROM `{DB_TABLE_DATA}` LIMIT %s OFFSET %s"
    conn = get_conn()
    try:
        cur = conn.cursor(dictionary=True)
        # ensure safe ints for LIMIT/OFFSET
        lim = max(0, int(limit))
        off = max(0, int(offset))
        cur.execute(query, (lim, off))
        rows = cur.fetchall()
        return rows
    except MySQLError as e:
        raise
    finally:
        try:
            cur.close()
        except Exception:
            pass
        conn.close()
@app.get("/Data")
@app.get("/data")
def read_data(limit: int = 10000, offset: int = 0):
    try:
        rows = fetch_data(limit=limit, offset=offset)
        # FastAPI encodes Decimals and datetimes; no custom serializer needed
        return JSONResponse(content=rows)
    except MySQLError as e:
        raise HTTPException(status_code=500, detail=f"MySQL error: {e.msg}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))






















@app.get("/policy", response_class=HTMLResponse)
async def read_policy():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
      <title>Privacy Policy - EvenTder</title>
      <style>
        body {
          font-family: sans-serif;
          line-height: 1.6;
          padding: 2rem;
          max-width: 800px;
          margin: auto;
          background-color: #fdfdfd;
          color: #333;
        }
        h1, h2 {
          color: #2a2a2a;
        }
        a {
          color: #0066cc;
          text-decoration: none;
        }
        a:hover {
          text-decoration: underline;
        }
        hr {
          margin: 2rem 0;
        }
      </style>
    </head>
    <body>

      <h1>Privacy Policy for EvenTder</h1>
      <p><strong>Last updated:</strong> November 7, 2025</p>

      <h2>1. Introduction</h2>
      <p>
        Welcome to <strong>EvenTder</strong> (“we,” “our,” “us”). Your privacy is important to us.
        This Privacy Policy explains how we collect, use, disclose, and protect your information when you use our mobile application
        <strong>EvenTder</strong> (the “App”).
      </p>
      <p>By using the App, you agree to this Privacy Policy. If you do not agree, please do not use the App.</p>

      <h2>2. Information We Collect</h2>
      <h3>a. Personal Information</h3>
      <p>We may collect your email address, name, and any data you voluntarily provide through contact or feedback forms.</p>

      <h3>b. Automatically Collected Information</h3>
      <ul>
        <li>Device details: OS version, model, language settings.</li>
        <li>Usage: Interactions with filters, selected cities/categories, screen views.</li>
        <li>Location data: GPS or network-based location if you permit it, used to show local event data.</li>
      </ul>

      <h3>c. Backend Logs</h3>
      <p>Login times, filter selections, and city interactions may be logged in a secure MariaDB database for analysis and improvement.</p>

      <h2>3. How We Use Your Information</h2>
      <ul>
        <li>To operate and improve EvenTder functionality.</li>
        <li>To personalize content and recommendations.</li>
        <li>To analyze usage and fix bugs.</li>
        <li>To respond to your requests or inquiries.</li>
      </ul>

      <h2>4. Sharing and Disclosure</h2>
      <p>We <strong>do not sell or rent</strong> your data.</p>
      <p>We may share data with trusted service providers (e.g., hosting, analytics) or when legally required. We may also share data with your consent.</p>

      <h2>5. Data Storage and Security</h2>
      <p>Data is stored securely with encryption, firewalls, and limited access. While we take reasonable precautions, no system is completely secure.</p>

      <h2>6. Data Retention</h2>
      <p>We retain anonymized logs for analysis. Personally identifiable data is stored only as long as needed or legally required.</p>

      <h2>7. Your Rights</h2>
      <p>You may request to access, modify, or delete your data. You may also disable location tracking through your device settings.</p>
      <p>Contact us via the emails below to make a request.</p>

      <h2>8. Children’s Privacy</h2>
      <p>EvenTder is not intended for users under 13. If we learn we’ve collected data from a child, we will delete it immediately.</p>

      <h2>9. Third-Party Services</h2>
      <p>The App may use services such as Google Maps or Firebase. These services have their own privacy policies. Please review them accordingly.</p>

      <h2>10. Changes to This Policy</h2>
      <p>This Privacy Policy may change over time. The updated version will always be available on this page, with the latest revision date above.</p>

      <h2>11. Contact Us</h2>
      <p>If you have questions or wish to exercise your rights, you can contact any of us:</p>
      <ul>
        <li><strong>Eduardo Massolini</strong> – <a href="mailto:eduardo@massolini.com.ar">eduardo@massolini.com.ar</a></li>
        <li><strong>Victor Hugo Bersan</strong> – <a href="mailto:vitorugoz@gmail.com">vitorugoz@gmail.com</a></li>
        <li><strong>Fankhauser Eric</strong> – <a href="mailto:eric_fanka@hotmail.com">eric_fanka@hotmail.com</a></li>
      </ul>

      <hr />
      <p>© 2025 EvenTder. All rights reserved.</p>

    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
