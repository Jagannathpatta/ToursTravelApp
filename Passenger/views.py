from datetime import datetime
from flask import Flask, request, render_template, redirect, url_for, session
import os
from oracleCon import get_db, close_db

def PassengerHome():
    return render_template('/PassengerSite/PassengerHome.html')

def PassengerSignUp():
    connection = get_db()
    if request.method == 'POST':
        fname = request.form['fname']
        mname = request.form['mname']
        lname = request.form['lname']
        email = request.form['email']
        password = request.form['password']
        state = request.form['state']
        district = request.form['district']
        pincode = request.form['pincode']
        addrline1 = request.form['addrline1']
        city = request.form['city']
        phone_no = request.form['phoneno']
        cursor = connection.cursor()
        userdata = dict(U_EMAIL = email, U_PASSWORD = password, U_PHONE = phone_no, U_F_NAME = fname, U_M_NAME = mname, U_L_NAME = lname, STATE = state, DISTRICT = district, CITY = city, PINCODE = pincode, LINE1 = addrline1, U_ROLE = 'P')
        cursor.execute('insert into USERDETAILS (U_EMAIL,U_PASSWORD,U_PHONE,U_F_NAME,U_M_NAME,U_L_NAME,STATE,DISTRICT,CITY,PINCODE,LINE1,U_ROLE) values (:U_EMAIL, :U_PASSWORD, :U_PHONE, :U_F_NAME, :U_M_NAME, :U_L_NAME, :STATE, :DISTRICT, :CITY, :PINCODE, :LINE1, :U_ROLE)', userdata)
        cursor.close()
    
    return 'sign up'