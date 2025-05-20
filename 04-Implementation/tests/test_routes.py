"""Test for chat endpoint."""
def test_chat_endpoint(client):
    response = client.post('/api/chat', json={'message': 'When is HW due?'})
    assert b'homework' in response.data