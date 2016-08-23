# coding=utf-8
from flask import Flask, request, render_template, redirect, flash, url_for
from func import sms


app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def do_login():
    """
    进行登陆验证
    :return:
    """
    error_msg = None
    if request.method == 'GET':
        # 获取 GET 请求参数
        phone_number = request.args.get('mobile_phone_number')
        if phone_number is not None:
            if sms.send_message(phone_number):
                return render_template('login.html')
            else:
                error_msg = 'Failed to get the verification code!'
    elif request.method == 'POST':
        # 获取 POST 请求的form
        phone_number = request.form['phone']
        code = request.form['code']
        if code == '':
            error_msg = 'Please input the verification code!'
        elif sms.verify(phone_number, code):
            return redirect(url_for('success'))
        else:
            error_msg = 'Your code is wrong, please check again!'
    return render_template('login.html', error_msg=error_msg)


@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)
