import requests


acc = '0d000721'
#单引号里输入你的账号（学号）

pas = '''1145141919810'''
#引号里输入你的密码
#请勿将修改后的文件发给他人，以防信息泄露！

way = ''
#如果你是联通的校园网，请在引号内填unicom
#移动填mobile
#电信填telecom
#如果想用默认的校园网，不用代拨，就不用管


url = 'http://202.117.144.205:8602/snnuportal/login'
turl = 'http://202.117.144.205:8602/snnuportal/logoff'

data = {
    'sourceurl': 'null',
    'account': acc,
    'password': pas,
    'yys': way,
    'issave': ''
}
#表单数据

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding': 'gzip, deflate',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'connection': 'keep-alive',
    #'content-length': '70',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'JSESSIONID=A7660C0C6B6262FED367DA30F448EB0B; issave=true; account=acc; password=pas',
    'host': '202.117.144.205:8602',
    'origin': 'http://202.117.144.205:8602',
    'referer': 'http://202.117.144.205:8602/snnuportal/logoff',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0'
}
#标头

response = requests.post(turl, headers=headers).status_code
#先断开连接
response = requests.post(url, data=data, headers=headers).status_code
#请求连接

