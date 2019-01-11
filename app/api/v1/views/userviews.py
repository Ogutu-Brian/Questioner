from .import user_view, User, db, status
from flask import jsonify, request, session
import bcrypt


@user_view.route('/sign-up', methods=['POST'])
def sign_up():
    """A post endpoint for creating a user or for sign up"""
    if request.is_json:
        valid, errors = db.users.is_valid(request.json)
        if not valid:
            return jsonify({
                "message": "You encountered {} errors".format(len(errors)),
                "status": status.invalid_data,
                "data": errors
            }), status.invalid_data
        else:
            data = request.json
            other_name = ""
            if data.get("othername"):
                other_name = data.get("othername")
            first_name = data.get("firstname")
            last_name = data.get("lastname")
            email = data.get("email")
            phone_number = data.get("phoneNumber")
            user_name = data.get("username")
            password = bcrypt.hashpw(data.get("password").encode(
                'utf8'), bcrypt.gensalt()).decode('utf8')
            user = User(first_name=first_name, last_name=last_name,
                        other_name=other_name, email=email, phone_number=phone_number, user_name=user_name, password=password)
            db.users.insert(user)
            return jsonify({
                "message": "Successuflly signed up",
                "status": status.created,
                "data": [user.to_dictionary()]
            }), status.created
    else:
        return jsonify({
            "message": "The data needs to be in JSON",
            "status": status.not_json
        }), status.not_json


@user_view.route('/log-in', methods=["POST"])
def login():
    """A post endpoint for a user login into Questioner"""
    if request.is_json:
        username = request.json.get("username")
        email = request.json.get("email")
        password = request.json.get("password")
        if not email and not username:
            return jsonify({
                "message": "Provide your username or email in order to log in",
                "status": status.invalid_data
            }), status.invalid_data
        if not password:
            return jsonify({
                "message": "Plase provide password in order to log in",
                "status": status.invalid_data
            }), status.invalid_data
        if username:
            if not db.users.query_by_field("username", username):
                return jsonify({
                    "message": "A user with that username does not exist",
                    "status": status.denied_access
                }), status.denied_access
            else:
                user = db.users.query_by_field("username", username)
                if bcrypt.checkpw(password.encode('utf8'), user.password.encode('utf8')):
                    session["email"] = user.email
                    return jsonify({
                        "message": "successfully logged into Questioner",
                        "status": status.success
                    }), status.success
                else:
                    return jsonify({
                        "message": "Invalid password",
                        "status": status.denied_access
                    }), status.denied_access
        else:
            if not db.users.query_by_field("email", email):
                return jsonify({
                    "message": "A user with that email address does not exist",
                    "status": status.denied_access
                }), status.denied_access
            else:
                user = db.users.query_by_field("email", email)
                if bcrypt.checkpw(password.encode('utf'), user.password.encode('utf8')):
                    session["email"] = user.email
                    return jsonify({
                        "message": "successfully logged into Questioner",
                        "status": status.success
                    }), status.success
                else:
                    return jsonify({
                        "message": "Invalid password",
                        "status": status.denied_access
                    }), status.denied_access
    else:
        return jsonify({
            "message": "The data needs to be JSON",
            "status": status.not_json
        }), status.not_json
