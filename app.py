from flask import Flask, render_template, request
import requests
app = Flask(__name__)

@app.route('/',methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        formData = request.form
        print(formData)
        print('post method')
        emailList = ['tanner.cordovatech@gmail.com','clayton@reviewlifter.com']
        requests.post(
        "https://api.mailgun.net/v3/reviewlifter.com/messages",
        auth=("api", "key-8fea8050ead5fed2215fac30f0a29f4a"),
        data={"from": "Review Lifter <postmaster@reviewlifter.com>",
        "to": 'tanner.cordovatech@gmail.com',
        "subject": "New Lead",
        "html": render_template('emailResults.html',result=formData)})

        return render_template('emailResults.html')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)