from flask import Flask, render_template, request, jsonify, session, redirect
import x
import uuid
import time
from flask_session import Session
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from icecream import ic
ic.configureOutput(prefix=f'______ | ', includeContext=True)

app = Flask(__name__)

app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

##############################
@app.get("/signup")
@x.no_cache
def show_signup():
    try:
        user = session.get("user", "")
        return render_template("page_signup.html", user=user, x=x)
    except Exception as ex:
        ic(ex)
        return "ups"

##############################
@app.post("/api-create-user")
def api_create_user():
    try:
        user_first_name = x.validate_user_first_name()
        user_last_name = x.validate_user_last_name()
        user_email = x.validate_user_email()
        user_password = x.validate_user_password()
        user_hashed_password = generate_password_hash(user_password)
        # ic(user_hashed_password) # 'scrypt:32768:8:1$V0NLEqHQsgKyjyA7$3a9f6420e4e9fa7a4e4ce6c89927e7dcb532e5f557aee6309277243e5882cc4518c94bfd629b61672553362615cd5d668f62eedfe4905620a8c9bb7db573de31'

        user_pk = uuid.uuid4().hex
        user_created_at = int(time.time())

        db, cursor = x.db()
        q = "INSERT INTO users VALUES(%s, %s, %s, %s, %s, %s)"
        cursor.execute(q, (user_pk, user_first_name, user_last_name, user_email, user_hashed_password, user_created_at))
        db.commit()

        form_signup = render_template("___form_signup.html", x=x)

        return f"""
            <browser mix-replace="form">{form_signup}</browser>
            <browser mix-redirect="/login"></browser>
        """

    except Exception as ex:
        ic(ex)

        if "company_exception user_first_name" in str(ex):
            error_message = f"user first name {x.USER_FIRST_NAME_MIN} to {x.USER_FIRST_NAME_MAX} characters"
            ___tip = render_template("___tip.html", status="error", message=error_message)
            return f"""<browser mix-after-begin="#tooltip">{___tip}</browser>""", 400

        if "company_exception user_last_name" in str(ex):
            error_message = f"user last name {x.USER_LAST_NAME_MIN} to {x.USER_LAST_NAME_MAX} characters"
            ___tip = render_template("___tip.html", status="error", message=error_message)
            return f"""<browser mix-after-begin="#tooltip">{___tip}</browser>""", 400

        if "company_exception user_email" in str(ex):
            error_message = f"user email invalid"
            ___tip = render_template("___tip.html", status="error", message=error_message)
            return f"""<browser mix-after-begin="#tooltip">{___tip}</browser>""", 400

        if "company_exception user_password" in str(ex):
            error_message = f"user password {x.USER_PASSWORD_MIN} to {x.USER_PASSWORD_MAX} characters"
            ___tip = render_template("___tip.html", status="error", message=error_message)
            return f"""<browser mix-after-begin="#tooltip">{___tip}</browser>""", 400

        if "Duplicate entry" in str(ex) and "user_email" in str(ex):
            error_message = "Email already exists"
            ___tip = render_template("___tip.html", status="error", message=error_message)
            return f"""<browser mix-after-begin="#tooltip">{___tip}</browser>""", 400

        # Worst case
        error_message = "System under maintenance"
        ___tip = render_template("___tip.html", status="error", message=error_message)        
        return f"""<browser mix-after-begin="#tooltip">{___tip}</browser>""", 500


    finally:
        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()

##############################
@app.get("/login")
@x.no_cache
def show_login():
    try:
        user = session.get("user", "")
        if not user: 
            return render_template("page_login.html", user=user, x=x)
        return redirect("/profile")
    except Exception as ex:
        ic(ex)
        return "ups"

##############################
@app.post("/api-login")
def api_login():
    try:
        user_email = x.validate_user_email()
        user_password = x.validate_user_password()

        db, cursor = x.db()
        q = "SELECT * FROM users WHERE user_email = %s"
        cursor.execute(q, (user_email,))
        user = cursor.fetchone()
        
        if not user:
            error_message = "Invalid credentials 1"
            ___tip = render_template("___tip.html", status="error", message=error_message)
            return f"""<browser mix-after-begin="#tooltip">{___tip}</browser>""", 400

        if not check_password_hash(user["user_password"], user_password):
            error_message = "Invalid credentials 2"
            ___tip = render_template("___tip.html", status="error", message=error_message)
            return f"""<browser mix-after-begin="#tooltip">{___tip}</browser>""", 400            

        user.pop("user_password")
        session["user"] = user

        return f"""<browser mix-redirect="/profile"></browser>"""

    except Exception as ex:
        ic(ex)

        if "--error-- user_email" in str(ex):
            error_message = f"user email invalid"
            ___tip = render_template("___tip.html", status="error", message=error_message)
            return f"""<browser mix-after-begin="#tooltip">{___tip}</browser>""", 400

        if "--error-- user_password" in str(ex):
            error_message = f"user password {x.USER_PASSWORD_MIN} to {x.USER_PASSWORD_MAX} characters"
            ___tip = render_template("___tip.html", status="error", message=error_message)
            return f"""<browser mix-after-begin="#tooltip">{___tip}</browser>""", 400

        # Worst case
        error_message = "System under maintenance"
        ___tip = render_template("___tip.html", status="error", message=error_message)        
        return f"""<browser mix-after-begin="#tooltip">{___tip}</browser>""", 500


    finally:
        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()

##############################
@app.get("/profile")
@x.no_cache
def show_profile():
    try:
        user = session.get("user", "")
        if not user: return redirect("/login")

        db, cursor = x.db()
        q = "SELECT * FROM user_destinations WHERE user_fk = %s"
        cursor.execute(q,(user["user_pk"],))
        destinations = cursor.fetchall()

        return render_template("page_profile.html", user=user, x=x, countries=x.COUNTRIES, destinations=destinations)
    except Exception as ex:
        ic(ex)
        return "ups"

##############################
@app.get("/logout")
def logout():
    try:
        session.clear()
        return redirect("/login")
    except Exception as ex:
        ic(ex)
        return "ups"    

##############################
@app.delete("/user_destinations/<destination_pk>")
def delete_destination(destination_pk):
    try: 
        db, cursor = x.db()
        q = "DELETE FROM user_destinations WHERE destination_pk = %s"
        cursor.execute(q, (destination_pk,))
        db.commit()

        return f"""<browser mix-remove="#destination-{destination_pk}" 
                mix-fade-2000></browser> """
    except Exception as ex: 
        ic(ex)
        return "ups ...", 500
    finally: 
        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()

##############################
@app.get("/user_destinations/<destination_pk>")
def get_destination_by_id(destination_pk):
    try:
        # Best case scenario
        # TODO: Validate the id

        db, cursor = x.db()
        q = "SELECT * FROM user_destinations WHERE destination_pk = %s"
        cursor.execute(q, (destination_pk,))
        destination = cursor.fetchone()

        destination_more_html = render_template("___destination_more.html", destination=destination)

        return f"""
            <browser>
            {destination_more_html}
            </browser>
        """
    except Exception as ex:
        ic(ex)
        return "ups ...", 500
    finally:
        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()

##############################
@app.get("/travel-details/<destination_pk>")
@x.no_cache
def travel_detail(destination_pk):
    try:
        user = session.get("user", "")
        if not user: return redirect("/login")

        db, cursor = x.db()
        q = "SELECT * FROM user_destinations WHERE destination_pk = %s AND user_fk = %s"
        cursor.execute(q, (destination_pk, user["user_pk"]))
        destination = cursor.fetchone()
        db.commit()

        if not destination:
            return redirect("/profile")

        return render_template("page_travel_details.html", user=user, x=x, countries=x.COUNTRIES, destination=destination)
    except Exception as ex:
        ic(ex)
        return "Could not get edit page",500
    finally:
        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()

##############################
@app.get("/update-destination/<destination_pk>")
@x.no_cache
def show_update_destination(destination_pk):
    try:
        user = session.get("user", "")
        if not user: return redirect("/login")

        db, cursor = x.db()
        q = "SELECT * FROM user_destinations WHERE destination_pk = %s AND user_fk = %s"
        cursor.execute(q, (destination_pk, user["user_pk"]))
        destination = cursor.fetchone()
        db.commit()

        if not destination:
            return redirect("/profile")

        return render_template("page_update_destination.html", user=user, x=x, countries=x.COUNTRIES, destination=destination)
    except Exception as ex:
        ic(ex)
        return "Could not get edit page",500
    finally:
        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()

##############################
@app.patch("/api-update-destination/<destination_pk>")
def update_destination_by_id(destination_pk):
    try:

        parts = []
        values = []

        destination_title = x.validate_destination_title()
        destination_start_date = x.validate_destination_start_date()
        destination_end_date = x.validate_destination_end_date(destination_start_date)
        destination_description = x.validate_destination_description()
        destination_location = x.validate_destination_location()
        destination_country = request.form.get("destination_country", "")
        
        if destination_title:
            parts.append("destination_title = %s")
            values.append(destination_title)

        if destination_start_date:
            parts.append("destination_start_date = %s")
            values.append(destination_start_date)
        
        if destination_end_date:
            parts.append("destination_end_date = %s")
            values.append(destination_end_date)
        
        if destination_description:
            parts.append("destination_description = %s")
            values.append(destination_description)
        
        if destination_location:
            parts.append("destination_location = %s")
            values.append(destination_location)
        
        if destination_country:
            parts.append("destination_country = %s")
            values.append(destination_country)

        if not parts: return "nothing to update", 400

        values.append(destination_pk)

        # Convert the list to a string with a comma in between
        partial_query = ", ".join(parts)

        q = f"""
            UPDATE user_destinations
            SET	{partial_query}
            WHERE destination_pk = %s
        """

        db, cursor = x.db()
        cursor.execute(q, values)
        db.commit()

        return """ <browser mix-redirect="page_profile.html"></browser>"""

    except Exception as ex:
        ic(ex)

        if "--error-- destination_title" in str(ex):
            error_message = f"destination title invalid"
            ___tip = render_template("___tip.html", status="error", message=error_message)
            return f"""<browser mix-after-begin="#tooltip">{___tip}</browser>""", 400

        if "--error-- destination_description" in str(ex):
            error_message = f"destination description invalid"
            ___tip = render_template("___tip.html", status="error", message=error_message)
            return f"""<browser mix-after-begin="#tooltip">{___tip}</browser>""", 400

        if "--error-- destination_location" in str(ex):
            error_message = f"destination location invalid"
            ___tip = render_template("___tip.html", status="error", message=error_message)
            return f"""<browser mix-after-begin="#tooltip">{___tip}</browser>""", 400

        if "--error-- end date can not be before start date" in str(ex):
            error_message = "End date can not be before start date"
            ___tip = render_template("___tip.html", status="error", message=error_message)
            return f"""<browser mix-after-begin="#tooltip">{___tip}</browser>""", 400

        # Worst case
        error_message = "System under maintenance"
        ___tip = render_template("___tip.html", status="error", message=error_message)        
        return f"""<browser mix-after-begin="#tooltip">{___tip}</browser>""", 500


        # Cast the exception to an string
        # return str(ex), 500 # Internal server error
    finally:
        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()

##############################
@app.get("/create-destination")
@x.no_cache
def show_create_destination():
    try:
        user = session.get("user", "")
        if not user: return redirect("/login")

        db, cursor = x.db()
        q = "SELECT * FROM user_destinations WHERE user_fk = %s"
        cursor.execute(q,(user["user_pk"],))

        return render_template("page_create_destination.html", user=user, x=x, countries=x.COUNTRIES)
    except Exception as ex:
        return "system under maintenance ...", 500

##############################
@app.post("/api-add-destination")
def add_destination():
    try:
        destination_title = x.validate_destination_title()
        destination_pk = uuid.uuid4().hex
        destination_start_date = x.validate_destination_start_date()
        destination_end_date = x.validate_destination_end_date(destination_start_date)
        destination_description = x.validate_destination_description()
        destination_location = x.validate_destination_location()
        destination_country = x.validate_destination_country()
    
        if not session.get("user"):
            return "Login please", 401
        
        logged_in_user_pk = session["user"]["user_pk"]

        db, cursor = x.db()
        q = "INSERT INTO user_destinations VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(q, (logged_in_user_pk, destination_pk, destination_title, destination_start_date, destination_end_date, destination_description, destination_location, destination_country))
        db.commit()

        destination = {
            "destination_pk": destination_pk, 
            "destination_title": destination_title,
            "destination_start_date": destination_start_date,
            "destination_end_date": destination_end_date,
            "destination_description": destination_description,
            "destination_location": destination_location,
            "destination_country" : destination_country
        }

        message = "Destination created!"
        
        destination_html = render_template("___destination.html", destination=destination)
        ___tip = render_template("___tip.html", status="ok", message=message)
    
    
        return f"""
        <browser 
            mix-after-begin="#destinations" mix-redirect="/profile"
        >
            {destination_html}
        </browser>
        <browser mix-after-begin="#tooltip">{___tip}</browser>
        """

    except Exception as ex: 

        ic(ex)

        if "--error-- destination_title" in str(ex):
            error_message = f"destination title invalid"
            ___tip = render_template("___tip.html", status="error", message=error_message)
            return f"""<browser mix-after-begin="#tooltip">{___tip}</browser>""", 400

        if "--error-- destination_description" in str(ex):
            error_message = f"destination description invalid"
            ___tip = render_template("___tip.html", status="error", message=error_message)
            return f"""<browser mix-after-begin="#tooltip">{___tip}</browser>""", 400

        if "--error-- destination_location" in str(ex):
            error_message = f"destination location invalid"
            ___tip = render_template("___tip.html", status="error", message=error_message)
            return f"""<browser mix-after-begin="#tooltip">{___tip}</browser>""", 400

        if "--error-- end date can not be before start date" in str(ex):
            error_message = "End date can not be before start date"
            ___tip = render_template("___tip.html", status="error", message=error_message)
            return f"""<browser mix-after-begin="#tooltip">{___tip}</browser>""", 400

        # Worst case
        error_message = "System under maintenance"
        ___tip = render_template("___tip.html", status="error", message=error_message)        
        return f"""<browser mix-after-begin="#tooltip">{___tip}</browser>""", 500

    finally: 
        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()