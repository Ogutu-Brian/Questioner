from .import meetup_view, status, db, Meetup, Rsvp
from flask import jsonify, request


@meetup_view.route('/meetups', methods=['POST'])
def create_meetup():
    """A post endpoint for creating a meetup"""
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
        return jsonify({
            "message": "Successfully created a meetup",
            "data": [meetup.to_dictionary()],
            "status": status.created
        }), status.created
    else:
        return jsonify({
            "mesaage": "The data must be in JSON",
            "status": status.not_json
        }), status.not_json


@meetup_view.route('/meetups/<meetup_id>', methods=["GET"])
def get_meetup(meetup_id):
    """ A get endpoint for getting a specific meetup given an id"""
    meetup = db.meetups.query_by_field("id", int(meetup_id))
    if not meetup:
        return jsonify({
            "message": "A meetup with that id does not exist",
            "status": status.not_found
        }), status.not_found
    else:
        return jsonify({
            "message": "A meetup was successfully found",
            "data": meetup.to_dictionary(),
            "status": status.success
        }), status.success


@meetup_view.route('/meetups/upcoming/', methods=["GET"])
def get_all_meetups():
    """An endpoint to get all upcoming meetup records"""
    meetups = db.meetups.query_all()
    if not meetups:
        print("No content")
        return jsonify({
            "message": "There are not meetups in the record",
            "status": status.no_content
        }), status.no_content
    result_set = []
    for meetup in meetups:
        result_set.append(meetup.to_dictionary())
    return jsonify({
        "status": status.success,
        "data": result_set,
        "message": "Successfully got all upcoming meetup records"
    })


@meetup_view.route('/meetups/<meetup_id>/rsvps', methods=["POST"])
def create_svp(meetup_id):
    """Endpoint that allows a user to respond to a meetup"""
    if request.is_json:
        valid, errors = db.rsvps.is_valid(request.json)
        if not valid:
            return jsonify({
                "message": "You encountered {} errors".format(len(errors)),
                "status": status.invalid_data
            }), status.invalid_data
        meetup = db.meetups.query_by_field("id", int(meetup_id))
        data = request.json
        if not meetup:
            return jsonify({
                "message": "meetup with that id does not exist",
                "status": status.not_found
            }), status.not_found
        if not db.users.query_by_field("id", data.get("user")):
            return jsonify({
                "message": "a user with that id does not exist",
                "status": status.invalid_data
            }), status.invalid_data
        rsvp = Rsvp(meetup=meetup_id, user=data.get(
            "user"), response=data.get("response"))
        db.rsvps.insert(rsvp)
        return jsonify({
            "message": "successfully created Rsvp",
            "status": status.created,
            "data": [{
                "meetup": meetup_id,
                "topic": meetup.to_dictionary().get("topic"),
                "status": rsvp.response
            }]
        }), status.created
    else:
        return jsonify({
            "message": "The data must be in JSOn",
            "status": status.not_json
        }), status.not_json
