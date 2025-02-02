import os
import flask

from ikamail.GmailHelper import GmailHelper

app = flask.Blueprint("google_gmail", __name__)
app.secret_key = os.environ.get("FN_FLASK_SECRET_KEY", default=False)


@app.route("/gmail/test", methods=["GET"])
def test_api_request():
    mails_id = GmailHelper("prod").get_message_id(
        "me", include_spam_trash=True, max_results=10
    )

    return flask.jsonify(results=mails_id)
