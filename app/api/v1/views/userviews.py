from .import user_view, User, db
from flask import jsonify, request
import bcrypt


@user_view.route('/sign-up', methods=['POST'])
def sign_up():
    if request.is_json:
        valid, errors = db.users.is_valid(request.json)
        if not valid:
            return jsonify({
                "status": "error",
                "data": errors
            }), 406
        else:
            data = request.json
            first_name = data.get("firstname")
            last_name = data.get("lastname")
            other_name = data.get("othername")
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
                "status": "success",
                "data": user.to_dictionary()
            }), 201
    else:
        return jsonify({
            "message": "The data needs to be in JSON",
            "status": "error"
        }), 422
