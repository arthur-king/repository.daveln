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
import xbmc,xbmcplugin,xbmcgui,xbmcaddon
	
addon      = xbmcaddon.Addon('plugin.video.nettivi')
profile    = xbmc.translatePath(addon.getAddonInfo('profile'))
mysettings = xbmcaddon.Addon(id='plugin.video.nettivi')
home       = mysettings.getAddonInfo('path')
fanart     = xbmc.translatePath(os.path.join(home, 'fanart.jpg'))
icon       = xbmc.translatePath(os.path.join(home, 'icon.png'))
logos      = xbmc.translatePath(os.path.join(home, 'logos\\'))
haingoai   = 'http://206.190.130.141:1935/liveStream/'
accessasia = 'http://live.accessasia.tv:1935/vnptg_channels/mp4:'
haotivi    = 'https://www.dropbox.com/s/fzw8dowr6uegqxk/haotivi.json?raw=1'
#haotivi    = 'http://haotivi.com/channels.json'
#vtcplay    = 'https://www.dropbox.com/s/fdv8bctp5fa51r8/vtcplay.json?raw=1'
vtcplay    = 'http://117.103.206.21:88/Channel/GetChannels'
tv24vn     = 'http://www.tv24.vn'
htvonline  = 'http://www.htvonline.com.vn/livetv'
#tokencode  = '1b#K8!3zc65ends!'

def categories():
        addDir('[COLOR yellow]TV Hải Ngoại[/COLOR]   ++   [COLOR cyan]Âm Nhạc[/COLOR]   ++   [COLOR lime]Radio[/COLOR]',haingoai,7,logos + 'tivihn.png')
        addDir('[COLOR deeppink]Access Asia Network[/COLOR]',accessasia,8,logos + 'accessasia.png')
        addDir('[COLOR cyan]Haotivi[/COLOR]',haotivi,2,logos + 'hao.png')		
        addDir('[COLOR orange]VTC Play TV[/COLOR]',vtcplay,9,logos + 'vtcplay.png')
        addDir('[COLOR magenta]HTVOnline TV[/COLOR]',htvonline,3,logos + 'htvonline.png')
        addDir('[COLOR lime]TV24VN[/COLOR]    [COLOR lime]>[/COLOR][COLOR magenta]>[/COLOR][COLOR orange]>[/COLOR][COLOR yellow]>[/COLOR]    [COLOR yellow]SCTV[/COLOR]',tv24vn,1,logos + 'tv24vn.png')		
       #addLink('[COLOR tan]Cartoon network[/COLOR]','rtmp://31.204.128.75/live/brlive_0028',logos + 'cartoon.png')		
        addLink('[COLOR lightgreen]Little Sai Gon TV[/COLOR]','http://stream.s15.cpanelservices.com/lstvlive/livestream/playlist.m3u8',logos + 'littlesaigon.png')	
        addLink('[COLOR silver]Animal Planet[/COLOR]','http://202.75.23.34:80/live/ch31//01.m3u8',logos + 'ap.png')	
        addLink('[COLOR violet]Discovery Channel[/COLOR]','http://202.75.23.34:80/live/ch29/01.m3u8',logos + 'discovery.png')	
        addLink('[COLOR pink]Discovery HD World[/COLOR]','http://202.75.23.34:80/live/ch30/01.m3u8',logos + 'dischd.png')	
        addLink('[COLOR olive]Discovery Science[/COLOR]','http://202.75.23.34:80/live/ch33/01.m3u8',logos + 'discsc.png')	
        addLink('[COLOR gold]History Channel[/COLOR]','http://202.75.23.36:80/live/ch45/01.m3u8',logos + 'history.png')	
       #addLink('[COLOR salmon]NatGeo Adventure[/COLOR]','http://hao-tv-proxy4.appspot.com/fpt.m3u8?t=sopchannel&c=nationalgeographicadventure',logos + 'natgeoadv.png')	
        addLink('[COLOR chocolate]NatGeo Wild[/COLOR]','http://202.75.23.35:80/live/ch39/01.m3u8',logos + 'natgeowild.png')	
        addLink('[COLOR blue]National Geographic[/COLOR]','http://202.75.23.35:80/live/ch38/01.m3u8',logos + 'natgeo.png')	
						
def tv24():						
        addDir('[COLOR lime]SCTV[/COLOR]    [COLOR cyan]>[/COLOR][COLOR magenta]>[/COLOR][COLOR orange]>[/COLOR][COLOR yellow]>[/COLOR]    [COLOR cyan]Sống  [/COLOR][COLOR magenta]Động  [/COLOR][COLOR orange]Từng  [/COLOR][COLOR yellow]Giây[/COLOR]',tv24vn + '/LiveTV/7/sctv1.html',5,logos + 'sctv.png')
        addDir('[COLOR cyan]Truyền Hình Việt Nam[/COLOR]',tv24vn + '/LiveTV/41/vtv1.html',5,logos + 'thvn.png')
        addDir('[COLOR magenta]Truyền Hình Thành Phố[/COLOR]',tv24vn + '/LiveTV/40/htv9.html',5,logos + 'thtp.png')		
        addDir('[COLOR orange]Truyền Hình Địa Phương[/COLOR]',tv24vn + '/LiveTV/44/ha_noi_1.html',5,logos + 'thdp.png')
 		
def hao():						
        #addDir('[COLOR yellow]Việt Nam[/COLOR]',haotivi,9,logos + 'vn.png')
        addDir('[COLOR lime]US[/COLOR]',haotivi,9,logos + 'us.png')
        addDir('[COLOR orange]France[/COLOR]',haotivi,9,logos + 'fr.png')
        addDir('[COLOR blue]Hong Kong[/COLOR]',haotivi,9,logos + 'hk.png')
        addDir('[COLOR magenta]Taiwan[/COLOR]',haotivi,9,logos + 'tw.png')
        addDir('[COLOR cyan]China[/COLOR]',haotivi,9,logos + 'cn.png')
        addDir('[COLOR silver]Brazil[/COLOR]',haotivi,9,logos + 'br.png')
        addDir('[COLOR pink]Spain[/COLOR]',haotivi,9,logos + 'sp.png')
        addDir('[COLOR tomato]Japan[/COLOR]',haotivi,9,logos + 'ja.png')
        addDir('[COLOR deeppink]Korea[/COLOR]',haotivi,9,logos + 'ko.png')
        addDir('[COLOR gold]Thailand[/COLOR]',haotivi,9,logos + 'th.png')
        addDir('[COLOR tan]Indonesia[/COLOR]',haotivi,9,logos + 'id.png')
        addDir('[COLOR coral]Malaysia[/COLOR]',haotivi,9,logos + 'my.png')
			
def htv(url):
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
		response = urllib2.urlopen(req, timeout=90)
		link=response.read()
		response.close()
		match=re.compile("<a class=\"mh-grids5-img\" href=\"([^\"]*)\" title=\"(.+?)\">\s.*?\s*<img src=\"(.*?)\"")
		for url,name,thumbnail in match.findall(link):
				addDir('[COLOR yellow]' + name + '[/COLOR]',url,4,thumbnail)
		
def htvlinks(url,name):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req, timeout=90)
        link=response.read()
        response.close()
        thumbnail=re.compile("<meta property=\"og:image\" content=\"([^\"]*)\"").findall(link)	
        match=re.compile("file: \"([^\"]*)\"")
        for url in match.findall(link):
                addLink(name,url,thumbnail[-1])
				
def tv24index(url):
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
		if 'sctv' in url:
				match=re.compile("<SPAN id=\"ctl16_TabContainer_TabPannel01_SPanChannel1\"><a href='(.*?)'><img src='([^\']*)' onmouseover=\"this.src='http:\/\/tv24.vn\/WebMedia\/Channels\/\d+\/([^']*).png'")
				for url,thumbnail,name in match.findall(link):
						addDir('[COLOR lime][UPPERCASE]' + name.replace('b','') + '[/UPPERCASE][/COLOR]',('%s%s' % (tv24vn, url)),6,thumbnail)					
		elif 'vtv' in url: 		
				match=re.compile("<SPAN id=\"ctl16_TabContainer_TabPannel11_SPanChannel1\"><a href='(.*?)'><img src='(.*?)' onmouseover=\"this.src='http:\/\/tv24.vn\/WebMedia\/Channels\/\d+\/(.+?).png'")
				for url,thumbnail,name in match.findall(link):
						addDir('[COLOR cyan][UPPERCASE]' + name + '[/UPPERCASE][/COLOR]',('%s%s' % (tv24vn, url)),6,thumbnail)					
		elif 'htv' in url:		
				match=re.compile("<SPAN id=\"ctl16_TabContainer_TabPannel21_SPanChannel1\"><a href='([^\']*)'><img src='(.+?)' onmouseover=\"this.src='http:\/\/tv24.vn\/WebMedia\/Channels\/\d+\/([^']+).png'")
				for url,thumbnail,name in match.findall(link):
						addDir('[COLOR magenta][UPPERCASE]' + name + '[/UPPERCASE][/COLOR]',('%s%s' % (tv24vn, url)),6,thumbnail)					
		elif 'ha_noi' in url:		
				match=re.compile("<SPAN id=\"ctl16_TabContainer_TabPannel31_SPanChannel1\"><a href='([^\']*)'><img src='(.*?)' onmouseover=\"this.src='http:\/\/tv24.vn\/WebMedia\/Channels\/\d+\/(.*?).png'")
				for url,thumbnail,name in match.findall(link):
						addDir('[COLOR orange][UPPERCASE]' + name + '[/UPPERCASE][/COLOR]',('%s%s' % (tv24vn, url)),6,thumbnail)					

def tv24links(url,name):
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
		match=re.compile('\'file\': \'http([^\']*)')
		for url in match.findall(link):
				addLink(name,('http' + url),logos + 'tv24vn.png')

def hnlinks(url,name):
        addLink('[COLOR yellow]Little Sai Gon TV[/COLOR]','http://stream.s15.cpanelservices.com/lstvlive/livestream/playlist.m3u8',logos + 'littlesaigon.png')	
        addLink('[COLOR lime]Sai Gon TV[/COLOR]','rtmp://74.63.219.99:1935/sgvp playpath=myStream.sdp swfUrl=http://saigontv.us/includes/flash/saigontv.swf pageUrl=http://www.saigontv.us',logos + 'saigontv.png')	
        addLink('[COLOR orange]VietSun TV[/COLOR]',haingoai + 'viettv24_1/playlist.m3u8',logos + 'vietsuntv.png')	
        addLink('[COLOR magenta]Hài 24/7[/COLOR]',haingoai + 'hai_1/playlist.m3u8',logos + 'hai247.png')		
        addLink('[COLOR silver]Cải Lương[/COLOR]',haingoai + 'cailuong_1/playlist.m3u8',logos + 'cailuong.png')	
        addLink('[COLOR violet]VPop TV[/COLOR]',haingoai + 'vpoptv_1/playlist.m3u8',logos + 'vpop.png')		
        addLink('[COLOR olive]Tuổi Thần Tiên[/COLOR]',haingoai + 'ttt_1/playlist.m3u8',logos + 'ttt.png')	
        addLink('[COLOR gold]Phật Từ Bi[/COLOR]',haingoai + 'ptb_1/playlist.m3u8',logos + 'phat.png')	
        addLink('[COLOR salmon]Dám TV[/COLOR]',haingoai + 'DAMTV_1/playlist.m3u8',logos + 'damtv.png')	
        addLink('[COLOR chocolate]Ngôi Nhà Vui Vẻ[/COLOR]',haingoai + 'BBBG_1/playlist.m3u8',logos + 'nnvv.png')	
        addLink('[COLOR deeppink]Viet News[/COLOR]',haingoai + 'kvla_1/playlist.m3u8',logos + 'kvla.png')	
        addLink('[COLOR tan]Van TV Houston[/COLOR]',haingoai + 'vantv_1/playlist.m3u8',logos + 'vantvhouston.png')	
        addLink('[COLOR yellow]VNA TV[/COLOR]','rtmp://24.43.140.12:1935/live playpath=vnatv573-11 swfUrl=http://fpdownload.adobe.com/strobe/FlashMediaPlayback.swf pageUrl=http://vnatv573.com swfVfy=true live=true timeout=60',logos + 'vnatv.png')	
        addLink('[COLOR lime]Viet TV CA[/COLOR]',haingoai + 'vietvla_1/playlist.m3u8',logos + 'viettv.png')	
        addLink('[COLOR orange]VietTop[/COLOR]',haingoai + 'vietop_1/playlist.m3u8',logos + 'viettop.png')	
        addLink('[COLOR magenta]Viet Global[/COLOR]','http://origin1-edge2.yourstreamlive.com:1935/live/yourstreamlive/out_956_2kr6rvfu/playlist.m3u8',logos + 'gm.png')		
        addLink('[COLOR silver]VBS[/COLOR]','rtmp://74.63.219.99:1935/vbsvp/myStream.sdp swfUrl=http://vbstelevision.com/ext/js/vbstv.swf pageUrl=http://www.vbstelevision.com/',logos + 'vbs.png')	
        addLink('[COLOR violet]VietFace CA[/COLOR]',haingoai + 'vface_1/playlist.m3u8',logos + 'vfca.png')	
        addLink('[COLOR pink]SET TV[/COLOR]',haingoai + 'set_1/playlist.m3u8',logos + 'set.png')	
        addLink('[COLOR olive]IBC[/COLOR]',haingoai + 'ibctv_1/playlist.m3u8',logos + 'ibc.png')	
        addLink('[COLOR gold]Viet Today[/COLOR]','mms://shared.streamwebtown.com/dong_sg',logos + 'viettoday.png')	
        addLink('[COLOR salmon]Viet Christian[/COLOR]','mms://live.vietchristian.com/tv',logos + 'christian.png')	
        addLink('[COLOR chocolate]SGN[/COLOR]','http://live.4ktech.net/hls-live/isgn2/_definst_/liveevent/livestream.m3u8',logos + 'sgn.png')	
        addLink('[COLOR pink]VMusic TV[/COLOR]',haingoai + 'mtv_1/playlist.m3u8',logos + 'vmusic.png')
        addLink('[COLOR white]Viet MTV[/COLOR]','http://64.62.143.5:1935/live/donotstealmy-Stream1/playlist.m3u8?bitrate=800&q=high',logos + 'vietmtv.png')	
        addLink('[COLOR blue]Nhạc Của Tui[/COLOR]','rtmp://123.30.134.108:1935/live playpath=nctlive swfUrl=http://hktivi.net/player.swf pageUrl=http://hktivi.net/kenh/nhaccuatui.php',logos + 'nct.png')	
        addLink('[COLOR silver]iTV[/COLOR]','http://117.103.224.73:1935/live/_definst_/ITV/ITV_live.smil/playlist.m3u8',logos + 'itv.png')
        addLink('[COLOR orange]M[COLOR red]TV[/COLOR][/COLOR]','rtmp://85.132.78.6:1935/live/ playpath=muztv.stream swfUrl=http://zui.vn/templates/images/jwplayer.swf pageUrl=http://zui.vn/livetv/mtv-81.html',logos + 'mtv.png')
        addLink('[COLOR deeppink]Sai Gon Radio Seatlle[/COLOR]','http://206.71.180.246:8888/',logos + 'srbsradio.png')	
        addLink('[COLOR tan]Radio Bolsa[/COLOR]','http://ice7.securenetsystems.net/RBVU?type=.flv&playSessionID=724B6190-D27B-7531-5AD645183B89ED51',logos + 'radiobolsa.png')	

def aalinks(url,name):
        addLink('[COLOR yellow]VTVcab 2[/COLOR]',accessasia + 'vctv2.480p/playlist.m3u8',logos + 'vtvcab2.png')	
        addLink('[COLOR lime]VTVcab 4[/COLOR]',accessasia + 'vctv4.480p/playlist.m3u8',logos + 'vtvcab4.png')	
        addLink('[COLOR orange]Thuần Việt HD[/COLOR]',accessasia + 'thuanviet.480p/playlist.m3u8',logos + 'thuanviethd.png')	
        addLink('[COLOR magenta]VTV 4[/COLOR]',accessasia + 'vtv4.480p/playlist.m3u8',logos + 'vtv4.png')		
        addLink('[COLOR silver]SCTV 7[/COLOR]',accessasia + 'sctv7.480p/playlist.m3u8',logos + 'sctv7.png')	
        addLink('[COLOR violet]Du Lịch Và Cuộc Sống[/COLOR]',accessasia + 'dulichcuocsong.480p/playlist.m3u8',logos + 'dulich.png')	
        addLink('[COLOR pink]SCTV HD[/COLOR]',accessasia + 'sctvhaihd.480p/playlist.m3u8',logos + 'sctvhd.png')	
        addLink('[COLOR olive]FBNC[/COLOR]',accessasia + 'htvcfbnc.480p/playlist.m3u8',logos + 'fnbc.png')	
        addLink('[COLOR gold]O2TV[/COLOR]',accessasia + 'vctv10.480p/playlist.m3u8',logos + 'o2tv.png')	
        addLink('[COLOR salmon]SCTV 14[/COLOR]',accessasia + 'sctv14.480p/playlist.m3u8',logos + 'sctv14.png')	
				
def otherlinks(url,name):
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
		response = urllib2.urlopen(req, timeout=90)
		link=response.read()
		response.close()
		if 'VTC Play TV' in name:
				match=re.compile("\"Name\":\"(.*?)\".+?\"Thumbnail2\":\"(.+?)\".+?\"Path\":\"([^\"]*)\"")
				for name,thumbnail,url in match.findall(link):
						addLink('[COLOR yellow]' + name.decode("utf-8") + '[/COLOR]',url,thumbnail)						
		elif 'Việt Nam' in name:
				match=re.compile("\"lang\":\"vi\".*?:\"([^\"]*)\",\"title\":\"(.+?)\"")
				for url,name in match.findall(link):
						addLink('[COLOR yellow]' + name + '[/COLOR]',url,logos + 'vn.png')
		elif 'Spain' in name:		
				match=re.compile("\"lang\":\"sp\".*?:\"([^\"]*)\",\"title\":\"(.+?)\"")
				for url,name in match.findall(link):
						addLink('[COLOR pink]' + name + '[/COLOR]',url,logos + 'sp.png')
		elif 'France' in name:						
				match=re.compile("\"lang\":\"fr\".*?:\"([^\"]*)\",\"title\":\"(.+?)\"")
				for url,name in match.findall(link):
						addLink('[COLOR orange]' + name + '[/COLOR]',url,logos + 'fr.png')
		elif 'Hong Kong' in name:						
				match=re.compile("\"lang\":\"hk\".*?:\"([^\"]*)\",\"title\":\".+?\",\"uid\":\"(.*?)\"")
				for url,name in match.findall(link):
						addLink('[COLOR blue]Hong Kong - [/COLOR][COLOR yellow]channel  ' + name + '[/COLOR]',url,logos + 'hk.png')
		elif 'Taiwan' in name:			
				match=re.compile("\"lang\":\"tw\".*?:\"([^\"]*)\",\"title\":\".+?\",\"uid\":\"(.*?)\"")
				for url,name in match.findall(link):
						addLink('[COLOR magenta]Taiwan - [/COLOR][COLOR yellow]channel  ' + name + '[/COLOR]',url,logos + 'tw.png')
		elif 'US' in name:		
				match=re.compile("\"lang\":\"us\".*?:\"([^\"]*)\",\"title\":\"(.+?)\"")
				for url,name in match.findall(link):
						addLink('[COLOR lime]' + name + '[/COLOR]',url,logos + 'us.png')
		elif 'China' in name:						
				match=re.compile("\"lang\":\"cn\".*?:\"([^\"]*)\",\"title\":\".+?\",\"uid\":\"(.*?)\"")
				for url,name in match.findall(link):
						addLink('[COLOR cyan]China - [/COLOR][COLOR yellow]channel  ' + name + '[/COLOR]',url,logos + 'cn.png')
		elif 'Brazil' in name:		
				match=re.compile("\"lang\":\"br\".*?:\"([^\"]*)\",\"title\":\"(.+?)\"")
				for url,name in match.findall(link):
						addLink('[COLOR silver]' + name + '[/COLOR]',url,logos + 'br.png')
		elif 'Korea' in name:		
				match=re.compile("\"lang\":\"ko\".*?:\"([^\"]*)\",\"title\":\".+?\",\"uid\":\"(.*?)\"")
				for url,name in match.findall(link):
						addLink('[COLOR deeppink]Korea - [/COLOR][COLOR yellow]channel  ' + name + '[/COLOR]',url,logos + 'ko.png')
		elif 'Thailand' in name:		
				match=re.compile("\"lang\":\"th\".*?:\"([^\"]*)\",\"title\":\"(.+?)\"")
				for url,name in match.findall(link):
						addLink('[COLOR gold]' + name + '[/COLOR]',url,logos + 'th.png')
		elif 'Japan' in name:
				response.close()		
				match=re.compile("\"lang\":\"ja\".*?:\"([^\"]*)\",\"title\":\"(.+?)\"")
				for url,name in match.findall(link):
						addLink('[COLOR tomato]' + name + '[/COLOR]',url,logos + 'ja.png')
		elif 'Indonesia' in name:		
				match=re.compile("\"lang\":\"id\".*?:\"([^\"]*)\",\"title\":\"(.+?)\"")
				for url,name in match.findall(link):
						addLink('[COLOR tan]' + name + '[/COLOR]',url,logos + 'id.png')
		elif 'Malaysia' in name:
				response.close()		
				match=re.compile("\"lang\":\"my\".*?:\"([^\"]*)\",\"title\":\"(.+?)\"")
				for url,name in match.findall(link):
						addLink('[COLOR coral]' + name + '[/COLOR]',url,logos + 'my.png')
		
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
        categories()
		
elif mode==1:
        print ""
        tv24()
		
elif mode==2:
        print ""
        hao()	
		
elif mode==3:
        print ""+url
        htv(url)
		
elif mode==4:
        print ""+url
        htvlinks(url,name)	
		
elif mode==5:
        print ""+url
        tv24index(url)
		
elif mode==6:
        print ""+url
        tv24links(url,name)	
		
elif mode==7:
        print ""+url
        hnlinks(url,name)

elif mode==8:
        print ""+url
        aalinks(url,name)
		
elif mode==9:
        print ""+url
        otherlinks(url,name)
				
xbmcplugin.endOfDirectory(int(sys.argv[1]))