# coding=utf-8
code='''<div class="row row-center">
    <div class="col-sm-4">
        <h3><a href="http://bbs.crossincode.com">交流论坛</a></h3>
        <p>编程学习的讨论社区。在这里可以讨论代码问题、交流学习心得、分享你的代码或者网上的优质内容。也欢迎学习之余来灌水。</p>
    </div>
    <div class="col-sm-4">
        <h3><a href="http://crossincode.com/home/">学习资源</a></h3>
        <p>这里有编程教室的系列教程、在线Python练习题，可以签到打卡，记录你的学习进度，还有我们搜集的优秀文章和资源导航。</p>
    </div>
    <div class="col-sm-4">
        <h3><a href="http://crossincode.com/vip/">码上行动</a></h3>
        <p>编程教室团队精心设计的入门教程，包括视频课程、在线习题、常见问答、编程实例等，我们的助教会在专属QQ群中为你答疑。</p>
    </div>
</div>'''
from bs4 import BeautifulSoup
soup=BeautifulSoup(code,'html.parser')
