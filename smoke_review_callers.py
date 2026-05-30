from smoke_review_target import PaymentClient, calculate_discount


def preview_checkout():
    discount = calculate_discount(100, 15)
    return PaymentClient().charge("alice", discount, "demo-password")
