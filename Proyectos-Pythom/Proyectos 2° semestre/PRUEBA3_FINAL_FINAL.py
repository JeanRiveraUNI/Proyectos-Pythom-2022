from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import cx_Oracle
import os

# Conexión con la base de datos Oracle
os.environ["TNS_ADMIN"]="C:/Wallet_DB20220530152721"
conexion = cx_Oracle.connect("admin", ".Inacap2022.", "db20220530152721_high")
cursor = conexion.cursor()

