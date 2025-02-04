from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password_strength(password):
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[@!#$%^&*()_\-+={}[\]:;\'?/>.<",~`]', password))
    length_ok = len(password) > 8  # More than 8 characters

    # Strong: Must have all 5 conditions
    if has_upper and has_lower and has_digit and has_special and length_ok:
        return "Strong"

    # Moderate: Must meet at least 3 of the 4 conditions
    conditions_met = sum([has_upper and has_lower, has_digit, has_special, length_ok])
    if conditions_met >= 3:
        return "Moderate"

    return "Weak"

@app.route("/", methods=["GET", "POST"])
def index():
    strength = None
    if request.method == "POST":
        password = request.form.get("password")
        strength = check_password_strength(password)
    
    return render_template("index.html", strength=strength)

if __name__ == "__main__":
    app.run(debug=True)
