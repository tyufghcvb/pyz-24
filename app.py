# import sqlite3
#
# from flask import Flask, render_template, request, redirect, url_for, flash, app
#
#
#
#
# def get_db_connection():
#     conn = sqlite3.connect(DATABASE)
#     conn.row_factory = sqlite3.Row
#     return conn
#
#
# @app.route('/')
# def index():
#     conn = get_db_connection()
#     users = conn.execute('SELECT * FROM camps').fetchall()
#     conn.close()
#     return render_template('index.html', users=users)
