from datetime import datetime
from flask import Flask, request, render_template, redirect, url_for, session
import os

def PassengerHome():
    return render_template('/PassengerSite/PassengerHome.html')