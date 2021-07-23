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


app.add_url_rule('/admin/Home', view_func = adminUrl.AdminHome)
app.add_url_rule('/hotelstaf/Home', view_func = hotelStafUrl.HotelStafHome)
app.add_url_rule('/Home', view_func = passengerUrl.PassengerHome)

@app.route('/', methods=['GET', 'POST'])
def Home():  
   return render_template('base.html')
   

if __name__ == "__main__":   
    app.run(host='0.0.0.0', port=3000 ) # localhost
    # app.run(host='192.168.0.106', port=8080 )  #Router
    # app.run()