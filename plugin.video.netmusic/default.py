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
import xbmc,xbmcplugin,xbmcgui,xbmcaddon

addon      = xbmcaddon.Addon('plugin.video.netmusic')
profile    = xbmc.translatePath(addon.getAddonInfo('profile'))
mysettings = xbmcaddon.Addon(id='plugin.video.netmusic')
home       = mysettings.getAddonInfo('path')
fanart     = xbmc.translatePath(os.path.join(home, 'fanart.jpg'))
icon       = xbmc.translatePath(os.path.join(home, 'icon.png'))
logos      = xbmc.translatePath(os.path.join(home, 'logos\\'))
nhacso     = 'http://nhacso.net/'
csn        = 'http://chiasenhac.com/'
pagestr    = map(str, range(1,50))

def categories():
        addDir('[COLOR yellow]Nhạc Số[/COLOR]',nhacso,2,logos + 'ns.png')		
        addDir('[COLOR lime]Chia Sẻ Nhạc[/COLOR]',csn,2,logos + 'csn.png')
        addLink('[COLOR gold]Vmusic[/COLOR]','http://206.190.130.141:1935/liveStream/mtv_1/playlist.m3u8',logos + 'vmusic.png')	
        addLink('[COLOR magenta]Viet MTV[/COLOR]','http://64.62.143.5:1935/live/donotstealmy-Stream1/playlist.m3u8?bitrate=800&q=high',logos + 'vietmtv.png')		
        #addLink('[COLOR lightgreen]Viet MTV[/COLOR]','rtmpe://64.62.143.5:1935/live/donotstealmy-Stream1 swfUrl=http://www.vietstartv.com/player.swf pageUrl=http://www.vietstartv.com',logos + 'vietmtv.png')		
        #addLink('[COLOR lightblue]Viet MTV[/COLOR]','rtmpe://64.62.143.5/live playpath=donotstealmy-Stream1 swfUrl=http://www.vietstartv.com/player.swf pageUrl=http://zui.vn/livetv/viet-mtv-83.html',logos + 'vietmtv.png')		
        addLink('[COLOR cyan]Nhạc Của Tui[/COLOR]','rtmp://123.30.134.108:1935/live playpath=nctlive swfUrl=http://hktivi.net/player.swf pageUrl=http://hktivi.net/kenh/nhaccuatui.php',logos + 'nct.png')	
        #addLink('[COLOR blue]Nhạc Của Tui[/COLOR]','rtmp://123.30.134.108/live/ playpath=nctlive swfUrl=http://zui.vn/templates/images/jwplayer.swf pageUrl=http://zui.vn/livetv/nhac-cua-tui-40.html',logos + 'nct.png')	
        #addLink('[COLOR chocolate]iTV[/COLOR]','rtmp://live.kenhitv.vn/liveweb/ playpath=itv_web_500k.stream swfUrl=http://zui.vn/templates/images/jwplayer.swf pageUrl=http://zui.vn/livetv/itv-10.html',logos + 'itv.png')
        addLink('[COLOR silver]iTV[/COLOR]','http://117.103.224.73:1935/live/_definst_/ITV/ITV_live.smil/playlist.m3u8',logos + 'itv.png')
        addLink('[COLOR orange]M[COLOR red]TV[/COLOR][/COLOR]','rtmp://85.132.78.6:1935/live/ playpath=muztv.stream swfUrl=http://zui.vn/templates/images/jwplayer.swf pageUrl=http://zui.vn/livetv/mtv-81.html',logos + 'mtv.png')
		
def search():
		if 'Nhạc Số' in name:
				try:
						keyb = xbmc.Keyboard('', '[COLOR yellow]Enter search text[/COLOR]')
						keyb.doModal()
						if (keyb.isConfirmed()):
								searchText = urllib.quote_plus(keyb.getText())
						url = nhacso + 'tim-kiem/'+searchText+'.html'
						index(url)
				except: pass
		if 'Chia Sẻ Nhạc' in name:
				try:
						keyb = xbmc.Keyboard('', '[COLOR yellow]Enter search text[/COLOR]')
						keyb.doModal()
						if (keyb.isConfirmed()):
								searchText = urllib.quote_plus(keyb.getText())
						url = csn + 'search.php?s='+searchText+'&song_list=""'
						index(url)
				except: pass

def main():
		if 'Nhạc Số' in name:
				addDir('[COLOR yellow]Nhạc Số[/COLOR][B]   [COLOR lime]>[/COLOR][COLOR magenta]>[/COLOR][COLOR cyan]>[/COLOR][COLOR orange]>[/COLOR]   [/B][COLOR lime]Tìm Nhạc[/COLOR]',nhacso,1,logos + 'ns.png')		
				addDir('[COLOR orange]Video Clips - Thể Loại[/COLOR]',nhacso,3,logos + 'ns.png')
				addDir('[COLOR magenta]Video Clips - Nghệ Sĩ Việt Nam[/COLOR]',nhacso,3,logos + 'ns.png')
				addDir('[COLOR cyan]Video Clips - Nghệ Sĩ Quốc Tế[/COLOR]',nhacso,3,logos + 'ns.png')
		if 'Chia Sẻ Nhạc' in name:
				addDir('[COLOR lime]Chia Sẻ Nhạc[/COLOR][B]   [COLOR lime]>[/COLOR][COLOR magenta]>[/COLOR][COLOR cyan]>[/COLOR][COLOR orange]>[/COLOR]   [/B][COLOR yellow]Tìm Nhạc[/COLOR]',csn,1,logos + 'csn.png')		
				addDir('[COLOR orange]Video Clips[/COLOR]',csn,3,logos + 'csn.png')

def sub():
		if 'Thể Loại' in name:
				addDir('[COLOR lime]Nhạc Trẻ[/COLOR]',nhacso + 'the-loai-video/nhac-tre-1/trang-1.html',5,logos + 'ns.png')
				addDir('[COLOR orange]Nhạc Trữ Tình[/COLOR]',nhacso + 'the-loai-video/nhac-tru-tinh-2/trang-1.html',5,logos + 'ns.png')
				addDir('[COLOR blue]Nhạc Quê Hương[/COLOR]',nhacso + 'the-loai-video/nhac-que-huong-11/trang-1.html',5,logos + 'ns.png')
				addDir('[COLOR magenta]Nhạc dân Tộc[/COLOR]',nhacso + 'the-loai-video/nhac-dan-toc-6/trang-1.html',5,logos + 'ns.png')
				addDir('[COLOR cyan]Nhạc Trịnh[/COLOR]',nhacso + 'the-loai-video/nhac-trinh-4/trang-1.html',5,logos + 'ns.png')
				addDir('[COLOR brown]Nhạc Tiền Chiến[/COLOR]',nhacso + 'the-loai-video/nhac-tien-chien-5/trang-1.html',5,logos + 'ns.png')
				addDir('[COLOR coral]Nhạc Thiếu Nhi[/COLOR]',nhacso + 'the-loai-video/nhac-thieu-nhi-7/trang-1.html',5,logos + 'ns.png')
				addDir('[COLOR gold]Rock Việt[/COLOR]',nhacso + 'the-loai-video/rock-viet-9/trang-1.html',5,logos + 'ns.png')
				addDir('[COLOR chocolate]Rap Việt - HipHop[/COLOR]',nhacso + 'the-loai-video/rap-viet-hiphop-14/trang-1.html',5,logos + 'ns.png')
				addDir('[COLOR green]Nhạc Âu Mỹ[/COLOR]',nhacso + 'the-loai-video/nhac-au-my-21/trang-1.html',5,logos + 'ns.png')
				addDir('[COLOR tomato]Nhạc Hàn[/COLOR]',nhacso + 'the-loai-video/nhac-han-16/trang-1.html',5,logos + 'ns.png')
				addDir('[COLOR deeppink]Nhạc Hoa[/COLOR]',nhacso + 'the-loai-video/nhac-hoa-15/trang-1.html',5,logos + 'ns.png')
				addDir('[COLOR maroon]Nhạc Nhật[/COLOR]',nhacso + 'the-loai-video/nhac-nhat-32/trang-1.html',5,logos + 'ns.png')
				addDir('[COLOR olive]Nhạc Pháp[/COLOR]',nhacso + 'the-loai-video/nhac-phap-17/trang-1.html',5,logos + 'ns.png')
				addDir('[COLOR pink]Nhạc Các Nước Khác[/COLOR]',nhacso + 'the-loai-video/nhac-cac-nuoc-khac-18/trang-1.html',5,logos + 'ns.png')
				addDir('[COLOR red]Nhân Tố Bí Ẩn[/COLOR]',nhacso + 'the-loai-video/nhan-to-bi-an-82/trang-1.html',5,logos + 'ns.png')
				addDir('[COLOR tan]Truyền Hình HomeTV[/COLOR]',nhacso + 'the-loai-video/truyen-hinh-hometv-81/trang-1.html',5,logos + 'ns.png')
				addDir('[COLOR violet]Giọng Hát Việt Nhí[/COLOR]',nhacso + 'the-loai-video/giong-hat-viet-nhi-68/trang-1.html',5,logos + 'ns.png')
				addDir('[COLOR silver]Fanmade / Radio[/COLOR]',nhacso + 'the-loai-video/fanmade-radio-66/trang-1.html',5,logos + 'ns.png')
				addDir('[COLOR salmon]Shining Show[/COLOR]',nhacso + 'the-loai-video/shining-show-63/trang-1.html',5,logos + 'ns.png')
		if 'Nghệ Sĩ Việt Nam' in name:
				addDir('[COLOR lime]Cẩm Ly[/COLOR]',nhacso + 'video-cua-nghe-si/cam-ly-17-1-1.html',5,logos + 'ns.png')
				addDir('[COLOR orange]Dương Ngọc Thái[/COLOR]',nhacso + 'video-cua-nghe-si/duong-ngoc-thai-789-1-1.html',5,logos + 'ns.png')
				addDir('[COLOR blue]Đàm Vĩnh Hưng[/COLOR]',nhacso + 'video-cua-nghe-si/dam-vinh-hung-47-1-1.html',5,logos + 'ns.png')
				addDir('[COLOR magenta]Đan Trường[/COLOR]',nhacso + 'video-cua-nghe-si/dan-truong-55-1-1.html',5,logos + 'ns.png')
				addDir('[COLOR cyan]Hồ Ngọc Hà[/COLOR]',nhacso + 'video-cua-nghe-si/ho-ngoc-ha-33-1-1.html',5,logos + 'ns.png')
				addDir('[COLOR brown]Khắc Việt[/COLOR]',nhacso + 'video-cua-nghe-si/khac-viet-4481-1-1.html',5,logos + 'ns.png')
				addDir('[COLOR coral]Lam Trường[/COLOR]',nhacso + 'video-cua-nghe-si/lam-truong-4-1-1.html',5,logos + 'ns.png')
				addDir('[COLOR gold]Lệ Quyên[/COLOR]',nhacso + 'video-cua-nghe-si/le-quyen-3-1-1.html',5,logos + 'ns.png')
				addDir('[COLOR green]Ngô Kiến Huy[/COLOR]',nhacso + 'video-cua-nghe-si/ngo-kien-huy-2228-1-1.html',5,logos + 'ns.png')
				addDir('[COLOR tomato]Noo Phước Thịnh[/COLOR]',nhacso + 'video-cua-nghe-si/noo-phuoc-thinh-2430-1-1.html',5,logos + 'ns.png')
				addDir('[COLOR deeppink]Phương Thanh[/COLOR]',nhacso + 'video-cua-nghe-si/phuong-thanh-110-1-1.html',5,logos + 'ns.png')
				addDir('[COLOR maroon]Quang Dũng[/COLOR]',nhacso + 'video-cua-nghe-si/quang-dung-79-1-1.html',5,logos + 'ns.png')
				addDir('[COLOR olive]The Men[/COLOR]',nhacso + 'video-cua-nghe-si/the-men-2407-1-1.html',5,logos + 'ns.png')
				addDir('[COLOR pink]Thuỷ Tiên[/COLOR]',nhacso + 'video-cua-nghe-si/thuy-tien-2429-1-1.html',5,logos + 'ns.png')
				addDir('[COLOR red]Uyên Linh[/COLOR]',nhacso + 'video-cua-nghe-si/uyen-linh-4525-1-1.html',5,logos + 'ns.png')
				addDir('[COLOR tan]Văn Mai Hương[/COLOR]',nhacso + 'video-cua-nghe-si/van-mai-huong-3159-1-1.html',5,logos + 'ns.png')
				addDir('[COLOR violet]Vmusic[/COLOR]',nhacso + 'video-cua-nghe-si/vmusic-4540-1-1.html',5,logos + 'ns.png')
		if 'Nghệ Sĩ Quốc Tế' in name:
				addDir('[COLOR lime]2NE1[/COLOR]',nhacso + 'video-cua-nghe-si/2ne1-3760-1-1.html',5,logos + 'ns.png')
				addDir('[COLOR orange]2PM[/COLOR]',nhacso + 'video-cua-nghe-si/2pm-3762-1-1.html',5,logos + 'ns.png')
				addDir('[COLOR blue]Adele[/COLOR]',nhacso + 'video-cua-nghe-si/adele-5903-1-1.html',5,logos + 'ns.png')
				addDir('[COLOR magenta]Avril Lavigne[/COLOR]',nhacso + 'video-cua-nghe-si/avril-lavigne-2496-1-1.html',5,logos + 'ns.png')
				addDir('[COLOR brown]Beyonce[/COLOR]',nhacso + 'video-cua-nghe-si/beyonce-2530-1-1.html',5,logos + 'ns.png')
				addDir('[COLOR coral]Big Bang[/COLOR]',nhacso + 'video-cua-nghe-si/big-bang-2536-1-1.html',5,logos + 'ns.png')
				addDir('[COLOR gold]Britney Spears[/COLOR]',nhacso + 'video-cua-nghe-si/britney-spears-2568-1-1.html',5,logos + 'ns.png')
				addDir('[COLOR chocolate]Girls Generation[/COLOR]',nhacso + 'video-cua-nghe-si/snsd-girls-generation-2802-1-1.html',5,logos + 'ns.png')
				addDir('[COLOR green]Jay Chou - Châu[/COLOR]',nhacso + 'video-cua-nghe-si/jay-chou-chau-kiet-luan-2926-1-1.html',5,logos + 'ns.png')
				addDir('[COLOR tomato]Justin Bieber[/COLOR]',nhacso + 'video-cua-nghe-si/justin-bieber-2976-1-1.html',5,logos + 'ns.png')
				addDir('[COLOR deeppink]Kelly Clarkson[/COLOR]',nhacso + 'video-cua-nghe-si/kelly-clarkson-3011-1-1.html',5,logos + 'ns.png')
				addDir('[COLOR maroon]Lady Gaga[/COLOR]',nhacso + 'video-cua-nghe-si/lady-gaga-3074-1-1.html',5,logos + 'ns.png')
				addDir('[COLOR pink]Rihanna[/COLOR]',nhacso + 'video-cua-nghe-si/rihanna-3375-1-1.html',5,logos + 'ns.png')
				addDir('[COLOR red]S.H.E[/COLOR]',nhacso + 'video-cua-nghe-si/s-h-e-3405-1-1.html',5,logos + 'ns.png')
				addDir('[COLOR tan]Super Junior[/COLOR]',nhacso + 'video-cua-nghe-si/super-junior-3514-1-1.html',5,logos + 'ns.png')
				addDir('[COLOR violet]TVXQ (DBDK)[/COLOR]',nhacso + 'video-cua-nghe-si/dbsk-tvxq-5218-1-1.html',5,logos + 'ns.png')
		if 'chiasenhac' in url:
				addDir('[COLOR lime]Video Việt Nam[/COLOR]',csn + 'hd/video/v-video',4,logos + 'csn.png')
				addDir('[COLOR orange]Video Âu, Mỹ[/COLOR]',csn + 'hd/video/u-video',4,logos + 'csn.png')
				addDir('[COLOR blue]Video Hoa[/COLOR]',csn + 'hd/video/c-video',4,logos + 'csn.png')
				addDir('[COLOR magenta]Video Hàn[/COLOR]',csn + 'hd/video/k-video',4,logos + 'csn.png')
				addDir('[COLOR cyan]Video Các Nước Khác[/COLOR]',csn + 'hd/video/o-video',4,logos + 'csn.png')
				addDir('[COLOR gold]Video Live[/COLOR]',csn + 'hd/video/l-video',4,logos + 'csn.png')
				addDir('[COLOR tomato]Video Hài[/COLOR]',csn + 'hd/video/h-video',4,logos + 'csn.png')
				
def pagelist():
		if 'v-video' in url:
				i=0
				for i in range(22):
						addDir('[COLOR lime]Video Việt Nam[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',csn + 'hd/video/v-video/new' + pagestr[i] + '.html',5,logos + 'csn.png')
						i+=1		
		if 'u-video' in url:
				i=0
				for i in range(22):		
						addDir('[COLOR orange]Video Âu, Mỹ[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',csn + 'hd/video/u-video/new' + pagestr[i] + '.html',5,logos + 'csn.png')
						i+=1 		
		if 'c-video' in url:
				i=0
				for i in range(22):
						addDir('[COLOR blue]Video Hoa[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',csn + 'hd/video/c-video/new' + pagestr[i] + '.html',5,logos + 'csn.png')
						i+=1		
		if 'k-video' in url:
				i=0
				for i in range(22):
						addDir('[COLOR magenta]Video[/COLOR] - [COLOR yellow]Hàn Trang ' + pagestr[i] + '[/COLOR]',csn + 'hd/video/k-video/new' + pagestr[i] + '.html',5,logos + 'csn.png')
						i+=1			
		if 'o-video' in url:
				i=0
				for i in range(22):
						addDir('[COLOR cyan]Video Các Nước Khác[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',csn + 'hd/video/o-video/new' + pagestr[i] + '.html',5,logos + 'csn.png')
						i+=1		
		if 'l-video' in url: 	
				i=0
				for i in range(22):		
						addDir('[COLOR gold]Video Live[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',csn + 'hd/video/l-video/new' + pagestr[i] + '.html',5,logos + 'csn.png')
						i+=1 		
		if 'h-video' in url:
				i=0
				for i in range(7):
						addDir('[COLOR tomato]Video Hài[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',csn + 'hd/video/h-video/new' + pagestr[i] + '.html',5,logos + 'csn.png')
						i+=1
							
def index(url):
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.4) Gecko/2008092417 Firefox/4.0.4')
		response = urllib2.urlopen(req, timeout=90)
		link=response.read()
		response.close()
		if 'chiasenhac' in url:		
				match=re.compile("<a href=\"([^\"]*)\" title=\"(.*?)\"><img src=\"([^\"]+)\"").findall(link)
				for url,name,thumbnail in match:
						addDir('[COLOR lime]' + name + '[/COLOR]',(csn + url),6,thumbnail)							
		if 'nhacso' in url:		
				if 'the-loai-video' in url:
						match=re.compile("<a href=\"([^\"]*)\" title=\"(.*?)\".+?\s.*?src=\"([^\"]+)\" width").findall(link)
						for url,name,thumbnail in match:
								addDir('[COLOR yellow]' + name + '[/COLOR]',url,6,thumbnail)
						match=re.compile("<li ><a href=\"(.+?)\">(\d+)<\/a><\/li>").findall(link)
						for url,name in match:
								addDir('[COLOR lime]Trang ' + name + '[/COLOR]',url,5,logos + 'ns.png')								
				else:
						match=re.compile("<a class=\"png_img playlist\" href=\"(.+?)\" title=\"([^\"]*)\".+?\s.*?src=\"([^\"]+)\" onerror").findall(link)
						for url,name,thumbnail in match:
								addDir('[COLOR cyan]' + name + '[/COLOR]',url,6,thumbnail)
						match=re.compile("<li ><a href=\"(.+?)\">(\d+)<\/a><\/li>").findall(link)
						for url,name in match:
								addDir('[COLOR lime]Trang ' + name + '[/COLOR]',url,5,logos + 'ns.png')								
 				
def vlinks(url,name):
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.4) Gecko/2008092417 Firefox/4.0.4')
		response = urllib2.urlopen(req, timeout=90)
		link=response.read()
		response.close()
		if 'chiasenhac' in url:		
				try:
						thumbnail=re.compile("<link rel=\"image_src\" href=\"([^\"]+)\"").findall(link)
						match=re.compile("\"hd-2\".+?\"([^\"]+)\"").findall(link)
						addLink(name,(match[0].replace('%3A',':').replace('%2F','/').replace('%2520',' ')),thumbnail[0])
				except:
						thumbnail=re.compile("<link rel=\"image_src\" href=\"([^\"]*)\"").findall(link)
						match=re.compile("\"file\".*?\"([^\"]*)\"").findall(link)
						addLink(name,(match[1].replace('%3A',':').replace('%2F','/').replace('%2520',' ')),thumbnail[-1])
		if 'nhacso' in url:	
				thumbnail=re.compile("<link href=\"([^\"]*)\" rel=\"image_src\"").findall(link)		
				match=re.compile("src=\"([^\"]+)\" data-setup").findall(link)		
				for url in match:
						addLink(name,url,thumbnail[0])
		
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
        search()	
		
elif mode==2:
        print ""
        main()		

elif mode==3:
        print ""
        sub()		

elif mode==4:
        print ""
        pagelist()		
		
elif mode==5:
        print ""+url
        index(url)
		
elif mode==6:
        print ""+url
        vlinks(url,name)		
		
xbmcplugin.endOfDirectory(int(sys.argv[1]))