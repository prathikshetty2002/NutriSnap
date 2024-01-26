from flask import Flask, request, jsonify
import google.generativeai as genai  
import requests  
import os
from dotenv import load_dotenv
from PIL import Image
import requests
from io import BytesIO

load_dotenv()
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

app = Flask(__name__)


@app.route('/body-analyse', methods=['GET'])
def body_analyse():
   
    img_url = request.args.get('img_url')

    if img_url:
        
        response = requests.get(img_url)

        
        if response.status_code == 200:
          
            image = Image.open(BytesIO(response.content))

           
            model = genai.GenerativeModel('gemini-pro-vision')

            response = model.generate_content(["Analyse the person and give output in this manner eg {'status':'healthy','description':'the person looks healthy and active lean', 'est body fat':'30 percent', 'remedies':'maintain diet and cardio' pls give a comprehensive report in remedies pointwise}", image], stream=True)
            response.resolve()

           
            return jsonify({"result": response.text})
        else:
            return jsonify({"error": "Failed to retrieve the image"}), 400
    else:
        return jsonify({"error": "img_url parameter is required"}), 400
    

@app.route('/food-snap', methods=['GET'])
def food_snap():
   
    img_url = request.args.get('img_url')

    if img_url:
        
        response = requests.get(img_url)

        
        if response.status_code == 200:
          
            image = Image.open(BytesIO(response.content))

           
            model = genai.GenerativeModel('gemini-pro-vision')

            response = model.generate_content(["Analyse the food and give output in this manner eg {'status':'unhealthy','description':'the food contains paneer and gravy'. 'est calories':'400-500 cal'}", image], stream=True)
            response.resolve()

           
            return jsonify({"result": response.text})
        else:
            return jsonify({"error": "Failed to retrieve the image"}), 400
    else:
        return jsonify({"error": "img_url parameter is required"}), 400
    
@app.route('/skin-analyse', methods=['GET'])
def skin_analyse():
   
    img_url = request.args.get('img_url')

    if img_url:
        
        response = requests.get(img_url)

        
        if response.status_code == 200:
          
            image = Image.open(BytesIO(response.content))

           
            model = genai.GenerativeModel('gemini-pro-vision')

            response = model.generate_content(["Analyse the skin of this human and suggest any remedies if necessary eg in this format {'status':'healthy' ,'description':'The skin appears to be healthy and clear', 'remedies':'However, the person may want to consider using a moisturizer to keep their skin hydrated, especially if they live in a dry climate. Additionally, the person may want to consider using a sunscreen with an SPF of 30 or higher to protect their skin from the sun's harmful UV rays.'}", image], stream=True)
            response.resolve()

           
            return jsonify({"result": response.text})
        else:
            return jsonify({"error": "Failed to retrieve the image"}), 400
    else:
        return jsonify({"error": "img_url parameter is required"}), 400



if __name__ == '__main__':
    app.run(debug=True)

