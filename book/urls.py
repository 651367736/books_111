from django.conf.urls import url
from . import views

urlpatterns = [
    # 首页跳转的页面
    url(r'^$', views.indexview),
    # 排行榜的页面
    url(r'^borrowbooktop/', views.borrowbooktopview),
    # 所有图书的页面
    url(r'^allbook$', views.allbookview),
    # 登录页面页面
    url(r'^login/', views.loginview),
    # 个人信息页面
    url(r'^myinfo/', views.myinfoview),
    # 查找图书页面
    url(r'^findbook/', views.findbookview),
    # 借书页面
    url(r'^borrowbook/', views.borrowbookview),
    # 还书页面
    url(r'^returnbook/', views.returnbookview),
    # 修改个人信息页面
    url(r'^changemyinfo/', views.changemyinfoview),
    # 逾期惩罚页面
    url(r'^punish/', views.punishview),
    # 所有图书页面（一刷新跳转的就是这个，前面的路由是info.html 没找到这个路由在哪，反正如果想改变一刷新页面就出来的东西，就在这个歌页面修改就OK了）
    url(r'^info.html/', views.allbookview),
    # 儿童专区页面
    url(r'^kids/', views.kidsview),
    # 教育专区域页面
    url(r'^education/', views.educationview),
    # 生活专区页面
    url(r'^life/', views.lifeview),
    # 科技专区页面
    url(r'^science/', views.scienceview),
    # 心愿单页面
    url(r'^wish_list/', views.wish_listview),
    # 关于我们 页面
    url(r'^about_our/', views.about_ourview),

]