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

addon      = xbmcaddon.Addon('plugin.video.phim3s.net')
profile    = xbmc.translatePath(addon.getAddonInfo('profile'))
mysettings = xbmcaddon.Addon(id='plugin.video.phim3s.net')
home       = mysettings.getAddonInfo('path')
fanart     = xbmc.translatePath(os.path.join(home, 'fanart.jpg'))
icon       = xbmc.translatePath(os.path.join(home, 'icon.png'))
logos      = xbmc.translatePath(os.path.join(home, 'logos\\'))
base_url   = 'http://phim3s.net/'
pagestr    = map(str, range(1,220))

def home():
        addDir('[COLOR yellow]Tìm Phim[/COLOR][B]   [COLOR lime]>[/COLOR][COLOR orange]>[/COLOR][COLOR blue]>[/COLOR][COLOR magenta]>[/COLOR]   [/B][COLOR yellow]Movie Search[/COLOR]',base_url,1,logos + 'logo.png')
        addDir('[COLOR lime]Thể Loại[/COLOR]',base_url + 'the-loai/phim-hanh-dong',2,icon)
        addDir('[COLOR orange]Quốc Gia[/COLOR]',base_url + 'quoc-gia/phim-my',2,logos + 'logo.png')
        addDir('[COLOR blue]Phim Lẻ[/COLOR]',base_url + 'danh-sach/phim-le',2,icon)
        addDir('[COLOR magenta]Phim Bộ[/COLOR]',base_url + 'danh-sach/phim-bo',2,logos + 'logo.png')
        addDir('[COLOR cyan]Phim Chiếu Rạp[/COLOR]',base_url + 'danh-sach/phim-chieu-rap',2,icon)
        addDir('[COLOR pink]Phim Mới[/COLOR]',base_url + 'danh-sach/phim-moi',2,logos + 'logo.png')
        addDir('[COLOR coral]Phim Thuyết Minh[/COLOR]',base_url + 'danh-sach/phim-thuyet-minh',3,icon)

def dirs():
		if 'the-loai' in url:
				addDir('[COLOR yellow]Phim Âm Nhạc[/COLOR]',base_url + 'the-loai/phim-am-nhac',3,logos + 'logo.png')
				addDir('[COLOR lime]Phim Chiến Tranh[/COLOR]',base_url + 'the-loai/phim-chien-tranh',3,icon)
				addDir('[COLOR orange]Phim Cổ Trang[/COLOR]',base_url + 'the-loai/phim-co-trang',3,logos + 'logo.png')
				addDir('[COLOR blue]Phim Hài Hước[/COLOR]',base_url + 'the-loai/phim-hai-huoc',3,icon)
				addDir('[COLOR magenta]Phim Hành Động[/COLOR]',base_url + 'the-loai/phim-hanh-dong',3,logos + 'logo.png')
				addDir('[COLOR tan]Phim Hình Sự[/COLOR]',base_url + 'the-loai/phim-hinh-su',3,icon)
				addDir('[COLOR chocolate]Phim Hoạt Hình[/COLOR]',base_url + 'the-loai/phim-hoat-hinh',3,logos + 'logo.png')
				addDir('[COLOR cyan]Phim Kinh Dị[/COLOR]',base_url + 'the-loai/phim-kinh-di',3,icon)
				addDir('[COLOR violet]Phim Phiêu Lưu[/COLOR]',base_url + 'the-loai/phim-phieu-luu',3,logos + 'logo.png')
				addDir('[COLOR gold]Phim Viễn Tưởng[/COLOR]',base_url + 'the-loai/phim-vien-tuong',3,icon)
				addDir('[COLOR white]Phim Võ Thuật[/COLOR]',base_url + 'the-loai/phim-vo-thuat',3,logos + 'logo.png')
				addDir('[COLOR silver]Phim Tâm Lý[/COLOR]',base_url + 'the-loai/phim-tam-ly',3,icon)
				addDir('[COLOR olive]Phim Thần Thoại[/COLOR]',base_url + 'the-loai/phim-than-thoai',3,logos + 'logo.png')
				addDir('[COLOR pink]Phim TV Show[/COLOR]',base_url + 'the-loai/phim-tv-show',3,icon)
		if 'quoc-gia' in url:
				addDir('[COLOR white]Phim Anh[/COLOR]',base_url + 'quoc-gia/phim-anh',3,logos + 'logo.png')
				addDir('[COLOR gold]Phim Ấn Độ[/COLOR]',base_url + 'quoc-gia/phim-an-do',3,icon)
				addDir('[COLOR violet]Phim Hàn Quốc[/COLOR]',base_url + 'quoc-gia/phim-han-quoc',3,logos + 'logo.png')
				addDir('[COLOR cyan]Phim Hồng Kông[/COLOR]',base_url + 'quoc-gia/phim-hong-kong',3,icon)
				addDir('[COLOR chocolate]Phim Khác[/COLOR]',base_url + 'quoc-gia/phim-khac',3,logos + 'logo.png')
				addDir('[COLOR tan]Phim Mỹ[/COLOR]',base_url + 'quoc-gia/phim-my',3,icon)
				addDir('[COLOR magenta]Phim Nhật Bản[/COLOR]',base_url + 'quoc-gia/phim-nhat-ban',3,logos + 'logo.png')
				addDir('[COLOR blue]Phim Pháp[/COLOR]',base_url + 'quoc-gia/phim-phap',3,icon)
				addDir('[COLOR orange]Phim Thái Lan[/COLOR]',base_url + 'quoc-gia/phim-thai-lan',3,logos + 'logo.png')
				addDir('[COLOR lime]Phim Trung Quốc[/COLOR]',base_url + 'quoc-gia/phim-trung-quoc',3,icon)
				addDir('[COLOR yellow]Phim Việt Nam[/COLOR]',base_url + 'quoc-gia/phim-viet-nam',3,logos + 'logo.png')
		if 'phim-le' in url:
				addDir('[COLOR lime]Toàn Bộ Phim Lẻ[/COLOR]',base_url + 'danh-sach/phim-le',3,icon)
				addDir('[COLOR silver]Phim Lẻ 2014[/COLOR]',base_url + 'danh-sach/phim-le/?year=2014',3,logos + 'logo.png')
				addDir('[COLOR violet]Phim Lẻ 2013[/COLOR]',base_url + 'danh-sach/phim-le/?year=2013',3,icon)
				addDir('[COLOR cyan]Phim Lẻ 2012[/COLOR]',base_url + 'danh-sach/phim-le/?year=2012',3,logos + 'logo.png')
		if 'phim-bo' in url:
				addDir('[COLOR lime]Toàn Bộ Phim Bộ[/COLOR]',base_url + 'danh-sach/phim-bo',3,icon)
				addDir('[COLOR silver]Phim Bộ 2014[/COLOR]',base_url + 'danh-sach/phim-bo/?year=2014',3,logos + 'logo.png')
				addDir('[COLOR violet]Phim Bộ 2013[/COLOR]',base_url + 'danh-sach/phim-bo/?year=2013',3,icon)
				addDir('[COLOR cyan]Phim Bộ 2012[/COLOR]',base_url + 'danh-sach/phim-bo/?year=2012',3,logos + 'logo.png')
		if 'phim-chieu-rap' in url:
				addDir('[COLOR lime]Toàn Bộ Phim Chiếu Rạp[/COLOR]',base_url + 'danh-sach/phim-chieu-rap',3,icon)
				addDir('[COLOR silver]Phim Chiếu Rạp 2014[/COLOR]',base_url + 'danh-sach/phim-chieu-rap/?year=2014',3,logos + 'logo.png')
				addDir('[COLOR violet]Phim Chiếu Rạp 2013[/COLOR]',base_url + 'danh-sach/phim-chieu-rap/?year=2013',3,icon)
				addDir('[COLOR cyan]Phim Chiếu Rạp 2012[/COLOR]',base_url + 'danh-sach/phim-chieu-rap/?year=2012',3,logos + 'logo.png')
		if 'phim-moi' in url:
				addDir('[COLOR lime]Toàn Bộ Phim Mới[/COLOR]',base_url + 'danh-sach/phim-moi',3,icon)
				addDir('[COLOR silver]Phim Mới 2014[/COLOR]',base_url + 'danh-sach/phim-2014',3,logos + 'logo.png')
				addDir('[COLOR violet]Phim Mới 2013[/COLOR]',base_url + 'danh-sach/phim-2013',3,icon)
				addDir('[COLOR cyan]Phim Mới 2012[/COLOR]',base_url + 'danh-sach/phim-2012',3,logos + 'logo.png')
		
def pagelist():
		if 'phim-am-nhac' in url:
				i=0
				for i in range(3):
						addDir('[COLOR yellow]Phim Âm Nhạc[/COLOR] - [COLOR lime]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'the-loai/phim-am-nhac/page-' + pagestr[i],4,icon)
						i+=1
		if 'phim-chien-tranh' in url:
				i=0
				for i in range(9):
						addDir('[COLOR lime]Phim Chiến Tranh[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'the-loai/phim-chien-tranh/page-' + pagestr[i],4,logos + 'logo.png')
						i+=1
		if 'phim-co-trang' in url:
				i=0
				for i in range(14):
						addDir('[COLOR orange]Phim Cổ Trang[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'the-loai/phim-co-trang/page-' + pagestr[i],4,icon)
						i+=1
		if 'phim-hai-huoc' in url:
				i=0
				for i in range(47):
						addDir('[COLOR blue]Phim Hài Hước[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'the-loai/phim-hai-huoc/page-' + pagestr[i],4,logos + 'logo.png')
						i+=1
		if 'phim-hanh-dong' in url:
				i=0
				for i in range(57):
						addDir('[COLOR magenta]Phim Hành Động[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'the-loai/phim-hanh-dong/page-' + pagestr[i],4,icon)
						i+=1
		if 'phim-hinh-su' in url:
				i=0
				for i in range(130):
						addDir('[COLOR tan]Phim Hình Sự[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'the-loai/phim-hinh-su/page-' + pagestr[i],4,logos + 'logo.png')
						i+=1
		if 'phim-hoat-hinh' in url:
				i=0
				for i in range(40):
						addDir('[COLOR chocolate]Phim Hoạt Hình[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'the-loai/phim-hoat-hinh/page-' + pagestr[i],4,icon)
						i+=1
		if 'phim-kinh-di' in url:
				i=0
				for i in range(21):
						addDir('[COLOR cyan]Phim Kinh Dị[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'the-loai/phim-kinh-di/page-' + pagestr[i],4,logos + 'logo.png')
						i+=1
		if 'phim-phieu-luu' in url:
				i=0
				for i in range(22):
						addDir('[COLOR violet]Phim Phiêu Lưu[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'the-loai/phim-phieu-luu/page-' + pagestr[i],4,icon)
						i+=1
		if 'phim-vien-tuong' in url:
				i=0
				for i in range(19):
						addDir('[COLOR gold]Phim Viễn Tưởng[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'the-loai/phim-vien-tuong/page-' + pagestr[i],4,logos + 'logo.png')
						i+=1
		if 'phim-vo-thuat' in url:
				i=0
				for i in range(20):
						addDir('[COLOR white]Phim Võ Thuật[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'the-loai/phim-vo-thuat/page-' + pagestr[i],4,icon)
						i+=1
		if 'phim-tam-ly' in url:
				i=0
				for i in range(68):
						addDir('[COLOR silver]Phim Tâm Lý[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'the-loai/phim-tam-ly/page-' + pagestr[i],4,logos + 'logo.png')
						i+=1
		if 'phim-than-thoai' in url:
				i=0
				for i in range(4):
						addDir('[COLOR olive]Phim Thần Thoại[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'the-loai/phim-than-thoai/page-' + pagestr[i],4,icon)
						i+=1
		if 'phim-tv-show' in url:
				i=0
				for i in range(18):
						addDir('[COLOR pink]Phim TV Show[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'the-loai/phim-tv-show/page-' + pagestr[i],4,logos + 'logo.png')
						i+=1
		if 'phim-anh' in url:
				i=0
				for i in range(2):
						addDir('[COLOR white]Phim Anh[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'quoc-gia/phim-anh/page-' + pagestr[i],4,icon)
						i+=1
		if 'phim-an-do' in url:
				i=0
				for i in range(3):
						addDir('[COLOR gold]Phim Ấn Độ[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'quoc-gia/phim-an-do/page-' + pagestr[i],4,logos + 'logo.png')
						i+=1
		if 'phim-han-quoc' in url:
				i=0
				for i in range(19):
						addDir('[COLOR violet]Phim Hàn Quốc[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'quoc-gia/phim-han-quoc/page-' + pagestr[i],4,icon)
						i+=1
		if 'phim-hong-kong' in url:
				i=0
				for i in range(13):
						addDir('[COLOR cyan]Phim Hồng Kông[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'quoc-gia/phim-hong-kong/page-' + pagestr[i],4,logos + 'logo.png')
						i+=1
		if 'phim-khac' in url:
				i=0
				for i in range(5):
						addDir('[COLOR chocolate]Phim Khác[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'quoc-gia/phim-khac/page-' + pagestr[i],4,icon)
						i+=1
		if 'phim-my' in url:
				i=0
				for i in range(90):
						addDir('[COLOR tan]Phim Mỹ[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'quoc-gia/phim-my/page-' + pagestr[i],4,logos + 'logo.png')
						i+=1
		if 'phim-nhat-ban' in url:
				i=0
				for i in range(34):
						addDir('[COLOR magenta]Phim Nhật Bản[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'quoc-gia/phim-nhat-ban/page-' + pagestr[i],4,icon)
						i+=1
		if 'phim-phap' in url:
				i=0
				for i in range(2):
						addDir('[COLOR blue]Phim Pháp[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'quoc-gia/phim-phap/page-' + pagestr[i],4,logos + 'logo.png')
						i+=1
		if 'phim-thai-lan' in url:
				i=0
				for i in range(3):
						addDir('[COLOR orange]Phim Thái Lan[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'quoc-gia/phim-thai-lan/page-' + pagestr[i],4,icon)
						i+=1
		if 'phim-trung-quoc' in url:
				i=0
				for i in range(27):
						addDir('[COLOR lime]Phim Trung Quốc[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'quoc-gia/phim-trung-quoc/page-' + pagestr[i],4,logos + 'logo.png')
						i+=1
		if 'phim-viet-nam' in url:
				i=0
				for i in range(17):
						addDir('[COLOR yellow]Phim Việt Nam[/COLOR] - [COLOR lime]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'quoc-gia/phim-viet-nam/page-' + pagestr[i],4,icon)
						i+=1
		if url==base_url + 'danh-sach/phim-le':
				i=0
				for i in range(131):
						addDir('[COLOR lime]Toàn Bộ Phim Lẻ[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'danh-sach/phim-le/page-' + pagestr[i],4,logos + 'logo.png')
						i+=1
		if url==base_url + 'danh-sach/phim-le/?year=2014':
				i=0
				for i in range(5):
						addDir('[COLOR silver]Phim Lẻ 2014[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'danh-sach/phim-le/page-' + pagestr[i] + '/?year=2014',4,icon)
						i+=1
		if url==base_url + 'danh-sach/phim-le/?year=2013':
				i=0
				for i in range(17):
						addDir('[COLOR violet]Phim Lẻ 2013[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'danh-sach/phim-le/page-' + pagestr[i] + '/?year=2013',4,logos + 'logo.png')
						i+=1
		if url==base_url + 'danh-sach/phim-le/?year=2012':
				i=0
				for i in range(21):
						addDir('[COLOR cyan]Phim Lẻ 2012[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'danh-sach/phim-le/page-' + pagestr[i] + '/?year=2012',4,icon)
						i+=1
		if url==base_url + 'danh-sach/phim-bo':
				i=0
				for i in range(79):
						addDir('[COLOR lime]Toàn Bộ Phim Bộ[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'danh-sach/phim-bo/page-' + pagestr[i],4,logos + 'logo.png')
						i+=1
		if url==base_url + 'danh-sach/phim-bo/?year=2014':
				i=0
				for i in range(4):
						addDir('[COLOR silver]Phim Bộ 2014[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'danh-sach/phim-bo/page-' + pagestr[i] + '/?year=2014',4,icon)
						i+=1
		if url==base_url + 'danh-sach/phim-bo/?year=2013':
				i=0
				for i in range(12):
						addDir('[COLOR violet]Phim Bộ 2013[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'danh-sach/phim-bo/page-' + pagestr[i] + '/?year=2013',4,logos + 'logo.png')
						i+=1
		if url==base_url + 'danh-sach/phim-bo/?year=2012':
				i=0
				for i in range(22):
						addDir('[COLOR cyan]Phim Bộ 2012[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'danh-sach/phim-bo/page-' + pagestr[i] + '/?year=2012',4,icon)
						i+=1						
		if url==base_url + 'danh-sach/phim-chieu-rap':
				i=0
				for i in range(22):
						addDir('[COLOR lime]Toàn Bộ Phim Chiếu Rạp[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'danh-sach/phim-chieu-rap/page-' + pagestr[i],4,logos + 'logo.png')
						i+=1
		if url==base_url + 'danh-sach/phim-chieu-rap/?year=2014':
				i=0
				for i in range(2):
						addDir('[COLOR silver]Phim Chiếu Rạp 2014[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'danh-sach/phim-chieu-rap/page-' + pagestr[i] + '/?year=2014',4,icon)
						i+=1
		if url==base_url + 'danh-sach/phim-chieu-rap/?year=2013':
				i=0
				for i in range(7):
						addDir('[COLOR violet]Phim Chiếu Rạp 2013[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'danh-sach/phim-chieu-rap/page-' + pagestr[i] + '/?year=2013',4,logos + 'logo.png')
						i+=1
		if url==base_url + 'danh-sach/phim-chieu-rap/?year=2012':
				i=0
				for i in range(8):
						addDir('[COLOR cyan]Phim Chiếu Rạp 2012[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'danh-sach/phim-chieu-rap/page-' + pagestr[i] + '/?year=2012',4,icon)
						i+=1
		if url==base_url + 'danh-sach/phim-moi':
				i=0
				for i in range(209):
						addDir('[COLOR lime]Toàn Bộ Phim Mới[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'danh-sach/phim-moi/page-' + pagestr[i],4,logos + 'logo.png')
						i+=1
		if url==base_url + 'danh-sach/phim-2014':
				i=0
				for i in range(9):
						addDir('[COLOR silver]Phim Mới 2014[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'danh-sach/phim-moi/page-' + pagestr[i] + '/?year=2014',4,icon)
						i+=1
		if url==base_url + 'danh-sach/phim-2013':
				i=0
				for i in range(28):
						addDir('[COLOR violet]Phim Mới 2013[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'danh-sach/phim-moi/page-' + pagestr[i] + '/?year=2013',4,logos + 'logo.png')
						i+=1
		if url==base_url + 'danh-sach/phim-2012':
				i=0
				for i in range(43):
						addDir('[COLOR cyan]Phim Mới 2012[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'danh-sach/phim-moi/page-' + pagestr[i] + '/?year=2012',4,icon)
						i+=1
		if 'phim-thuyet-minh' in url:
				i=0
				for i in range(48):
						addDir('[COLOR coral]Phim Thuyết Minh[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',base_url + 'danh-sach/phim-thuyet-minh/page-' + pagestr[i],4,logos + 'logo.png')
						i+=1
						
def index(url):
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
		response = urllib2.urlopen(req, timeout=90)
		link=response.read()
		response.close()
		match=re.compile("<div class=\"inner\"><a href=\"(.*?)\" title=\"([^\"]*)\"><img src=\"(.+?)\"").findall(link)
		for url,name,thumbnail in match:
				addDir('[COLOR yellow]' + name + '[/COLOR]',('%s%sxem-phim' % (base_url, url)),5,thumbnail)					
		
def videolinks(url,name):
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
		response = urllib2.urlopen(req, timeout=90)
		link=response.read()
		response.close()
		thumbnail=re.compile("<meta property=\"og:image\" content=\"([^\"]*)\"").findall(link)		
		match=re.compile("a data-type=\"watch\" data-episode-id.+?href=\"([^\"]*)\" title=\"(.*?)\"").findall(link)
		for url,title in match:
				addLink(('%s   -   %s' % ('[COLOR lime]' + title + '[/COLOR]',name )),('%s%svideo.mp4' % (base_url, url)),thumbnail[-1])
		
def search():
    try:
        keyb = xbmc.Keyboard('', '[COLOR yellow]Enter search text[/COLOR]')
        keyb.doModal()
        if (keyb.isConfirmed()):
			searchText = urllib.quote_plus(keyb.getText())
        url = base_url + 'search?keyword='+searchText
        index(url)
    except: pass
				
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
        search()
		
elif mode==2:
        print ""
        dirs()

elif mode==3:
        print ""
        pagelist()
				
elif mode==4:
        print ""+url
        index(url)
        
elif mode==5:
        print ""+url
        videolinks(url,name)

xbmcplugin.endOfDirectory(int(sys.argv[1]))