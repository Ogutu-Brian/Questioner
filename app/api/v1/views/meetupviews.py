from .import meetup_view, status, db, Meetup, Rsvp
from flask import jsonify, request, make_response


@meetup_view.route('/meetups', methods=['POST'])
def create_meetup():
    """A post endpoint for creating a meetup"""
    cummulative_errors = []
    if request.is_json:
        valid, errors = db.meetups.is_valid(request.json)
        if not valid:
            cummulative_errors.append({
                "message": "You encountered {} errors".format(len(errors)),
                "data": errors,
                "status": status.invalid_data
            }), status.invalid_data
        else:
            data = request.json
            location = data.get("location")
            images = data.get("images")
            topic = data.get("topic")
            happening_on = data.get("happeningOn")
            tags = data.get("Tags")
            meetup = Meetup(location=location, images=images,
                            topic=topic, happening_on=happening_on, tags=tags)
            db.meetups.insert(meetup)
    else:
        cummulative_errors.append({
            "mesaage": "The data must be in JSON",
            "status": status.not_json
        }), status.not_json
    response = None
    if not cummulative_errors:
        response = jsonify({
            "message": "Successfully created a meetup",
            "data": [meetup.to_dictionary()],
            "status": status.created
        }), status.created
    else:
        response = jsonify(
            cummulative_errors[0]
        ), cummulative_errors[0].get("status")
    return response


@meetup_view.route('/meetups/<meetup_id>', methods=["GET"])
def get_meetup(meetup_id):
    """ A get endpoint for getting a specific meetup given an id"""
    response = None
    meetup = db.meetups.query_by_field("id", int(meetup_id))
    if not meetup:
        response = jsonify({
            "message": "A meetup with that id does not exist",
            "status": status.not_found
        }), status.not_found
    else:
        response = jsonify({
            "message": "A meetup was successfully found",
            "data": meetup.to_dictionary(),
            "status": status.success
        }), status.success
    return response


@meetup_view.route('/meetups/upcoming/', methods=["GET"])
def get_all_meetups():
    """An endpoint to get all upcoming meetup records"""
    response = None
    meetups = db.meetups.query_all()
    if not meetups:
        response = jsonify({
            "message": "There are not meetups in the record",
            "status": status.no_content
        }), status.no_content
    else:
        result_set = []
        for meetup in meetups:
            result_set.append(meetup.to_dictionary())
        response = jsonify({
            "status": status.success,
            "data": result_set,
            "message": "Successfully got all upcoming meetup records"
        }), status.success
    return response


@meetup_view.route('/meetups/<meetup_id>/rsvps', methods=["POST"])
def create_svp(meetup_id):
    """Endpoint that allows a user to respond to a meetup"""
    response = None
    cummulative_errors = []
    if request.is_json:
        valid, errors = db.rsvps.is_valid(request.json)
        if not valid:
            cummulative_errors.append({
                "message": "You encountered {} errors".format(len(errors)),
                "status": status.invalid_data
            })
        else:
            meetup = db.meetups.query_by_field("id", int(meetup_id))
            data = request.json
            if not meetup:
                cummulative_errors.append({
                    "message": "meetup with that id does not exist",
                    "status": status.not_found
                })
            elif not db.users.query_by_field("id", data.get("user")):
                cummulative_errors.append({
                    "message": "a user with that id does not exist",
                    "status": status.invalid_data
                })
            else:
                rsvp = Rsvp(meetup=meetup_id, user=data.get(
                    "user"), response=data.get("response"))
                db.rsvps.insert(rsvp)
                response = jsonify({
                    "message": "successfully created Rsvp",
                    "status": status.created,
                    "data": [{
                        "meetup": meetup_id,
                        "topic": meetup.to_dictionary().get("topic"),
                        "status": rsvp.response
                    }]
                }), status.created
    else:
        response = jsonify({
            "message": "The data must be in JSOn",
            "status": status.not_json
        }), status.not_json
    if cummulative_errors:
        response = jsonify(
            cummulative_errors[0]), cummulative_errors[0].get("status")
    return response
