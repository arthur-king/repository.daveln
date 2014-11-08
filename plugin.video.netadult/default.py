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

import urllib,urllib2,re,os
import xbmcplugin,xbmcgui,xbmcaddon

addon=xbmcaddon.Addon('plugin.video.netadult')
profile=xbmc.translatePath(addon.getAddonInfo('profile'))
mysettings=xbmcaddon.Addon(id='plugin.video.netadult')
home=mysettings.getAddonInfo('path')
fanart=xbmc.translatePath(os.path.join(home, 'fanart.jpg'))
icon=xbmc.translatePath(os.path.join(home, 'icon.png'))
logos=xbmc.translatePath(os.path.join(home, 'logos\\'))
xvietsimpletv='https://raw.githubusercontent.com/giolao/Viet-Simpletv/master/x_playlist.m3u'
vietsextv='rtmpe://64.62.143.5/live/do%20not%20steal%20my-Stream2'
xvideos='http://www.xvideos.com'
youjizz='http://www.youjizz.com'
tube8='http://www.tube8.com/'

def makeRequest(url):
  try:
    req=urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0')
    response=urllib2.urlopen(req, timeout=90)
    link=response.read()
    response.close()  
    return link
  except urllib2.URLError, e:
    print 'We failed to open "%s".' % url
    if hasattr(e, 'code'):
      print 'We failed with error code - %s.' % e.code	
    if hasattr(e, 'reason'):
      print 'We failed to reach a server.'
      print 'Reason: ', e.reason
 
def main():
  addLink('[COLOR orange]Viet [COLOR red][B]Sex TV[/B][/COLOR]',vietsextv,logos+'vietsextv.png')
  addDir('[COLOR yellow]HD [COLOR red][B] Adult Videos[/B][COLOR cyan] - [COLOR lime]Tube8[/COLOR]',tube8+'cat/hd/22/',5,logos+'hdadult.png')  
  addDir('[COLOR lime]VietSimple [COLOR red][B] Adult TV[/B][/COLOR]',xvietsimpletv,3,logos+'vietsimpletv.png')	
  addDir('[COLOR yellow]YouJizz [COLOR red][B] Adult Videos[/B][/COLOR]',youjizz,2,logos+'youjizz.png')	
  addDir('[COLOR cyan]XVideos [COLOR red][B] Adult Videos[/B][/COLOR]',xvideos,2,logos+'xvideos.png')	
  addDir('[COLOR magenta]Tube8 [COLOR red][B] Adult Videos[/B][/COLOR]',tube8,2,logos+'tube8.png')  
  
def search():
  if 'youjizz.com' in name:
    try:
      keyb=xbmc.Keyboard('', '[COLOR yellow]Enter search text[/COLOR]')
      keyb.doModal()
      if (keyb.isConfirmed()):
        searchText=urllib.quote_plus(keyb.getText())
      url='http://www.youjizz.com/srch.php?q='+searchText
      print "Searching URL: "+url	  
      mediaList(url)
    except: pass
  if 'xvideos.com' in name:
    try:
      keyb=xbmc.Keyboard('', '[COLOR yellow]Enter search text[/COLOR]')
      keyb.doModal()
      if (keyb.isConfirmed()):
        searchText=urllib.quote_plus(keyb.getText())
      url=xvideos+'/?k='+searchText
      print "Searching URL: "+url	  
      mediaList(url)
    except: pass	
  if 'tube8.com' in name:
    try:
      keyb=xbmc.Keyboard('', '[COLOR yellow]Enter search text[/COLOR]')
      keyb.doModal()
      if (keyb.isConfirmed()):
        searchText=urllib.quote_plus(keyb.getText())
      url=tube8+'searches.html?q='+searchText
      print "Searching URL: "+url	  
      mediaList(url)
    except: pass	  
  
def categories(url): 
  content=makeRequest(url)
  if 'youjizz' in url:
    addDir('[COLOR yellow]youjizz.com[B]   [COLOR lime]>[COLOR cyan]>[COLOR orange]>[COLOR magenta]>   [/B][COLOR yellow]Movie Search[/COLOR]',youjizz,1,logos+'youjizz.png')
    match=re.compile("<a href=\"(.+?)\" ><span>(.+?)<\/span><\/a>").findall(content)
    for url,name in match:
      addDir('[COLOR cyan]'+name+'[/COLOR]',youjizz+url,3,logos+'youjizz.png')  
    match=re.compile("<a href=\"([^\"]*)\"><span>(.+?)<\/span><\/a>").findall(content)[1:-1]
    for url,name in match:
      addDir('[COLOR cyan]'+name+'[/COLOR]',youjizz+url,3,logos+'youjizz.png')
  if 'xvideos' in url:
    addDir('[COLOR lightgreen]xvideos.com[B]   [COLOR lime]>[COLOR cyan]>[COLOR orange]>[COLOR magenta]>   [/B][COLOR lightgreen]Movie Search[/COLOR]',xvideos,1,logos+'xvideos.png')
    match=re.compile("href=\"([^\"]*)\" title=\"([^\"]+)\"><img src=\"(.+?)\"").findall(content)
    for url,name,thumbnail in match:
      add_Link('[COLOR yellow]'+name+'[/COLOR]',xvideos+url,thumbnail)
    match=re.compile("href=\"([^\"]*)\">1<").findall(content)	
    addDir('[COLOR lime]New Videos[/COLOR]',xvideos+match[-1],3,logos+'xvideos.png')
    match=re.compile("href=\"([^\"]+)\">Best Videos<").findall(content)  
    addDir('[COLOR orange]Best Videos[/COLOR]',xvideos+match[0],3,logos+'xvideos.png')  
    content=makeRequest(xvideos)
    match=re.compile("<li><a href=\"\/c\/(.+?)\">(.+?)<\/a>").findall(content) 
    for url,name in match:
      addDir('[COLOR cyan]'+name+'[/COLOR]',xvideos+'/c/'+url,3,logos+'xvideos.png')  
  if 'tube8' in url:
    addDir('[COLOR lime]tube8.com[B]   [COLOR lime]>[COLOR cyan]>[COLOR orange]>[COLOR magenta]>   [/B][COLOR lime]Movie Search[/COLOR]',tube8,1,logos+'tube8.png')
    match=re.compile('href=\'([^\']*)\'>(.+?)<').findall(content)
    for url,name in match:
      if 'HD' in name:
        addDir('[COLOR yellow]'+name+'[/COLOR]',url,3, logos+'tube8.png')
    match=re.compile('href=\'([^\']*)\'>(.+?)<').findall(content)
    for url,name in match:	  
      if 'HD' in name:
	    pass
      else:  
        addDir('[COLOR cyan]'+name+'[/COLOR]',url,3, logos+'tube8.png')	  

def tube8_HD(url):
  content=makeRequest(url)
  match=re.compile("href=\"(.+?)\" class=\"video-thumb-link\".+?src=\"(.+?)\" alt=\"(.+?)\"").findall(content)
  for url,thumbnail,name in match:
    add_Link('[COLOR yellow]'+name+'[/COLOR]',url,thumbnail)
  match=re.compile("href=\"(.+?)\">(\d+)<").findall(content) 
  for url,name in match:  
   addDir('[COLOR lime]Trang '+name+'[COLOR orange] >>>>[/COLOR]',url,5,logos+'hdadult.png') 
     
def mediaList(url):
  content=makeRequest(url)
  if 'Viet-Simpletv' in url:  
    match=re.compile('#EXTINF.+?,(.+)\s([^"]*)\n').findall(content)
    for name,url in match:
	  addLink('[COLOR lime]'+name.replace('>','y ')+'[/COLOR]',url,logos+'vietsimpletv.png')
  if 'youjizz' in url:	  
    if 'random' in url or 'srch.php' in url:
      match=re.compile("<a class=\"frame\" href='(.+?)'.+?><\/a>\s*<img class.+?data-original=\"(.+?)\"").findall(content)		
      for url,thumbnail in match:
        add_Link('[COLOR yellow]'+url.replace('/videos/','').replace('-',' ').replace('.html','')+'[/COLOR]',youjizz+url,thumbnail)
    else:
      match=re.compile("<a class=\"frame\" href='(.+?)'.+?><\/a>\s*<img class.+?data-original=\"(.+?)\">\s*<\/span>\s*<span id=\"title1\">(.+?)<\/span>\s*<span id=\"title2\">\s*<span class='thumbtime'><span>(.+?)<\/span>").findall(content)		
      for url,thumbnail,name,duration in match:
        add_Link('[COLOR yellow]'+name+' [COLOR lime]('+duration+')[/COLOR]',youjizz+url,thumbnail)
      match=re.compile("<a href=\"(.+?).html\">(\d+)<\/a>").findall(content)
      for url,name in match:	
        addDir('[COLOR orange]Trang '+name+'[COLOR cyan]  >>>>[/COLOR]',youjizz+url +'.html',3,logos+'youjizz.png')
      match=re.compile("<a href='([^>]*)'>(\d+)<\/a>").findall(content)
      for url,name in match:	
        addDir('[COLOR red]Trang '+name+'[COLOR magenta]  >>>>[/COLOR]',youjizz+url,3,logos+'youjizz.png')
  if 'xvideos' in url:
    match=re.compile("href=\"([^\"]*)\" title=\"([^\"]+)\"><img src=\"(.+?)\"").findall(content)
    for url,name,thumbnail in match:
      add_Link('[COLOR yellow]'+name+'[/COLOR]',xvideos+url,thumbnail)
    match=re.compile("class=\"nP\" href=\"(.+?)\">Next<").findall(content)  
    addDir('[COLOR lime]Trang[COLOR orange]  Kế[COLOR cyan]  Tiếp[COLOR red]  >>>>[/COLOR]',xvideos+match[0],3,logos+'xvideos.png')
  if 'tube8' in url:
    match=re.compile("href=\"(.+?)\" class=\"video-thumb-link\".+?src=\"(.+?)\" alt=\"(.+?)\"").findall(content)
    for url,thumbnail,name in match:
      add_Link('[COLOR yellow]'+name+'[/COLOR]',url,thumbnail)
    match=re.compile("href=\"(.+?)\">(\d+)<").findall(content) 
    for url,name in match:  
     addDir('[COLOR lime]Trang '+name+'[COLOR orange] >>>>[/COLOR]',url,3,logos+'tube8.png')
  
def resolveUrl(url):
  content=makeRequest(url)
  if 'youjizz' in url:
    mediaUrl=re.compile("<a href=\"(.+?)\" style=\".+?\" >Download This Video<\/a>").findall(content)[0]
  if 'xvideos' in url:
    mediaUrl=urllib.unquote(re.compile("flv_url=(.+?)&amp").findall(content)[-1]) 
  if 'tube8' in url:
    mediaUrl=re.compile('videoUrlJS	= \'(.+?)\'').findall(content)[0]	
  item=xbmcgui.ListItem(path=mediaUrl)
  xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)	  
  return
  
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

def add_Link(name,url,iconimage):
  u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode=4"  
  liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
  liz.setInfo( type="Video", infoLabels={ "Title": name } )
  liz.setProperty('IsPlayable', 'true')  
  ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)  
  
def addDir(name,url,mode,iconimage):
  u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
  ok=True
  liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
  liz.setInfo( type="Video", infoLabels={ "Title": name } )
  ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
  return ok
    
def addLink(name,url,iconimage):
  ok=True
  liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
  liz.setInfo( type="Video", infoLabels={ "Title": name } )
  ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
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
  main()

elif mode==1:
  search()

elif mode==2:
  categories(url)
  
elif mode==3:
  mediaList(url)
  
elif mode==4:
  resolveUrl(url) 

elif mode==5:
  tube8_HD(url)  
  
xbmcplugin.endOfDirectory(int(sys.argv[1]))