# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 15:12:11 2020

@author: EL ORCHE
"""
import socks
import socket
import urllib3
import smtplib
import requests
import random
import errno
from socket import error as socket_error    
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart                       

#import base64
#import ssl
URL = "http://ip-api.com/json/"
TIMEOUT = (10)
ptimeout = (2.05,27)
usedproxies = []
email_errors = []

#global loop = True 
    
def send_tracking(proxy,pixel):
    user_agent_list = [
		'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
		'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15',
		'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
		'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
		'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
		'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
		'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
		'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
		'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
		'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000',
		"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6", 
		"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1", 
		"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0", 
		"Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5", 
		"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6", 
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11", 
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20", 
		"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",]
    '''
        Function for check proxy return ERROR
        if proxy is Bad else
        Function return None
    '''
    try:
        session = requests.Session()
        session.headers['User-Agent'] = random.choice(user_agent_list)
        session.max_redirects = 300
        proxy = proxy.split('\n',1)[0]
        session.get(URL, proxies={'http':'socks5://' + proxy}, timeout=ptimeout,allow_redirects=True)
    except requests.exceptions.ConnectionError as e:
        pass
        return e
    except requests.exceptions.ConnectTimeout as e:
        pass
        return e
    except requests.exceptions.HTTPError as e:
        pass
        return e
    except requests.exceptions.Timeout as e:
        pass
        return e
    except urllib3.exceptions.ProxySchemeUnknown as e:
        pass
        return e
    except requests.exceptions.TooManyRedirects as e:
        pass
        return e
def check_proxy(proxy):
    user_agent_list = [
		'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
		'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15',
		'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
		'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
		'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
		'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
		'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
		'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
		'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
		'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000',
		"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)", 
		"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6", 
		"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1", 
		"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0", 
		"Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5", 
		"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6", 
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11", 
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20", 
		"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",]
    '''
        Function for check proxy return ERROR
        if proxy is Bad else
        Function return None
    '''
    try:
        session = requests.Session()
        session.headers['User-Agent'] = random.choice(user_agent_list)
        session.max_redirects = 300
        proxy = proxy.split('\n',1)[0]
        print('Checking ' + proxy)
        #design.t22.setText('Checking ' + str(proxy))
        session.get(URL, proxies={'http':'socks5://' + proxy}, timeout=ptimeout,allow_redirects=True)
        session.close()
    except requests.exceptions.ConnectionError as e:
        pass
        return e
    except requests.exceptions.ConnectTimeout as e:
        pass
        return e
    except requests.exceptions.HTTPError as e:
        pass
        return e
    except requests.exceptions.Timeout as e:
        pass
        return e
    except urllib3.exceptions.ProxySchemeUnknown as e:
        pass
        return e
    except requests.exceptions.TooManyRedirects as e:
        pass
        return e  
    
def verifyproxy():
    global sock
    f = open('./data/socks5_proxies.txt')
    try:
        for proxy in f:
            proxy = proxy.strip()
            if proxy in usedproxies:
                pass
            else:
                try:
                    if check_proxy(proxy):
                        pass
                    else:
                        sock = proxy 
                        break
                except KeyboardInterrupt:
                     exit
    except FileNotFoundError:
        print('Error!\nFile Not found!')
    except IndexError:
        print('Error!\nMissing filename!')
        
    return sock

def create_connection(address, timeout=None, source_address=None):
    sock = socks.socksocket()
    sock.connect(address)
    return sock

def email_content():
    quotelist = []
    quotefile = open('./data/email_body.txt','r')
    
    for line in quotefile:
        quote = line.strip()
        quotelist.append(quote)
    
    todayquote = random.choice(quotelist)
    return  todayquote


def subject_line():
    quotelist = []
    quotefile = open('./data/subject_line.txt','r')
    
    for line in quotefile:
        quote = line.strip()
        quotelist.append(quote)
    
    subjectline = random.choice(quotelist)
    return  subjectline




def sendmail(userhot,passhot,target):
    
    global server
    global resultat
    useremail = str(userhot.strip())
    userpassword = str(passhot.strip())
    sendto = str(target.strip())
    fileLog = "Email: "+userhot+"\n"
    
    while True:
        try:
            #verify proxy life
            proxy = verifyproxy()
            print("Valid Proxy: ",proxy)
            i,p = proxy.split(":")
            ip = str(i)
            port = int(p)
            socks.setdefaultproxy(socks.SOCKS5, ip, port)
            socket.socket = socks.socksocket
            socks.socket.setdefaulttimeout(20)
            socket.create_connection = create_connection
            socks.wrapmodule(smtplib)
            print("Proxy connection Created")
    
            print('start sending...')
            smtpserver = 'your smtp server'
            AUTHREQUIRED = 1 
   
            message = MIMEMultipart("alternative")
            message["Subject"] = subject_line()
            message["From"] = useremail
            message["To"] = sendto
            text = email_content()
            
            part1 = MIMEText(text, "plain")
            message.attach(part1)
      
            with smtplib.SMTP_SSL(smtpserver, 465,timeout=120) as server:
                #server.ehlo()
                #server.starttls()
                server.ehlo()
                server.login(useremail, userpassword)
                server.sendmail(useremail, sendto, message.as_string())
                
            
            print("sending output : success")
            usedproxies.append(proxy)
            server.close()
            
            return resultat
            break
        except socks.ProxyConnectionError as e:
            print("proxy connection error",e)
            continue    
        except socket.timeout:
            print("connection timeout")
            continue
        except socket_error as serr:
            if serr.errno != errno.ECONNREFUSED:
                print("connection refused",serr)    
            continue
        except Exception as e:
            if 'Invalid credentials' in str(e):
                fileLog += "It seems that password was incorrect."
                print("It seems that password was incorrect.")
                break
            else:
                print("Acces Denied",e )
                continue  
        except:
            print("Connexion Failed...")
            continue
    
    with open('File Execution.txt', 'w') as f:
        f.write(fileLog)

        


    
def main():
    sendmail("email","password","send to...")
    
    
if __name__ == "__main__":
    main()
