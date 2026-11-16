# 3xxx/engineercms

- **仓库名**：3xxx/engineercms
- **原文链接**：https://github.com/3xxx/engineercms
- **Star 数**：1424（取自 GitHub 搜索 API；本环境数值可能偏高，待核实）
- **最近更新时间**：2026-10-04T14:17:09Z
- **许可证**：Apache-2.0
- **语言**：Go
- **质量分 / 适配分 / 混合分**：89.2 / 64.4 / 78.0
- **结论**：ADOPT
- **标记**：无
- **领域适配**：领域词:engineer/cms

## 用途摘要
工程师知识管理系统：基于golang语言（beego框架），支持分布式文件存储minio集群部署。engineercms为土木工程师基于web的知识管理系统。管理个人、工程项目资料，业主—设计—监理—施工方均从平台获得资料。支持提取码分享文件、onlyoffice实时文档协作，在线利用mindoc创作你的书籍，阅览PDF文件。手机端配套小程序，微信搜索“设计与管理”即可呼出小程序。

## 适配理由
✓ 命中任务词：工程/资料/管理/项目/文档/系统；△ 未命中：程资/料管/目文/档归/归档/档相/相关/关的/的开/开源/源系

## README 要点
## EngineerCMS
————工程师知识管理系统

[![License](https://img.shields.io/hexpm/l/plug.svg)](LICENSE) [![Build Status](https://travis-ci.org/3xxx/engineercms.svg?branch=master)](https://travis-ci.org/3xxx/engineercms) [![GoDoc](https://godoc.org/github.com/3xxx/engineercms?status.svg)](https://godoc.org/github.com/3xxx/engineercms)
<img src="https://img.shields.io/liberapay/gives/~1861683.svg?logo=liberapay">

[Demo](https://www.zsj123.net/)
——基于engineercms的设代资料管理平台（真实应用环境）

```bash
# linux
# /root/gocode/src/github.com/3xxx/engineercms编译
# /usr/src/engineercms运行
# /root/gocode/src/github.com/3xxx/engineercms/vendor下载的包
# 1.更新包：go mod vendor
# 2.改名go-pay的utils里的slice.go为slice.go.back
# 3. bee run -gendoc=true -downdoc=true

# go mod使用
# https://www.jianshu.com/p/760c97ff644c

# 克隆源码
# git clone https://github.com/3xxx/engineercms.git
# go run main.go
# go包自动安装
# 设置go代理
# go env -w GO111MODULE=on
# go env -w GOPROXY=https://goproxy.io,direct

# 升级某个依赖
# 无需 clone 仓库中的代码，直接在项目目录中执行
# go get -u github.com/wechatpay-apiv3/wechatpay-go
# 来升级/添加依赖，自动完成 go.mod 修改与依赖的下载。
# 由于go.sum未更新，则运行go mod tidy更新go.sum文件

# 初始化mod：
# go mod init

# 代码中有新的库加入，需要更新mod：
# go mod tidy——下载新增的依赖包
# go mod vendor——更新

# 将新增的依赖包自动写入当前项目的 vendor 目录：
# go mod vendor
# 如果 go.mod 发生变化，应当重新执行 go mod vendor！
# 执行go mod vendor将删除项目中已存在的vendor目录；
# 永远不要对vendor中的依赖库进行二次修改、更改！
# go命令不检查vendor中的依赖库是否被修改
# 关闭——这个看情况，go mod vendor时，提示Get https://sum.golang.org/lookup/xxxxxx: dial tcp 216.58.200.49:443: i/o timeout
# go env -w GOSUMDB=off
```

```bash
# linux系统上编译：拷贝go.mod go.sum 以及其他文件，然后执行go mod vendor，

# 再执行bee generate docs
# bee generate routers
# 再执行bee run -gendoc=true -downdoc=true

# 编译(sqlite需要CGO支持)
# go build -ldflags "-w"
# 数据库初始化(此步骤执行之前，需配置`conf/app.conf`)
# ./engineercms install

# linux上升级，先杀死engineercms.exe进程，再拷贝新的engineercms.exe执行文件和路由swagger文件：
# killall engineercms
# 拷贝engineercms和swagger里的swagger.yml和swagger.json到服务器上对应文件夹里
# $ chmod +x engineercms 
# $ nohup ./engineercms &
# $ systemctl stop firewalld.service // 关闭防火墙
```

```bash
# beego 2.0.0 升级指南
# 获取最新版本的 bee 工具 go install github.com/beego/bee/v2@latest
# 更新 beego 框架 go get -u github.com/beego/beego/v2
# 然后进入项目，执行: bee fix -t 2
# 需要注意的是，如果你是 windows 用户，那么你需要在 WSL 内部运行该命令。
# 在项目文件夹下鼠标右键——Git Bash Here
# 这里需要导入的包是
# github.com/beego/beego/v2/server/web/context
# 而不是
# ~ github.com/beego/beego/v2/adapter/context ~
# 目前来说因为你所有的包都切换过去了beego/beego/v2，所以你对应的context要使用beego/beego/v2/server/web/context下的这个。
# 我教你一个小技巧。当你发现依赖找不到的时候，你把import里面对应的东西删掉，IDE会帮你补全，或者给你提示。如果你用的GOLANG IDE，那么会自动帮你把对应依赖引入。

# 记住一个核心原则：如果你用的是adapter的包，那么所有的包都应该是adapter的；如果你用的是beego/beego/v2（非adapter)，那么所有的都应该是beego/beego/v2下的。

# 手动执行 bee generate routers 重新生成commentsRouter_controllers.go，新版本删除了自动生成功能
# bee run -gendoc=true -downdoc=true

# go get 是拉取远程包的命令，还是继续使用的
# go install 是对项目进行编译并自动拉取所需包并生成 可执行文件的。

# 解决步骤：
# 1 go get -u github.com/beego/bee/v2
# 2 cd 到这个bee/v2版本中
# 3 go mod tidy 整理一下
# 4 go install
# 此时在 GOPATH目录bin文件夹下生成了bee.exe 。
# 测试 ./bee.exe new hello 已正常创建项目，自己将bin目录加入到全局即可。
```

```bash
# https://www.cnblogs.com/cqlb/p/13396107.html
# 一、创建标签
# 在Git中打标签非常简单，首先，切换到需要打标签的分支上：

# 要在engineercms文件夹下，鼠标右键，用“git bash here”来启动git，然后执行以下命令。
# 1 $ git branch
# 2 * dev
# 3   master
# 4 $ git checkout master
# 5 Switched to branch 'master'
# git add .
# git commit -m "update"
# 然后，敲命令git tag <tagname> 就可以打一个新标签：

# $ git tag v2.0.5
# 因为创建的标签都只存储在本地，不会自动推送到远程。所以，打错的标签可以在本地安全删除。
# 如果要推送某个标签到远程，使用命令
# git push --tags
# $ git push origin <tagname>

# git add .
# git commit -m "message"
# git push origin master
# 只不过20年10月之后的版本master一词都改成了main
```

```bash
#  /d/engineercms (master|REBASE-i)
# $ git push --delete origin v2.0.0
# To https://github.com/3xxx/engineercms
#  - [deleted]         v2.0.0

#  /d/engineercms (master|REBASE-i)
# $ git push --delete origin v2.0.2
# To https://github.com/3xxx/engineercms
#  - [deleted]         v2.0.2
# 如果有人想知道如何一次删除多个标签，你可以用空格简单地列出它们，例如git push --delete origin tag1 tag2。本地标签删除git tag -d tag1 tag2同样有效。
```

```bash
# 升级gorm——进入Git cmd
# D:\gowork\src\github.com\3xxx\engineercms>go get gorm.io/gorm
# go: downloading gorm.io/gorm v1.25.12
# go: upgraded gorm.io/gorm v1.24.3 => v1.25.12
# 
# D:\gowork\src\github.com\3xxx\engineercms>go get gorm.io/driver/sqlite
# go: downloading gorm.io/driver/sqlite v1.5.6
# go: warning: github.com/mattn/go-sqlite3@v2.0.3+incompatible: retracted by module author: Accidental; no major changes or features.
# go: to switch to the latest unretracted version, run:
#         go get github.com/mattn/go-sqlite3@latest
# go: upgraded gorm.io/driver/sqlite v1.4.4 => v1.5.6
# 
# D:\gowork\src\github.com\3xxx\engineercms>go get github.com/mattn/go-sqlite3@latest
# go: downloading github.com/mattn/go-sqlite3 v1.14.24
# go: downloading github.com/onsi/ginkgo v1.7.0
# go: downloading github.com/onsi/gomega v1.4.3
# go: downloading gopkg.in/check.v1 v1.0.0-20190902080502-41f04d3bba15
# go: removed github.com/casbin/beego-orm-adapter/v3 v3.0.2
# go: downgraded github.com/mattn/go-sqlite3 v2.0.3+incompatible => v1.14.24
```
一 特性：
1. 本系统采用go语言（基于[beego](https://github.com/astaxie/beego)框架）开发，运行文件为编译后的二进制可执行文件，所以无需像其他语言（php、nodejs、java等语言）编写的web应用那样，需要配置运行服务环境。
2. 数据库采用sqlite嵌入式数据库，所以也无需配置数据库服务环境。
3. 开箱即用，无需网络开发知识。
4. 对onlyoffice document server的二次开发，实现企业的实时文档协作，非常方便，避免了文档的汇总等繁琐事物，效率大大提高，协作更加优雅有趣。除了支持office的docx，xlsx及pptx格式外，还支持国产wps，et和dps格式。
5. ~在线直接预览dwg文件，避免了图纸转换成pdf的麻烦，也避免了先下载附件然后用本机电脑打开图纸的麻烦，方便设计人员查阅图纸。~
6. 采用最新的froala富文本编辑器，支持word图文直接粘贴发布，word中的图片自动上传，发布文章轻松快捷，文章支持视频和文件附件。
7. 微信小程序客户端访问和添加图文，打开微信，搜索“设计与管理”即可，小程序端也[开源](https://github.com/3xxx/wechatengineercms)。
8. web端和微信小程序多项目切换。
9. 可在conf里定制9个快捷导航条菜单。
10. 后台查看日志。
11. 通用的文档流程设置。文档审批，文档校审，合同评审流程，图纸校审流程，……
12. 整合了[mindoc](https://github.com/mindoc-org/mindoc)，实现了在线创作、查阅、分享、导入、导出电子书籍。
13. 文件分享提取码。
14. 全文检索：上传office文档、pdf等，
...（截断，原文见链接）

## 核心代码片段（来源：main.go）
```go
package main

import (
	"errors"
	"fmt"
	"github.com/3xxx/engineercms/commands/daemon"
	"github.com/3xxx/engineercms/conf"
	"github.com/3xxx/engineercms/controllers"
	"github.com/3xxx/engineercms/models"
	_ "github.com/3xxx/engineercms/routers" //这个最大的坑！！！！！
	"github.com/beego/beego/v2/adapter/toolbox"
	"github.com/beego/beego/v2/client/orm"
	"github.com/beego/beego/v2/core/logs"
	"github.com/beego/beego/v2/server/web"
	"github.com/beego/i18n"
	"github.com/kardianos/service"
	_ "github.com/mattn/go-sqlite3"
	"io"
	// "log"
	"net/http"
	"os"
	"os/exec"
	"path"
	"strings"
	"time"
)

// graceful错误——删除router下的另外2个文件，重新运行生成即可。
// 项目引用了vendor里面的库，里面库go文件在init函数里面有同样的命名，从而在加载引用的时候会被调用，从而在main运行的时候提示已经解析多次。
// 用goland查找默认是该项目下的文件，可以通过指定vendor目录进行查找。

// 2021-8-30发现建表有问题：
// 1.beego是首先运行controllers里的init()，然后运行models里的init()，这是不科学的。gorm就先运行models里的init()，建立表格
// 2.因为controllers里先查询表还是操作表啥的出错，eforce那个，总是提示没有casbin_rule表，出错，程序走不下去，不去models里执行init()里的建表代码
// 3.将controllers里错误注释掉，它就执行建表了。但是user表总是到它为止，将user表后面的注释，就可以继续自动建表了，也没找到什么地方不对，再恢复，好像也可以。
// 4.在eforce里加个判断，如果查询有admin角色，则说明建好了角色表，可以执行操作了，否则return，不执行后面的建立角色-权限表。

func main() {
	// beego.AddFuncMap("dict", dict)
	//web.AutoRender = false
	//beego.TemplateLeft = "<<<"
	//beego.TemplateRight = ">>>"
	//web.TemplateLeft = "<<<"
	//web.TemplateRight = ">>>"
	//自动建表——坑：一定要放在main里，否则很多表建不了，casbin_rule表也建不了，出现错误
	orm.RunSyncdb("default", false, true)
	// orm.RunSyncdb("default", true, true)
	models.InsertUser()
	// models.InsertGroup()
	models.InsertRole()

	// err := orm.RunSyncdb("default", false, true) // mindoc
	// if err == nil {
	// 	initialization()
	// } else {
	// 	panic(err.Error())
	// }

	web.AddFuncMap("loadtimes", loadtimes)
	web.AddFuncMap("subsuffix", subsuffix)
	//默认关闭orm调试模式——仅仅针对beego的orm有效。
	ormDebug, err := web.AppConfig.String("ormDebug")
	if err != nil {
		logs.Error("获取ormDebug ->", err.Error())
	}
	if ormDebug == "true" {
		orm.Debug = true
	} else {
		orm.Debug = false
	}
	//创建附件目录ModePerm FileMode = 0777 // 覆盖所有Unix权限位（用于通过&获取类型位）
	os.Mkdir("attachment", os.ModePerm)
	//创建轮播图片存放目录
	os.Mkdir("attachment/carousel", os.ModePerm)

	// time1 := "0/" + time + " * * * * *"

	// time1 := "* 30 8 * * 1-5"
	time1, err := web.AppConfig.String("tasktime")
	if err != nil {
		logs.Error("获取tasktime ->", err.Error())
	}
	if time1 != "" {
		tk1 := toolbox.NewTask("tk1", time1, func() error { controllers.SendMessage(); return nil }) //func() error { fmt.Println("tk1"); return nil }
		toolbox.AddTask("tk1", tk1)
		toolbox.StartTask()
		defer toolbox.StopTask()
	}
	// 定时备份数据库
	time2, err := web.AppConfig.String("backupdatatime")
	if err != nil {
		logs.Error("获取tasktime ->", err.Error())
	}
	// logs.Info(time2)
	if time2 != "" {
		tk2 := toolbox.NewTask("tk2", time2, func() error { controllers.Postdata(); return nil }) //func() error { fmt.Println("tk1"); return nil }
		toolbox.AddTask("tk2", tk2)
		toolbox.StartTask()
		defer toolbox.StopTask()
	}
	// ********mindoc*********
	// if len(os.Args) >= 3 && os.Args[1] == "service" {
	// 	if os.Args[2] == "install" {
	//    daemon.Install()
	// 	} else if os.Args[2] == "remove" {
	// 		daemon.Uninstall()
	// 	} else if os.Args[2] == "restart" {
	// 		daemon.Restart()
	// 	}
	// }

	initialization()
	// commands.RegisterCache()
	// commands.RegisterLogger(conf.LogFile)
	// commands.RegisterCommand()

	d := daemon.NewDaemon()
	s, err := service.New(d, d.Config())
	if err != nil {
		fmt.Println("Create service error => ", err)
		os.Exit(1)
	}
	if err := s.Run(); err != nil {
		// log.Fatal("启动程序失败 ->", err)
		logs.Error("启动程序失败 ->", err)
	}

	// ********mindoc*********
	// web.SetStaticPath("/down1", "download1")
	web.Run()
	// 开启pprof，监听请求,无效
	// go func() {
	// 	log.Println(http.ListenAndServe("127.0.0.1:6060", nil))
	// }()
}

// 显示页面加载时间
func loadtimes(t time.Time) int {
	return int(time.Now().Sub(t).Nanoseconds() / 1e6)
}

// 去除扩展名
func subsuffix(in string) string {
	fileSuffix := path.Ext(in)
	return strings.TrimSuffix(in, fileSuffix)

...（截断，原文见链接）
```
