from flask import Flask, jsonify, request
from text_generation import generate_response, generate_background_image_prompt
from image_generation import create_image
app = Flask(__name__)


@app.route('/generate_text', methods=['POST'])
async def generate_text():
    data = request.get_json()
    messages = data.get('messages', [])
    scenario = data.get('scenario', '')
    # print(messages, scenario)

    response = await generate_response(messages, scenario)
    return jsonify({"response": response.strip()})


@app.route('/generate_background_image', methods=['POST'])
async def generate_background_image():
    data = request.get_json()
    messages = data.get('messages', [])
    scenario = data.get('scenario', '')
    style = data.get('style', '')
    print(messages, scenario, style)

    image_prompt = await generate_background_image_prompt(messages, scenario, style)
    response = await create_image(image_prompt.strip())
    return jsonify({"response": str(response)})


if __name__ == '__main__':
    app.run(debug=True)
