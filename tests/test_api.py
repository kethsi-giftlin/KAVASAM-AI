from fastapi.testclient import TestClient
from app.main import app

client=TestClient(app)

def test_health(): assert client.get('/health').json()['status']=='ok'

def test_root(): assert client.get('/').json()['name']=='Kavasam AI'

def test_register_login():
    email='test_user_kavasam@example.com'
    r=client.post('/api/auth/register',json={'name':'Test User','email':email,'password':'StrongPass123!'})
    if r.status_code==400:
        r=client.post('/api/auth/login',json={'email':email,'password':'StrongPass123!'})
    assert r.status_code==200
    token=r.json()['token']
    h={'Authorization':'Bearer '+token}
    a=client.post('/api/analyze/text',json={'text':'URGENT! Your bank account will be blocked today. Send your OTP.'},headers=h)
    assert a.status_code==200 and a.json()['risk_score']>=40
