# -*- coding: utf-8 -*-
import pytest


@pytest.fixture()
def db():
    print("connection successful")

    yield

    print('connection closed')


def search_user(user_id):
    d = {
        '001': 'xiaoming'
    }
    return d[user_id]


def test_search(db):
    assert search_user('001') == 'xiaoming'
