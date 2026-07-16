# wechat-sketch-cover

wechat-sketch-cover 是一个固定风格的 Codex Skill：根据准确的中文标题和可选文章内容，生成一张暖色手绘笔记风的微信公众号封面，并输出严格为 1923 x 818 的 PNG。

行为变更时递增 `wechat-sketch-cover/SKILL.md` frontmatter 中 `metadata.version` 的语义版本。

## 安装

~~~
npx skills add https://github.com/BruceL017/wechat-sketch-cover
~~~

可安装 Skill 位于仓库中的 wechat-sketch-cover/ 目录。

## 使用

~~~
请使用 $wechat-sketch-cover，给文章《为什么 AI 工作流总是难以复用？》制作公众号封面。
文章主要讨论输入、过程记录和复盘之间的断层。
~~~

也可以提供一个包含 frontmatter title 或一级标题的 Markdown 文件。

## 固定合同

- 最终格式：PNG。
- 最终尺寸：1923 x 818，约 2.35:1。
- 构图：左侧准确标题，右侧内容隐喻插画。
- 风格：米色纸张、深棕手绘线条、橙色与金色强调。
- 标题字体：中文手写标题字体，粗笔刷、手写毛笔风，marker / brush handwritten Chinese。
- 文字：只允许文章标题；不生成副标题、标签、Logo 或水印。
- 标题长度：2–35 个非空白 Unicode 字符（含标点）。
- 后端：开放使用 Codex 原生 imagegen、其他图片 Skill、CLI、API、SVG、HTML、CSS、Canvas 或其他可用图片后端。
- 尝试次数：最多三次；仅当标题仍可读、错误是唯一剩余问题且属于局部字形偏差时，才以 BEST_EFFORT 交付并明确报告；其他失败不生成 cover.png。

图片归一化需要 Python 3 和 Pillow 11.3.0：

~~~
python3 -m pip install Pillow==11.3.0
~~~

## 输出

输出位于当前工作目录：

~~~
wechat-sketch-cover-output/<title-slug>/
├── source.md
├── prompts/
├── candidates/
└── cover.png
~~~

Prompt、构建说明和候选图会被保留，便于复现和对比。候选图可以由图片模型生成，也可以通过程序化合成、覆盖或修补完成；最终统一归一化为固定 PNG。

## 验证

~~~
python3 -m unittest discover -s tests -v
python3 /path/to/skill-creator/scripts/quick_validate.py wechat-sketch-cover
~~~

## 来源与许可

本项目从 JimLiu/baoyu-skills 的 baoyu-cover-image 中抽取并重写了暖色手绘封面流程，来源提交为 6b7a2e417500561a5ecdd0b168332f4142584617。

项目按 MIT License 发布。上游归属和修改说明见 LICENSE 与 NOTICE。
