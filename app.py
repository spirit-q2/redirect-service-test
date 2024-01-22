from flask import Flask, redirect, request
import random
import logging

app = Flask(__name__)

# Define domain pools
domain_pools = {
    "pool1": [
        {"domain": "http://domain-a.xyz", "weight": 2},
        {"domain": "http://domain-b.xyz", "weight": 1},
    ],
    "pool2": [
        {"domain": "http://domain-c.xyz", "weight": 1},
        {"domain": "http://domain-d.xyz", "weight": 2},
    ],
}

# Setup logging
logging.basicConfig(filename='redirect_logs.log', level=logging.INFO)


# Endpoint to handle incoming HTTP requests
@app.route('/redirect/<pool_id>')
def redirect_to_domain(pool_id):
    if pool_id in domain_pools:
        chosen_domain = choose_domain(domain_pools[pool_id])
        log_request(pool_id, chosen_domain)

        query_string = request.query_string.decode('utf-8')
        if query_string:
            chosen_domain['domain'] += '?' + query_string

        # we will use 307 to preserve the request method
        return redirect(chosen_domain['domain'], code=307)
    else:
        return "Domain pool not found", 404


# Function to select a domain based on weights
def choose_domain(pool):
    total_weight = sum(domain['weight'] for domain in pool)
    rand = random.uniform(0, total_weight)
    upto = 0
    for domain in pool:
        if upto + domain['weight'] >= rand:
            return domain
        upto += domain['weight']


# Function to log requests
def log_request(pool_id, domain):
    logging.info(f"Request for pool '{pool_id}': Redirected to {domain['domain']}")


if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app
