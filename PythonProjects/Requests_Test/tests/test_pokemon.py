import requests
import pytest

token='ca2b8b647c2a3f1a74f0876fa7e35154'
host='https://api.pokemonbattle.me:9104' 

def test_status_code():
    responce =requests.get(f'{host}/trainers', params={'trainer_id': 1703})
    assert responce.status_code == 200