# 博客发布流程

## 方式一：本地 Web 编辑器（推荐）

1. 在项目目录下运行：
   ```bash
   cd blog-editor && npm install && npm start
   ```
2. 浏览器打开 http://localhost:3456
3. 填写标题、分类、正文，点击「保存到本地」
4. 点击「保存并推送到 GitHub」即可发布

---

## 方式二：在 Cursor 中手动写

### 1. 新建文章文件

在 `_posts/` 目录下新建文件，**文件名格式**：`YYYY-MM-DD-英文标题.md`

### 2. 写文章内容

```markdown
---
layout: post
title: "文章标题"
date: 2026-02-15
category: Writing
excerpt: "首页卡片显示的摘要（可选）"
---

正文用 Markdown 写。
```

**常用 Markdown 语法：** `**粗体**` `*斜体*` `## 标题` `- 列表` `> 引用` `[链接](url)`

### 3. 发布

```bash
git add _posts/文件名.md
git commit -m "Add post: 标题"
git push origin main
```

---

## 本地预览

```bash
bundle exec jekyll serve
```

浏览器打开 http://localhost:4000 预览。
