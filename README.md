# VestibularScope 项目进展展示网站

基于 Streamlit 的项目进展展示网站，用于展示 VestibularScope 前庭功能检测设备的开发进展。

## 功能特性

- 📊 项目概述页面
- 🔧 原型机介绍页面（包含图片和视频展示）
- 🚀 技术进展展示
- 👥 团队介绍

## 安装和运行

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行应用

```bash
streamlit run app.py
```

应用将在浏览器中自动打开，默认地址：http://localhost:8501

## 文件结构

```
VestibularScope/
├── app.py                 # 主应用文件
├── requirements.txt       # Python 依赖
├── README.md             # 项目说明
└── media/                # 媒体文件目录
    ├── images/           # 图片文件
    └── videos/           # 视频文件
```

## 添加媒体内容

### 图片文件
将原型机图片放入 `media/images/` 目录中：
- 支持格式：.jpg, .png, .jpeg
- 建议分辨率：至少 800x600 像素
- 文件命名示例：
  - `prototype_front.jpg` - 正面图
  - `prototype_side.jpg` - 侧面图
  - `prototype_components.jpg` - 组件图

### 视频文件
将演示视频放入 `media/videos/` 目录中：
- 支持格式：.mp4, .mov
- 建议时长：1-3 分钟
- 文件命名示例：
  - `demo_operation.mp4` - 操作演示
  - `demo_results.mp4` - 结果展示

## 技术栈

- **前端框架**: Streamlit
- **编程语言**: Python 3.8+
- **媒体处理**: Pillow (PIL)

## 开发说明

- 页面布局采用宽屏模式，支持响应式设计
- 侧边栏提供页面导航
- 媒体文件自动检测和展示
- 支持实时更新内容
