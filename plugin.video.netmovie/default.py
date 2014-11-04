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
anhtrang = 'http://phim.anhtrang.org/'
m_anhtrang = 'http://m.anhtrang.org/'
hd_caphe='http://phim.hdcaphe.com/'
phim3s='http://phim3s.net/'
dchd='http://dangcaphd.com/'
pgt='http://phimgiaitri.vn/'
fptplay='http://fptplay.net/'
zui='http://zui.vn/'

def makeRequest(url):
  try:
    req=urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0')
    response=urllib2.urlopen(req, timeout=120)
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
  addDir('[COLOR yellow]phim3s.net[/COLOR]',phim3s,2,logos+'phim3s_1.png')
  addDir('[COLOR lime]dangcaphd.com[/COLOR]',dchd,2,logos+'dchd_1.png')
  addDir('[COLOR lightblue]hdcaphe[/COLOR]',hd_caphe,2,logos+'hdcaphe.png')
  addDir('[COLOR orange]anhtrang.org[/COLOR]',anhtrang,2,logos+'anhtrang.png')  
  addDir('[COLOR cyan]phimgiaitri.vn[/COLOR]',pgt,5,logos+'pgt.png')   
  addDir('[COLOR magenta]fptplay.net[/COLOR]',fptplay,2,logos+'fptplay.png')
  addDir('[COLOR lightgreen]zui.vn[/COLOR]',zui,2,logos+'zui.png')   

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
  if 'fptplay' in name:
    try:
      keyb=xbmc.Keyboard('', '[COLOR lime]Enter search text[/COLOR]')
      keyb.doModal()
      if (keyb.isConfirmed()):
        searchText=urllib.quote_plus(keyb.getText())
      url=fptplay+'Search/'+searchText
      mediaList(url)
    except: pass
  if 'zui' in name:
    try:
      keyb=xbmc.Keyboard('', '[COLOR yellow]Enter search text[/COLOR]')
      keyb.doModal()
      if (keyb.isConfirmed()):
	    searchText=urllib.quote_plus(keyb.getText())
      url='http://zui.vn/tim-kiem-nc/'+searchText+'.html'
      mediaList(url)
    except: pass
  if 'hdcaphe' in name:		
    try:
      keyb=xbmc.Keyboard('', '[COLOR yellow]Enter search text[/COLOR]')
      keyb.doModal()
      if (keyb.isConfirmed()):
        searchText=urllib.quote_plus(keyb.getText())
      url=hd_caphe+'search-result.html?keywords='+searchText
      mediaList(url)
    except: pass	
  if 'anhtrang' in name:		
    try:
      keyb=xbmc.Keyboard('', '[COLOR yellow]Enter search text[/COLOR]')
      keyb.doModal()
      if (keyb.isConfirmed()):
        searchText=urllib.quote_plus(keyb.getText())
      url=anhtrang+'tim-kiem='+searchText+'.html'
      mediaList(url)
    except: pass	
	
def categories(url):
  content=makeRequest(url)
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
  if 'fptplay' in url:
    addDir('[COLOR lime]fptplay[/COLOR][B]   [COLOR lime]>[/COLOR][COLOR orange]>[/COLOR][COLOR blue]>[/COLOR][COLOR magenta]>[/COLOR]   [/B][COLOR lime]Tìm Video[/COLOR]',fptplay,1,logos+'fptplay.png')
    match=re.compile("<li ><a href=\"(.+?)\" class=\".+?\">(.+?)<\/a><\/li>").findall(content)
    for url,name in match:
      if 'livetv' in url:
        pass
      else:
        addDir('[COLOR magenta]'+name+'[/COLOR]',fptplay+url,6,logos+'fptplay.png')	
  if 'zui' in url:
    addDir('[COLOR magenta]zui[/COLOR][B]   [COLOR lime]>[/COLOR][COLOR orange]>[/COLOR][COLOR blue]>[/COLOR][COLOR magenta]>[/COLOR]   [/B][COLOR magenta]Tìm Phim[/COLOR]',zui,1,logos+'zui.png') 
    match=re.compile("<li><a title=\".+?\" href=\"([^\"]*)\">([^>]+)<\/a><\/li>").findall(content)[0:3]
    for url,name in match:
      addDir('[COLOR yellow]'+name+'[/COLOR]',url,7,logos+'zui.png')	  
    match=re.compile("<li><a href='([^']*)'><b class=\"larrow\"><\/b>(.+?)<\/a><\/li>").findall(content)[0:17]
    for url,name in match:
      addDir('[COLOR lime]'+name+'[/COLOR]',url,7,logos+'zui.png')
    match=re.compile('<li><a href=\'([^\']*)\'><b class="larrow"><\/b>([^>]*)<\/a><\/li>').findall(content)[17:28]
    for url,name in match:
      addDir('[COLOR cyan]'+name+'[/COLOR]',url,7,logos+'zui.png')
    match=re.compile('<li><a href=\'([^\']*)\' style=.+?<\/b>(\d+)<\/a><\/li>').findall(content)
    for url,name in match:
      addDir('[COLOR lightgreen]'+name+'[/COLOR]',url,7,logos+'zui.png')	
  if 'hdcaphe' in url:
    addDir('[COLOR yellow]hdcaphe[/COLOR][B]   [COLOR lime]>[/COLOR][COLOR orange]>[/COLOR][COLOR blue]>[/COLOR][COLOR magenta]>[/COLOR]   [/B][COLOR yellow]Tìm Phim[/COLOR]',hd_caphe,1,logos+'hdcaphe.png')
    addDir('[COLOR lime]Phim Xem Nhiều[/COLOR]',hd_caphe+'phim-xem-nhieu-nhat.html',7,logos+'hdcaphe.png')
    addDir('[COLOR lightblue]Phim Mới[/COLOR]',hd_caphe+'phim-moi-nhat.html',7,logos+'hdcaphe.png')
    addDir('[COLOR orange]Phim Hot[/COLOR]',hd_caphe+'phim-hot-trong-thang.html',7,logos+'hdcaphe.png')
    addDir('[COLOR blue]Phim Full HD[/COLOR]',hd_caphe+'PHIM_HD.html',7,logos+'hdcaphe.png')
    addDir('[COLOR magenta]Phim Hành Động Châu Á[/COLOR]',hd_caphe+'hanh-dong-chau-a.html',7,logos+'hdcaphe.png')
    addDir('[COLOR magenta]Phim Hành Động Mỹ[/COLOR]',hd_caphe+'hanh-dng-m-56.html',7,logos+'hdcaphe.png')		
    addDir('[COLOR tan]Phim Kinh Dị Châu Á[/COLOR]',hd_caphe+'kinh-d-ma-chau-a-52.html',7,logos+'hdcaphe.png')
    addDir('[COLOR tan]Phim Kinh Dị Mỹ[/COLOR]',hd_caphe+'kinh-d-ma-chau-a.html',7,logos+'hdcaphe.png')		
    addDir('[COLOR chocolate]Phim Tình Cảm Châu Á[/COLOR]',hd_caphe+'phim-chau-a.html',7,logos+'hdcaphe.png')
    addDir('[COLOR chocolate]Phim Tình Cảm Mỹ[/COLOR]',hd_caphe+'phim-chau-au.html',7,logos+'hdcaphe.png')
    addDir('[COLOR cyan]Phim Bộ Châu Á[/COLOR]',hd_caphe+'PHIM_BO_HD.html',7,logos+'hdcaphe.png')
    addDir('[COLOR cyan]Phim Bộ Mỹ[/COLOR]',hd_caphe+'phim-b-m.html',7,logos+'hdcaphe.png')		
    addDir('[COLOR violet]Phim Hoạt Hình[/COLOR]',hd_caphe+'PHIM_HD_IPHONE_MAY_TINH_BANG_TABLET.html',7,logos+'hdcaphe.png')
  if 'anhtrang' in url:  
    addDir('[COLOR yellow]anhtrang[/COLOR][B]   [COLOR lime]>[/COLOR][COLOR cyan]>[/COLOR][COLOR orange]>[/COLOR][COLOR magenta]>[/COLOR]   [/B][COLOR yellow]Tìm Phim[/COLOR]',anhtrang,1,logos + 'anhtrang.png')
    content = makeRequest(anhtrang)
    match = re.compile("<a class=\"link\" href=\"([^\"]*)\" >\s*<span>(.+?)<\/span>").findall(content)
    for url,name in match:
      addDir('[COLOR lime]' + name + '[/COLOR]',url,7,logos + 'anhtrang.png')  
    match = re.compile("<a class=\"link\" href=\"([^\"]+)\">\s*<span>(.+?)<\/span>").findall(content)[0:7]
    for url,name in match:
      addDir('[COLOR cyan]' + name + '[/COLOR]',url,7,logos + 'anhtrang.png')
    match = re.compile("<a class=\"link\" href=\"([^\"]+)\">\s*<span>(.+?)<\/span>").findall(content)[7:19]
    for url,name in match:
      addDir('[COLOR orange]' + name + '[/COLOR]',url,7,logos + 'anhtrang.png')	
    match = re.compile('<li class="item27">\s*<a class="topdaddy link" href="([^"]*)">\s*<span>(.+?)<\/span>').findall(content)
    for url,name in match:
      addDir('[COLOR magenta]' + name + '[/COLOR]',url,7,logos + 'anhtrang.png') 
    match = re.compile('<li class="item28">\s*<a class="topdaddy link" href="(.+?)">\s*<span>(.+?)<\/span>').findall(content)
    for url,name in match:
      addDir('[COLOR lightblue]' + name + '[/COLOR]',url,7,logos + 'anhtrang.png') 
  
def index(url):
  content=makeRequest(url)
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
      addDir('[COLOR lime]Trang '+name+'[/COLOR]',pgt+url.replace(' ','%20'),3,logos+'pgt.png')					
 
def videoLinks(url,name):
  content=makeRequest(url)
  thumbnail=re.compile("<meta property=\"og:image\" content=\"([^\"]*)\"").findall(content)[0]		
  match=re.compile("a data-type=\"watch\" data-episode-id.+?href=\"([^\"]*)\" title=\"(.*?)\"").findall(content)
  for url,title in match:
    addLink(('%s   -   %s' % ('[COLOR lime]'+title+'[/COLOR]',name )),('%s%svideo.mp4' % (phim3s, url)),thumbnail)
	
def pgtri():
  #addDir('[COLOR cyan]Phimgiaitri[/COLOR]',pgt,5,logos+'pgt.png')
  content=makeRequest(url)
  match=re.compile('<li class="has-sub"><a href=\'#\'><span>(.+?)<\/span><\/a>').findall(content)[0]  
  addDir('[COLOR yellow]'+match+'[/COLOR]',pgt,2,logos+'pgt.png')			
  match=re.compile('<li class="has-sub"><a href=\'#\'><span>(.+?)<\/span><\/a>').findall(content)[1]		
  addDir('[COLOR lime]'+match+'[/COLOR]',pgt,6,logos+'pgt.png')	
 
def dirs(url):
  content=makeRequest(url) 
  if 'phimgiaitri' in url:
    addDir('[COLOR yellow]phimgiatri[/COLOR][B]   [COLOR lime]>[/COLOR][COLOR orange]>[/COLOR][COLOR blue]>[/COLOR][COLOR magenta]>[/COLOR]   [/B][COLOR yellow]Tìm Phim Bộ[/COLOR]',pgt,9,logos+'pgt.png')
    match=re.compile('<a href=\'result.php\?type=Phim Bộ(.+?)\'><span>(.+?)<\/span>').findall(content) 
    for url,name in match:
      addDir('[COLOR lime]'+name+'[/COLOR]',pgt+'result.php?type=Phim%20B%E1%BB%99'+url.replace(' ','%20'),7,logos+'pgt.png')
  if 'fptplay' in url:
    match=re.compile("<h3><a href=\"(.+?)\">(.+?)<\/a><\/h3>").findall(content)
    for url,name in match:	
      addDir('[COLOR yellow]'+name+'[/COLOR]',fptplay+url,7,logos+'fptplay.png')
	  
def mediaList(url):
  content=makeRequest(url)
  if 'phimgiaitri' in url:  
    match=re.compile('href=\'([^\']*).html\'>\s*<img style=.+?src=(.+?) ><div class=\'text\'>\s*<p>.+?<\/p>\s*<\/div>.+?>([^<]*)\s*<\/').findall(content)
    for url,thumbnail,name in match:
      addDir('[COLOR lime]'+name+'[/COLOR]',pgt+url+'/Tap-1.html',8,pgt+thumbnail)				
    match=re.compile("<a  href='(.+?)'>(\d+)  <\/a>").findall(content)
    for url,name in match:
      addDir('[COLOR yellow]Trang '+name+'[/COLOR]',pgt+url.replace(' ','%20'),7,logos+'pgt.png')
  if 'fptplay' in url:
    match=re.compile("<div class=\"col\">\s*<a href=\"([^\"]+)\">\s*<img src=\"([^\"]*)\" alt=\"(.+?)\"").findall(content)
    for url,thumbnail,name in match:	
      addDir('[COLOR lime]'+name.replace('&amp;','[COLOR cyan]và[/COLOR]')+'[/COLOR]',fptplay+url,8,thumbnail)
    match=re.compile("<li><a href=\"(.+?)\">(\d+)<\/a><\/li>").findall(content)
    for url,name in match:	
      addDir('[COLOR yellow]Trang '+name+'[/COLOR]',fptplay+url,7,logos+'fptplay.png')
  if 'zui' in url:
    match=re.compile('<a data-tooltip=".+?" href="(.+?)" title="(.+?)".+?>\s*<img src="(.+?)"').findall(content)
    if 'phim-bo' in url:
      for url,name,thumbnail in match:
        addDir('[COLOR yellow]'+name+'[/COLOR]',url,8,thumbnail)
      match=re.compile("<a href=\"([^\"]*)\" title='.+?'>([^>]*)<\/a><\/li>").findall(content)
      for url,name in match:
        addDir('[COLOR lime]Trang '+name.replace('&laquo;','[COLOR cyan]Kế Trước[/COLOR]').replace(' &raquo;','[COLOR magenta]Kế Tiếp[/COLOR]')+'[/COLOR]',url,7,logos+'zui.png')	  
    else:
      for url,name,thumbnail in match:
        add_Link('[COLOR yellow]'+name+'[/COLOR]',url,thumbnail)
      match=re.compile("<a href=\"([^\"]+)\" title='.+?'>([^>]*)<\/a><\/li>").findall(content)
      for url,name in match:
        addDir('[COLOR lime]Trang '+name.replace('&laquo;','[COLOR cyan]Kế Trước[/COLOR]').replace(' &raquo;','[COLOR magenta]Kế Tiếp[/COLOR]')+'[/COLOR]',url,7,logos+'zui.png')
  if 'hdcaphe' in url:
    match=re.compile("a style=\"position: relative;display: block;\" href=\"(.+?)\">\s*<img class=\"imgborder\" width=\"165\" src=\"(.+?)\"").findall(content)		
    for url,thumbnail in match:
      addDir('[COLOR lime][UPPERCASE]'+url.replace('detail/movies/','').replace('-',' ').replace('.html','')+'[/UPPERCASE][/COLOR]',hd_caphe+url.replace('detail','video').replace('.html','/play/clip_1.html'),8,hd_caphe+thumbnail)
    match=re.compile("<span class=\"next\"><a href=\"(.+?)\" class=\"next\" title=\"(.+?)\">").findall(content)
    for url,name in match:	
      addDir('[COLOR yellow]'+name.replace('Go to page','Trang')+' >>>>[/COLOR]',hd_caphe+url,7,logos+'hdcaphe.png')
    match=re.compile("<span class=\"last\"><a href=\"(.+?)\" class=\"last\" title=\"(.+?)\">").findall(content)
    for url,name in match:	
      addDir('[COLOR yellow]'+name.replace('Go to page','Trang')+'[/COLOR][COLOR cyan][B] = [/B][/COLOR][COLOR red]Trang cuối cùng >>>>[/COLOR]',hd_caphe+url,7,logos+'hdcaphe.png')
  if 'anhtrang' in url:
    match = re.compile("<a href=\"([^\"]*)\" title=\"([^\"]+)\"><img src=\"(.+?)\"").findall(content)		
    for url,name,thumbnail in match:
      addDir('[COLOR yellow]' + name + '[/COLOR]',url.replace(anhtrang,m_anhtrang),8,thumbnail)
    match = re.compile("<a class=\"pagelink\" href=\"(.+?)\">(.+?)<\/a>").findall(content)
    for url,name in match:	
      addDir('[COLOR lime]Trang ' + name + '[COLOR cyan] >>>>[/COLOR]',url,7,logos + 'anhtrang.png')
    match = re.compile("<a class=\"pagelast\" href=\"([^\"]*)\">(.+?)<\/a>").findall(content)
    for url,name in match:	
      addDir('[COLOR red]Trang ' + name.replace('Cuối','[COLOR red]Cuối[COLOR magenta] >>>>[/COLOR]') + '[/COLOR]',url,7,logos + 'anhtrang.png')
   
def episodes(url,name):
  content=makeRequest(url)
  if 'phimgiaitri' in url:    
    thumbnail=re.compile("<meta property=\"og:image\" content=\"(.+?)\"").findall(content)
    get_Link('[COLOR yellow]Tập 1  -  [/COLOR]'+name,url,thumbnail[0])
    match=re.compile("<a href=\"(.+?)\" page=(\d+)>").findall(content)
    for url,title in match:
      get_Link('[COLOR yellow]Tập '+title+'  -  '+name+'[/COLOR]',url,thumbnail[0])
  if 'fptplay' in url:
    title=re.compile('<title>([^\']+)</title>').findall(content)		
    match=re.compile("<a href=\"\/Video([^\"]*)\">(.*?)<\/a><\/li>").findall(content)
    for url,name in match:
      add_Link(('%s   -   %s' % ('[COLOR lime]Tập '+name+'[/COLOR]','[COLOR yellow]'+title[-1].replace('&amp;','[COLOR cyan]và[/COLOR]')+'[/COLOR]')),('%sVideo%s' % (fptplay, url)),logos+'fptplay.png')
  if 'zui' in url:
    thumbnail=re.compile("<meta property=\"og:image\" content=\"(.+?)\"").findall(content)[0]		
    match=re.compile('<a id=\'.+?\' href=\'(.+?)\'  >(.+?)<\/a><\/li>').findall(content)
    for url,episode in match:
      add_Link(('%s   -   %s' % ('[COLOR lime]Tập '+episode+'[/COLOR]',name )),zui+url,'http://vncdn.zui.vn'+thumbnail)					
  if 'hdcaphe' in url:
    add_Link(name,url,logos+'hdcaphe.png')  
    match=re.compile("<a style=\"margin-left:10px\" href=\"(.+?)\"  >(\d+)<\/a>").findall(content)
    for url,title in match:
      add_Link('[COLOR yellow]Tập '+title+'[/COLOR]',hd_caphe+url,logos+'hdcaphe.png')  
  if 'anhtrang' in url:
    add_Link('[COLOR lime]Tập 1' + '[COLOR cyan][B]  -  [/B][/COLOR]'+name,url,logos + 'anhtrang.png')
    match = re.compile('<a href="(.+?)" class="ep">(.+?)<\/a>').findall(content)
    for url,title in match:
      add_Link('[COLOR lime]Tập ' + title + '[COLOR cyan][B]  -  [/B][/COLOR]' + name,url,logos + 'anhtrang.png')   
  
def inquiry():
  try:
    keyb=xbmc.Keyboard('', '[COLOR lime]Enter search text[/COLOR]')
    keyb.doModal()
    if (keyb.isConfirmed()):
      searchText=urllib.quote_plus(keyb.getText())
    url=pgt+'result.php?type=search&keywords='+searchText
    mediaList(url)
  except: pass
	  
def resolveUrl(url):
  content=makeRequest(url)
  if 'dangcaphd' in url:
    try:	
	  mediaUrl=re.compile('<a _episode="1" _link="(.+?)_\d_\d+.mp4"').findall(content)[0]+'.mp4'
    except:		
	  mediaUrl=re.compile('<a _episode="1" _link="(.+?)"').findall(content)[0]
  if 'phimgiaitri' in url:	
    mediaUrl='http://phimgiaitri.vn/phimtv/phimle'+re.compile('file: "rtmpe:.+?phimle(.+?)"').findall(content)[0]
  if 'fptplay' in url:
	mediaUrl=re.compile('"<source src=\'([^\']*)\'').findall(content)[0] 
  if 'zui' in url:
    mediaUrl='rtmp'+re.compile("'rtmp(.+?)'").findall(content)[0]#+'/playlist.m3u8'
  if 'hdcaphe' in url:	
    mediaUrl=re.compile('\'http.startparam\':\'start\',\s*file: \'(.+?)\'').findall(content)[0].replace(' ','%20')	
  if 'anhtrang' in url:
    try:
      mediaUrl = re.compile("<source src=\"([^\"]*)\"").findall(content)[0]
    except: 
      mediaUrl = re.compile("var video_src_mv=\"(.+?)\"").findall(content)[0]   
  item=xbmcgui.ListItem(path=mediaUrl)
  xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)	  
  return

def urlResolver(url):
  content=makeRequest(url)
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
   
def get_Link(name,url,iconimage):
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
  main()

elif mode==1:
  search()
		
elif mode==2:
  categories(url)
				
elif mode==3:
  index(url)
        
elif mode==4:
  videoLinks(url,name)

elif mode==5:
  pgtri()
  
elif mode==6:
  dirs(url)
  
elif mode==7:
  mediaList(url)
  
elif mode==8:
  episodes(url,name)
  
elif mode==9:
  inquiry()
 
elif mode==10:
  resolveUrl(url)

elif mode==11:
  urlResolver(url) 
  
xbmcplugin.endOfDirectory(int(sys.argv[1]))