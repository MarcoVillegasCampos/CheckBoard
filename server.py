from flask import Flask, render_template


app= Flask( __name__)


@app.route('/play', methods=['GET'])
def loadHome():
    
    return render_template('index.html')


@app.route('/play/<x>/<y>', methods=['GET'])
def loadTimes(x,y):
    x=int(x)
    y=int(y)
    return render_template('index.html', x=x, y=y)

@app.route('/play/<times>/<color>', methods=['GET'])
def loadColor(times,color):
    numBoxes=int(times)    
    return render_template('index.html', numBoxes=numBoxes, color=color)





if __name__ == "__main__":
    app.run(debug=True)
    