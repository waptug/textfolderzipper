from flask import Flask, jsonify, request
import os
import stripe
from send_email import send_zip_email  # You'll need to implement this to send emails with attachments

app = Flask(__name__)

ZIP_FOLDER = "path/to/secure/zip/folder"
stripe.api_key = "YOUR_STRIPE_SECRET_KEY"

@app.route("/list_files", methods=["GET"])
def list_files():
    files = os.listdir(ZIP_FOLDER)
    return jsonify(files)

@app.route("/buy_file", methods=["POST"])
def buy_file():
    data = request.json
    # Implement the Stripe payment logic here...
    # After successful payment, send the ZIP file to the user's email
    file_path = os.path.join(ZIP_FOLDER, data["file"])
    send_zip_email(data["email"], data["name"], file_path)
    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(debug=True)
