from os import link
from turtle import title
from typing import List, Dict
from flask import Flask, request
import mysql.connector
import json
app = Flask(__name__)
DB_conf = {
    'user': 'root',
    'password': 'root',
    'host': 'db',
    'port': '3306',
    'database': 'imagerepo'
}

def test_table():
    connection = mysql.connector.connect(**DB_conf)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM images')
    results = [c for c in cursor]
    cursor.close()
    connection.close()
    return results


def add_item(link, title, alt_text):
    connection = mysql.connector.connect(**DB_conf)
    cursor = connection.cursor()
    request = f"INSERT INTO images (link, title, alt_text) VALUES ('{link}', '{title}', '{alt_text}');"
    cursor.execute(request)
    connection.commit()
    cursor.close()
    connection.close()
    return request

def delete_item(title):
    connection = mysql.connector.connect(**DB_conf)
    cursor = connection.cursor()
    request = f"DELETE FROM images WHERE title='{title}';"
    cursor.execute(request)
    connection.commit()
    cursor.close()
    connection.close()
    return request

def style():
    S  = "<style>\n"
    S += "   table {width: 100%; border-collapse: collapse;}\n"
    S += "   body {background-color: #FFEEDD; }\n"
    S += "</style>\n"
    return S

@app.route('/add')
def add():
    link = request.args.get("link", "", str)
    title = request.args.get("title", "", str)
    alt_text = request.args.get("alt_text", "", str)
    S  = "<!DOCTYPE html>\n"
    S += "<html>\n"
    S += style()
    S += "   <head>\n"
    S += "      <title>Added a capital</title>\n"
    S += "   </head>\n"
    S += "   <body>\n"
    S += "      <h1>Added a capital</h1>\n"
    if link != "" and title != "" and alt_text:
        S += add_item(link, title, alt_text)
    S += "      <p><a href='/'>Back!</a></p>\n"
    S += "   </body>\n"
    S += "</html>\n"
    return S

@app.route('/')
def index():
    S  = "<!DOCTYPE html>\n"
    S += "<html>\n"
    S += style()
    S += "   <head>\n"
    S += "      <title>Nation cities list</title>\n"
    S += "   </head>\n"
    S += "   <body>\n"
    S += "      <h1>Imagebank</h1>\n"
    S += "      <form action='/delete'>"
    S += "      <table>"
    S += "          <tr>"
    S += "              <th>Link URL</th>"
    S += "              <th>Title</th>"
    S += "              <th>Alt text</th>"
    S += "          </tr>"
    for (link, title, alt_text) in test_table():
        S += f"     <tr>"
        S += f"         <td> {link}<td>"
        S += f"         <td> {title}</td>"
        S += f"         <td> {alt_text}</td>"
        S += f"         <td><img src='{link}' alt='{alt_text}' style='width:50px;height:60px;'>"
        S += f"         <td><input type='radio' value='{title}' id='{title}'></td>"
        S += f"     </tr>\n"
    S += "      </table>\n"
    S += "<div>\n"
    S += "<button type='submit' name='action' value='Delete'>delete</button>"
    S += "</div>\n"
    S += "</form>\n"
    S += "      <h2>Add link</h2>\n"
    S += "      <form action='/add'>\n"
    S += "        <input type='text' name='title' value='Title'/>\n"
    S += "        <input type='text' name='link' value='www.link.com'/>\n"
    S += "        <input type='text' name='alt_text' value='Write alt-text'/>\n"
    S += "        <input type='submit' value='Submit'/>\n"
    S += "      </form>\n"
    S += "   </body>\n"
    S += "</html>\n"
    return S

@app.route('/delete')
def delete():
    title = request.args.get("title", "", str)
    S  = "<!DOCTYPE html>\n"
    S += "<html>\n"
    S += style()
    S += "   <head>\n"
    S += "      <title>Deleted an image</title>\n"
    S += "   </head>\n"
    S += "   <body>\n"
    S += "      <h1>Deleted an image</h1>\n"
    if title != "":
        S += delete_item(title)
    S += "      <p><a href='/'>Back!</a></p>\n"
    S += "   </body>\n"
    S += "</html>\n"
    return S

@app.route('/addform')
def addform():
    S  = "<!DOCTYPE html>\n"
    S += "<html>\n"
    S += style()
    S += "   <head>\n"
    S += "      <title>Entering a value</title>\n"
    S += "   </head>\n"
    S += "   <body>\n"
    S += "      <h1>Entering a value</h1>\n"
    S += "      <form action='/add'>\n"
    S += "        <input type='text' name='title' value='Title'/>\n"
    S += "        <input type='text' name='link' value='www.link.com'/>\n"
    S += "        <input type='text' name='alt_text' value='Write alt-text'/>\n"
    S += "        <input type='submit' value='Submit'/>\n"
    S += "      </form>\n"
    S += "   </body>\n"
    S += "</html>\n"
    return S

@app.route('/deleteform')
def deleteform():
    S  = "<!DOCTYPE html>\n"
    S += "<html>\n"
    S += style()
    S += "   <head>\n"
    S += "      <title>Entering a value</title>\n"
    S += "   </head>\n"
    S += "   <body>\n"
    S += "      <h1>Entering a value</h1>\n"
    S += "      <form action='/delete'>\n"
    S += "        <input type='text' name='title' value=''/>\n"
    S += "        <input type='submit' value='Submit'/>\n"
    S += "      </form>\n"
    S += "   </body>\n"
    S += "</html>\n"
    return S

if __name__ == '__main__':
    app.run(host='0.0.0.0')