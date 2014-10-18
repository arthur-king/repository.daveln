# -*- coding: utf-8 -*-

'''
Copyright (C) 2014                                                     

This program is free software: you can redistribute it and/or modify   
it under the terms of the GNU General Public License as published by   
the Free Software Foundation, either version 4 of the License, or      
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

addon=xbmcaddon.Addon('plugin.video.netmusic')
profile=xbmc.translatePath(addon.getAddonInfo('profile'))
mysettings=xbmcaddon.Addon(id='plugin.video.netmusic')
home=mysettings.getAddonInfo('path')
fanart=xbmc.translatePath(os.path.join(home, 'fanart.jpg'))
icon=xbmc.translatePath(os.path.join(home, 'icon.png'))
logos=xbmc.translatePath(os.path.join(home, 'logos\\'))
nhacso='http://nhacso.net/'
csn='http://chiasenhac.com/'

def make_request(url):
  try:
    req=urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response=urllib2.urlopen(req, timeout=90)
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
  addDir('[COLOR yellow]Video Nhạc Số[/COLOR]',nhacso,2,logos+'ns.png')		
  addDir('[COLOR lime]Video Chia Sẻ Nhạc[/COLOR]',csn,2,logos+'csn.png')
  addLink('[COLOR gold]Vmusic[/COLOR]','http://206.190.130.141:1935/liveStream/mtv_1/playlist.m3u8',logos+'vmusic.png')	
  addLink('[COLOR magenta]Viet MTV[/COLOR]','http://64.62.143.5:1935/live/donotstealmy-Stream1/playlist.m3u8?bitrate=800&q=high',logos+'vietmtv.png')		
  #addLink('[COLOR lightgreen]Viet MTV[/COLOR]','rtmpe://64.62.143.5:1935/live/donotstealmy-Stream1 swfUrl=http://www.vietstartv.com/player.swf pageUrl=http://www.vietstartv.com',logos+'vietmtv.png')		
  #addLink('[COLOR lightblue]Viet MTV[/COLOR]','rtmpe://64.62.143.5/live playpath=donotstealmy-Stream1 swfUrl=http://www.vietstartv.com/player.swf pageUrl=http://zui.vn/livetv/viet-mtv-83.html',logos+'vietmtv.png')		
  addLink('[COLOR violet]VPop TV[/COLOR]','http://206.190.130.141:1935/liveStream/vpoptv_1/playlist.m3u8',logos+'vpop.png')
  addLink('[COLOR cyan]Nhạc Của Tui[/COLOR]','rtmp://123.30.134.108:1935/live playpath=nctlive swfUrl=http://hktivi.net/player.swf pageUrl=http://hktivi.net/kenh/nhaccuatui.php',logos+'nct.png')	
  #addLink('[COLOR blue]Nhạc Của Tui[/COLOR]','rtmp://123.30.134.108/live/ playpath=nctlive swfUrl=http://zui.vn/templates/images/jwplayer.swf pageUrl=http://zui.vn/livetv/nhac-cua-tui-40.html',logos+'nct.png')	
  #addLink('[COLOR chocolate]iTV[/COLOR]','rtmp://live.kenhitv.vn/liveweb/ playpath=itv_web_500k.stream swfUrl=http://zui.vn/templates/images/jwplayer.swf pageUrl=http://zui.vn/livetv/itv-10.html',logos+'itv.png')
  addLink('[COLOR silver]iTV[/COLOR]','http://117.103.224.73:1935/live/_definst_/ITV/ITV_live.smil/playlist.m3u8',logos+'itv.png')
  addLink('[COLOR orange]M[COLOR red]TV[/COLOR][/COLOR]','rtmp://85.132.78.6:1935/live/ playpath=muztv.stream swfUrl=http://zui.vn/templates/images/jwplayer.swf pageUrl=http://zui.vn/livetv/mtv-81.html',logos+'mtv.png')

def search():
  if 'Nhạc Số' in name:
    try:
      keyb=xbmc.Keyboard('', '[COLOR yellow]Enter search text[/COLOR]')
      keyb.doModal()
      if (keyb.isConfirmed()):
        searchText=urllib.quote_plus(keyb.getText())
      url=nhacso+'tim-kiem/'+searchText+'.html'
      index(url)
    except: pass
  if 'Chia Sẻ Nhạc' in name:
    try:
      keyb=xbmc.Keyboard('', '[COLOR yellow]Enter search text[/COLOR]')
      keyb.doModal()
      if (keyb.isConfirmed()):
        searchText=urllib.quote_plus(keyb.getText())
      url=csn+'search.php?s='+searchText+'&song_list=""'
      index(url)
    except: pass
  
def categories(url):
  if 'nhacso' in url:
    addDir('[COLOR lime]Nhạc Số[/COLOR][B]   [COLOR lime]>[/COLOR][COLOR magenta]>[/COLOR][COLOR cyan]>[/COLOR][COLOR orange]>[/COLOR]   [/B][COLOR lime]Tìm Nhạc[/COLOR]',nhacso,1,logos+'ns.png')		
    content=make_request(url)	
    match=re.compile("<a href=\"http:\/\/nhacso.net\/the-loai-video(.+?)\" title=\"([^\"]*)\"").findall(content)[0:21]
    for url,name in match:
      if 'Nhạc Cách Mạng' in name: 
        pass
      else:	
	    addDir('[COLOR yellow]'+name+'[/COLOR]',nhacso+'the-loai-video'+url,3,logos+'ns.png')	  
    match=re.compile("<a href=\"http:\/\/nhacso.net\/nghe-si(.+?)\">(.*?)</a>").findall(content)[0:36]
    for url,name in match:
      if 'Lord Wind' in name: 
        pass
      else:		
        addDir('[COLOR cyan]'+name+'[/COLOR]',nhacso+'video-cua-nghe-si'+url.replace('.html','-1-1.html'),3,logos+'ns.png')	  	  
  if 'chiasenhac' in url:
    addDir('[COLOR yellow]Chia Sẻ Nhạc[/COLOR][B]   [COLOR lime]>[/COLOR][COLOR magenta]>[/COLOR][COLOR cyan]>[/COLOR][COLOR orange]>[/COLOR]   [/B][COLOR yellow]Tìm Nhạc[/COLOR]',csn,1,logos+'csn.png')		
    content=make_request(url)
    match=re.compile("<a href=\"hd(.+?)\" title=\"([^\"]*)\"").findall(content)[1:8]
    for url,name in match:
	  addDir('[COLOR lime]'+name+'[/COLOR]',csn+'hd'+url,3,logos+'csn.png')
							
def index(url):
  content=make_request(url)
  if 'chiasenhac' in url:		
    match=re.compile("<a href=\"([^\"]*)\" title=\"(.*?)\"><img src=\"([^\"]+)\"").findall(content)
    for url,name,thumbnail in match:
      add_Link('[COLOR yellow]'+name+'[/COLOR]',(csn+url),thumbnail)
    match=re.compile("<a href=\"(.+?)video\/\" class=\"npage\">1<\/a>").findall(content)[0:1]
    for url in match:
      addDir('[COLOR cyan]Trang Đầu Tiên (Nhạc Video Mới Chia Sẻ + Download Mới Nhất)[/COLOR]',csn+url+'video/',3,thumbnail)
    match=re.compile("<a href=\"hd\/video\/([a-z]-video\/new[0-9]+).html\" class=\"npage\">(\d+)<\/a>").findall(content)
    for url,name in match:
      addDir('[COLOR lime]Trang Mới Chia Sẻ '+name+'[/COLOR]',csn+'hd/video/'+url+'.html',3,logos+'csn.png')
    match=re.compile("<a href=\"hd\/video\/([a-z]-video\/down[0-9]+).html\" class=\"npage\">(\d+)<\/a>").findall(content)
    for url,name in match:
      addDir('[COLOR orange]Trang Download Mới Nhất '+name+'[/COLOR]',csn+'hd/video/'+url+'.html',3,logos+'csn.png')	  	    
  if 'nhacso' in url:		
    if 'the-loai-video' in url:
      match=re.compile("<a href=\"([^\"]*)\" title=\"(.*?)\".+?\s.*?src=\"([^\"]+)\" width").findall(content)
      for url,name,thumbnail in match:
        add_Link('[COLOR yellow]'+name+'[/COLOR]',url,thumbnail)
      match=re.compile("<li ><a href=\"(.+?)\">(\d+)<\/a><\/li>").findall(content)
      for url,name in match:
        addDir('[COLOR lime]Trang '+name+'[/COLOR]',url,3,logos+'ns.png')								
    else:
      match=re.compile("<a class=\"png_img playlist\" href=\"(.+?)\" title=\"([^\"]*)\".+?\s.*?src=\"([^\"]+)\" onerror").findall(content)
      for url,name,thumbnail in match:
        add_Link('[COLOR cyan]'+name+'[/COLOR]',url,thumbnail)
      match=re.compile("<li ><a href=\"(.+?)\">(\d+)<\/a><\/li>").findall(content)
      for url,name in match:
        addDir('[COLOR lime]Trang '+name+'[/COLOR]',url,3,logos+'ns.png')
		
def resolve_url(url):
  content=make_request(url)
  if 'chiasenhac' in url:		
    try:
      mediaUrl=re.compile("\"hd-2\".+?\"([^\"]+)\"").findall(content)[0].replace('%3A',':').replace('%2F','/').replace('%2520','%20')
    except:
      mediaUrl=re.compile("\"file\".*?\"([^\"]*)\"").findall(content)[-1].replace('%3A',':').replace('%2F','/').replace('%2520','%20')
  if 'nhacso' in url:		
    mediaUrl=re.compile("src=\"([^\"]+)\" data-setup").findall(content)[0]		
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
  
def add_Link(name,url,iconimage):
  u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode=4"  
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
  resolve_url(url)		
		
xbmcplugin.endOfDirectory(int(sys.argv[1]))