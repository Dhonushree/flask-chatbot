"""Chat route handler."""
from flask import Blueprint, jsonify, request, render_template
from .nlp_processor import process_query

chat = Blueprint('chat', __name__)

@chat.route('/api/chat', methods=['POST'])
def handle_query():
    """API endpoint for chatbot query."""
    try:
        user_input = request.json['message']
        response = process_query(user_input)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@chat.route('/chat', methods=['GET'])
def chat_ui():
    """Serve the chatbot interface."""
    return render_template('chat.html')
