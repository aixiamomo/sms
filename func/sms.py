# coding=utf-8
import json
import requests

# 请求的头部信息
headers = {
    "X-LC-Id": "WyScMsDiSXOP4Efmxvj6EcwU-gzGzoHsz",
    "X-LC-Key": "naf33O8TOwnfQq7rfapWGpOf",
    "Content-Type": "application/json",
}

# 请求发送验证码 API
REQUEST_SMS_CODE_URL = "https://api.leancloud.cn/1.1/requestSmsCode"

# 请求校验验证码 API
VERIFY_SMS_CODE_URL = "https://api.leancloud.cn/1.1/verifySmsCode/"


def send_message(phone):
    """
    通过requests.post 请求 requestSmsCode API 发送验证码到指定手机
    :param phone: 通过网页表单获取的电话号
    :return:
    """
    data = {
        "mobilePhoneNumber": phone,
    }

    # requests.post 方法参数包含三部分: url, data, headers
    r = requests.post(url=REQUEST_SMS_CODE_URL, data=json.dumps(data), headers=headers)

    # 响应 r 的 status_code 值为 200 表示请求成功
    if r.status_code == 200:
        return True
    else:
        return False


def verify(phone, code):
    """
    发送 Post 请求到verifySmsCode API 校验验证码
    :param phone: 通过网页获取的电话号
    :param code: 通过网页表单获取的验证码
    :return:
    """
    # 使用传入的参数拼接完整的URL
    target_url = VERIFY_SMS_CODE_URL + '%s?mobilePhoneNumber=%s' % (code, phone)

    # 这里的 post 只传入两个参数，请求的url和headers
    r = requests.post(url=target_url, headers=headers)
    if r.status_code == 200:
        return True
    else:
        return False
