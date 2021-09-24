from flask import Flask, render_template


app= Flask( __name__)


@app.route('/', methods=['GET'])
def loadHome():
    x=int(8)
    y=int(8)
    return render_template('index.html', x=x, y=y)


@app.route('/play/<x>/<y>', methods=['GET'])
def loadTimes(x,y):
    x=int(x)
    y=int(y)
    return render_template('index.html', x=x, y=y)

@app.route('/play/<y>', methods=['GET'])
def loadOnce(y):
    x=int(8)
    y=int(y)
    return render_template('index.html', x=x, y=y)

@app.route('/play/<x>/<y>/<color1>/<color2>', methods=['GET'])
def loadColor(x,y,color1,color2):
    x=int(x)
    y=int(y)
    color1=color1
    color2=color2
    return render_template('index.html', x=x,y=y, color1=color1, color2=color2)





if __name__ == "__main__":
    app.run(debug=True)
    