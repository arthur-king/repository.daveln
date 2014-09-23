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
import xbmc,xbmcplugin,xbmcgui,xbmcaddon

addon      = xbmcaddon.Addon('plugin.video.htvonlinevn')
profile    = xbmc.translatePath(addon.getAddonInfo('profile'))
mysettings = xbmcaddon.Addon(id='plugin.video.htvonlinevn')
home       = mysettings.getAddonInfo('path')
fanart     = xbmc.translatePath(os.path.join(home, 'fanart.jpg'))
icon       = xbmc.translatePath(os.path.join(home, 'icon.png'))
logos      = xbmc.translatePath(os.path.join(home, 'logos\\'))
base_url   = 'http://www.htvonline.com.vn/'
pagestr    = map(str, range(1,20))

def home():
        addDir('[COLOR lime]HTVONLINE - [/COLOR][COLOR yellow]TV Channels[/COLOR]',base_url + 'livetv',2,logos + 'logo.png')
        addDir('[COLOR cyan]Phim Việt Nam[/COLOR]',base_url + 'phim-viet-nam',1,logos + 'logo.png')
        addDir('[COLOR magenta]TV Show[/COLOR]',base_url + 'shows',1,logos + 'logo.png')		

def pagelist():
		if 'Phim Việt Nam' in name:
				i=0
				for i in range(6):
						addDir('[COLOR cyan]Phim Việt Nam - [/COLOR][COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'phim-viet-nam/trang-' + pagestr[i],2,icon)
						i+=1
		if 'TV Show' in name:
				i=0
				for i in range(5):
						addDir('[COLOR magenta]TV Show - [/COLOR][COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'shows/trang-' + pagestr[i],2,icon)
						i+=1
		
def index(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req, timeout=90)
        link=response.read()
        response.close()
        if'livetv' in url:
				match=re.compile("<a class=\"mh-grids5-img\" href=\"([^\"]*)\" title=\"(.+?)\">\s.*?\s*<img src=\"(.*?)\"").findall(link)
				for url,name,thumbnail in match:
						addDir('[COLOR yellow]' + name + '[/COLOR]',url,3,thumbnail)
        else:
				match=re.compile("<a class=.*?href=\"([^\"]*)\">\s+<img src=.+?data-original=\"(.*?)\".*?alt=\"hình phim(.+?)\(\)\">").findall(link)
				for url,thumbnail,name in match:
						addDir('[COLOR yellow]' + name + '[/COLOR]',url,3,thumbnail)
				
def videolinks(url,name):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req, timeout=90)
        link=response.read()
        response.close()
        thumbnail=re.compile("<meta property=\"og:image\" content=\"([^\"]*)\"").findall(link)	
        match=re.compile("file: \"([^\"]*)\"").findall(link)
        for url in match:
                addLink(name,url,thumbnail[-1])
                        
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
		
def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok

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
        home()

elif mode==1:
        print ""
        pagelist()		
		
elif mode==2:
        print ""+url
        index(url)
       
elif mode==3:
        print ""+url
        videolinks(url,name)
		
xbmcplugin.endOfDirectory(int(sys.argv[1]))