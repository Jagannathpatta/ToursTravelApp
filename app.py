from crypt import methods
from flask import Flask, request, render_template, flash,  redirect, url_for, send_from_directory, send_file, session
from werkzeug.utils import secure_filename
import os
from datetime import datetime

from Passenger import views as passengerUrl
from HotelStaf import views as hotelStafUrl
from Admin import views as adminUrl


app = Flask('app')
app.debug = True

# Admin Urls 
app.add_url_rule('/admin/Home', view_func = adminUrl.AdminHome)
app.add_url_rule('/admin/Home', view_func = adminUrl.AdminContact)



# Hotel Staff Urls
app.add_url_rule('/hotelstaf/Home', view_func = hotelStafUrl.HotelStafHome)


#Passenger Urls
app.add_url_rule('/Home', view_func = passengerUrl.PassengerHome)


def check_user(page):
    if session.get("email"):
        return page
    else:
        return 'login.html'
        
@app.route('/', methods=['GET', 'POST'])
def Home():  
   return render_template('base.html')
   

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        try :
            conn = sqlite3.connect("DataBase/quizAppDataBase.db")
            cursor = conn.cursor()
            email = str(request.form['email'])
            password = str(request.form["password"])
            print(email , 'email' , password , 'password')
            # mydoc = cursor.execute("SELECT * from USER")
            mydoc = cursor.execute("SELECT * from USER WHERE USER_EMAIL = ? AND PASSWORD = ?", (email, password))
            myresult = mydoc.fetchone()

            # print(myresult , type(myresult[0]) , 'myresult' , mydoc)
            # cursor.close()
            # conn.close()
            if myresult:
                session['email'] = str(myresult[1])
                session['user_id'] = myresult[0]
                session['user_role'] = str(myresult[4])
                session['image_ids'] = test.readAllBlobData()
                if myresult[4] == 'S':
                    session['username'] , session['role_id']  = cursor.execute("SELECT STUDENT_NAME , STUDENT_ID from STUDENT WHERE USER_ID = ?", (myresult[0],)).fetchone()
                    # course_ids = cursor.execute("SELECT COURSE_ID from ENROLLMENT WHERE STUDENT_ID = ?" , ( session['role_id'],)).fetchall()                    
                    session['courses'] = cursor.execute("SELECT COURSE_ID , COURSE_NAME , TEACHER_ID from COURSE WHERE COURSE_ID IN ( SELECT COURSE_ID from ENROLLMENT_COURSE WHERE STUDENT_ID = ? )" , ( session['role_id'] , )).fetchall()
                    session['quizes'] = cursor.execute("SELECT QUIZ_ID , QUIZ_NAME , TEACHER_ID , COURSE_ID from QUIZ WHERE QUIZ_ID IN ( SELECT QUIZ_ID from ENROLLMENT_QUIZ WHERE STUDENT_ID = ? )" , ( session['role_id'] , )).fetchall()
                    cursor.close()
                    conn.close()
                    # print(course_ids , "course_ids")
                    return redirect('/student/Home')
                elif myresult[4] == 'T':
                    session['username'] , session['role_id'] = cursor.execute("SELECT TEACHER_NAME , TEACHER_ID from TEACHER WHERE USER_ID = ?", (myresult[0],)).fetchone()
                    session['courses'] = cursor.execute("SELECT COURSE_ID , COURSE_NAME from COURSE WHERE TEACHER_ID = ?" , ( session['role_id'],)).fetchall()
                    cursor.close()
                    conn.close()
                    return redirect('/teacher/Home')
                else:
                    return redirect('/admin/Home')
            else:
                return render_template('login.html', msg='email id or password is not matching')
        
        except Exception as e:
            return render_template('login.html', msg=e)


@app.route("/sign", methods=["GET", "POST"])
def sign():
    if request.method == "POST":
        try:
            conn = sqlite3.connect("DataBase/quizAppDataBase.db")
            cursor = conn.cursor()
            fname = str(request.form["fname"])
            lname = str(request.form["lname"])
            password = str(request.form["password"])
            email = str(request.form['email'])
            phone = str(request.form['phoneNo'])
            cursor.execute("SELECT * from USER WHERE USER_EMAIL = ?", (str(email),))
            if cursor.fetchall():
                return render_template("sign.html", msg="Email Already Exist Try Different")
            else:
                cursor.execute("INSERT INTO USER(USER_EMAIL, PASSWORD, PHONE_NO) VALUES (?, ?, ?)",
                            (str(email), str(password), int(phone)))
                conn.commit()

                mydoc = cursor.execute("SELECT * from USER WHERE USER_EMAIL = ?" , (str(email),))
                myresult = mydoc.fetchone()

                cursor.execute("UPDATE STUDENT SET STUDENT_NAME = ? WHERE USER_ID = ?",
                            (str(fname) + ' ' + str(lname), int(myresult[0])))
                conn.commit()

                # print('Singin User :', myresult)
                # session['username'] = str(fname)+" "+str(lname)
                # session['email'] = str(email)
                # session['user_id'] = myresult[0]
                # session['user_role'] = str(myresult[4])
            cursor.close()
            conn.close()
            return render_template('login.html', msg = 'Successfully Registered')

        except Exception as e:
            return render_template('sign.html', msg=e)
        



if __name__ == "__main__":   
    app.run(host='0.0.0.0', port=3000 ) # localhost
    # app.run(host='192.168.0.106', port=8080 )  #Router
    # app.run()