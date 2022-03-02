from flask import Flask, render_template


app = Flask(__name__)   
@app.route('/')         
def level1():
    return render_template("index.html")  

@app.route('/<int:num1>')         
def level2(num1):
    return render_template("index.html", row = num1, col=8, color_a='red', color_b='black')  


@app.route('/<int:num1>/<int:num2>')         
def level3(num1, num2):
    return render_template("index.html", row = num1, col=num2, color_a='red', color_b='black')  


@app.route('/<int:x>/<int:y>/<string:one>')
def row_col_one(x,y,one):
    return render_template("index.html",row=x,col=y,color_one=one,color_two='black')

@app.route('/<int:x>/<int:y>/<string:one>/<string:two>')
def row_col_two(x,y,one,two):
    return render_template("index.html",row=x,col=y,color_a=one,color_b=two)



if __name__=="__main__":     
    app.run(debug=True)   

