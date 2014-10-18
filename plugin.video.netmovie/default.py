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

addon=xbmcaddon.Addon('plugin.video.netmovie')
profile=xbmc.translatePath(addon.getAddonInfo('profile'))
mysettings=xbmcaddon.Addon(id='plugin.video.netmovie')
home=mysettings.getAddonInfo('path')
fanart=xbmc.translatePath(os.path.join(home, 'fanart.jpg'))
icon=xbmc.translatePath(os.path.join(home, 'icon.png'))
logos=xbmc.translatePath(os.path.join(home, 'logos\\'))
phim3s='http://phim3s.net/'
dchd='http://dangcaphd.com/'
pgt='http://phimgiaitri.vn/'

def make_request(url):
  try:
    req=urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response=urllib2.urlopen(req, timeout=120)
    link=response.read()
    response.close()  
    return link
  except:
    print 'We failed to open "%s".' % url
    if hasattr(e, 'reason'):
      print 'We failed to reach a server.'
      print 'Reason: ', e.reason
    if hasattr(e, 'code'):
      print 'We failed with error code - %s.' % e.code  
 
def main():
  addDir('[COLOR yellow]phim3s.net[/COLOR]',phim3s,2,logos+'phim3s_1.png')
  addDir('[COLOR lime]dangcaphd.com[/COLOR]',dchd,2,logos+'dchd_1.png')
  addDir('[COLOR cyan]phimgiaitri.vn[/COLOR]',pgt,5,logos+'pgt.png')   
	  
def search():
  if 'phim3s' in name:
    try:
      keyb=xbmc.Keyboard('', '[COLOR yellow]Enter search text[/COLOR]')
      keyb.doModal()
      if (keyb.isConfirmed()):
        searchText=urllib.quote_plus(keyb.getText())
      url=phim3s+'search?keyword='+searchText
      index(url)
    except: pass
  if 'dangcaphd' in name:
    try:
      keyb=xbmc.Keyboard('', '[COLOR yellow]Enter search text[/COLOR]')
      keyb.doModal()
      if (keyb.isConfirmed()):
        searchText=urllib.quote_plus(keyb.getText())
      url=dchd+'movie/search.html?key='+searchText+'&search_movie=0'
      index(url)
    except: pass
  if 'Tìm Phim Lẻ' in name:
    try:
      keyb=xbmc.Keyboard('', '[COLOR yellow]Enter search text[/COLOR]')
      keyb.doModal()
      if (keyb.isConfirmed()):
        searchText=urllib.quote_plus(keyb.getText())
      url=pgt+'result.php?type=search&keywords='+searchText
      index(url)
    except: pass

def categories(url):
  content=make_request(url)
  if 'phim3s' in url:
    addDir('[COLOR yellow]phim3s[/COLOR][B]   [COLOR lime]>[/COLOR][COLOR orange]>[/COLOR][COLOR blue]>[/COLOR][COLOR magenta]>[/COLOR]   [/B][COLOR yellow]Tìm Phim[/COLOR]',phim3s,1,logos+'phim3s_1.png')
    match=re.compile("<a href=\"the-loai([^\"]*)\" title=\"([^\"]+)\">.+?<\/a>").findall(content) 
    for url,name in match:
      addDir('[COLOR cyan]'+name+'[/COLOR]',('%sthe-loai%s' % (phim3s, url)),3,logos+'phim3s_2.png')					
    match=re.compile("<a href=\"quoc-gia([^\"]*)\" title=\"([^\"]+)\">.+?<\/a>").findall(content) 
    for url,name in match:
      addDir('[COLOR lime]'+name+'[/COLOR]',('%squoc-gia%s' % (phim3s, url)),3,logos+'phim3s_3.png')					
    match=re.compile("<a href=\"danh-sach([^\"]*)\" title=\"([^\"]+)\">.+?<\/a>").findall(content) 
    for url,name in match:
      addDir('[COLOR lightblue]'+name+'[/COLOR]',('%sdanh-sach%s' % (phim3s, url)),3,logos+'phim3s_4.png')					
  if 'dangcaphd' in url:
    addDir('[COLOR yellow]dangcaphd[/COLOR][B]   [COLOR lime]>[/COLOR][COLOR cyan]>[/COLOR][COLOR orange]>[/COLOR][COLOR lightgreen]>[/COLOR]   [/B][COLOR yellow]Tìm Phim[/COLOR]',dchd+'',1,logos+'dchd_1.png')
    match=re.compile("<a href=\"([^\"]*)\" class='menutop' title='([^']+)'>").findall(content)
    for url,name in match:
      addDir('[COLOR lime]'+name+'[/COLOR]',url,3,logos+'dchd_2.png')  
    match=re.compile("<li><a href=\"http:\/\/dangcaphd.com\/cat(.+?)\" title=\"([^\"]*)\">").findall(content)[0:22]
    for url,name in match:
      addDir('[COLOR cyan]'+name+'[/COLOR]',dchd+'cat'+url,3,logos+'dchd_3.png')
    match=re.compile("<li><a href=\"http:\/\/dangcaphd.com\/country(.+?)\" title=\"([^\"]+)\">").findall(content)[0:12]
    for url,name in match:
      addDir('[COLOR orange]'+name+'[/COLOR]',dchd+'country'+url,3,logos+'dchd_1.png')
    match=re.compile("<a href=\"http:\/\/dangcaphd.com\/movie(.+?)\"><span>(.*?)<\/span><\/a>").findall(content)[0:3]
    for url,name in match:
      addDir('[COLOR lightgreen]'+name+'[/COLOR]',dchd+'movie'+url,3,logos+'dchd_2.png')					
  if 'phimgiaitri' in url:
    addDir('[COLOR lime]phimgiatri[/COLOR][B]   [COLOR lime]>[/COLOR][COLOR orange]>[/COLOR][COLOR blue]>[/COLOR][COLOR magenta]>[/COLOR]   [/B][COLOR lime]Tìm Phim Lẻ[/COLOR]',pgt,1,logos+'pgt.png')
    match=re.compile('<a href=\'result.php\?type=Phim Lẻ(.+?)\'><span>(.+?)<\/span>').findall(content)
    for url,name in match:
      addDir('[COLOR yellow]'+name+'[/COLOR]',pgt+'result.php?type=Phim%20L%E1%BA%BB'+url.replace(' ','%20'),3,logos+'pgt.png')	
   
def index(url):
  content=make_request(url)
  if 'phim3s' in url:
    match=re.compile("<div class=\"inner\"><a href=\"(.*?)\" title=\"([^\"]*)\"><img src=\"(.+?)\"").findall(content)
    for url,name,thumbnail in match:
      addDir('[COLOR yellow]'+name+'[/COLOR]',('%s%sxem-phim' % (phim3s, url)),4,thumbnail)					
    match=re.compile("<span class=\"item\"><a href=\"([^\"]*)\">(\d+)<\/a><\/span>").findall(content)
    for url,name in match:
      addDir('[COLOR lime]Trang '+name+'[/COLOR]',('%s%s' % (phim3s, url)),3,logos+'phim3s_4.png')					
  if 'dangcaphd' in url:
    match=re.compile('<a href="(.+?)" title="(.+?)">\s*<img src="(.+?)"').findall(content)
    for url,name,thumbnail in match:
      add_Link('[COLOR yellow]'+name+'[/COLOR]',(url.replace('movie','watch')),thumbnail) 
    match=re.compile("<a href=\"([^\"]+)\">&lt;&lt;<\/a>").findall(content)
    for url in match:
      addDir('[COLOR cyan]Trang Đầu[/COLOR]',url.replace('amp;',''),3,logos+'dchd_1.png')
    #match=re.compile("<a href=\"([^\"]*)\">&lt;<\/a>").findall(content)
    #for url in match:
      #addDir('[COLOR cyan]Trang Kế Trước[/COLOR]',url.replace('amp;',''),3,logos+'dchd_3.png')	
    match=re.compile("<a href=\"([^>]*)\">(\d+)<\/a>").findall(content)
    for url,name in match:
      addDir('[COLOR lime]Trang '+name+'[/COLOR]',url.replace('amp;',''),3,logos+'dchd_2.png')
    #match=re.compile("<a href=\"(.+?)\">&gt;<\/a>").findall(content)
    #for url in match:
      #addDir('[COLOR blue]Trang Kế Tiếp[/COLOR]',url.replace('amp;',''),3,logos+'dchd_1.png')
    match=re.compile("<a href=\"([^\"]*)\">&gt;&gt;<\/a>").findall(content)
    for url in match:
      addDir('[COLOR red]Trang Cuối[/COLOR]',url.replace('amp;',''),3,logos+'dchd_3.png')
  if 'phimgiaitri' in url:
    match=re.compile('<a style=\'text-decoration:none\' href=\'([^\']*).html\'>\s*<img style=.+?src=(.+?) ><table style.+?:0px\'>(.+?)\s*<\/font>').findall(content)
    for url,thumbnail,name in match:
      add_Link('[COLOR yellow]'+name+'[/COLOR]',pgt+url+'/Tap-1.html',pgt+thumbnail)					
    match=re.compile("<a  href='(.+?)'>(\d+)  <\/a>").findall(content)
    for url,name in match:
      addDir('[COLOR lime]Trang '+name+'[/COLOR]',pgt+url.replace(' ','%20'),3,logos + 'pgt.png')					
 
def videolinks(url,name):
  content=make_request(url)
  thumbnail=re.compile("<meta property=\"og:image\" content=\"([^\"]*)\"").findall(content)[0]		
  match=re.compile("a data-type=\"watch\" data-episode-id.+?href=\"([^\"]*)\" title=\"(.*?)\"").findall(content)
  for url,title in match:
    addLink(('%s   -   %s' % ('[COLOR lime]'+title+'[/COLOR]',name )),('%s%svideo.mp4' % (phim3s, url)),thumbnail)
	
def pgtri_bo():
  #addDir('[COLOR cyan]Phimgiaitri[/COLOR]',pgt,5,logos+'pgt.png')
  content=make_request(url)
  match=re.compile('<li class="has-sub"><a href=\'#\'><span>(.+?)<\/span><\/a>').findall(content)[0]  
  addDir('[COLOR yellow]'+match+'[/COLOR]',pgt,2,logos+'pgt.png')			
  match=re.compile('<li class="has-sub"><a href=\'#\'><span>(.+?)<\/span><\/a>').findall(content)[1]		
  addDir('[COLOR lime]'+match+'[/COLOR]',pgt,6,logos+'pgt.png')	
 
def pgtri_bo_categories(url):
  addDir('[COLOR yellow]phimgiatri[/COLOR][B]   [COLOR lime]>[/COLOR][COLOR orange]>[/COLOR][COLOR blue]>[/COLOR][COLOR magenta]>[/COLOR]   [/B][COLOR yellow]Tìm Phim Bộ[/COLOR]',pgt,9,logos+'pgt.png')
  content=make_request(url) 
  match=re.compile('<a href=\'result.php\?type=Phim Bộ(.+?)\'><span>(.+?)<\/span>').findall(content) 
  for url,name in match:
    addDir('[COLOR lime]'+name+'[/COLOR]',pgt+'result.php?type=Phim%20B%E1%BB%99'+url.replace(' ','%20'),7,logos+'pgt.png')
	
def pgtri_bo_pagelist(url):
  content=make_request(url)
  match=re.compile('href=\'([^\']*).html\'>\s*<img style=.+?src=(.+?) ><div class=\'text\'>\s*<p>.+?<\/p>\s*<\/div>.+?>([^<]*)\s*<\/').findall(content)
  for url,thumbnail,name in match:
    addDir('[COLOR lime]'+name+'[/COLOR]',pgt+url+'/Tap-1.html',8,pgt+thumbnail)				
  match=re.compile("<a  href='(.+?)'>(\d+)  <\/a>").findall(content)
  for url,name in match:
    addDir('[COLOR yellow]Trang '+name+'[/COLOR]',pgt+url.replace(' ','%20'),7,logos+'pgt.png')
	
def pgtri_bo_episodes(url,name):
  content=make_request(url)
  thumbnail=re.compile("<meta property=\"og:image\" content=\"(.+?)\"").findall(content)
  get_link('[COLOR yellow]Tập 1  -  [/COLOR]'+name,url,thumbnail[0])
  match=re.compile("<a href=\"(.+?)\" page=(\d+)>").findall(content)
  for url,title in match:
    get_link('[COLOR yellow]Tập '+title+'  -  '+name+'[/COLOR]',url,thumbnail[0])
	  		  
def inquiry():
  try:
    keyb=xbmc.Keyboard('', '[COLOR lime]Enter search text[/COLOR]')
    keyb.doModal()
    if (keyb.isConfirmed()):
      searchText=urllib.quote_plus(keyb.getText())
    url=pgt+'result.php?type=search&keywords='+searchText
    plist(url)
  except: pass
	  
def resolve_url(url):
  content=make_request(url)
  if 'dangcaphd' in url:
    try:	
	  mediaUrl=re.compile('<a _episode="1" _link="(.+?)_\d_\d+.mp4"').findall(content)[0]+'.mp4'
    except:		
	  mediaUrl=re.compile('<a _episode="1" _link="(.+?)"').findall(content)[0]
  if 'phimgiaitri' in url:	
    mediaUrl='http://phimgiaitri.vn/phimtv/phimle'+re.compile('file: "rtmpe:.+?phimle(.+?)"').findall(content)[0]
  item=xbmcgui.ListItem(path=mediaUrl)
  xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)	  
  return

def url_resolver(url):
  content=make_request(url)
  mediaUrl='http://phimgiaitri.vn:83/phimtv/phimbo'+re.compile('file: "rtmpe:.+?phimbo(.+?)"').findall(content)[0]
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
				  
def addDir(name,url,mode,iconimage):
  u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
  ok=True
  liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
  liz.setInfo( type="Video", infoLabels={ "Title": name } )
  ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
  return ok
   
def get_link(name,url,iconimage):
  u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode=11"  
  liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
  liz.setInfo( type="Video", infoLabels={ "Title": name } )
  liz.setProperty('IsPlayable', 'true')  
  ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz) 
  
def add_Link(name,url,iconimage):
  u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode=10"  
  liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
  liz.setInfo( type="Video", infoLabels={ "Title": name } )
  liz.setProperty('IsPlayable', 'true')  
  ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)  
  
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
  print ""
  main()

elif mode==1:
  search()
		
elif mode==2:
  print ""+url
  categories(url)
				
elif mode==3:
  print ""+url
  index(url)
        
elif mode==4:
  print ""+url
  videolinks(url,name)

elif mode==5:
  print ""
  pgtri_bo()
  
elif mode==6:
  print ""+url
  pgtri_bo_categories(url)
  
elif mode==7:
  print ""+url
  pgtri_bo_pagelist(url)
  
elif mode==8:
  print ""+url
  pgtri_bo_episodes(url,name)
  
elif mode==9:
  inquiry()
 
elif mode==10:
  print ""+url
  resolve_url(url)

elif mode==11:
  print ""+url
  url_resolver(url)  
  
xbmcplugin.endOfDirectory(int(sys.argv[1]))