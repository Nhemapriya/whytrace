from whytrace import why
@why
def approve_loan(user):
    if user["credit_score"] > 700 and not user["blacklisted"]:
        print("Loan approved")
    elif user["credit_score"] > 650:
        print("Manual review")
    else:
        print("Rejected")

approve_loan(
    user={"credit_score": 680, "blacklisted": False}
)
