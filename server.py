from flask import Flask, render_template


app= Flask( __name__)


@app.route('/play', methods=['GET'])
def loadHome():
    numBoxes=int(3)
    return render_template('index.html',numBoxes=numBoxes)


@app.route('/play/<times>', methods=['GET'])
def loadTimes(times):
    numBoxes=int(times)
    return render_template('index.html', numBoxes=numBoxes)

@app.route('/play/<times>/<color>', methods=['GET'])
def loadColor(times,color):
    numBoxes=int(times)    
    return render_template('index.html', numBoxes=numBoxes, color=color)





if __name__ == "__main__":
    app.run(debug=True)
    