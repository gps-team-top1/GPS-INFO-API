from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/player-info")
def player_info():
    uid = request.args.get("uid")
    region = request.args.get("region")
    # هنا ضع منطقك لإرجاع بيانات اللاعب
    return jsonify({"uid": uid, "region": region})