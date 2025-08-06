import sqlite3
import pandas as pd
import numpy as np

from flask import Flask, redirect, render_template, request, session
from flask_session import Session

# Set connection to SQLite database
db = sqlite3.connect(r"starmap\stars.db")

# Extract CSV data and write to tables using Pandas
hyg_data = pd.read_csv(r"D:\Documents\Coding\Projects\starmap\raw data\hygdata_v42\hyg_v42.csv")
try:
    hyg_data.to_sql("hyg", db)
except ValueError:
    print("hyg table already exists.")

habcat_data = pd.read_csv(r"D:\Documents\Coding\Projects\starmap\raw data\APJ-HABCAT2\APJ-HABCAT2.csv")
try:
    habcat_data.to_sql("habcat", db)
except ValueError:
    print("habcat table already exists.")

# Close database connection
db.close()

