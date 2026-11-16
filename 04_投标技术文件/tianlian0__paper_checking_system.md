# tianlian0/paper_checking_system

- **仓库名**：tianlian0/paper_checking_system
- **原文链接**：https://github.com/tianlian0/paper_checking_system
- **Star 数**：520（取自 GitHub 搜索 API；本环境数值可能偏高，待核实）
- **最近更新时间**：2025-03-15T11:04:27Z
- **许可证**：GPL-2.0
- **语言**：C#
- **质量分 / 适配分 / 混合分**：69.4 / 48.7 / 60.1
- **结论**：REVIEW
- **标记**：STALE>1y
- **领域适配**：领域词:标书

## 用途摘要
基于C#和C++开发的文本查重/论文查重系统，一亿字次级论文库秒级查重。关联：查重算法、数据去重、文档查重、文本去重、标书查重、辅助防串标、作业查重、duplicate check

## 适配理由
✓ 命中任务词：标书；△ 未命中：施工/工组/组织/织设/设计/投标/标技/技术/术文/文件/书生/成相/相关/关工

## README 要点
﻿# 简体中文论文查重系统

#### 衍生软件及SDK
目前团队开发了JAVA版查重SDK，可深度集成到您的私有项目中  
使用示例：https://github.com/tianlian0/duplicate-check-sample  
目前已有多个商用查重系统基于此SDK开发上线。欢迎大家试用、反馈，希望它能帮助大家开发出自己应用场景下的查重系统。  
基于本项目，我们开发了付费衍生产品“标书查重”，标书查重软件基于标书查重场景提供更高的可靠性及相关技术支持  
试用链接：https://xincheck.com/?id=20  

#### 安装使用教程
1、clone源代码  
2、使用vs打开、编译（vs需安装.NET开发组件）  
3、运行paper_checking.exe文件即可  
兼容性要求：  
windows 7及以上，可用内存1.5GB以上。开发工具：vs2017及以上，需安装vc2015运行库和.NET Framework4.6。其它版本需自行测试。  
报错排除：  
1、如果Spire报错，可能是因为项目刚拉下来相关第三方包还未下载完毕，可等待vs自动下载或打开NuGet手动下载缺少的包。  
2、本项目已不提供32位操作系统支持，如您使用32位操作系统将无法使用本系统。  
3、为什么查重的结果永远是0？①这个系统是使用本地比对库进行纵向查重的，查重之前需要先添加本地比对库，不添加结果肯定是0。各位正在写论文或者作业的同学们，想给自己的论文查重请自行去各大查重平台购买，这个系统不适用没有本地比对库的用户。②添加比对库的时候必须使用比对库管理选项卡下的“添加到比对库”按钮进行添加，自己向文件夹中直接复制文件是不生效的，相当于没有添加比对库。  

#### 项目中包含了很多二进制DLL文件的说明
项目中使用了第三方开源组件PDFBOX和IKVM：  
IKVM已于2017年停止维护，现在使用NuGet可以引用的是5年前的IKVM，存在一些BUG，因此本项目没有通过NuGet直接引用IKVM，而是对IKVM的一些bug进行了修复以后，编译成了DLL文件提供到本项目中，这样大家就不用自己编译了，我修改后的IKVM的源码在我的GitHub主页也可以看到，需要源码的同学可以自行Clone。  
PdfBox只有Java版，C#中想要使用需要转成DLL，因此我是直接转好以后把二进制放到项目中的。有代码洁癖的用户可以自行去PdfBox官网下载jar包进行转换。  

#### 项目介绍与功能说明
该系统目前支持对简体中文的文件进行横向查重和纵向查重。  
两个核心功能点说明如下:  
1、纵向查重  
选择一批待查文件后，将该批文件和比对库中的文件比对。通常用以检查该批文件有没有复制比对库中的文本。  
2、横向查重  
选择一批待查文件后，在该批次文件之间进行比对，用以检查该批次文件有没有互相复制的情况。这个功能是目前主流查重平台支持度较差的。  

软件中涉及的其它功能点及名词说明如下：  
1、添加到比对库  
将文件添加到比对库中。这个功能是服务于纵向查重的，将文件通过这个功能添加到比对库中，在使用纵向查重功能的就可与比对库中的文件进行比对。需要选中存放文件的文件夹，然后点击“添加到比对库”按钮，按钮会变灰，等待按钮恢复正常即添加完毕。该过程需要耗费一定时间。  
2、查重阈值的设置  
该值的设置决定了待查文件连续多少个字与其它文件相同即判定为抄袭。推荐值为10至16，用户亦可根据实际情况自行设定为1至99之间的任意整数值。  
3、保存查重报告的文件夹  
选择一个文件夹，待查重完毕后查重报告将会输出到这个文件夹中。  
4、生成统计表  
查重结束后是否生成csv格式的统计表。  
5、中断恢复  
选中复选框，软件将不会清除上一次查重的结果继续查重。该复选框适用于应用程序中途意外退出，想从退出时的进度继续查重。  
6、关键词过滤  
将一些可能影响重复率的关键词添加到关键词过滤功能中，在查重时会将待查文本中出现的关键词全部删除，以避免它们对重复率的影响。这类关键词通常可能为学校名、机构名等。  
7、查重进程数  
该值的设置影响查重速度，默认为当前机器CPU逻辑核心数减2。  
8、格式转换线程数  
文件在查重前会进行格式转换，该值的设置影响文件格式转换的速度，默认为当前机器CPU逻辑核心数减2。  

注意事项：  
如果待查文件在比对库中存在，文件名相同会自动跳过比对，若文件名不相同，则会导致查重重复率高于90%的情况（相当于是两篇相同的文本进行比对，至于为什么不是100%后续有说明）。  

#### 查重原理说明
每两篇文件之间比对连续相同的字符串，超过查重阈值即认为这些字是重复的。但是，如果单篇文本重复率在0.25%以下或重复字数在30字以下，将不判定为重复。同时，如果一篇文本从其它文本复制了某句话很多次，只认为其中的一次为重复。  
文件格式转换使用了pdfbox和spire word free。  
文本格式化时会去掉文本中的摘要、目录、参考文献及非中文字符。  
生成的查重报告为rtf格式。  

#### 已知bug
极少量正常的pdf、word文件转换失败，如您发现此类文件，希望您通过issuse进行反馈并提供下载链接，十分感谢。  

#### 其它说明
1、现在我们已经开发了一套全新的支持多语言的web版查重系统，暂无开源计划，如有相关需求可以通过[商业合作]联系进行试用/定制开发。该系统中使用的核心查重模块已以SDK的形式开放使用（https://xincheck.com/?id=16 ）。  
2、该开源版本为一个简化版本，拥有查重所需的所有核心功能并输出一个较为简易的查重报告，有其它定制需求见[商业合作]。  

#### 项目截图
![image](https://github.com/tianlian0/paper_checking_system/blob/master/images/pic1.png)  
![image](https://github.com/tianlian0/paper_checking_system/blob/master/images/pic2.png)  
![image](https://github.com/tianlian0/paper_checking_system/blob/master/images/pic3.png)  
项目运行演示视频：链接：https://pan.baidu.com/s/1VM9g4CT4nAwlZXOHePkoXQ 提取码：t059  
PS：截图的查重报告为商用版，开源版的报告内容没这个丰富。商用版和开源版的安装包均可在右侧的Release中下载。  

#### 反馈交流群&捐助
![image](https://github.com/tianlian0/paper_checking_system/blob/master/images/shang.png)  
欢迎各位免费、付费用户进入反馈交流QQ群：778041438；欢迎捐助本项目。  

#### 商业合作
本项目遵守GPL2协议，同时本项目已申请三项软件著作权  
本项目可以提供c#/java版本的技术支持。欢迎各企业、高校、机构合作。商业合作专用微信/QQ：654062779。添加好友烦请备注公司名称；个人项目合作可备注您的姓氏。非商业合作以及无购买需求的用户可加入上方的反馈交流QQ群。  
可合作应用场景：高校论文查重、标书查重、辅助防串标、项目申报书查重、企业内部文档查重、舆情数据去重、学生作业查重等  


## 核心代码片段（来源：LICENSE）
```c#
﻿                    GNU GENERAL PUBLIC LICENSE
                       Version 2, June 1991

 Copyright (C) 1989, 1991 Free Software Foundation, Inc.,
 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The licenses for most software are designed to take away your
freedom to share and change it.  By contrast, the GNU General Public
License is intended to guarantee your freedom to share and change free
software--to make sure the software is free for all its users.  This
General Public License applies to most of the Free Software
Foundation's software and to any other program whose authors commit to
using it.  (Some other Free Software Foundation software is covered by
the GNU Lesser General Public License instead.)  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
this service if you wish), that you receive source code or can get it
if you want it, that you can change the software or use pieces of it
in new free programs; and that you know you can do these things.

  To protect your rights, we need to make restrictions that forbid
anyone to deny you these rights or to ask you to surrender the rights.
These restrictions translate to certain responsibilities for you if you
distribute copies of the software, or if you modify it.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must give the recipients all the rights that
you have.  You must make sure that they, too, receive or can get the
source code.  And you must show them these terms so they know their
rights.

  We protect your rights with two steps: (1) copyright the software, and
(2) offer you this license which gives you legal permission to copy,
distribute and/or modify the software.

  Also, for each author's protection and ours, we want to make certain
that everyone understands that there is no warranty for this free
software.  If the software is modified by someone else and passed on, we
want its recipients to know that what they have is not the original, so
that any problems introduced by others will not reflect on the original
authors' reputations.

  Finally, any free program is threatened constantly by software
patents.  We wish to avoid the danger that redistributors of a free
program will individually obtain patent licenses, in effect making the
program proprietary.  To prevent this, we have made it clear that any
patent must be licensed for everyone's free use or not licensed at all.

  The precise terms and conditions for copying, distribution and
modification follow.

                    GNU GENERAL PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. This License applies to any program or other work which contains
a notice placed by the copyright holder saying it may be distributed
under the terms of this General Public License.  The "Program", below,
refers to any such program or work, and a "work based on the Program"
means either the Program or any derivative work under copyright law:
that is to say, a work containing the Program or a portion of it,
either verbatim or with modifications and/or translated into another
language.  (Hereinafter, translation is included without limitation in
the term "modification".)  Each licensee is addressed as "you".

Activities other than copying, distribution and modification are not
covered by this License; they are outside its scope.  The act of
running the Program is not restricted, and the output from the Program
is covered only if its contents constitute a work based on the
Program (independent of having been made by running the Program).
Whether that is true depends on what t
...（截断，原文见链接）
```
