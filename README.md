# PiDayPHormation Manim 示例集（零基础中文教程）

这个仓库包含了多份 **Manim** 示例脚本，适合用来入门“用 Python 做动画”。

- `basic_manim.py`：最基础的 Manim CE 动画示例合集（文字、图形、函数图像、3D 等）
- `a_little_complex_manim.py`：更偏“数学可视化”的示例（黎曼和、单位圆生成正弦、利萨如曲线、傅里叶近似）
- `manim_ce_opengl.py`：Manim CE 的 OpenGL 渲染 + 键盘交互示例
- `manim_gl_for_grant_sanderson.py`：ManimGL（3Blue1Brown 风格）示例（窗口交互更强）

---

## 你需要准备什么（完全没学过 Python 也能做）

### 1. 安装 Python

建议安装 **Python 3.10 或 3.11**（过新/过旧都可能踩坑）。

- 如果你已经装了 Python：在终端输入

```bash
python3 --version
```

看到 `Python 3.x.x` 就可以。

### 2. 安装 FFmpeg（非常重要）

Manim 渲染视频需要 FFmpeg。

macOS 推荐用 Homebrew：

```bash
brew install ffmpeg
```

安装后检查：

```bash
ffmpeg -version
```

如果提示找不到命令，说明环境变量或安装没成功。

---

## 第一次运行（推荐流程）

### 1. 创建虚拟环境（推荐）

在仓库根目录（也就是你看到这些 `.py` 文件的地方）打开终端，然后执行：

```bash
python3 -m venv .venv
```

激活虚拟环境：

```bash
source .venv/bin/activate
```

激活成功后，你会看到终端提示符前面多一个类似 `(.venv)` 的标记。

### 2. 安装依赖

```bash
python -m pip install -U pip
pip install -r requirements.txt
```

注意：`requirements.txt` 里包含了 Manim CE、ManimGL 等多个方向的依赖。第一次安装会比较久。

---

## 如何渲染（最常用的命令）

### A. Manim CE（推荐从这里开始）

命令格式：

```bash
manim -pql 文件名.py 场景类名
```

- `-p`：渲染完成后自动打开视频
- `-ql`：低质量（更快，适合调试）

示例：

```bash
manim -pql basic_manim.py HelloWorld
manim -pql basic_manim.py GraphExample
manim -pql a_little_complex_manim.py FourierSquareWave
```

### B. Manim CE + OpenGL 渲染（带交互）

```bash
manim -qm -p --renderer=opengl manim_ce_opengl.py ColorSwitcher
manim -qm -p --renderer=opengl manim_ce_opengl.py PolygonExplorer
```

- `-qm`：中等质量（OpenGL 交互时更舒服）

运行后会弹出窗口：

- `ColorSwitcher`：
  - `R/G/B` 切换颜色
  - `+/-` 调整亮度
  - `Space` 旋转
- `PolygonExplorer`：
  - `W/S` 或 `↑/↓` 调整边数
  - `Space` 开关旋转

### C. ManimGL（3Blue1Brown 的版本，命令不同）

命令格式：

```bash
manimgl 文件名.py 场景类名
```

示例：

```bash
manimgl manim_gl_for_grant_sanderson.py Introduction
manimgl manim_gl_for_grant_sanderson.py SurfaceExample
```

交互模式（可以在终端输入 Python 指令控制场景）：

```bash
manimgl manim_gl_for_grant_sanderson.py TerminalTransform -i
```

进入交互后，你可以在终端输入（示例）：

```python
self.play(h1.animate.move_to([2, 0, 0]))
self.play(h2.animate.move_to([-1, 2, 0]))
self.play(h1.animate.move_to([1, 0, 0]), h2.animate.move_to([0, 1, 0]))
```

---

## 渲染输出在哪里？

Manim CE 默认会把输出放到 `./media/` 下（视频、图片、临时文件）。

ManimGL 的输出路径与参数有关（例如 `-w/-o`）。

---

## 常见问题（新手最容易卡住的点）

### 1) 运行 `manim ...` 提示 command not found

- 你可能没有安装成功依赖，或没有激活虚拟环境。
- 先执行：

```bash
source .venv/bin/activate
pip show manim
```

如果 `pip show manim` 没有输出，说明没装成功。

### 2) 报错找不到 ffmpeg

- 确认你能运行：

```bash
ffmpeg -version
```

如果不行，请先 `brew install ffmpeg`。

### 3) Tex/LaTeX 相关报错

本仓库示例用到 `MathTex`（LaTeX 渲染）。如果你遇到 LaTeX 环境问题：

- 可以先从不含 LaTeX 的场景开始（例如 `HelloWorld`、`Shapes`）
- 或安装 LaTeX（较重）：Mac 推荐安装 `MacTeX`（体积很大）

### 4) OpenGL 交互窗口打不开/黑屏

- 先确保你在 macOS 上已经装好图形环境（一般默认没问题）
- 尝试降低渲染压力：

```bash
manim -ql --renderer=opengl manim_ce_opengl.py ColorSwitcher
```


