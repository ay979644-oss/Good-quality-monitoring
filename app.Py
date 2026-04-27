from flask import Flask, render_template, request
import random
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['image']

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Dummy AI Logic (Hackathon Demo)
        result = random.choice(["Fresh ✅", "Stale ⚠️", "Unsafe ❌"])
        score = random.randint(40, 100)

        return render_template('result.html', result=result, score=score, image=filepath)

    return "Error uploading file"

if __name__ == '__main__':
    app.run(debug=True)
