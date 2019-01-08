from .import meetup_view
from flask import jsonify, request


@meetup_view.route('/meetups', methods=['POST'])
def create_meetup():
    pass