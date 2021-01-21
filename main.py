from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def splash():
    return render_template('splash.html')

@app.route('/play/video=<videoID>&sound=<soundID>')
def dualplayers(videoID, soundID):
    return render_template('dualplayer.html', ids={'videoid': str(videoID), 'soundid': str(soundID)})

if __name__ == "__main__":
    app.run(
        debug=True
    )
    