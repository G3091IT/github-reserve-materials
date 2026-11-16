# ZeroTang05/cyber-doctor

- **仓库名**：ZeroTang05/cyber-doctor
- **原文链接**：https://github.com/ZeroTang05/cyber-doctor
- **Star 数**：512（取自 GitHub 搜索 API；本环境数值可能偏高，待核实）
- **最近更新时间**：2026-10-27T07:01:28Z
- **许可证**：GPL-3.0
- **语言**：Python
- **质量分 / 适配分 / 混合分**：90.3 / 52.9 / 73.5
- **结论**：ADOPT
- **标记**：无
- **领域适配**：领域词:知识库/rag/问答

## 用途摘要
赛博医生项目——”赛博华佗“，基于多模态大模型的多功能智能体，一键搭建本地多模态大模型。接入医疗健康相关的知识图谱和知识库后可以进行疾病初诊，病历分析，专业知识问答等功能，成为你的私人医生。赛博华佗项目能帮助实现医疗资源的跨地域传播，让更多人借助大模型改善健康水平。"Cyber ​​Huatuo" - Easy to build a personal doctor agent based on LLM and Knowledge Graph/Knowledge Database.

## 适配理由
✓ 命中任务词：分析/知识/识库；△ 未命中：招投/投标/标文/文档/档分/评标/库检/检索/与投/标资/资料/料仓/仓库/库关/关联/联泛/泛化/化检

## README 要点
<div align="center">
 <img src="README/bot.jpg" width="200" />
</div>

<h1 align="center">「赛博华佗」🩺 cyber-doctor 你的健康小管家</h1>

**语言**

- [English](./README_en.md)
- [中文](./README.md)

---

![](https://img.shields.io/github/stars/Warma10032/cyber-doctor?style=social)
![](https://img.shields.io/github/forks/Warma10032/cyber-doctor?style=social)
![](https://img.shields.io/github/contributors/Warma10032/cyber-doctor)
![](https://img.shields.io/github/issues/Warma10032/cyber-doctor)
![](README/License-GPLv3-blue.svg)

## 项目演示视频

https://www.bilibili.com/video/BV1CU2aYpEn2

## 项目背景

医疗资源不平衡一直以来是社会关注的重点问题，它导致众多医疗不公平事件发生。在相对落后地区的人们想要获得优秀的医疗资源往往需要前往一线城市，这不仅费时费力费钱，而且极大的影响了他们的接受医疗救助的基本权利。当前多模态大语言模型不断发展，在许多领域都有了不错的应用。我们小组基于东南大学暑期实训课程，开发了一个医疗健康领域的多模态大模型，这个大模型的目标用户是所有对自己健康关心的人，帮助进行基本的疾病诊断，病历分析，专业知识答疑等功能。本项目狭义上可以作为一个多功能的健康小助手，帮助管理个人健康，提供基础的医疗建议；广义上可以配置在任何领域，通过微调的大模型和RAG技术让大模型掌握目标领域的专业知识，成为任意专业的专家。

## 界面展示

### 文本交流界面

![](README/文本交流界面.png)

### 语音对话界面

![](README/语音对话界面.png)

## 功能特色

- **多功能多模态整合，借助AI智能体判断任务的种类，将多个模型整合工作，解决复杂问题。**
- **单独的语音对话模块，语音输入语音输出，只需要会说话就能使用，降低大模型学习成本。**

## 功能介绍

![功能模块](README/功能模块.png)

| 功能         | 功能介绍                                                                                                 |
| ------------ | -------------------------------------------------------------------------------------------------------- |
| 图片识别     | 借助多模态大模型的能力，识别图片中的图像和文字。可用于识别病历，识别药品说明书等                         |
| 视频生成     | 借助多模态大模型的能力，生成视频                                                                         |
| 图片生成     | 借助多模态大模型的能力，生成图片                                                                         |
| ppt/word生成 | 可自动生成固定格式的纯文字PPT和Word文档                                                                  |
| 多轮对话     | 具有记忆功能，对话界面的所有内容会作为历史记录一同输入大模型                                             |
| 检索增强对话 | 多模态输入框不只能输入文本，还能上传文件。大模型会根据文件内容调整输出                                   |
| 语音输入     | 多模态输入框可以上传音频文件。进入语音对话模式可以直接使用麦克风进行语音输入                             |
| 语音输出     | 要求大模型以语音的形式进行输出时，大模型会返回一段音频，支持多种方言，在语音对话模式下默认以语言形式输出 |
| 知识图谱增强 | 支持配置相关领域的neo4j知识图谱，用专业知识改善大模型输出                                                |
| 知识库增强   | 支持利用多种格式的文件作为专属知识库，大模型会结合知识库中的文件进行输出                                 |
| 联网检索增强 | 通过自动化爬虫检索网络上的相关信息，利用网络增强大模型知识的时效性                                       |

## 典型功能展示

### 病历识别

![](README/病历识别.png)

### PPT/Word生成

![](README/PPT&Word生成.png)

![](README/PPT&Word展示.png)

### 知识图谱检索增强：

![](README/知识图谱检索.png)

### 联网检索增强：

![](README/联网搜索.png)

## 技术栈

- **Python**
- **PyTorch**
- **Transformers**
- **Gradio**：简易的UI和交互生成工具
- **Langchain**：基于 Langchain 框架，构建语言模型进行链式操作
- **modelscope & huggingface**：预训练大模型的下载与配置
- **RAG**：结合检索与生成的技术，用于增强生成式模型的回答质量
- **Knowledge Graph (Neo4j)**：Neo4j图数据库的配置和Cypher语句操作
- **TTS (edge-tts)，STT (whisper)**：语音转文本，文本转语音
- **OpenAi & zhipuai**：相关大模型sdk调用方法

Option：

- **Ollama**：本地大模型api封装

## 如何启动项目

1. **从Github上拉取项目**

   ```bash
   git clone https://github.com/Warma10032/cyber-doctor.git
   或者
   git clone git@github.com:Warma10032/cyber-doctor.git
   ```
   
2. **配置大模型API**

   复制 `.env.example`为 `.env`，填写 `.env`内相关API配置。

   API目前支持：

   1. 所有支持OpenAI SDK接口的API，包括
      - [智谱AI](https://open.bigmodel.cn/)
      - [豆包大模型](https://www.volcengine.com/experience/ark?utm_term=202502dsinvite&ac=DSASUQY5&rc=II9TBGSX)
      - [硅基流动集成平台](https://cloud.siliconflow.cn/i/VWOdVvvM)
      - [deepseek](https://platform.deepseek.com/)
      - [千问Qwen](https://bailian.console.aliyun.com/)
   2. Ollama封装的本地API

如果你还未申请API，欢迎通过我的邀请链接进行注册获取新人试用额度。

   由于团队本身缺少申请/测试多家API的能力，可能会有各种bug，**欢迎各位提出相关的issue和PR一起来解决API适配问题，你的行动是对开源社区最大的帮助。**

3. **填写 `config/config-web.yaml`配置文件**

4. **创建python环境（python>=3.10，建议为3.10）**

   建议使用conda管理环境

   ```bash
   conda create --name myenv python=3.10
   conda activate myenv
   ```

   安装依赖库

   ```bash
   pip install -r requirements.txt
   ```
   
5. **启动项目**

   ```bash
   python app.py
   ```

   启动后访问 http://localhost:7860

Option：

1. **下载Neo4j图数据库（使用知识图谱检索增强功能的必要条件）**

   推荐教程：

   - [Windows系统下Neo4j安装教程——CSDN博客](https://blog.csdn.net/jing_zhong/article/details/112557084)
   - [Docker化部署Neo4j](https://cloud.baidu.com/article/3314714)

   提醒：

   - 免费的社区版即可，能创建一个图数据库
   - 创建时记住用户名和密码
   - 填写config/config-web.yaml配置文件
   - 记得启动Neo4j服务
2. **配置一个专业领域的图数据库**

   推荐开源知识图谱平台：[OpenKG](http://openkg.cn/datasets-type/)

   如果想配置医疗健康领域的数据库，推荐下载如下开源知识图谱

   [面向家庭常见疾病的知识图谱](http://data.openkg.cn/dataset/medicalgraph)（本项目使用了该图谱，使用该图谱可以不更改config/config-web.yaml的相关配置文件）

   1. 下载到本地后，改.dump文件名为你要导入的数据库名称（eg：neo4j.dump）
   2. 关闭neo4j服务

      ```
      Windows: neo4j stop
      Linux: sudo neo4j stop
      ```
   3. 运行导入指令（这一步简中互联网上找不到正确的教程😡）

      ```
      neo4j-admin database load <database-name> --from-path=/path/to/dump-folder/ --overwrite-destination=true
      ```

      `--from-path`：存放对应"database-name".dump文件的文件夹路径

      `--overwrite-destination`：**注意会覆盖你原先数据库中的数据**
   4. 若运行上面的命令后输出

      ```
      The loaded database 'neo4j' is not on a supported version (current format: AF4.3.0 introduced in 4.3.0). Use the 'neo4j-admin database migrate' command
      ```

      还需要运行如下命令

      ```
      neo4j-admin database migrate 
      ```
   5. 启动neo4j服务

      ```
      Windows: neo4j start
      Linux: sudo neo4j start
      ```

## 项目结构

```
cyber-doctor/
├── .env                            # 环境配置文件，存储API密钥、模型配置等敏感信息
├── .env.example                    # 环境配置文件示例，展示需要配置的环境变量
├── .gitignore                      # Git版本控制忽略文件配置
├── LICENSE                         # 项目许可证文件
├── README.md                       # 项目中文说明文档
├── README_en.md                    # 项目英文说明文档
├── __init__.py                     # Python包初始化文件
├── app.py                          # 项目启动文件，构建Gradio界面，处理多模态信息，可自定义ASR模型和界面
├── env.py                          # 封装读取.env文件的接口
├── requirements.txt                # 项目依赖包列表
├── Internet/                       # 联网搜索相关功能模块
│   ├── __init__.py                   # 包初始化文件
│   ├── Internet_chain.py            
...（截断，原文见链接）

## 核心代码片段（来源：app.py）
```python
import base64
from qa.answer import get_answer
from qa.question_parser import parse_question
from qa.function_tool import process_image_describe_tool
from qa.purpose_type import userPurposeType
from audio.audio_generate import audio_generate

import PyPDF2
import chardet
import mimetypes
import gradio as gr
from icecream import ic
from docx import Document
from pydub import AudioSegment
import speech_recognition as sr
from opencc import OpenCC
import os


AVATAR = ("resource/user.png", "resource/bot.jpg")
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# pip install whisper
# pip install openai-whisper
# pip install soundfile
# pip install pydub
# pip install opencc-python-reimplemented


def convert_to_simplified(text):
    converter = OpenCC("t2s")
    return converter.convert(text)


def convert_audio_to_wav(audio_file_path):
    audio = AudioSegment.from_file(audio_file_path)  # 自动识别格式
    wav_file_path = audio_file_path.rsplit(".", 1)[0] + ".wav"  # 生成 WAV 文件路径
    audio.export(wav_file_path, format="wav")  # 将音频文件导出为 WAV 格式
    return wav_file_path


def audio_to_text(audio_file_path):
    # 创建识别器对象
    # 如果不是 WAV 格式，先转换为 WAV
    if not audio_file_path.endswith(".wav"):
        audio_file_path = convert_audio_to_wav(audio_file_path)

    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)
        # 使用 Google Web Speech API 进行语音识别，不用下载模型但对网络要求高
        # text = recognizer.recognize_google(audio_data, language="zh-CN")
        # 使用 whisper 进行语音识别，自动下载模型到本地
        text = recognizer.recognize_whisper(audio_data, language="zh")
        text_simplified = convert_to_simplified(text)
    return text_simplified


# pip install PyPDF2
def pdf_to_str(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


def docx_to_str(file_path):
    doc = Document(file_path)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    return "\n".join(text)


# pip install chardet
def text_file_to_str(text_file):
    with open(text_file, "rb") as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result["encoding"]

    # 使用检测到的编码来读取文件
    with open(text_file, "r", encoding=encoding) as file:
        return file.read()


def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
        return encoded_string


# 核心函数
def grodio_view(chatbot, chat_input):

    # 用户消息立即显示
    user_message = chat_input["text"]
    bot_response = "loading..."
    chatbot.append([user_message, bot_response])
    yield chatbot

    # 处理用户上传的文件
    files = chat_input["files"]
    audios = []
    images = []
    pdfs = []
    docxs = []
    texts = []

    for file in files:
        file_type, _ = mimetypes.guess_type(file)
        if file_type.startswith("audio/"):
            audios.append(file)
        elif file_type.startswith("image/"):
            images.append(file)
        elif file_type.startswith("application/pdf"):
            pdfs.append(file)
        elif file_type.startswith(
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        ):
            docxs.append(file)
        elif file_type.startswith("text/"):
            texts.append(file)
        else:
            user_message += "请你将下面的句子修饰后输出，不要包含额外的文字，句子:'该文件为不支持的文件类型'"
            print(f"Unknown file type: {file_type}")

    # 图片文件解析
    if images != []:
        image_url = images
        image_base64 = [image_to_base64(image) for image in image_url]

        for i, image in enumerate(image_base64):
            chatbot[-1][
                0
            ] += f"""
                <div>
                    <img src="data:image/png;base64,{image}" alt="Generated Image" style="max-width: 100%; height: auto; cursor: pointer;" />
      
...（截断，原文见链接）
```
