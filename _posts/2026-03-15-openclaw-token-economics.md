---
layout: post
title: OpenClaw 爆火背后：AI Agent 的 Token 成本悖论
title_en: The Hidden Cost of AI Agents — What the OpenClaw Hype Reveals
date: 2026-03-15
category: Writing
excerpt: 为什么越来越多「一人公司」开始重新思考 AI 工作流？OpenClaw 爆火背后，AI Agent 的 Token 经济学与成本悖论。
excerpt_en: Why AI agents like OpenClaw burn so many tokens, and what it means for
  one-person companies building with AI.
cover: /assets/images/posts/2026-03-15-openclaw-token-economics/cover.png
image:
  path: /assets/images/posts/2026-03-15-openclaw-token-economics/og-card.png
  alt: The Hidden Cost of AI Agents — What the OpenClaw Hype Reveals
---


### 中文版:

### OpenClaw 爆火背后：AI Agent 的 Token 成本悖论

#### 为什么越来越多“一人公司”开始重新思考 AI 工作流

**Date:** Mar. 15, 2026  
**Topic:** Token Economics of AI Agents

---

### 最近 AI 开发社区出现了一个奇怪的现象

过去几周，一个叫 **OpenClaw** 的 AI Agent 项目在开发者社区突然爆火

如果你关注 AI 开源圈，可能已经看到很多类似内容：

- “我用 OpenClaw 自动开发了一个工具”
- “AI agent 帮我完成整个项目”
- “AI 已经可以自动执行复杂任务”

看起来，一个新时代似乎正在到来

AI 不再只是聊天机器人，而开始变成：

> **可以主动执行任务的系统**

但与此同时，另一种声音也越来越多：

**Token 在燃烧**

很多开发者在测试 OpenClaw 时发现：

一个看起来很简单的任务，  可能消耗 **几十万甚至上百万 token**

甚至有人在几天时间里：**花掉几千到上万美元的 API 成本**

而与此同时，很多开发者用另一种方式完成类似任务：

**Cursor + Workflow**

成本却只是：**60 美元 / 月**

于是一个问题浮现出来：

> AI Agent 真的比 Workflow 更高效吗？

---

### AI 自动化越强，成本反而越高？

很多人对 AI Agent 的想象是：

```
给 AI 一个目标
AI 自动完成一切
```

听起来非常完美, 但现实情况往往是：

**自动化越强 → 系统越复杂 → token 成本越高**

当 AI 不只是回答问题，而是开始：

- 规划任务  
- 调用工具  
- 记录状态  
- 持续执行

系统复杂度会指数级增长

于是很多开发者在测试 Agent 时产生一种奇怪的体验：

> AI 确实更强大了  
> 但成本也突然变得难以控制

---

### AI 的成本结构正在发生变化

如果把这波 AI Agent 热潮总结成一句话，大概是：

> **AI 的成本结构正在改变**

过去 AI 的主要成本是：**计算成本**

而现在，越来越多成本来自：**执行成本**

换句话说：

当 AI 开始 **执行任务** 时, 系统成本不再只是模型调用

还包括：

- 状态管理  
- memory  
- 工具调用  
- 多轮规划  
- context 维护

OpenClaw 只是第一个把这个问题暴露出来的项目

---

### 我越来越确信的一个概念

我越来越觉得，AI Agent 其实有一套它自己的经济学：

> **Token Economics of AI Agents**

也就是：**AI 自动化的成本结构**

很多人讨论：

- AI 能不能自动工作
- AI 能不能替代人

但很少有人讨论：**AI 执行任务的成本结构**

而这可能才是 AI Agent 是否能规模化的关键

---

### Chatbot vs Agent

理解这个变化，可以看一个简单模型

传统 AI（Chatbot）：

```
用户提问
↓
AI回答
```

而 Agent 系统是：

```
目标
↓
AI规划
↓
调用工具
↓
执行任务
↓
分析结果
↓
继续行动
```

也就是说：

AI 从：**回答机器**

变成：**执行机器**

这种系统现在通常被称为：**Agentic AI**

---

### Token Economics of AI Agents

Agent 系统在每次调用模型时，都必须携带大量上下文信息，例如：

- 当前任务目标  
- 历史行动记录  
- 工具说明  
- API 文档  
- memory  
- 系统指令

这些内容都会写入 prompt

于是 prompt 会变成这样：

```
任务目标
当前状态
历史行动
工具描述
系统规则
```

当 Agent 反复循环执行任务时：**context 会不断膨胀**

于是同一个任务：token 使用量可能被放大 **数倍甚至十倍**

这就是：

> **AI Agent 的 Token 经济学**

---

### 一个真实测试

一位开发者做过一个很有代表性的实验

任务：让 AI **读取一个大型项目文件夹，并生成项目进展总结**

项目包含：

- 文档  
- 任务记录  
- 工作日志  
- 记忆数据

这是一个典型的 **AI 开发辅助任务**

他用三种工具完成：

#### Claude Code

Token：约 **7 万**

成本：约 **5.6 RMB**

---

#### GPT-5.3 Codex（高推理模式）

Token：约 **13 万**

几乎翻倍

原因是：  高推理模式会产生更多 **thinking tokens**

---

#### OpenClaw

Token：**77 万**

---

结果非常直观：


| 工具            | Token |
| ------------- | ----- |
| Claude Code   | 7 万   |
| GPT-5.3 Codex | 13 万  |
| OpenClaw      | 77 万  |


OpenClaw 的成本：**接近 Claude Code 的 10 倍**

原因不是模型

而是：**Agent 架构本身**

---

### 中国 vs 海外：Agent 使用方式的差异

另一个有趣现象是：Agent 在不同地区的使用方式非常不同

#### 西方开发者

更多用于：

- 自动化开发  
- DevOps  
- 数据研究  
- AI research

这些任务特点是：**复杂 + 高价值**

---

### 中国开发者

很多早期实验集中在：

- 自媒体自动化  
- 内容生产  
- 电商抓取  
- 账号管理

问题在于：

很多任务其实只需要：**脚本 + API**

于是就出现了一些极端情况：有人花 **上万美元 token**

做出一个：**简单数据工具**

---

### 一个中国开发者的真实实验

最近一位独立开发者分享了自己的 OpenClaw 实测

总成本：**约 2000 美金**

他测试了几个场景：

#### AI 新闻监控

每天抓取 **X（Twitter）AI 新闻** 推送到飞书

相当于一个：**AI 情报助手**

---

#### 马斯克新闻追踪

任务设定：

> “每天告诉我马斯克又干了什么”

系统自动抓取：

- xAI  
- Tesla  
- SpaceX

---

#### 自动运营小红书账号

工作流：

1 下载 YouTube 视频  
2 自动剪辑  
3 生成封面  
4 写文案  
5 自动发布  

技术上：**完全可行**

---

#### 数据分析

自动抓取：

- 7 天曝光  
- 30 天增长  
- 内容表现

生成报告

---

#### 但问题也非常明显

为了保证质量，他使用：**Claude Opus**

每天成本：**几十美元**

如果换便宜模型：质量明显下降

他的结论非常现实：

> OpenClaw 更像未来产品  
> 而不是今天的生产工具

---

### 我的 Vibe Coding 实践

过去几个月，我也在做类似实践

不过我走的是另一条路线：**AI + Workflow**, 而不是复杂 Agent

我是一个 **时尚设计师出身的人**，不是工程师

但通过 **Cursor + AI**，我已经做了十几个项目

其中几个比较有代表性

---

#### ViralLab — 创作者灵感工具

GitHub:  [https://github.com/Funghi88/ViralLab](https://github.com/Funghi88/ViralLab)

目标：

> 分析互联网内容的传播结构

功能包括：

- viral 内容分析  
- 内容结构提取  
- 创作灵感提示

开发方式：**Cursor Composer**

开发时间：**2 天**

token 成本：**约 20 美元**

现在我正在增加新的功能：

- 科技新闻抓取  
- 内容结构分析  
- 创作提示系统

整个系统其实就是：**AI + 内容创作 workflow**, 完全不需要复杂 Agent

---

#### DreamWork — AI 工作流实验

GitHub:  [https://github.com/Funghi88/DreamWork](https://github.com/Funghi88/DreamWork)

这个项目也是：**2 天完成**

目标是探索：

AI 如何帮助一个人完成：

- 内容整理  
- 白板思考  
- 项目规划

本质上是一个：**个人 AI 工作系统**

成本：**20 美元以内**

---

#### Aegis Vaults — Web3 数据工具

GitHub:  [https://github.com/Funghi88/Aegis-Vaults](https://github.com/Funghi88/Aegis-Vaults)

这是我在 **Polkadot 生态**做的项目

功能包括：

- 稳定币质押信息  
- DeFi 流动性数据  
- 多平台数据聚合

前端 + 后端：全部用 **Cursor** 构建

当时 Cursor 还没有 Composer, 所以 token 消耗非常低

这个项目 + 我的博客 + 几个 Web3 小工具：**全部加起来都没有用完 20 美元**

---

#### 我的博客系统

GitHub:  [https://github.com/Funghi88/Funghi88.github.io](https://github.com/Funghi88/Funghi88.github.io)

这是我所有内容的起点

博客本身也是：**Cursor + AI 一起构建的**

我把这里当作：

> Personal AI Editorial Lab

记录我的：

- AI 实验  
- 创作方法  
- Web3 研究  
- 一人公司探索

---

### 一个有趣的结论

把这些实践放在一起看，会发现一件事：

很多人讨论：**AI Agent 会不会改变工作方式**

但在我的实验中：很多时候并不需要复杂 Agent

只需要：

- AI coding tools  
- 清晰 workflow  
- 一点耐心

一个人就可以构建很多工具

而成本：通常只是 **几十美元**

---

#### OpenClaw 的愿景很迷人

AI 自动完成一切

但现实是：很多创作者和独立开发者并不需要那么复杂的系统

很多时候：**简单 workflow + AI coding tools**, 就已经足够强大

也许未来真正的趋势不是：

> 每个人拥有一个 AI 公司

而是：

> **每个人拥有一个 AI 工具箱**

---

如果你成立一家 **一人公司**，你会怎么选？

A:  AI Agent 自动执行一切

B:  人类设计 Workflow,  AI 负责执行

---

### The Hidden Cost of AI Agents

##### What the OpenClaw Hype Reveals About the Economics of AI

  
**Topic:** Token Economics of AI Agents

---

#### Something strange is happening in the AI developer world

Over the past few weeks, a project called **OpenClaw** has exploded across the AI community.



If you spend any time on GitHub, X, or developer Discords, you've probably seen posts like these:

- “I built an entire tool with OpenClaw.”
- “My AI agent completed a project on its own.”
- “AI can now run complex workflows autonomously.”

The excitement is obvious.



For years, AI mostly lived inside chat windows.  
You asked questions. It answered.



But systems like OpenClaw promise something very different.

> AI that doesn’t just talk —  
> **AI that acts.**



Instead of responding to prompts, these systems can:

- plan tasks
- call tools
- run code
- analyze results
- iterate toward a goal



In other words, the dream of a **digital worker** suddenly feels close.

But as developers started experimenting with it, another story began to surface.

A quieter one.

**Tokens are burning.**

---

#### The moment people started checking the bill

Some developers noticed something unexpected.



A task that looked simple could suddenly consume:

- **hundreds of thousands of tokens**
- sometimes **millions**



A few experiments reportedly burned through **thousands of dollars in API costs** in just a few days.

Meanwhile, other developers were solving similar problems using a much simpler stack:

**Cursor + manual workflow design**



Total cost?

About **$60 per month**.



This created a strange tension in the community.

If AI agents are supposed to automate work…

why do they sometimes feel **more expensive** than doing it yourself?



Which leads to a deeper question:

> Are AI agents actually the most efficient way to use AI?

---

#### The dream of full automation

Most people imagine AI agents working like this:

```
Give the AI a goal
↓
The AI figures everything out
↓
The task gets completed
```



It’s an incredibly appealing vision.

You don’t write the steps.  
You don’t design the system.

You just describe the outcome.



But the reality of agent systems looks very different.

Once AI stops answering questions and starts **executing tasks**, the complexity of the system increases dramatically.



An agent now has to:

- plan actions
- track state
- call tools
- remember past steps
- evaluate results
- decide what to do next

Instead of a simple interaction, you now have an **ongoing process**.

And every step of that process requires another model call.



The result is something many developers didn’t expect:

> The more autonomous the system becomes,  
> **the harder it is to control its cost.**

---

#### AI is entering a new economic phase

One way to understand this is to look at how the **cost structure of AI** is changing.

In the early era of AI tools, the main cost was simple:

**compute.**



You paid for the model to generate a response.

But once AI systems start executing tasks, new costs appear.



Now you’re paying for things like:

- maintaining task state
- storing memory
- loading tool descriptions
- replaying historical actions
- repeated planning loops



In other words:

AI is no longer just **thinking**.

It is **doing**.

And doing things is expensive.

---

#### The Token Economics of AI Agents

This led me to a concept I’ve started thinking about a lot recently:

> **The Token Economics of AI Agents**



Or simply:

**the cost structure of AI automation.**



When people talk about AI agents, they usually debate questions like:

- Can AI replace developers?
- Can AI run businesses?
- Can AI work autonomously?



But a far more practical question often gets ignored:

> How much does it cost for AI to execute tasks repeatedly?

Because that cost determines whether these systems can scale.

---

#### Chatbots vs Agents

To see why the cost changes so dramatically, compare two basic models.

Traditional AI tools look like this:

```
User prompt
↓
Model response
```

One prompt.  
One output.



Now compare that to an agent system:

```
Goal
↓
Planning
↓
Tool usage
↓
Execution
↓
Result analysis
↓
Next action
```

Instead of one interaction, the system loops continuously.



Every loop involves:

- more prompts
- more context
- more reasoning

Which means more tokens.

---

#### Why token costs explode

Agent systems must carry large amounts of context every time they call a model.

That context often includes:

- the original task goal
- current progress
- previous actions
- tool documentation
- system instructions
- memory



The prompt quickly starts to look like this:

```
Task goal
Current state
Action history
Tool descriptions
System rules
```

And with every iteration, the context grows larger.

Each step includes everything that came before it.



This means that over time:

> **token usage compounds.**



The same task might end up consuming **five to ten times more tokens** than a simple AI interaction.

Not because the model is worse.

But because the **architecture itself is heavier.**

---

#### A simple experiment

One developer ran a small experiment to test this.

The task was straightforward:

Have AI read a large project folder and produce a progress summary.



The folder contained:

- documentation
- task records
- development notes
- memory files



Three different approaches were used.

#### Claude Code

Token usage: about **70k tokens**

Cost: roughly **$0.80**

---

#### GPT-5.3 Codex (high reasoning mode)

Token usage: about **130k tokens**

Almost double.

Higher reasoning means more internal thinking tokens.

---

#### OpenClaw agent workflow

Token usage:

**770k tokens**

Nearly **ten times higher** than the simplest approach.



The model wasn’t dramatically different.

The architecture was.

---

#### Different regions, different experiments

Interestingly, the way developers experiment with agents differs across regions.

In Western developer communities, agents are often used for:

- automated software workflows
- DevOps tasks
- research automation
- data analysis

These tasks tend to be **complex and high-value**.



In China, many early experiments focused on areas like:

- social media automation
- content generation
- e-commerce scraping
- account management

But many of these tasks don’t actually require complex agents.

A simple script plus an API often works just fine.



Which led to some extreme cases.

Developers spending **thousands of dollars in tokens**…

to build tools that could have been implemented with basic automation.

---

#### A $2000 experiment

One Chinese indie developer shared a particularly interesting experiment.

He spent around **$2000 in token costs** testing OpenClaw in real workflows.



His goal was simple:

Could an AI agent act as a personal assistant?



He tested several scenarios.

#### AI news monitoring

The system scanned trending AI news on X every morning and sent a report to his work tools.

Effectively an **AI intelligence feed**.

---

#### Tracking Elon Musk

He gave the system a simple instruction:

> “Tell me what Elon Musk did today.”



The agent monitored updates related to:

- xAI
- Tesla
- SpaceX

---

#### Running a social media account

He even tried automating a social media workflow.

The system would:

1. download YouTube videos
2. generate clips
3. create thumbnails
4. write captions
5. publish posts

Technically, it worked.

But there was a problem.

---

#### The cost reality

To maintain decent quality, the developer had to use **Claude Opus**.

The daily operating cost quickly reached **tens of dollars per day**.



Cheaper models reduced the cost.

But the output quality dropped significantly.



His final conclusion was surprisingly pragmatic:

> OpenClaw feels more like a **prototype of the future**  
> than a production tool for today.

---

#### My own experiments

Over the past few months, I’ve been exploring a different path.

Instead of building complex agent systems, I’ve been experimenting with something simpler:

**AI + structured workflows.**



I’m not a software engineer by training.

My background is actually in **fashion design**.



But with tools like Cursor, I’ve been able to build more than a dozen small projects using AI-assisted coding.

A few examples stand out.

---

### ViralLab

[https://github.com/Funghi88/ViralLab](https://github.com/Funghi88/ViralLab)

ViralLab is a small tool I built to analyze the structure of viral content online.

It helps creators identify patterns behind successful posts.

The entire project was built with **Cursor Composer**.



Development time:

**two days.**

Token cost:

about **$20**.

---

### DreamWork

[https://github.com/Funghi88/DreamWork](https://github.com/Funghi88/DreamWork)

DreamWork explores how AI can help individuals structure thinking and planning.

It acts like a lightweight personal workflow system for:

- idea capture
- project planning
- content organization



Again, the build time was around **two days**.

Total token cost: **under $20**.

---

### Aegis Vaults

[https://github.com/Funghi88/Aegis-Vaults](https://github.com/Funghi88/Aegis-Vaults)

This project was built earlier while I was experimenting with the Polkadot ecosystem.

It aggregates DeFi liquidity and staking data across several platforms.

Both the front-end and back-end were built with AI-assisted coding.



At that time Cursor didn’t even have Composer yet.

So the total token usage across that project, my blog, and several smaller Web3 tools…

never even exceeded **$20**.

---

### My blog

[https://github.com/Funghi88/Funghi88.github.io](https://github.com/Funghi88/Funghi88.github.io)

My blog itself was also built together with AI tools.

I think of it as a kind of **personal AI editorial lab**.



A place where I explore ideas around:

- AI experiments
- creator workflows
- Web3 research
- the future of one-person companies

---

#### A pattern begins to appear

Looking across all these experiments, something interesting becomes clear.

Many people ask whether **AI agents will change how we work**.

But in my experience, complex agents are often unnecessary.



What works surprisingly well is much simpler:

- AI coding tools  
- clearly designed workflows  
- a bit of patience

With those ingredients, one person can build many useful tools.

And the cost is often just **tens of dollars**.

---

#### The future might look simpler than we think

The vision behind projects like OpenClaw is fascinating.

A world where AI systems autonomously run entire operations.



But for many creators and indie builders today, that level of complexity isn’t required.

Often, a simple combination of:

**AI tools + well-designed workflows**

is already incredibly powerful.



Which leads to a thought I keep coming back to:

Maybe the future isn’t about everyone running an **AI company**.

Maybe it’s about everyone having an **AI toolkit**.

---

#### One last question

If you were building a **one-person company** today, which direction would you choose?



A world where:

**A. AI agents run everything autonomously**

or

**B. Humans design workflows, and AI executes the tasks**

Because the answer to that question might define how we actually build with AI.