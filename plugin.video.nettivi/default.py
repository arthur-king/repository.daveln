# -*- coding: utf-8 -*-

'''
Copyright (C) 2014                                                     

This program is free software: you can redistribute it and/or modify   
it under the terms of the GNU General Public License as published by   
the Free Software Foundation, either version 3 of the License, or      
(at your option) any later version.                                    

This program is distributed in the hope that it will be useful,        
but WITHOUT ANY WARRANTY; without even the implied warranty of         
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          
GNU General Public License for more details.                           

You should have received a copy of the GNU General Public License      
along with this program. If not, see <http://www.gnu.org/licenses/  
'''                                                                           

import urllib,urllib2,re,os,sys
import xbmcplugin,xbmcgui,xbmcaddon
	
addon = xbmcaddon.Addon('plugin.video.nettivi')
profile = xbmc.translatePath(addon.getAddonInfo('profile'))
mysettings = xbmcaddon.Addon(id='plugin.video.nettivi')
home = mysettings.getAddonInfo('path')
fanart = xbmc.translatePath(os.path.join(home, 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join(home, 'icon.png'))
logos = xbmc.translatePath(os.path.join(home, 'logos\\'))
tvchannels = 'https://www.dropbox.com/s/kwodh4i7zsovhjl/tvchannels.json?raw=1'
haotivi = 'https://www.dropbox.com/s/e2wycvbvnh2sh49/haotivi.json?raw=1'
vtcplay = 'http://117.103.206.21:88/Channel/GetChannels'
htvonline = 'http://www.htvonline.com.vn/livetv'
fptplay = 'http://fptplay.net/'
tv24vn = 'http://www.tv24.vn'

def HD():
  req = urllib2.Request(htvonline)
  req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
  response = urllib2.urlopen(req, timeout=90)
  link=response.read()
  response.close()
  match=re.compile("<a class=\"mh-grids5-img\" href=\"([^\"]*)\" title=\"(.+?)\">\s.*?\s*<img src=\"(.*?)\"").findall(link)
  for url,name,thumbnail in match:
    if ' HD' in name or 'NATIONAL GEOGRAPHIC' in name:
	  addDir('[COLOR cyan]'+name+'[/COLOR]',url,7,thumbnail)
  req = urllib2.Request(vtcplay)
  req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
  response = urllib2.urlopen(req, timeout=90)
  link=response.read()
  response.close()
  match=re.compile("\"Name\":\"(.*?)\".+?\"Thumbnail2\":\"(.+?)\".+?\"Path\":\"([^\"]*)\"").findall(link)
  for  name,thumbnail,url in match:
    if ' HD' in name:
	  addLink('[COLOR yellow]'+name.decode("utf-8")+'[/COLOR]',url,thumbnail)
	  
def dirs(url):
  req = urllib2.Request(url)
  req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.4) Gecko/2008092417 Firefox/4.0.4')
  response = urllib2.urlopen(req, timeout=90)
  link=response.read()
  response.close()
  match=re.compile("<h3><a href=\"(.+?)\">(.+?)<\/a><\/h3>").findall(link)
  for url,name in match:	
    addDir('[COLOR yellow]'+name+'[/COLOR]',fptplay+url,3,logos+'fptplay.png')
  
def categories():						
  #addDir('[COLOR yellow]Việt Nam[/COLOR]',haotivi,7,logos+'vn.png')
  addDir('[COLOR lime]US[/COLOR]',haotivi,7,logos+'us.png')
  addDir('[COLOR orange]France[/COLOR]',haotivi,7,logos+'fr.png')
  addDir('[COLOR blue]Hong Kong[/COLOR]',haotivi,7,logos+'hk.png')
  addDir('[COLOR magenta]Taiwan[/COLOR]',haotivi,7,logos+'tw.png')
  addDir('[COLOR cyan]China[/COLOR]',haotivi,7,logos+'cn.png')
  addDir('[COLOR silver]Brazil[/COLOR]',haotivi,7,logos+'br.png')
  addDir('[COLOR pink]Spain[/COLOR]',haotivi,7,logos+'sp.png')
  addDir('[COLOR tomato]Japan[/COLOR]',haotivi,7,logos+'ja.png')
  addDir('[COLOR deeppink]Korea[/COLOR]',haotivi,7,logos+'ko.png')
  addDir('[COLOR gold]Thailand[/COLOR]',haotivi,7,logos+'th.png')
  addDir('[COLOR tan]Indonesia[/COLOR]',haotivi,7,logos+'id.png')
  addDir('[COLOR coral]Malaysia[/COLOR]',haotivi,7,logos+'my.png')
	    
def fpt(url):
  req = urllib2.Request(url)
  req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
  response = urllib2.urlopen(req, timeout=90)
  link=response.read()
  response.close()
  match=re.compile("<li ><a href=\"(.+?)\" class=\".+?\">(.+?)<\/a><\/li>").findall(link)
  for url,name in match:
    if 'livetv' in url:
      addDir('[COLOR yellow]'+name+'[/COLOR]',fptplay+url,6,logos+'fptplay.png')
    else:
      addDir('[COLOR lime]'+name+'[/COLOR]',fptplay+url,4,logos+'fptplay.png')			
	  
def index(url):
  req = urllib2.Request(url)
  req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
  response = urllib2.urlopen(req, timeout=90)
  link=response.read()
  response.close()
  if 'tv24' in url:
	match=re.compile("<SPAN id=\".+?\"><a href='(.+?)'><img src='(.+?)' onmouseover=\"this.src='http:\/\/tv24.vn\/WebMedia\/Channels\/\d+\/(.+?).png'").findall(link)
	for url,thumbnail,name in match:
	  if 'vtv' in name:
	    addDir('[COLOR yellow][UPPERCASE]'+name+'[/UPPERCASE][/COLOR]',('%s%s' % (tv24vn, url)),7,thumbnail)	  
	  else:	  
	    addDir('[COLOR lime][UPPERCASE]'+name.replace('b','')+'[/UPPERCASE][/COLOR]',('%s%s' % (tv24vn, url)),7,thumbnail)
  if 'htvonline' in url:
	match=re.compile("<a class=\"mh-grids5-img\" href=\"([^\"]*)\" title=\"(.+?)\">\s.*?\s*<img src=\"(.*?)\"").findall(link)
	for url,name,thumbnail in match:
	  addDir('[COLOR yellow]'+name+'[/COLOR]',url,7,thumbnail)
  if 'fptplay' in url:
	match=re.compile("channel=\"(.*?)\" href=\"(.+?)\" data=\".+?\">\s+<img src=\"(.*?)\"").findall(link)
	for name,url,thumbnail in match:
	  addDir('[COLOR lime]'+name+'[/COLOR]',fptplay+url,8,thumbnail)						
	  
def get_params():
  param=[]
  paramstring=sys.argv[2]
  if len(paramstring)>=2:
    params=sys.argv[2]
    cleanedparams=params.replace('?','')
    if (params[len(params)-1]=='/'):
      params=params[0:len(params)-2]
    pairsofparams=cleanedparams.split('&')
    param={}
    for i in range(len(pairsofparams)):
      splitparams={}
      splitparams=pairsofparams[i].split('=')
      if (len(splitparams))==2:
        param[splitparams[0]]=splitparams[1]
  return param
	  			
def vlinks(url,name):
  req = urllib2.Request(url)
  req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
  response = urllib2.urlopen(req, timeout=90)
  link=response.read()
  response.close()
  if 'htvonline' in url:
    thumbnail=re.compile("<meta property=\"og:image\" content=\"([^\"]*)\"").findall(link)		
    match=re.compile("file: \"([^\"]*)\"").findall(link)
    for url in match:
      addLink(name,url,thumbnail[-1])							
  elif 'tv24' in url:
    match=re.compile('\'file\': \'http([^\']*)').findall(link)
    for url in match:
      addLink(name,('http'+url),logos+'tv24vn.png')										
  elif 'Access Asia Network' in name:
    match=re.compile("\"BroadcastStation\":\"accessasia\",\"Channel\":\"(.*?)\",\"Path\":\"([^\"]*)\",\"Thumbnail\":\"(.+?)\"").findall(link)
    for name,url,thumbnail in match:
      addLink('[COLOR yellow]'+name+'[/COLOR]',url,thumbnail)								
  elif 'TV Hải Ngoại' in name:
    match=re.compile("\"BroadcastStation\":\"haingoaitv\",\"Channel\":\"(.*?)\",\"Path\":\"([^\"]*)\",\"Thumbnail\":\"(.+?)\"").findall(link)
    for name,url,thumbnail in match:
      addLink('[COLOR yellow]'+name+'[/COLOR]',url,thumbnail)										
  elif 'VTCPlay' in name:
    match=re.compile("\"Name\":\"(.*?)\".+?\"Thumbnail2\":\"(.+?)\".+?\"Path\":\"([^\"]*)\"").findall(link)
    for name,thumbnail,url in match:
      addLink('[COLOR yellow]'+name.decode("utf-8")+'[/COLOR]',url,thumbnail)						
  elif 'VTC' in name:
    match=re.compile("\"BroadcastStation\":\"vtccomvn\",\"Channel\":\"(.*?)\",\"Path\":\"([^\"]*)\",\"Thumbnail\":\"(.+?)\"").findall(link)
    for name,url,thumbnail in match:
      addLink('[COLOR yellow]'+name+'[/COLOR]',url,thumbnail)								
  elif 'Việt Nam' in name:
    match=re.compile("\"lang\":\"vi\".*?:\"([^\"]*)\",\"title\":\"(.+?)\"").findall(link)
    for url,name in match:
      addLink('[COLOR yellow]'+name+'[/COLOR]',url,logos+'vn.png')
  elif 'Spain' in name:		
    match=re.compile("\"lang\":\"sp\".*?:\"([^\"]*)\",\"title\":\"(.+?)\"").findall(link)
    for url,name in match:
      addLink('[COLOR pink]'+name+'[/COLOR]',url,logos+'sp.png')
  elif 'France' in name:						
    match=re.compile("\"lang\":\"fr\".*?:\"([^\"]*)\",\"title\":\"(.+?)\"").findall(link)
    for url,name in match:
      addLink('[COLOR orange]'+name+'[/COLOR]',url,logos+'fr.png')
  elif 'Hong Kong' in name:						
    match=re.compile("\"lang\":\"hk\".*?:\"([^\"]*)\",\"title\":\".+?\",\"uid\":\"(.*?)\"").findall(link)
    for url,name in match:
      addLink('[COLOR blue]Hong Kong - [/COLOR][COLOR yellow]channel  '+name+'[/COLOR]',url,logos+'hk.png')
  elif 'Taiwan' in name:			
    match=re.compile("\"lang\":\"tw\".*?:\"([^\"]*)\",\"title\":\".+?\",\"uid\":\"(.*?)\"").findall(link)
    for url,name in match:
      addLink('[COLOR magenta]Taiwan - [/COLOR][COLOR yellow]channel  '+name+'[/COLOR]',url,logos+'tw.png')
  elif 'US' in name:		
    match=re.compile("\"lang\":\"us\".*?:\"([^\"]*)\",\"title\":\"(.+?)\"").findall(link)
    for url,name in match:
      addLink('[COLOR lime]'+name+'[/COLOR]',url,logos+'us.png')
  elif 'China' in name:						
    match=re.compile("\"lang\":\"cn\".*?:\"([^\"]*)\",\"title\":\".+?\",\"uid\":\"(.*?)\"").findall(link)
    for url,name in match:
      addLink('[COLOR cyan]China - [/COLOR][COLOR yellow]channel  '+name+'[/COLOR]',url,logos+'cn.png')
  elif 'Brazil' in name:		
    match=re.compile("\"lang\":\"br\".*?:\"([^\"]*)\",\"title\":\"(.+?)\"").findall(link)
    for url,name in match:
      addLink('[COLOR silver]'+name+'[/COLOR]',url,logos+'br.png')
  elif 'Korea' in name:		
    match=re.compile("\"lang\":\"ko\".*?:\"([^\"]*)\",\"title\":\".+?\",\"uid\":\"(.*?)\"").findall(link)
    for url,name in match:
      addLink('[COLOR deeppink]Korea - [/COLOR][COLOR yellow]channel  '+name+'[/COLOR]',url,logos+'ko.png')
  elif 'Thailand' in name:		
    match=re.compile("\"lang\":\"th\".*?:\"([^\"]*)\",\"title\":\"(.+?)\"").findall(link)
    for url,name in match:
      addLink('[COLOR gold]'+name+'[/COLOR]',url,logos+'th.png')
  elif 'Japan' in name:						
    match=re.compile("\"lang\":\"ja\".*?:\"([^\"]*)\",\"title\":\"(.+?)\"").findall(link)
    for url,name in match:
      addLink('[COLOR tomato]'+name+'[/COLOR]',url,logos+'ja.png')
  elif 'Indonesia' in name:		
    match=re.compile("\"lang\":\"id\".*?:\"([^\"]*)\",\"title\":\"(.+?)\"").findall(link)
    for url,name in match:
      addLink('[COLOR tan]'+name+'[/COLOR]',url,logos+'id.png')
  elif 'Malaysia' in name:						
    match=re.compile("\"lang\":\"my\".*?:\"([^\"]*)\",\"title\":\"(.+?)\"").findall(link)
    for url,name in match:
      addLink('[COLOR coral]'+name+'[/COLOR]',url,logos+'my.png')
	  
def main():
  addDir('[COLOR lime]HD[/COLOR] [COLOR cyan]Channels[/COLOR]','hdchannels',9,logos+'hd.png')
  addDir('[COLOR yellow]TV Hải Ngoại[/COLOR]   ++   [COLOR cyan]Âm Nhạc[/COLOR]   ++   [COLOR lime]Radio[/COLOR]',tvchannels,7,logos+'tivihn.png')
  addDir('[COLOR deeppink]Access Asia Network[/COLOR]',tvchannels,7,logos+'accessasia.png')
  addDir('[COLOR lightblue]FPTPlay[/COLOR]',fptplay,2,logos+'fptplay.png')  
  addDir('[COLOR cyan]haotivi[/COLOR]',haotivi,1,logos+'hao.png')		
  addDir('[COLOR orange]VTCPlay[/COLOR]',vtcplay,7,logos+'vtcplay.png')
  addDir('[COLOR cyan]VTC[/COLOR]',tvchannels,7,logos+'vtccomvn.png')		
  addDir('[COLOR magenta]HTVOnline[/COLOR]',htvonline,6,logos+'htvonline.png')
  addDir('[COLOR lime]TV24VN[/COLOR]    [COLOR lime]>[/COLOR][COLOR magenta]>[/COLOR][COLOR orange]>[/COLOR][COLOR yellow]>[/COLOR]    [COLOR yellow]SCTV[/COLOR]',tv24vn,6,logos+'tv24vn.png')				
  addLink('[COLOR lightgreen]Little Sai Gon TV[/COLOR]','http://stream.s15.cpanelservices.com/lstvlive/livestream/playlist.m3u8',logos+'littlesaigon.png')	
  addLink('[COLOR silver]Animal Planet[/COLOR]','http://202.75.23.34:80/live/ch31//01.m3u8',logos+'ap.png')	
  addLink('[COLOR violet]Discovery Channel[/COLOR]','http://202.75.23.34:80/live/ch29/01.m3u8',logos+'discovery.png')	
  addLink('[COLOR pink]Discovery HD World[/COLOR]','http://202.75.23.34:80/live/ch30/01.m3u8',logos+'dischd.png')	
  addLink('[COLOR olive]Discovery Science[/COLOR]','http://202.75.23.34:80/live/ch33/01.m3u8',logos+'discsc.png')	
  addLink('[COLOR gold]History Channel[/COLOR]','http://202.75.23.36:80/live/ch45/01.m3u8',logos+'history.png')	
  addLink('[COLOR chocolate]NatGeo Wild[/COLOR]','http://202.75.23.35:80/live/ch39/01.m3u8',logos+'natgeowild.png')	
  addLink('[COLOR blue]National Geographic[/COLOR]','http://202.75.23.35:80/live/ch38/01.m3u8',logos+'natgeo.png')	

def addLink(name,url,iconimage):
  ok=True
  liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
  liz.setInfo( type="Video", infoLabels={ "Title": name } )
  ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
  return ok
		
def fptlinks(url,name):
  req = urllib2.Request(url)
  req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.4) Gecko/2008092417 Firefox/4.0.4')
  response = urllib2.urlopen(req, timeout=90)
  link=response.read()
  response.close()
  if 'livetv' in url:
	match=re.compile('var video_str = "<video id=\'main-video\' src=\'" \+ "(.+?)"').findall(link)
	for url in match:
	  addLink(name,url.replace('1000.stream','2500.stream'),logos+'fptplay.png')						
  else:
	match=re.compile('"<source src=\'([^\']*)\'').findall(link)
	for url in match:
	  addLink(name,url,logos+'fptplay.png')
    
def plist(url):	
  req = urllib2.Request(url)
  req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.4) Gecko/2008092417 Firefox/4.0.4')
  response = urllib2.urlopen(req, timeout=90)
  link=response.read()
  response.close()
  match=re.compile("<div class=\"col\">\s*<a href=\"([^\"]+)\">\s*<img src=\"([^\"]*)\" alt=\"(.+?)\"").findall(link)
  for url,thumbnail,name in match:	
    addDir('[COLOR lime]'+name+'[/COLOR]',fptplay+url,5,thumbnail)
  match=re.compile("<li><a href=\"(.+?)\">(\d+)<\/a><\/li>").findall(link)
  for url,name in match:	
    addDir('[COLOR yellow]Trang '+name+'[/COLOR]',fptplay+url,3,logos+'fptplay.png')

def eps(url):
  req = urllib2.Request(url)
  req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.4) Gecko/2008092417 Firefox/4.0.4')
  response = urllib2.urlopen(req, timeout=90)
  link=response.read()
  response.close()
  title=re.compile('<title>([^\']+)</title>').findall(link)		
  match=re.compile("<a href=\"\/Video([^\"]*)\">(.*?)<\/a><\/li>").findall(link)
  for url,name in match:
    addDir(('%s   -   %s' % ('[COLOR lime]Tập '+name+'[/COLOR]','[COLOR yellow]'+title[-1]+'[/COLOR]')),('%s/Video%s' % (fptplay, url)),8,logos+'fptplay.png')

def addDir(name,url,mode,iconimage):
  u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
  ok=True
  liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
  liz.setInfo( type="Video", infoLabels={ "Title": name } )
  ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
  return ok
 	  
params=get_params()
url=None
name=None
mode=None

try:
  url=urllib.unquote_plus(params["url"])
except:
  pass
try:
  name=urllib.unquote_plus(params["name"])
except:
  pass
try:
  mode=int(params["mode"])
except:
  pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
  print ""
  main()

elif mode==1:
  print ""
  categories()
		
elif mode==2:
  print ""+url
  fpt(url)
		
elif mode==3:
  print ""+url
  plist(url)
		
elif mode==4:
  print ""+url
  dirs(url)
		
elif mode==5:
  print ""+url
  eps(url)
		
elif mode==6:
  print ""+url
  index(url)
		
elif mode==7:
  print ""+url
  vlinks(url,name)

elif mode==8:
  print ""+url
  fptlinks(url,name)

elif mode==9:
  print ""
  HD()	
  
xbmcplugin.endOfDirectory(int(sys.argv[1]))