from flask import request, make_response
import mysql.connector
import re # Regular expressions also called Regex
from functools import wraps
from datetime import datetime

##############################
def db():
    try:
        db = mysql.connector.connect(
            host = "mariadb",
            user = "root",  
            password = "password",
            database = "2026_1_travel"
        )
        cursor = db.cursor(dictionary=True)
        return db, cursor
    except Exception as e:
        print(e, flush=True)
        raise Exception("Database under maintenance", 500)


##############################
def no_cache(view):
    @wraps(view)
    def no_cache_view(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
        return response
    return no_cache_view


##############################
USER_FIRST_NAME_MIN = 2
USER_FIRST_NAME_MAX = 20
REGEX_USER_FIRST_NAME = f"^.{{{USER_FIRST_NAME_MIN},{USER_FIRST_NAME_MAX}}}$"
def validate_user_first_name():
    user_first_name = request.form.get("user_first_name", "").strip()
    if not re.match(REGEX_USER_FIRST_NAME, user_first_name):
        raise Exception("--error-- user_first_name")
    return user_first_name


##############################
USER_LAST_NAME_MIN = 2
USER_LAST_NAME_MAX = 20
REGEX_USER_LAST_NAME = f"^.{{{USER_LAST_NAME_MIN},{USER_LAST_NAME_MAX}}}$"
def validate_user_last_name():
    user_last_name = request.form.get("user_last_name", "").strip()
    if not re.match(REGEX_USER_LAST_NAME, user_last_name):
        raise Exception("--error-- user_last_name")
    return user_last_name


##############################
REGEX_USER_EMAIL = "^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$"
def validate_user_email():
    user_email = request.form.get("user_email", "").strip()
    if not re.match(REGEX_USER_EMAIL, user_email): 
        raise Exception("--error-- user_email")
    return user_email


##############################
USER_PASSWORD_MIN = 8
USER_PASSWORD_MAX = 50
REGEX_USER_PASSWORD = f"^.{{{USER_PASSWORD_MIN},{USER_PASSWORD_MAX}}}$"
def validate_user_password():
    user_password = request.form.get("user_password", "").strip()
    if not re.match(REGEX_USER_PASSWORD, user_password):
        raise Exception("--error-- user_password")
    return user_password


##############################
DESTINATION_TITLE_MIN = 2
DESTINATION_TITLE_MAX = 50
REGEX_DESTINATION_TITLE = f"^.{{{DESTINATION_TITLE_MIN},{DESTINATION_TITLE_MAX}}}$"
def validate_destination_title():
    destination_title = request.form.get("destination_title", "").strip()
    if not re.match(REGEX_DESTINATION_TITLE, destination_title):
        raise Exception("--error-- destination_title")
    return destination_title

##############################
def validate_destination_start_date():
    destination_start_date = request.form.get("destination_start_date").strip()
    if not destination_start_date:
        raise Exception("--error-- destination_start_date")
    
    try: 
        datetime.strptime(destination_start_date, '%Y-%m-%d')
        return destination_start_date
    except Exception as ex: 
        raise Exception("--error-- invalid date format start date")
        
##############################
def validate_destination_end_date(destination_start_date):
    destination_end_date = request.form.get("destination_end_date").strip()
    if not destination_end_date:
        raise Exception("--error-- destination_end_date")
    
    try: 
        # Convert dates to objects to compare them
        start_date_obj = datetime.strptime(destination_start_date, '%Y-%m-%d')
        end_date_obj = datetime.strptime(destination_end_date, '%Y-%m-%d')
    except Exception: 
        raise Exception("--error-- invalid date format end date")

    if end_date_obj < start_date_obj:
        raise Exception("--error-- end date can not be before start date")
        
    return destination_end_date

##############################
def validate_destination_description():
    destination_description = request.form.get("destination_description", "").strip()
    if len(destination_description) > 60000:
        raise Exception("--error-- destination_description is too long")
    return destination_description

##############################
DESTINATION_LOCATION_MIN = 2
DESTINATION_LOCATION_MAX = 90
REGEX_DESTINATION_LOCATION = f"^.{{{DESTINATION_LOCATION_MIN},{DESTINATION_LOCATION_MAX}}}$"
def validate_destination_location():
    destination_location = request.form.get("destination_location", "").strip()
    if not re.match(REGEX_DESTINATION_LOCATION, destination_location):
        raise Exception("--error-- destination_location")
    return destination_location

##############################
COUNTRIES = ["Afghanistan", "Albanien", "Algeriet", "Andorra", "Angola", "Antigua og Barbuda", "Argentina", "Armenien", "Aserbajdsjan", "Australien", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belgien", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnien-Hercegovina", "Botswana", "Brasilien", "Brunei", "Bulgarien", "Burkina Faso", "Burundi", "Cambodja", "Cameroun", "Canada", "Centralafrikanske Republik", "Chad", "Chile", "Colombia", "Comorerne", "Congo (Brazzaville)", "Congo (Kinshasa)", "Costa Rica", "Cuba", "Cypern", "Danmark", "Djibouti", "Dominica", "Dominikanske Republik", "Ecuador", "Egypten", "El Salvador", "Elfenbenskysten", "Eritrea", "Estland", "Eswatini", "Etiopien", "Fiji", "Filippinerne", "Finland", "Forenede Arabiske Emirater", "Frankrig", "Gabon", "Gambia", "Georgien", "Ghana", "Grenada", "Grækenland", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hviderusland", "Indien", "Indonesien", "Irak", "Iran", "Irland", "Island", "Israel", "Italien", "Jamaica", "Japan", "Jordan", "Kap Verde", "Kasakhstan", "Kenya", "Kina", "Kirgisistan", "Kiribati", "Kuwait", "Kroatien", "Laos", "Lesotho", "Letland", "Libanon", "Liberia", "Libyen", "Liechtenstein", "Litauen", "Luxembourg", "Madagaskar", "Malawi", "Malaysia", "Maldiverne", "Mali", "Malta", "Marokko", "Marshalløerne", "Mauretanien", "Mauritius", "Mexico", "Mikronesien", "Moldova", "Monaco", "Mongoliet", "Montenegro", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Nederlandene", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Nordkorea", "Nordmakedonien", "Norge", "Oman", "Pakistan", "Palau", "Palæstina", "Panama", "Papua Ny Guinea", "Paraguay", "Peru", "Polen", "Portugal", "Qatar", "Rumænien", "Rusland", "Rwanda", "Saint Kitts og Nevis", "Saint Lucia", "Saint Vincent og Grenadinerne", "Samoa", "San Marino", "Sao Tome og Principe", "Saudi-Arabien", "Schweiz", "Senegal", "Serbien", "Seychellerne", "Sierra Leone", "Singapore", "Slovakiet", "Slovenien", "Salomonøerne", "Somalia", "Sydafrika", "Sydkorea", "Sydsudan", "Spanien", "Sri Lanka", "Sudan", "Surinam", "Sverige", "Syrien", "Tadsjikistan", "Tanzania", "Thailand", "Tjekkiet", "Togo", "Tonga", "Trinidad og Tobago", "Tunesien", "Turkmenistan", "Tuvalu", "Tyrkiet", "Tyskland", "Uganda", "Ukraine", "Ungarn", "Uruguay", "USA", "Usbekistan", "Vanuatu", "Vatikanstaten", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe", "Østrig", "Østtimor"]

def validate_destination_country():
    destination_country = request.form.get("destination_country", "").strip()
    if not destination_country in COUNTRIES:
        raise Exception("--error-- destination_country")
    return destination_country
