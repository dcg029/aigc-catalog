# ChatGLM-6B搭建本地知识库

## 1. 闻达
## 1.1 ChatGLM-6B

**硬件需求**

| **量化等级**   | **最低 GPU 显存**（推理） | **最低 GPU 显存**（高效参数微调） | 量化代码                        |
| -------------- | ------------------------- | --------------------------------- | ------------------------------- |
| FP16（无量化） | 13 GB                     | 14 GB                             | model.half().cuda()             |
| INT8           | 8 GB                      | 9 GB                              | model.half().quantize(8).cuda() |
| INT4           | 6 GB                      | 7 GB                              | model.half().quantize(4).cuda() |

GitHub链接：https://github.com/THUDM/ChatGLM-6B

## 1.2 wenda

闻达：一个大规模语言模型调用平台。旨在通过使用为小模型外挂知识库查找的方式，实现近似于大模型的生成能力。

- 目前支持模型：chatGLM-6B、chatRWKV、chatYuan、llama系列。
- 知识库扩展模型能力：fess模式（已删除s、x模式）、bing模式、bingxs模式、 bingsite模式

GitHub链接：https://github.com/l15y/wenda

## 2. 创建本地知识库

因为本人有读微信文章的习惯，但碍于记忆力不好，所以想把自己读到的优秀文章做成一个知识库，利用ChatGLM形式给自己做一个整理，方便对知识有一个更好的利用。

### 2.1 批量下载微信文章

使用wxArticleCatcher下载微信历史文章

参考链接1：https://www.52pojie.cn/forum.php?mod=viewthread&tid=1765143

参考链接2：https://www.52pojie.cn/forum.php?mod=viewthread&tid=1770516

拼凑历史主页，B站视频：https://www.bilibili.com/video/BV1qL4y147Mr/

程序的使用方法，B站视频：https://www.bilibili.com/video/BV1Tf4y157Rf

```
// 在浏览器提取“历史主页”代码
let og_url = document.head.querySelector("meta[property~='og:url']").content;

og_url.substring(og_url.indexOf('?__biz=') + '?__biz='.length,og_url.indexOf('&'))

// 将提取出来的“历史主页”做拼接
https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz={_biz}&scene=124

// 执行命令
wxArticleCatcher_20230326.exe -t 10 -n 100 -p "C:/download" -off 0 -O "..."
```

### 2.2 文件格式转换

下载好的是html文件，博主推荐使用pandoc转换。因为我要转成txt格式，试用了一下，效果不理想（txt中包含大量html相关代码，不纯净）。

参考链接：https://zhuanlan.zhihu.com/p/528377939

GitHub链接：https://github.com/jgm/pandoc/releases



最后采用的是TextForever工具进行转换

参考链接：https://www.52pojie.cn/thread-1389159-1-1.html

### 3 在AutoDL搭建wenda环境

