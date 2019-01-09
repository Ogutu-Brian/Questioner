from .import user_view, User, db, status
from flask import jsonify, request
import bcrypt


@user_view.route('/sign-up', methods=['POST'])
def sign_up():
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
            result_set = []
            for user_ in db.users.query_all():
                result_set.append(user_.to_dictionary())
            return jsonify({
                "message": "Successuflly signed up",
                "status": status.created,
                "data": result_set
            }), status.created
    else:
        return jsonify({
            "message": "The data needs to be in JSON",
            "status": status.not_json
        }), status.not_json
