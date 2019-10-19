from . import home
from flask import render_template, redirect, url_for


@home.route("/")
def index():
    return render_template("home/index.html")  # 匹配对应蓝图下的模板


@home.route("/login/")
def login():
    return render_template("home/login.html")


@home.route("/logout/")
def logout():
    return redirect(url_for("home.login"))  # url_for返回蓝图下的函数对应的路由地址

@home.route("/register/")
def register():
    return render_template("home/register.html")

@home.route('/user/')
def user():
    return render_template('home/user.html')

@home.route('/pwd/')
def pwd():
    return render_template('home/pwd.html')


@home.route('/comments/')
def comments():
    return render_template('home/comments.html')


@home.route('/loginlog/')
def login_log():
    return render_template('home/loginlog.html')


@home.route('/moviecol/')
def movie_col():
    return render_template('home/moviecol.html')

