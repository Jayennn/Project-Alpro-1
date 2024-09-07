from flask import jsonify, Response


def success_response(data: object, status: int = 200) -> Response:
    """Format a successful response."""
    return jsonify({
        "status": status,
        "message": "Successful Response",
        "data": data,
        "success": True
    })

def error_response(message: str, status: int) -> Response:
    """Format an error response."""
    return jsonify({
        "status": status,
        "message": message,
        "success": False
    })
