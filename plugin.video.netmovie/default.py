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

addon      = xbmcaddon.Addon('plugin.video.netmovie')
profile    = xbmc.translatePath(addon.getAddonInfo('profile'))
mysettings = xbmcaddon.Addon(id='plugin.video.netmovie')
home       = mysettings.getAddonInfo('path')
fanart     = xbmc.translatePath(os.path.join(home, 'fanart.jpg'))
icon       = xbmc.translatePath(os.path.join(home, 'icon.png'))
logos      = xbmc.translatePath(os.path.join(home, 'logos\\'))
phim3s     = 'http://phim3s.net/'
pagestr    = map(str, range(1,220))

def categories():
		addDir('[COLOR lime]Phim3s.net[/COLOR]',phim3s,2,logos + 'phim3s.png')
		
def search():
    try:
        keyb = xbmc.Keyboard('', '[COLOR yellow]Enter search text[/COLOR]')
        keyb.doModal()
        if (keyb.isConfirmed()):
			searchText = urllib.quote_plus(keyb.getText())
        url = phim3s + 'search?keyword='+searchText
        index(url)
    except: pass

def main():
		if 'phim3s' in url:
				addDir('[COLOR yellow]Tìm Phim[/COLOR][B]   [COLOR lime]>[/COLOR][COLOR orange]>[/COLOR][COLOR blue]>[/COLOR][COLOR magenta]>[/COLOR]   [/B][COLOR yellow]Movie Search[/COLOR]',phim3s,1,logos + 'phim3s.png')
				addDir('[COLOR lime]Thể Loại[/COLOR]',phim3s + 'the-loai/phim-hanh-dong',3,logos + 'phim3s.png')
				addDir('[COLOR orange]Quốc Gia[/COLOR]',phim3s + 'quoc-gia/phim-my',3,logos + 'phim3s.png')
				addDir('[COLOR blue]Phim Lẻ[/COLOR]',phim3s + 'danh-sach/phim-le',3,logos + 'phim3s.png')
				addDir('[COLOR magenta]Phim Bộ[/COLOR]',phim3s + 'danh-sach/phim-bo',3,logos + 'phim3s.png')
				addDir('[COLOR cyan]Phim Chiếu Rạp[/COLOR]',phim3s + 'danh-sach/phim-chieu-rap',3,logos + 'phim3s.png')
				addDir('[COLOR pink]Phim Mới[/COLOR]',phim3s + 'danh-sach/phim-moi',3,logos + 'phim3s.png')
				addDir('[COLOR coral]Phim Thuyết Minh[/COLOR]',phim3s + 'danh-sach/phim-thuyet-minh',4,logos + 'phim3s.png')

def sub():
		if 'phim3s' in url:
				if 'the-loai' in url:
						addDir('[COLOR yellow]Phim Âm Nhạc[/COLOR]',phim3s + 'the-loai/phim-am-nhac',4,logos + 'phim3s.png')
						addDir('[COLOR lime]Phim Chiến Tranh[/COLOR]',phim3s + 'the-loai/phim-chien-tranh',4,logos + 'phim3s.png')
						addDir('[COLOR orange]Phim Cổ Trang[/COLOR]',phim3s + 'the-loai/phim-co-trang',4,logos + 'phim3s.png')
						addDir('[COLOR blue]Phim Hài Hước[/COLOR]',phim3s + 'the-loai/phim-hai-huoc',4,logos + 'phim3s.png')
						addDir('[COLOR magenta]Phim Hành Động[/COLOR]',phim3s + 'the-loai/phim-hanh-dong',4,logos + 'phim3s.png')
						addDir('[COLOR tan]Phim Hình Sự[/COLOR]',phim3s + 'the-loai/phim-hinh-su',4,logos + 'phim3s.png')
						addDir('[COLOR chocolate]Phim Hoạt Hình[/COLOR]',phim3s + 'the-loai/phim-hoat-hinh',4,logos + 'phim3s.png')
						addDir('[COLOR cyan]Phim Kinh Dị[/COLOR]',phim3s + 'the-loai/phim-kinh-di',4,logos + 'phim3s.png')
						addDir('[COLOR violet]Phim Phiêu Lưu[/COLOR]',phim3s + 'the-loai/phim-phieu-luu',4,logos + 'phim3s.png')
						addDir('[COLOR gold]Phim Viễn Tưởng[/COLOR]',phim3s + 'the-loai/phim-vien-tuong',4,logos + 'phim3s.png')
						addDir('[COLOR white]Phim Võ Thuật[/COLOR]',phim3s + 'the-loai/phim-vo-thuat',4,logos + 'phim3s.png')
						addDir('[COLOR silver]Phim Tâm Lý[/COLOR]',phim3s + 'the-loai/phim-tam-ly',4,logos + 'phim3s.png')
						addDir('[COLOR olive]Phim Thần Thoại[/COLOR]',phim3s + 'the-loai/phim-than-thoai',4,logos + 'phim3s.png')
						addDir('[COLOR pink]Phim TV Show[/COLOR]',phim3s + 'the-loai/phim-tv-show',4,logos + 'phim3s.png')
				if 'quoc-gia' in url:
						addDir('[COLOR white]Phim Anh[/COLOR]',phim3s + 'quoc-gia/phim-anh',4,logos + 'phim3s.png')
						addDir('[COLOR gold]Phim Ấn Độ[/COLOR]',phim3s + 'quoc-gia/phim-an-do',4,logos + 'phim3s.png')
						addDir('[COLOR violet]Phim Hàn Quốc[/COLOR]',phim3s + 'quoc-gia/phim-han-quoc',4,logos + 'phim3s.png')
						addDir('[COLOR cyan]Phim Hồng Kông[/COLOR]',phim3s + 'quoc-gia/phim-hong-kong',4,logos + 'phim3s.png')
						addDir('[COLOR chocolate]Phim Khác[/COLOR]',phim3s + 'quoc-gia/phim-khac',4,logos + 'phim3s.png')
						addDir('[COLOR tan]Phim Mỹ[/COLOR]',phim3s + 'quoc-gia/phim-my',4,logos + 'phim3s.png')
						addDir('[COLOR magenta]Phim Nhật Bản[/COLOR]',phim3s + 'quoc-gia/phim-nhat-ban',4,logos + 'phim3s.png')
						addDir('[COLOR blue]Phim Pháp[/COLOR]',phim3s + 'quoc-gia/phim-phap',4,logos + 'phim3s.png')
						addDir('[COLOR orange]Phim Thái Lan[/COLOR]',phim3s + 'quoc-gia/phim-thai-lan',4,logos + 'phim3s.png')
						addDir('[COLOR lime]Phim Trung Quốc[/COLOR]',phim3s + 'quoc-gia/phim-trung-quoc',4,logos + 'phim3s.png')
						addDir('[COLOR yellow]Phim Việt Nam[/COLOR]',phim3s + 'quoc-gia/phim-viet-nam',4,logos + 'phim3s.png')
				if 'phim-le' in url:
						addDir('[COLOR lime]Toàn Bộ Phim Lẻ[/COLOR]',phim3s + 'danh-sach/phim-le',4,logos + 'phim3s.png')
						addDir('[COLOR silver]Phim Lẻ 2014[/COLOR]',phim3s + 'danh-sach/phim-le/?year=2014',4,logos + 'phim3s.png')
						addDir('[COLOR violet]Phim Lẻ 2013[/COLOR]',phim3s + 'danh-sach/phim-le/?year=2013',4,logos + 'phim3s.png')
						addDir('[COLOR cyan]Phim Lẻ 2012[/COLOR]',phim3s + 'danh-sach/phim-le/?year=2012',4,logos + 'phim3s.png')
				if 'phim-bo' in url:
						addDir('[COLOR lime]Toàn Bộ Phim Bộ[/COLOR]',phim3s + 'danh-sach/phim-bo',4,logos + 'phim3s.png')
						addDir('[COLOR silver]Phim Bộ 2014[/COLOR]',phim3s + 'danh-sach/phim-bo/?year=2014',4,logos + 'phim3s.png')
						addDir('[COLOR violet]Phim Bộ 2013[/COLOR]',phim3s + 'danh-sach/phim-bo/?year=2013',4,logos + 'phim3s.png')
						addDir('[COLOR cyan]Phim Bộ 2012[/COLOR]',phim3s + 'danh-sach/phim-bo/?year=2012',4,logos + 'phim3s.png')
				if 'phim-chieu-rap' in url:
						addDir('[COLOR lime]Toàn Bộ Phim Chiếu Rạp[/COLOR]',phim3s + 'danh-sach/phim-chieu-rap',4,logos + 'phim3s.png')
						addDir('[COLOR silver]Phim Chiếu Rạp 2014[/COLOR]',phim3s + 'danh-sach/phim-chieu-rap/?year=2014',4,logos + 'phim3s.png')
						addDir('[COLOR violet]Phim Chiếu Rạp 2013[/COLOR]',phim3s + 'danh-sach/phim-chieu-rap/?year=2013',4,logos + 'phim3s.png')
						addDir('[COLOR cyan]Phim Chiếu Rạp 2012[/COLOR]',phim3s + 'danh-sach/phim-chieu-rap/?year=2012',4,logos + 'phim3s.png')
				if 'phim-moi' in url:
						addDir('[COLOR lime]Toàn Bộ Phim Mới[/COLOR]',phim3s + 'danh-sach/phim-moi',4,logos + 'phim3s.png')
						addDir('[COLOR silver]Phim Mới 2014[/COLOR]',phim3s + 'danh-sach/phim-2014',4,logos + 'phim3s.png')
						addDir('[COLOR violet]Phim Mới 2013[/COLOR]',phim3s + 'danh-sach/phim-2013',4,logos + 'phim3s.png')
						addDir('[COLOR cyan]Phim Mới 2012[/COLOR]',phim3s + 'danh-sach/phim-2012',4,logos + 'phim3s.png')
		
def pagelist():
		if 'phim3s' in url:
				if 'phim-am-nhac' in url:
						i=0
						for i in range(3):
								addDir('[COLOR yellow]Phim Âm Nhạc[/COLOR] - [COLOR lime]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'the-loai/phim-am-nhac/page-' + pagestr[i],5,logos + 'phim3s.png')
								i+=1
				if 'phim-chien-tranh' in url:
						i=0
						for i in range(9):
								addDir('[COLOR lime]Phim Chiến Tranh[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'the-loai/phim-chien-tranh/page-' + pagestr[i],5,logos + 'phim3s.png')
								i+=1
				if 'phim-co-trang' in url:
						i=0
						for i in range(14):
								addDir('[COLOR orange]Phim Cổ Trang[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'the-loai/phim-co-trang/page-' + pagestr[i],5,logos + 'phim3s.png')
								i+=1
				if 'phim-hai-huoc' in url:
						i=0
						for i in range(47):
								addDir('[COLOR blue]Phim Hài Hước[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'the-loai/phim-hai-huoc/page-' + pagestr[i],5,logos + 'phim3s.png')
								i+=1
				if 'phim-hanh-dong' in url:
						i=0
						for i in range(57):
								addDir('[COLOR magenta]Phim Hành Động[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'the-loai/phim-hanh-dong/page-' + pagestr[i],5,logos + 'phim3s.png')
								i+=1
				if 'phim-hinh-su' in url:
						i=0
						for i in range(130):
								addDir('[COLOR tan]Phim Hình Sự[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'the-loai/phim-hinh-su/page-' + pagestr[i],5,logos + 'phim3s.png')
								i+=1
				if 'phim-hoat-hinh' in url:
						i=0
						for i in range(40):
								addDir('[COLOR chocolate]Phim Hoạt Hình[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'the-loai/phim-hoat-hinh/page-' + pagestr[i],5,logos + 'phim3s.png')
								i+=1
				if 'phim-kinh-di' in url:
						i=0
						for i in range(21):
								addDir('[COLOR cyan]Phim Kinh Dị[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'the-loai/phim-kinh-di/page-' + pagestr[i],5,logos + 'phim3s.png')
								i+=1
				if 'phim-phieu-luu' in url:
						i=0
						for i in range(22):
								addDir('[COLOR violet]Phim Phiêu Lưu[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'the-loai/phim-phieu-luu/page-' + pagestr[i],5,logos + 'phim3s.png')
								i+=1
				if 'phim-vien-tuong' in url:
						i=0
						for i in range(19):
								addDir('[COLOR gold]Phim Viễn Tưởng[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'the-loai/phim-vien-tuong/page-' + pagestr[i],5,logos + 'phim3s.png')
								i+=1
				if 'phim-vo-thuat' in url:
						i=0
						for i in range(20):
								addDir('[COLOR white]Phim Võ Thuật[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'the-loai/phim-vo-thuat/page-' + pagestr[i],5,logos + 'phim3s.png')
								i+=1
				if 'phim-tam-ly' in url:
						i=0
						for i in range(68):
								addDir('[COLOR silver]Phim Tâm Lý[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'the-loai/phim-tam-ly/page-' + pagestr[i],5,logos + 'phim3s.png')
								i+=1
				if 'phim-than-thoai' in url:
						i=0
						for i in range(4):
								addDir('[COLOR olive]Phim Thần Thoại[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'the-loai/phim-than-thoai/page-' + pagestr[i],5,logos + 'phim3s.png')
								i+=1
				if 'phim-tv-show' in url:
						i=0
						for i in range(18):
								addDir('[COLOR pink]Phim TV Show[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'the-loai/phim-tv-show/page-' + pagestr[i],5,logos + 'phim3s.png')
								i+=1
				if 'phim-anh' in url:
						i=0
						for i in range(2):
								addDir('[COLOR white]Phim Anh[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'quoc-gia/phim-anh/page-' + pagestr[i],5,logos + 'phim3s.png')
								i+=1
				if 'phim-an-do' in url:
						i=0
						for i in range(3):
								addDir('[COLOR gold]Phim Ấn Độ[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'quoc-gia/phim-an-do/page-' + pagestr[i],5,logos + 'phim3s.png')
								i+=1
				if 'phim-han-quoc' in url:
						i=0
						for i in range(19):
								addDir('[COLOR violet]Phim Hàn Quốc[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'quoc-gia/phim-han-quoc/page-' + pagestr[i],5,logos + 'phim3s.png')
								i+=1
				if 'phim-hong-kong' in url:
						i=0
						for i in range(13):
								addDir('[COLOR cyan]Phim Hồng Kông[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'quoc-gia/phim-hong-kong/page-' + pagestr[i],5,logos + 'phim3s.png')
								i+=1
				if 'phim-khac' in url:
						i=0
						for i in range(5):
								addDir('[COLOR chocolate]Phim Khác[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'quoc-gia/phim-khac/page-' + pagestr[i],5,logos + 'phim3s.png')
								i+=1
				if 'phim-my' in url:
						i=0
						for i in range(90):
								addDir('[COLOR tan]Phim Mỹ[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'quoc-gia/phim-my/page-' + pagestr[i],5,logos + 'phim3s.png')
								i+=1
				if 'phim-nhat-ban' in url:
						i=0
						for i in range(34):
								addDir('[COLOR magenta]Phim Nhật Bản[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'quoc-gia/phim-nhat-ban/page-' + pagestr[i],5,logos + 'phim3s.png')
								i+=1
				if 'phim-phap' in url:
						i=0
						for i in range(2):
								addDir('[COLOR blue]Phim Pháp[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'quoc-gia/phim-phap/page-' + pagestr[i],5,logos + 'phim3s.png')
								i+=1
				if 'phim-thai-lan' in url:
						i=0
						for i in range(3):
								addDir('[COLOR orange]Phim Thái Lan[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'quoc-gia/phim-thai-lan/page-' + pagestr[i],5,logos + 'phim3s.png')
								i+=1
				if 'phim-trung-quoc' in url:
						i=0
						for i in range(27):
								addDir('[COLOR lime]Phim Trung Quốc[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'quoc-gia/phim-trung-quoc/page-' + pagestr[i],5,logos + 'phim3s.png')
								i+=1
				if 'phim-viet-nam' in url:
						i=0
						for i in range(17):
								addDir('[COLOR yellow]Phim Việt Nam[/COLOR] - [COLOR lime]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'quoc-gia/phim-viet-nam/page-' + pagestr[i],5,logos + 'phim3s.png')
								i+=1
				if url==phim3s + 'danh-sach/phim-le':
						i=0
						for i in range(131):
								addDir('[COLOR lime]Toàn Bộ Phim Lẻ[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'danh-sach/phim-le/page-' + pagestr[i],5,logos + 'phim3s.png')
								i+=1
				if url==phim3s + 'danh-sach/phim-le/?year=2014':
						i=0
						for i in range(5):
								addDir('[COLOR silver]Phim Lẻ 2014[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'danh-sach/phim-le/page-' + pagestr[i] + '/?year=2014',5,logos + 'phim3s.png')
								i+=1
				if url==phim3s + 'danh-sach/phim-le/?year=2013':
						i=0
						for i in range(17):
								addDir('[COLOR violet]Phim Lẻ 2013[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'danh-sach/phim-le/page-' + pagestr[i] + '/?year=2013',5,logos + 'phim3s.png')
								i+=1
				if url==phim3s + 'danh-sach/phim-le/?year=2012':
						i=0
						for i in range(21):
								addDir('[COLOR cyan]Phim Lẻ 2012[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'danh-sach/phim-le/page-' + pagestr[i] + '/?year=2012',5,logos + 'phim3s.png')
								i+=1
				if url==phim3s + 'danh-sach/phim-bo':
						i=0
						for i in range(79):
								addDir('[COLOR lime]Toàn Bộ Phim Bộ[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'danh-sach/phim-bo/page-' + pagestr[i],5,logos + 'phim3s.png')
								i+=1
				if url==phim3s + 'danh-sach/phim-bo/?year=2014':
						i=0
						for i in range(4):
								addDir('[COLOR silver]Phim Bộ 2014[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'danh-sach/phim-bo/page-' + pagestr[i] + '/?year=2014',5,logos + 'phim3s.png')
								i+=1
				if url==phim3s + 'danh-sach/phim-bo/?year=2013':
						i=0
						for i in range(12):
								addDir('[COLOR violet]Phim Bộ 2013[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'danh-sach/phim-bo/page-' + pagestr[i] + '/?year=2013',5,logos + 'phim3s.png')
								i+=1
				if url==phim3s + 'danh-sach/phim-bo/?year=2012':
						i=0
						for i in range(22):
								addDir('[COLOR cyan]Phim Bộ 2012[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'danh-sach/phim-bo/page-' + pagestr[i] + '/?year=2012',5,logos + 'phim3s.png')
								i+=1						
				if url==phim3s + 'danh-sach/phim-chieu-rap':
						i=0
						for i in range(22):
								addDir('[COLOR lime]Toàn Bộ Phim Chiếu Rạp[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'danh-sach/phim-chieu-rap/page-' + pagestr[i],5,logos + 'phim3s.png')
								i+=1
				if url==phim3s + 'danh-sach/phim-chieu-rap/?year=2014':
						i=0
						for i in range(2):
								addDir('[COLOR silver]Phim Chiếu Rạp 2014[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'danh-sach/phim-chieu-rap/page-' + pagestr[i] + '/?year=2014',5,logos + 'phim3s.png')
								i+=1
				if url==phim3s + 'danh-sach/phim-chieu-rap/?year=2013':
						i=0
						for i in range(7):
								addDir('[COLOR violet]Phim Chiếu Rạp 2013[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'danh-sach/phim-chieu-rap/page-' + pagestr[i] + '/?year=2013',5,logos + 'phim3s.png')
								i+=1
				if url==phim3s + 'danh-sach/phim-chieu-rap/?year=2012':
						i=0
						for i in range(8):
								addDir('[COLOR cyan]Phim Chiếu Rạp 2012[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'danh-sach/phim-chieu-rap/page-' + pagestr[i] + '/?year=2012',5,logos + 'phim3s.png')
								i+=1
				if url==phim3s + 'danh-sach/phim-moi':
						i=0
						for i in range(209):
								addDir('[COLOR lime]Toàn Bộ Phim Mới[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'danh-sach/phim-moi/page-' + pagestr[i],5,logos + 'phim3s.png')
								i+=1
				if url==phim3s + 'danh-sach/phim-2014':
						i=0
						for i in range(9):
								addDir('[COLOR silver]Phim Mới 2014[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'danh-sach/phim-moi/page-' + pagestr[i] + '/?year=2014',5,logos + 'phim3s.png')
								i+=1
				if url==phim3s + 'danh-sach/phim-2013':
						i=0
						for i in range(28):
								addDir('[COLOR violet]Phim Mới 2013[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'danh-sach/phim-moi/page-' + pagestr[i] + '/?year=2013',5,logos + 'phim3s.png')
								i+=1
				if url==phim3s + 'danh-sach/phim-2012':
						i=0
						for i in range(43):
								addDir('[COLOR cyan]Phim Mới 2012[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'danh-sach/phim-moi/page-' + pagestr[i] + '/?year=2012',5,logos + 'phim3s.png')
								i+=1
				if 'phim-thuyet-minh' in url:
						i=0
						for i in range(48):
								addDir('[COLOR coral]Phim Thuyết Minh[/COLOR] - [COLOR yellow]Trang ' + pagestr[i] + '[/COLOR]',phim3s + 'danh-sach/phim-thuyet-minh/page-' + pagestr[i],5,logos + 'phim3s.png')
								i+=1
						
def index(url):
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
		response = urllib2.urlopen(req, timeout=90)
		link=response.read()
		response.close()
		if 'phim3s' in url:		
				match=re.compile("<div class=\"inner\"><a href=\"(.*?)\" title=\"([^\"]*)\"><img src=\"(.+?)\"").findall(link)
				for url,name,thumbnail in match:
						addDir('[COLOR yellow]' + name + '[/COLOR]',('%s%sxem-phim' % (phim3s, url)),6,thumbnail)					
		
def vlinks(url,name):
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
		response = urllib2.urlopen(req, timeout=90)
		link=response.read()
		response.close()
		if 'phim3s' in url:		
				thumbnail=re.compile("<meta property=\"og:image\" content=\"([^\"]*)\"").findall(link)		
				match=re.compile("a data-type=\"watch\" data-episode-id.+?href=\"([^\"]*)\" title=\"(.*?)\"").findall(link)
				for url,title in match:
						addLink(('%s   -   %s' % ('[COLOR lime]' + title + '[/COLOR]',name )),('%s%svideo.mp4' % (phim3s, url)),thumbnail[-1])
				
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