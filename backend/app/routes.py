from flask import Blueprint, jsonify, request
from .models import SpecialPlan, SpecialScore
from . import db

main = Blueprint('main', __name__)

@main.route('/api/special-plan', methods=['GET'])
def get_special_plan():
    filters = request.args
    query = SpecialPlan.query
    
    for attr, value in filters.items():
        query = query.filter(getattr(SpecialPlan, attr) == value)
    
    results = query.limit(100).all()
    return jsonify([result.as_dict() for result in results])

@main.route('/api/special-score', methods=['GET'])
def get_special_score():
    filters = request.args
    query = SpecialScore.query
    
    for attr, value in filters.items():
        query = query.filter(getattr(SpecialScore, attr) == value)
    
    results = query.limit(100).all()
    return jsonify([result.as_dict() for result in results])
