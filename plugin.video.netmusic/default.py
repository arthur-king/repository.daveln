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
pagestr    = map(str, range(1,50))

def categories():
        addDir('[COLOR yellow]Nhạc Số[/COLOR]','http://nhacso.net',2,logos + 'ns.png')		
        addDir('[COLOR lime]Chia Sẻ Nhạc[/COLOR]','http://chiasenhac.com',2,logos + 'csn.png')
        addLink('[COLOR orange]Vmusic[/COLOR]','http://206.190.130.141:1935/liveStream/mtv_1/playlist.m3u8',logos + 'vmusic.png')	
        addLink('[COLOR magenta]Viet MTV[/COLOR]','http://64.62.143.5:1935/live/donotstealmy-Stream1/playlist.m3u8?bitrate=800&q=high',logos + 'vietmtv.png')		
        addLink('[COLOR cyan]Nhạc Của Tui[/COLOR]','rtmp://123.30.134.108:1935/live playpath=nctlive swfUrl=http://hktivi.net/player.swf pageUrl=http://hktivi.net/kenh/nhaccuatui.php',logos + 'nct.png')	
	
def search():
		if 'Nhạc Số' in name:
				try:
						keyb = xbmc.Keyboard('', '[COLOR yellow]Enter search text[/COLOR]')
						keyb.doModal()
						if (keyb.isConfirmed()):
								searchText = urllib.quote_plus(keyb.getText())
						url = 'http://nhacso.net/?KeyName='+searchText
						index(url)
				except: pass
		if 'Chia Sẻ Nhạc' in name:
				try:
						keyb = xbmc.Keyboard('', '[COLOR yellow]Enter search text[/COLOR]')
						keyb.doModal()
						if (keyb.isConfirmed()):
								searchText = urllib.quote_plus(keyb.getText())
						url = 'http://search.chiasenhac.com/search.php?s='+searchText+'&song_list=""'
						index(url)
				except: pass

def main():
		if 'Nhạc Số' in name:
				addDir('[COLOR yellow]Nhạc Số[/COLOR][B]   [COLOR lime]>[/COLOR][COLOR magenta]>[/COLOR][COLOR cyan]>[/COLOR][COLOR orange]>[/COLOR]   [/B][COLOR lime]Tìm Nhạc[/COLOR]','http://nhacso.net',1,logos + 'ns.png')		
				addDir('[COLOR orange]Video Clips - Thể Loại[/COLOR]','http://nhacso.net',3,logos + 'ns.png')
				addDir('[COLOR magenta]Video Clips - Nghệ Sĩ Việt Nam[/COLOR]','http://nhacso.net',3,logos + 'ns.png')
				addDir('[COLOR cyan]Video Clips - Nghệ Sĩ Quốc Tế[/COLOR]','http://nhacso.net',3,logos + 'ns.png')
		if 'Chia Sẻ Nhạc' in name:
				addDir('[COLOR lime]Chia Sẻ Nhạc[/COLOR][B]   [COLOR lime]>[/COLOR][COLOR magenta]>[/COLOR][COLOR cyan]>[/COLOR][COLOR orange]>[/COLOR]   [/B][COLOR yellow]Tìm Nhạc[/COLOR]','http://chiasenhac.com',1,logos + 'csn.png')		
				addDir('[COLOR orange]Video Clips[/COLOR]','http://chiasenhac.com',3,logos + 'csn.png')

def sub():
		if 'Thể Loại' in name:
				addDir('[COLOR lime]Nhạc Trẻ[/COLOR]','http://nhacso.net/the-loai-video/nhac-tre-1/trang-1.html',4,logos + 'ns.png')
				addDir('[COLOR orange]Nhạc Trữ Tình[/COLOR]','http://nhacso.net/the-loai-video/nhac-tru-tinh-2/trang-1.html',4,logos + 'ns.png')
				addDir('[COLOR blue]Nhạc Quê Hương[/COLOR]','http://nhacso.net/the-loai-video/nhac-que-huong-11/trang-1.html',4,logos + 'ns.png')
				addDir('[COLOR magenta]Nhạc dân Tộc[/COLOR]','http://nhacso.net/the-loai-video/nhac-dan-toc-6/trang-1.html',4,logos + 'ns.png')
				addDir('[COLOR cyan]Nhạc Trịnh[/COLOR]','http://nhacso.net/the-loai-video/nhac-trinh-4/trang-1.html',4,logos + 'ns.png')
				addDir('[COLOR brown]Nhạc Tiền Chiến[/COLOR]','http://nhacso.net/the-loai-video/nhac-tien-chien-5/trang-1.html',4,logos + 'ns.png')
				addDir('[COLOR coral]Nhạc Thiếu Nhi[/COLOR]','http://nhacso.net/the-loai-video/nhac-thieu-nhi-7/trang-1.html',4,logos + 'ns.png')
				addDir('[COLOR gold]Rock Việt[/COLOR]','http://nhacso.net/the-loai-video/rock-viet-9/trang-1.html',4,logos + 'ns.png')
				addDir('[COLOR chocolate]Rap Việt - HipHop[/COLOR]','http://nhacso.net/the-loai-video/rap-viet-hiphop-14/trang-1.html',4,logos + 'ns.png')
				addDir('[COLOR green]Nhạc Âu Mỹ[/COLOR]','http://nhacso.net/the-loai-video/nhac-au-my-21/trang-1.html',4,logos + 'ns.png')
				addDir('[COLOR tomato]Nhạc Hàn[/COLOR]','http://nhacso.net/the-loai-video/nhac-han-16/trang-1.html',4,logos + 'ns.png')
				addDir('[COLOR deeppink]Nhạc Hoa[/COLOR]','http://nhacso.net/the-loai-video/nhac-hoa-15/trang-1.html',4,logos + 'ns.png')
				addDir('[COLOR maroon]Nhạc Nhật[/COLOR]','http://nhacso.net/the-loai-video/nhac-nhat-32/trang-1.html',4,logos + 'ns.png')
				addDir('[COLOR olive]Nhạc Pháp[/COLOR]','http://nhacso.net/the-loai-video/nhac-phap-17/trang-1.html',4,logos + 'ns.png')
				addDir('[COLOR pink]Nhạc Các Nước Khác[/COLOR]','http://nhacso.net/the-loai-video/nhac-cac-nuoc-khac-18/trang-1.html',4,logos + 'ns.png')
				addDir('[COLOR red]Nhân Tố Bí Ẩn[/COLOR]','http://nhacso.net/the-loai-video/nhan-to-bi-an-82/trang-1.html',4,logos + 'ns.png')
				addDir('[COLOR tan]Truyền Hình HomeTV[/COLOR]','http://nhacso.net/the-loai-video/truyen-hinh-hometv-81/trang-1.html',4,logos + 'ns.png')
				addDir('[COLOR violet]Giọng Hát Việt Nhí[/COLOR]','http://nhacso.net/the-loai-video/giong-hat-viet-nhi-68/trang-1.html',4,logos + 'ns.png')
				addDir('[COLOR silver]Fanmade / Radio[/COLOR]','http://nhacso.net/the-loai-video/fanmade-radio-66/trang-1.html',4,logos + 'ns.png')
				addDir('[COLOR salmon]Shining Show[/COLOR]','http://nhacso.net/the-loai-video/shining-show-63/trang-1.html',4,logos + 'ns.png')
		if 'Nghệ Sĩ Việt Nam' in name:
				addDir('[COLOR lime]Cẩm Ly[/COLOR]','http://nhacso.net/video-cua-nghe-si/cam-ly-17-1-1.html',4,logos + 'ns.png')
				addDir('[COLOR orange]Dương Ngọc Thái[/COLOR]','http://nhacso.net/video-cua-nghe-si/duong-ngoc-thai-789-1-1.html',4,logos + 'ns.png')
				addDir('[COLOR blue]Đàm Vĩnh Hưng[/COLOR]','http://nhacso.net/video-cua-nghe-si/dam-vinh-hung-47-1-1.html',4,logos + 'ns.png')
				addDir('[COLOR magenta]Đan Trường[/COLOR]','http://nhacso.net/video-cua-nghe-si/dan-truong-55-1-1.html',4,logos + 'ns.png')
				addDir('[COLOR cyan]Hồ Ngọc Hà[/COLOR]','http://nhacso.net/video-cua-nghe-si/ho-ngoc-ha-33-1-1.html',4,logos + 'ns.png')
				addDir('[COLOR brown]Khắc Việt[/COLOR]','http://nhacso.net/video-cua-nghe-si/khac-viet-4481-1-1.html',4,logos + 'ns.png')
				addDir('[COLOR coral]Lam Trường[/COLOR]','http://nhacso.net/video-cua-nghe-si/lam-truong-4-1-1.html',4,logos + 'ns.png')
				addDir('[COLOR gold]Lệ Quyên[/COLOR]','http://nhacso.net/video-cua-nghe-si/le-quyen-3-1-1.html',4,logos + 'ns.png')
				addDir('[COLOR green]Ngô Kiến Huy[/COLOR]','http://nhacso.net/video-cua-nghe-si/ngo-kien-huy-2228-1-1.html',4,logos + 'ns.png')
				addDir('[COLOR tomato]Noo Phước Thịnh[/COLOR]','http://nhacso.net/video-cua-nghe-si/noo-phuoc-thinh-2430-1-1.html',4,logos + 'ns.png')
				addDir('[COLOR deeppink]Phương Thanh[/COLOR]','http://nhacso.net/video-cua-nghe-si/phuong-thanh-110-1-1.html',4,logos + 'ns.png')
				addDir('[COLOR maroon]Quang Dũng[/COLOR]','http://nhacso.net/video-cua-nghe-si/quang-dung-79-1-1.html',4,logos + 'ns.png')
				addDir('[COLOR olive]The Men[/COLOR]','http://nhacso.net/video-cua-nghe-si/the-men-2407-1-1.html',4,logos + 'ns.png')
				addDir('[COLOR pink]Thuỷ Tiên[/COLOR]','http://nhacso.net/video-cua-nghe-si/thuy-tien-2429-1-1.html',4,logos + 'ns.png')
				addDir('[COLOR red]Uyên Linh[/COLOR]','http://nhacso.net/video-cua-nghe-si/uyen-linh-4525-1-1.html',4,logos + 'ns.png')
				addDir('[COLOR tan]Văn Mai Hương[/COLOR]','http://nhacso.net/video-cua-nghe-si/van-mai-huong-3159-1-1.html',4,logos + 'ns.png')
				addDir('[COLOR violet]Vmusic[/COLOR]','http://nhacso.net/video-cua-nghe-si/vmusic-4540-1-1.html',4,logos + 'ns.png')
		if 'Nghệ Sĩ Quốc Tế' in name:
				addDir('[COLOR lime]2NE1[/COLOR]','http://nhacso.net/video-cua-nghe-si/2ne1-3760-1-1.html',4,logos + 'ns.png')
				addDir('[COLOR orange]2PM[/COLOR]','http://nhacso.net/video-cua-nghe-si/2pm-3762-1-1.html',4,logos + 'ns.png')
				addDir('[COLOR blue]Adele[/COLOR]','http://nhacso.net/video-cua-nghe-si/adele-5903-1-1.html',4,logos + 'ns.png')
				addDir('[COLOR magenta]Avril Lavigne[/COLOR]','http://nhacso.net/video-cua-nghe-si/avril-lavigne-2496-1-1.html',4,logos + 'ns.png')
				addDir('[COLOR brown]Beyonce[/COLOR]','http://nhacso.net/video-cua-nghe-si/beyonce-2530-1-1.html',4,logos + 'ns.png')
				addDir('[COLOR coral]Big Bang[/COLOR]','http://nhacso.net/video-cua-nghe-si/big-bang-2536-1-1.html',4,logos + 'ns.png')
				addDir('[COLOR gold]Britney Spears[/COLOR]','http://nhacso.net/video-cua-nghe-si/britney-spears-2568-1-1.html',4,logos + 'ns.png')
				addDir('[COLOR chocolate]Girls Generation[/COLOR]','http://nhacso.net/video-cua-nghe-si/snsd-girls-generation-2802-1-1.html',4,logos + 'ns.png')
				addDir('[COLOR green]Jay Chou - Châu[/COLOR]','http://nhacso.net/video-cua-nghe-si/jay-chou-chau-kiet-luan-2926-1-1.html',4,logos + 'ns.png')
				addDir('[COLOR tomato]Justin Bieber[/COLOR]','http://nhacso.net/video-cua-nghe-si/justin-bieber-2976-1-1.html',4,logos + 'ns.png')
				addDir('[COLOR deeppink]Kelly Clarkson[/COLOR]','http://nhacso.net/video-cua-nghe-si/kelly-clarkson-3011-1-1.html',4,logos + 'ns.png')
				addDir('[COLOR maroon]Lady Gaga[/COLOR]','http://nhacso.net/video-cua-nghe-si/lady-gaga-3074-1-1.html',4,logos + 'ns.png')
				addDir('[COLOR pink]Rihanna[/COLOR]','http://nhacso.net/video-cua-nghe-si/rihanna-3375-1-1.html',4,logos + 'ns.png')
				addDir('[COLOR red]S.H.E[/COLOR]','http://nhacso.net/video-cua-nghe-si/s-h-e-3405-1-1.html',4,logos + 'ns.png')
				addDir('[COLOR tan]Super Junior[/COLOR]','http://nhacso.net/video-cua-nghe-si/super-junior-3514-1-1.html',4,logos + 'ns.png')
				addDir('[COLOR violet]TVXQ (DBDK)[/COLOR]','http://nhacso.net/video-cua-nghe-si/dbsk-tvxq-5218-1-1.html',4,logos + 'ns.png')
		if 'chiasenhac' in url:
				addDir('[COLOR lime]Video Việt Nam[/COLOR]','http://chiasenhac.com/hd/video/v-video',4,logos + 'csn.png')
				addDir('[COLOR orange]Video Âu, Mỹ[/COLOR]','http://chiasenhac.com/hd/video/u-video',4,logos + 'csn.png')
				addDir('[COLOR blue]Video Hoa[/COLOR]','http://chiasenhac.com/hd/video/c-video',4,logos + 'csn.png')
				addDir('[COLOR magenta]Video Hàn[/COLOR]','http://chiasenhac.com/hd/video/k-video',4,logos + 'csn.png')
				addDir('[COLOR cyan]Video Các Nước Khác[/COLOR]','http://chiasenhac.com/hd/video/o-video',4,logos + 'csn.png')
				addDir('[COLOR gold]Video Live[/COLOR]','http://chiasenhac.com/hd/video/l-video',4,logos + 'csn.png')
				addDir('[COLOR tomato]Video Hài[/COLOR]','http://chiasenhac.com/hd/video/h-video',4,logos + 'csn.png')
				
def pagelist():
		if 'nhac-tre' in url:
				i=0
				for i in range(42):
						addDir('[COLOR lime]Nhạc Trẻ[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/the-loai-video/nhac-tre-1/trang-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1
		if 'nhac-tru-tinh' in url:
				i=0
				for i in range(42):		
						addDir('[COLOR orange]Nhạc Trữ Tình[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/the-loai-video/nhac-tru-tinh-2/trang-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1 		
		if 'nhac-que-huong' in url:
				i=0
				for i in range(18):
						addDir('[COLOR blue]Nhạc Quê Hương[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/the-loai-video/nhac-que-huong-11/trang-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1		
		if 'nhac-dan-toc' in url:
				i=0
				for i in range(37):
						addDir('[COLOR magenta]Nhạc dân Tộc[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/the-loai-video/nhac-dan-toc-6/trang-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1			
		if 'nhac-trinh' in url:
				i=0
				for i in range(4):
						addDir('[COLOR cyan]Nhạc Trịnh[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/the-loai-video/nhac-trinh-4/trang-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1		
		if 'nhac-tien-chien' in url: 	
				i=0
				for i in range(4):		
						addDir('[COLOR brown]Nhạc Tiền Chiến[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/the-loai-video/nhac-tien-chien-5/trang-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1		
		if 'nhac-thieu-nhi' in url:
				i=0
				for i in range(10):
						addDir('[COLOR coral]Nhạc Thiếu Nhi[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/the-loai-video/nhac-thieu-nhi-7/trang-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1						
		if 'rock-viet' in url:
				i=0
				for i in range(4):
						addDir('[COLOR gold]Rock Việt[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/the-loai-video/rock-viet-9/trang-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1		
		if 'rap-viet-hiphop' in url:
				i=0
				for i in range(3):		
						addDir('[COLOR chocolate]Rap Việt - HipHop[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/the-loai-video/rap-viet-hiphop-14/trang-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1 		
		if 'nhac-au-my' in url:
				i=0
				for i in range(42):
						addDir('[COLOR green]Nhạc Âu Mỹ[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/the-loai-video/nhac-au-my-21/trang-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1		
		if 'nhac-han' in url:
				i=0
				for i in range(42):
						addDir('[COLOR tomato]Nhạc Hàn[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/the-loai-video/nhac-han-16/trang-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1			
		if 'nhac-hoa' in url:
				i=0
				for i in range(42):
						addDir('[COLOR deeppink]Nhạc Hoa[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/the-loai-video/nhac-hoa-15/trang-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1		
		if 'nhac-nhat' in url: 	
				i=0
				for i in range(42):		
						addDir('[COLOR maroon]Nhạc Nhật[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/the-loai-video/nhac-nhat-32/trang-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1 		
		if 'nhac-phap' in url:
				i=0
				for i in range(1):
						addDir('[COLOR olive]Nhạc Pháp[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/the-loai-video/nhac-phap-17/trang-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1						
		if 'nhac-cac-nuoc-khac' in url:
				i=0
				for i in range(18):
						addDir('[COLOR pink]Nhạc Các Nước Khác[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/the-loai-video/nhac-cac-nuoc-khac-18/trang-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1		
		if 'nhan-to-bi-an' in url:
				i=0
				for i in range(3):		
						addDir('[COLOR red]Nhân Tố Bí Ẩn[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/the-loai-video/nhan-to-bi-an-82/trang-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1 		
		if 'truyen-hinh-hometv' in url:
				i=0
				for i in range(1):
						addDir('[COLOR tan]Truyền Hình HomeTV[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/the-loai-video/truyen-hinh-hometv-81/trang-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1		
		if 'giong-hat-viet-nhi' in url:
				i=0
				for i in range(4):
						addDir('[COLOR violet]Giọng Hát Việt Nhí[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/the-loai-video/giong-hat-viet-nhi-68/trang-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1			
		if 'fanmade-radio' in url:
				i=0
				for i in range(3):
						addDir('[COLOR silver]Fanmade / Radio[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/the-loai-video/fanmade-radio-66/trang-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1		
		if 'shining-show' in url: 	
				i=0
				for i in range(4):		
						addDir('[COLOR salmon]Shining Show[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/the-loai-video/shining-show-63/trang-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1						
		if 'cam-ly' in url:
				i=0
				for i in range(18):
						addDir('[COLOR lime]Cẩm Ly[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/video-cua-nghe-si/cam-ly-17-1-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1		
		if 'duong-ngoc-thai' in url:
				i=0
				for i in range(3):		
						addDir('[COLOR orange]Dương Ngọc Thái[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/video-cua-nghe-si/duong-ngoc-thai-789-1-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1 		
		if 'dam-vinh-hung' in url:
				i=0
				for i in range(13):
						addDir('[COLOR blue]Đàm Vĩnh Hưng[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/video-cua-nghe-si/dam-vinh-hung-47-1-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1		
		if 'dan-truong' in url:
				i=0
				for i in range(23):
						addDir('[COLOR magenta]Đan Trường[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/video-cua-nghe-si/dan-truong-55-1-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1			
		if 'ho-ngoc-ha' in url:
				i=0
				for i in range(9):
						addDir('[COLOR cyan]Hồ Ngọc Hà[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/video-cua-nghe-si/ho-ngoc-ha-33-1-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1		
		if 'khac-viet' in url: 	
				i=0
				for i in range(3):		
						addDir('[COLOR brown]Khắc Việt[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/video-cua-nghe-si/khac-viet-4481-1-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1 		
		if 'lam-truong' in url:
				i=0
				for i in range(6):
						addDir('[COLOR coral]Lam Trường[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/video-cua-nghe-si/lam-truong-4-1-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1						
		if 'le-quyen' in url:
				i=0
				for i in range(6):
						addDir('[COLOR gold]Lệ Quyên[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/video-cua-nghe-si/le-quyen-3-1-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1		
		if 'ngo-kien-huy' in url:
				i=0
				for i in range(3):		
						addDir('[COLOR green]Ngô Kiến Huy[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/video-cua-nghe-si/ngo-kien-huy-2228-1-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1 		
		if 'noo-phuoc-thinh' in url:
				i=0
				for i in range(4):
						addDir('[COLOR tomato]Noo Phước Thịnh[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/video-cua-nghe-si/noo-phuoc-thinh-2430-1-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1		
		if 'phuong-thanh' in url:
				i=0
				for i in range(7):
						addDir('[COLOR deeppink]Phương Thanh[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/video-cua-nghe-si/phuong-thanh-110-1-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1			
		if 'quang-dung' in url:
				i=0
				for i in range(3):
						addDir('[COLOR maroon]Quang Dũng[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/video-cua-nghe-si/quang-dung-79-1-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1		
		if 'the-men' in url: 	
				i=0
				for i in range(4):		
						addDir('[COLOR olive]The Men[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/video-cua-nghe-si/the-men-2407-1-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1 		
		if 'thuy-tien' in url:
				i=0
				for i in range(3):
						addDir('[COLOR pink]Thuỷ Tiên[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/video-cua-nghe-si/thuy-tien-2429-1-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1						
		if 'uyen-linh' in url:
				i=0
				for i in range(2):
						addDir('[COLOR red]Uyên Linh[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/video-cua-nghe-si/uyen-linh-4525-1-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1		
		if 'van-mai-huong' in url:
				i=0
				for i in range(4):		
						addDir('[COLOR tan]Văn Mai Hương[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/video-cua-nghe-si/van-mai-huong-3159-1-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1		
		if 'vmusic' in url:
				i=0
				for i in range(4):
						addDir('[COLOR violet]Vmusic[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/video-cua-nghe-si/vmusic-4540-1-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1		
		if '2ne1' in url:
				i=0
				for i in range(4):
						addDir('[COLOR lime]2NE1[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/video-cua-nghe-si/2ne1-3760-1-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1			
		if '2pm' in url:
				i=0
				for i in range(6):
						addDir('[COLOR orange]2PM[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/video-cua-nghe-si/2pm-3762-1-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1		
		if 'adele' in url: 	
				i=0
				for i in range(2):		
						addDir('[COLOR blue]Adele[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/video-cua-nghe-si/adele-5903-1-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1
		if 'avril-lavigne' in url:
				i=0
				for i in range(4):
						addDir('[COLOR magenta]Avril Lavigne[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/video-cua-nghe-si/avril-lavigne-2496-1-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1		
		if 'beyonce' in url:
				i=0
				for i in range(8):
						addDir('[COLOR brown]Beyonce[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/video-cua-nghe-si/beyonce-2530-1-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1		
		if 'big-bang' in url:
				i=0
				for i in range(4):
						addDir('[COLOR coral]Big Bang[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/video-cua-nghe-si/big-bang-2536-1-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1			
		if 'britney-spears' in url:
				i=0
				for i in range(4):
						addDir('[COLOR gold]Britney Spears[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/video-cua-nghe-si/britney-spears-2568-1-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1		
		if 'snsd-girls-generation' in url: 	
				i=0
				for i in range(18):		
						addDir('[COLOR chocolate]Girls Generation[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/video-cua-nghe-si/snsd-girls-generation-2802-1-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1 		
		if 'jay-chou-chau-kiet-luan' in url:
				i=0
				for i in range(13):
						addDir('[COLOR green]Jay Chou - Châu[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/video-cua-nghe-si/jay-chou-chau-kiet-luan-2926-1-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1						
		if 'justin-bieber' in url:
				i=0
				for i in range(4):
						addDir('[COLOR tomato]Justin Bieber[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/video-cua-nghe-si/justin-bieber-2976-1-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1		
		if 'kelly-clarkson' in url:
				i=0
				for i in range(3):		
						addDir('[COLOR deeppink]Kelly Clarkson[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/video-cua-nghe-si/kelly-clarkson-3011-1-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1 		
		if 'lady-gaga' in url:
				i=0
				for i in range(4):
						addDir('[COLOR maroon]Lady Gaga[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/video-cua-nghe-si/lady-gaga-3074-1-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1		
		if 'rihanna' in url:
				i=0
				for i in range(6):
						addDir('[COLOR pink]Rihanna[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/video-cua-nghe-si/rihanna-3375-1-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1			
		if 's-h-e' in url:
				i=0
				for i in range(12):
						addDir('[COLOR red]S.H.E[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/video-cua-nghe-si/s-h-e-3405-1-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1		
		if 'super-junior' in url: 	
				i=0
				for i in range(4):		
						addDir('[COLOR tan]Super Junior[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/video-cua-nghe-si/super-junior-3514-1-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1 		
		if 'dbsk-tvxq' in url:
				i=0
				for i in range(6):
						addDir('[COLOR violet]TVXQ (DBDK)[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://nhacso.net/video-cua-nghe-si/dbsk-tvxq-5218-1-' + pagestr[i] + '.html',5,logos + 'ns.png')
						i+=1
		if 'v-video' in url:
				i=0
				for i in range(22):
						addDir('[COLOR lime]Video Việt Nam[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://chiasenhac.com/hd/video/v-video/new' + pagestr[i] + '.html',5,logos + 'csn.png')
						i+=1		
		if 'u-video' in url:
				i=0
				for i in range(22):		
						addDir('[COLOR orange]Video Âu, Mỹ[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://chiasenhac.com/hd/video/u-video/new' + pagestr[i] + '.html',5,logos + 'csn.png')
						i+=1 		
		if 'c-video' in url:
				i=0
				for i in range(22):
						addDir('[COLOR blue]Video Hoa[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://chiasenhac.com/hd/video/c-video/new' + pagestr[i] + '.html',5,logos + 'csn.png')
						i+=1		
		if 'k-video' in url:
				i=0
				for i in range(22):
						addDir('[COLOR magenta]Video[/COLOR] - [COLOR yellow]Hàn Trang ' + pagestr[i] + '[/COLOR]','http://chiasenhac.com/hd/video/k-video/new' + pagestr[i] + '.html',5,logos + 'csn.png')
						i+=1			
		if 'o-video' in url:
				i=0
				for i in range(22):
						addDir('[COLOR cyan]Video Các Nước Khác[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://chiasenhac.com/hd/video/o-video/new' + pagestr[i] + '.html',5,logos + 'csn.png')
						i+=1		
		if 'l-video' in url: 	
				i=0
				for i in range(22):		
						addDir('[COLOR gold]Video Live[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://chiasenhac.com/hd/video/l-video/new' + pagestr[i] + '.html',5,logos + 'csn.png')
						i+=1 		
		if 'h-video' in url:
				i=0
				for i in range(7):
						addDir('[COLOR tomato]Video Hài[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]','http://chiasenhac.com/hd/video/h-video/new' + pagestr[i] + '.html',5,logos + 'csn.png')
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
						addDir('[COLOR lime]' + name + '[/COLOR]',('http://chiasenhac.com/' + url),6,thumbnail)				
		if 'nhacso' in url:		
				if 'the-loai-video' in url:
						match=re.compile("<a href=\"([^\"]*)\" title=\"(.*?)\".+?\s.*?src=\"([^\"]+)\" width").findall(link)
						for url,name,thumbnail in match:
								addDir('[COLOR yellow]' + name + '[/COLOR]',url,6,thumbnail)						
				else:
						match=re.compile("<a class=\"png_img playlist\" href=\"(.+?)\" title=\"([^\"]*)\".+?\s.*?src=\"([^\"]+)\" onerror").findall(link)
						for url,name,thumbnail in match:
								addDir('[COLOR cyan]' + name + '[/COLOR]',url,6,thumbnail)
 				
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