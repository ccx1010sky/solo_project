from flask import Flask, render_template

#  注册
from controllers.products_controller import products_blueprint
from controllers.manufs_controller import manufs_blueprint

app = Flask(__name__)

# 注册
app.register_blueprint(products_blueprint)
app.register_blueprint(manufs_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)