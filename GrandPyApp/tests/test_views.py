

def test_should_status_code_ok_for_index(client):
    response = client.get('/')
    assert response.status_code == 200


def test_should_status_code_ok_for_index_question(client):
    response = client.post('/index_question')
    assert response.status_code == 200
