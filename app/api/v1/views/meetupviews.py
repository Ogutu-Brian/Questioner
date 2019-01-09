from .import meetup_view, status, db, Meetup
from flask import jsonify, request


@meetup_view.route('/meetups', methods=['POST'])
def create_meetup():
    if request.is_json:
        valid, errors = db.meetups.is_valid(request.json)
        if not valid:
            return jsonify({
                "message": "You encountered {} errors".format(len(errors)),
                "data": errors,
                "status": status.invalid_data
            }), status.invalid_data
        data = request.json
        location = data.get("location")
        images = data.get("images")
        topic = data.get("topic")
        happening_on = data.get("happeningOn")
        tags = data.get("Tags")
        meetup = Meetup(location=location, images=images,
                        topic=topic, happening_on=happening_on, tags=tags)
        db.meetups.insert(meetup)
        result_set = []
        for meetup_ in db.meetups.query_all().values():
            result_set.append(meetup_.to_dictionary())
        return jsonify({
            "message": "Successfully created a meetup",
            "data": result_set,
            "status": status.created
        }), status.created
    else:
        return jsonify({
            "mesaage": "The data must be in JSON",
            "status": status.not_json
        }), status.not_json
