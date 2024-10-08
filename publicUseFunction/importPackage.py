from flask import Flask, render_template, request, redirect, url_for, session, Blueprint, jsonify, Response, send_file
import psycopg2
import psycopg2.pool
import os
import datetime
import smtplib
import json
from flask_mail import Mail, Message
import csv
import socket
import requests
import uuid
import shutil
import ntplib
from time import ctime

DB_URI = "postgresql://postgres:sam101554@127.0.0.1/Python_FlaskProject03"

conn = psycopg2.connect(host='127.0.0.1',
                        dbname='Python_FlaskProject03',
                        user='postgres',
                        password='sam101554')

# 使用Python抓取NTP（Network Time Protocol）時間
def get_ntp_time():
    client = ntplib.NTPClient()
    response = client.request('pool.ntp.org')
    return ctime(response.tx_time)

