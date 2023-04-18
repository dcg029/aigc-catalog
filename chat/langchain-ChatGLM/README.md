# ChatGLM-6B搭建本地知识库

## 1. langchain-ChatGLM
## 1.1 langchain

GitHub链接：https://github.com/hwchase17/langchain



## 1.2 langchain-ChatGLM

langchain-ChatGLM，一种利用 ChatGLM-6B + langchain 实现的基于本地知识的 ChatGLM 应用。

Embedding 选用的是 GanymedeNil/text2vec-large-chinese，LLM 选用的是 ChatGLM-6B。



项目实现原理如下图所示，过程包括加载文件 -> 读取文本 -> 文本分割 -> 文本向量化 -> 问句向量化 -> 在文本向量中匹配出与问句向量最相似的top k个 -> 匹配出的文本作为上下文和问题一起添加到prompt中 -> 提交给LLM生成回答。

![实现原理图](https://github.com/imClumsyPanda/langchain-ChatGLM/raw/master/img/langchain+chatglm.png)

GitHub链接：https://github.com/imClumsyPanda/langchain-ChatGLM

部署参考链接：https://d29l201m55.feishu.cn/docx/LFREdCeOIoIdSQxpCG7cDpAJnJe



## 2. 安装部署

### 2.1 下载langchain-ChatGLM

```
# 拉取仓库
git clone https://github.com/imClumsyPanda/langchain-ChatGLM.git

# 安装依赖（使用清华源）
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```



### 2.2 下载Embedding，选用的是text2vec-large-chinese

由于下载网速限制，最好采用网盘方式进行下载。

```
# 安装 git-lfs
sudo apt-get install git-lfs

# 安装 git lfs
git lfs install

# 下载
git clone https://huggingface.co/GanymedeNil/text2vec-large-chinese
```



修改模型参数配置

```
vim /langchain-ChatGLM/configs/model_config.py
```



参考链接：https://huggingface.co/GanymedeNil/text2vec-large-chinese/tree/main

git: ‘lfs‘ is not a git command：https://blog.csdn.net/lovechris00/article/details/128618537



### 2.3 下载LLM，选用的是 ChatGLM-6B

```
# 从 Hugging Face Hub 下载模型需要先安装Git LFS，然后运行
git clone https://huggingface.co/THUDM/chatglm-6b

# 如果你从 Hugging Face Hub 上下载 checkpoint 的速度较慢，可以只下载模型实现
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/THUDM/chatglm-6b
```



### 2.4 启动

```
# 修改端口号配置
demo.queue(concurrency_count=3).launch(
    server_name='127.0.0.1',
    server_port=6006,
    # show_api=False,
    share=False,
    inbrowser=False)

# 启动
python cli_demo.py
python webui.py

# AutoDL为每个实例都预留了一个可对外暴露的6006端口
COMMANDLINE_ARGS="--medvram --always-batch-cond-uncond --port 6006" REQS_FILE="requirements.txt" python webui.py
```



加载完txt文件，问的问题没有命中，需要排查问题。

执行cli_demo，看下面source_documents合不合理。不合理就到llm之前步骤找问题，合理就是llm的问题。



启动参考链接：https://zhuanlan.zhihu.com/p/574200991
