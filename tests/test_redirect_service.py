from app import app, choose_domain

import pytest


# Fixture to set up the Flask app client for testing
@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


@pytest.mark.parametrize(
    "pool_id, expected_domains",
    [
        ("pool1", ["http://domain-a.xyz", "http://domain-b.xyz"]),
        ("pool2", ["http://domain-c.xyz", "http://domain-d.xyz"]),
    ],
)
def test_redirect_endpoint(client, pool_id, expected_domains):
    response = client.get("/redirect/" + pool_id)

    # Check if the redirection is to one of the domains in the pool
    assert response.headers["Location"] in expected_domains

    # Check if redirection returns a 307 status code
    assert response.status_code == 307


def test_redirect_endpoint_not_existing_pool(client):
    response = client.get("/redirect/not_existing_pool")
    assert response.status_code == 404


def test_choose_domain():
    test_pool = [
        {"domain": "domain-a.xyz", "weight": 2},
        {"domain": "domain-b.xyz", "weight": 1},
    ]
    chosen_domain = choose_domain(test_pool)
    assert chosen_domain in test_pool  # Check if the chosen domain is in the pool
