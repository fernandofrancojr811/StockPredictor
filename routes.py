from flask import render_template, request
from model_integration import make_prediction

def init_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/predict', methods=['POST'])
    def predict():
        # Extract features from the request
        # Example: feature1 = request.form['feature1']
        
        # Call the prediction function
        prediction = make_prediction([feature1, feature2, ...])

        # Render a template or return a response with the prediction
        return render_template('result.html', prediction=prediction)