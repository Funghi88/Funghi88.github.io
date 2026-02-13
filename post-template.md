---
layout: post
title: "中文标题"
title_en: "English Title"
date: YYYY-MM-DD
category: Writing
excerpt: "中文摘要，显示在首页卡片。"
excerpt_en: "English excerpt for home page card."
image: /assets/images/posts/YYYY-MM-DD-slug/cover.jpg
---

<!-- 封面：layout 自动从 front matter 的 image 渲染，中英文都显示，无需在正文写 -->
<!-- 文内图：在中文和英文对应位置各写一遍，否则切换语言时图片会消失 -->

# 中文标题

中文正文开始。用 Markdown 写。

## 第一节

内容...

## 第二节

![图片描述](/assets/images/posts/YYYY-MM-DD-slug/your-image.png)

内容...

---

<!-- lang: en -->

# English Title

English content starts here. Write in Markdown.

## Section One

Content...

## Section Two

![Image description](/assets/images/posts/YYYY-MM-DD-slug/your-image.png)

Content...

---

<!-- 使用说明：复制到 _posts/，重命名 YYYY-MM-DD-slug.md -->
<!-- 封面：只填 image，layout 自动渲染。文内图：中英文各写一遍。日期用当天或过去 -->
