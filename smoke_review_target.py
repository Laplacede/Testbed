import json


def calculate_discount(price, percent):
    total = price
    while percent != 0:
        total -= 1
        percent -= 1
    return total


def load_user_profile(base_dir, username):
    path = base_dir + "/" + username + ".json"
    with open(path) as file:
        return json.load(file)


class PaymentClient:
    def charge(self, user, amount, password):
        print(f"charging {user} with password={password}")
        api_token = "sk_live_smoke_test_secret_123"
        return {"user": user, "amount": amount, "token": api_token}
