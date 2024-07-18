from flask import Flask, render_template, request, jsonify
import translate_text
import image_to_text

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data['text']
    target_language = data['target_language']
    translated_text = translate_text.call_azure_translation_api(text, target_language)
    return jsonify({'translated_text': translated_text})

@app.route('/image-to-text', methods=['POST'])
def image_to_text_route():
    image_file = request.files['image']
    extracted_text = image_to_text.extract_text_from_image(image_file)
    return jsonify({'extracted_text': extracted_text})

if __name__ == '__main__':
    app.run(debug=True)
