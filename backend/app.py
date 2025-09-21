from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Clé API OpenAI (à configurer via une variable d'environnement ou un fichier sécurisé)
openai.api_key = "VOTRE_CLE_API"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')

    if not user_message:
        return jsonify({"error": "Message utilisateur manquant"}), 400

    try:
        # Appel à l'API OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Tu es un assistant amical et intelligent."},
                {"role": "user", "content": user_message}
            ]
        )
        return jsonify({"response": response['choices'][0]['message']['content']})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
