import requests ,os,json
# server酱开关，填0不开启(默认)，填2同时开启cookie失效通知和签到成功通知
sever = 'on'
# 填写server酱sckey,不开启server酱则不用填（自己更改）
sckey = 'SCT112056TrLbOea3lI86gJpm3upucEaow'
# 填入glados账号对应cookie
cookie = ''
referer = 'https://glados.rocks/console/checkin'

def start():  
    url= "https://glados.rocks/api/user/checkin"
    url2= "https://glados.rocks/api/user/status"
    origin = "https://glados.rocks"
    referer = "https://glados.rocks/console/checkin"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    payload={
        'token': 'glados_network'
    }
    
    dict = {}
    dict['fanjiduo_163'] = "_ga=GA1.2.1494940055.1641987501; _gid=GA1.2.87403142.1641987501; koa:sess=eyJ1c2VySWQiOjEyNDkxMywiX2V4cGlyZSI6MTY2NzkwNzU1NTM5MywiX21heEFnZSI6MjU5MjAwMDAwMDB9; koa:sess.sig=uvb7YJ0Y1St0RGygZp9fA6sJGW0; _gat_gtag_UA_104464600_2=1"
    #dict['key2'] = "second_cookie"
    #dict['key3'] = "third_cookie"
    
    for key in dict:
        checkin = requests.post(url,headers={'cookie': dict[key] ,'referer': referer,'origin':origin,'user-agent':useragent,'content-type':'application/json;charset=UTF-8'},data=json.dumps(payload))
        state =  requests.get(url2,headers={'cookie': dict[key] ,'referer': referer,'origin':origin,'user-agent':useragent})
        # print(res)

        if 'message' in checkin.text:
            mess = checkin.json()['message']
            if mess == '\u6ca1\u6709\u6743\u9650':
                requests.get('https://sc.ftqq.com/' + sckey + '.send?text=' + key + '账号cookie过期')
            time = state.json()['data']['leftDays']
            time = time.split('.')[0]
            #print(time)
            messStr = key + ', ' + mess
            notice(time,sckey,sever,messStr)

        
def notice(time,sckey,sever,mess):
    if sever == 'off':
        return
    if sever == 'on':
        requests.get('https://sc.ftqq.com/' + sckey + '.send?text='+mess+'，you have '+time+' days left')
    else:
        requests.get('https://sc.ftqq.com/' + sckey + '.send?text=通知没打开')
        
def main_handler(event, context):
  return start()

if __name__ == '__main__':
    start()
