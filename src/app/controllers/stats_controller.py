from app.models.dictionary import Dictionary
from flask import Blueprint
from flask import request, Response

stats = Blueprint('stats', __name__)


@stats.route('/stats', methods=['GET'])
def get_stats():
    """Get top most requested words

    Returns a list of JSON objects with the top 'N' where 5 <= N <= 100 most downloaded words.

    query parameter: /stats?limit=somenumber
    where 5 <= somenumber <= 100

    no request body

    :rtype: List[Dictionary]
    """
    limit = int(request.args.get('limit'))
    if limit < 5 or limit > 100:
        limit = 20
    o = Dictionary.objects(in_dictionary=False).order_by(
        '-times_requested')[:limit]
    return Response(o.to_json(), mimetype='application/json')
