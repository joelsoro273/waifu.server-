from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Bienvenue sur mon serveur Flask hébergé sur Render !"

@app.route('/waifu',  methods=['POST'])
def waifu():
  data = request.json
  message = data.get("message","")
  print(f"Message reçu : {message}")

  # Réponse simulée avec une fausse URL de video
  return jsonify({"video_url":
"http://example.com/video.mp4"})

if __name__ =='__main__':
  app.run(host="0.0.0.0", port=5000)
