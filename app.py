import streamlit as st
import os
from pathlib import Path

# 设置页面配置
st.set_page_config(
    page_title="VestibularScope 项目展示",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 创建媒体文件夹路径
MEDIA_DIR = Path("media")
IMAGES_DIR = MEDIA_DIR / "images"
VIDEOS_DIR = MEDIA_DIR / "videos"

def main():
    st.sidebar.title("🔬 VestibularScope")
    st.sidebar.markdown("---")
    
    page = st.sidebar.radio(
        "导航",
        ["原型机展示", "技术参数详解"]
    )

    if page == "原型机展示":
        show_prototype_demo()
    elif page == "技术参数详解":
        show_tech_specs()

def show_prototype_demo():
    st.title("🔬 VestibularScope 原理机展示")
    
    st.markdown("""
    > 本项目旨在开发一套便携、高精度的前庭功能检测系统，通过机器视觉与深度学习技术，实现对眼震信号的自动化采集与定量分析。
    """)
    
    st.markdown("---")

    # ==========================================
    # Part 1: 原型机设计
    # ==========================================
    st.header("1️⃣ 原型机设计理念")
    
    st.markdown("""
    VestibularScope 原型机采用轻量化、可调节的机械结构设计，确保患者在检测过程中的位置固定。
    """)
    
    prototype_img = IMAGES_DIR / "prototype.jpg"
    if prototype_img.exists():
        c1, c2, c3 = st.columns([1, 2, 1])
        with c2:
            st.image(str(prototype_img), caption="VestibularScope 原型机手绘设计图", use_column_width=True)

    st.markdown("---")

    # ==========================================
    # Part 2: 系统工作流程
    # ==========================================
    st.header("2️⃣ 系统工作流程")
    
    st.markdown("""
    VestibularScope 的核心工作流程包含三个主要阶段：
    1.  **被视安置**：调节设备位置，确保成像质量。
    2.  **视频信号采集**：进行眼震试验，录制原始眼动视频。
    3.  **算法处理与参数输出**：深度学习模型提取信号，计算临床指标。
    """)
    
    workflow_img = IMAGES_DIR / "workflow.png"
    if workflow_img.exists():
        c1, c2, c3 = st.columns([1, 3, 1])
        with c2:
            st.image(str(workflow_img), caption="VestibularScope 系统操作流程图", use_column_width=True)

    st.markdown("---")

    # ==========================================
    # Part 3: 实地测试与数据演示
    # ==========================================
    st.header("3️⃣ 实地测试与核心处理流程演示")
    st.markdown("以下展示从实地数据采集到最终参数生成的全过程。")

    # Step 1: 实地场景与原始采集
    st.subheader("Step 1: 实地场景与原始采集")
    st.markdown("""
    下图为了使用视靶诱发眼震测试模拟患者的眼震情况的试验场集。
    """)

    # 实地拍摄图片
    col1, col2 = st.columns(2)
    shoot1 = IMAGES_DIR / "camerashoot.jpeg"
    shoot2 = IMAGES_DIR / "camerashoot2.jpeg"
    
    with col1:
        if shoot1.exists():
            st.image(str(shoot1), caption="场景一：设备部署与患者准备", use_column_width=True)
    with col2:
        if shoot2.exists():
            st.image(str(shoot2), caption="场景二：视靶诱发眼震测试进行中", use_column_width=True)

    st.markdown("####")
    
    # 原始采集视频
    st.markdown("**🎥 原始采集视频示例：**")
    video_shot = VIDEOS_DIR / "camera_shot.mp4"
    if video_shot.exists():
        st.video(str(video_shot))
    else:
        st.info("待补充：原始采集视频 (camera_shot.mp4)")

    st.markdown("#### ⬇️")

    # Step 2: 信号提取
    st.subheader("Step 2: 深度学习信号提取")
    st.markdown("""
    我们将采集到的视频输入 Mediapipe 深度学习模型，进行实时的瞳孔追踪与信号提取。
    
    下图展示了我们的实时处理界面：
    1.  **左上窗口**：原始视频输入，实时显示摄像头捕捉画面。
    2.  **左下窗口**：眼部 ROI (Region of Interest) 提取，利用深度学习定位瞳孔。
    3.  **中间图表**：实时波形图，展示 Pitch (红线) 和 Yaw (蓝线) 的角度变化，包含原始数据(Raw)和平滑处理(Smoothed)后的数据。
    4.  **右侧面板**：系统控制与文件操作界面。
    """)
    
    # 插入 signal.png
    signal_img = IMAGES_DIR / "signal.png"
    if signal_img.exists():
        st.image(str(signal_img), caption="深度学习信号提取与实时可视化界面", use_column_width=True)
    
    st.markdown("####")
    st.markdown("**🎥 信号提取过程演示：**")
    
    video_signal = VIDEOS_DIR / "video2signal.mp4"
    if not video_signal.exists():
        video_signal = VIDEOS_DIR / "video2signal2.mp4"

    if video_signal.exists():
        st.video(str(video_signal))
    else:
        st.info("待补充：信号提取演示视频 (video2signal.mp4)")

    st.markdown("#### ⬇️")

    # Step 3: 参数量化分析
    st.subheader("Step 3: 参数量化与分析")
    st.markdown("""
    对提取出的眼动信号进行进一步分析嘛，输出眼震测试中SPV、眼震方向等关键参数。
    """)
    
    video_param = VIDEOS_DIR / "signal2parameter.mp4"
    if video_param.exists():
        st.video(str(video_param))
    else:
        st.info("待补充：参数分析演示视频 (signal2parameter.mp4)")

    # 底部
    st.markdown("---")
    st.caption("© 2023 VestibularScope Project Team")

def show_tech_specs():
    st.title("⚙️ 技术参数详解")
    
    st.markdown("""
    > 本页面详细列出了原理机的硬件参数、算法性能指标以及后续的升级规划。
    """)

    st.markdown("---")

    # 1. 硬件采集参数
    st.header("1️⃣ 拍摄与采集参数")
    st.info("当前原理机采用高性能工业相机，确保原始数据的高质量采集。")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("采集帧率", "120 fps", "Frame Rate")
        st.metric("分辨率", "1920 x 1080", "Full HD")
    with col2:
        st.metric("视频格式", "MJPEG", "Compression")
        st.metric("接口标准", "USB 2.0", "Bandwidth: ~2MB/s")

    st.markdown("---")

    # 2. 模型与算力性能 (原第3部分，现前移为第2部分)
    st.header("2️⃣ 模型与推理性能")
    
    col_model, col_perf = st.columns(2)
    
    with col_model:
        st.markdown("#### 🧠 模型参数")
        st.write("- **模型大小**: 29 MB")
        st.write("- **参数量**: 7.6 M")
        
    with col_perf:
        st.markdown("#### 💻 硬件环境与性能")
        st.write("- **CPU**: Intel i5-12400 @ 2.5GHz")
        st.write("- **内存**: 16GB")
        st.write("- **推理速度**: **56 fps** (CPU Only)")

    st.markdown("---")

    # 3. 临床分析指标 (原第2部分，现后移为第3部分)
    st.header("3️⃣ 临床分析指标")
    
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("✅ 当前可计算参数")
        st.markdown("""
        - **眼震有无** (Nystagmus Presence)
        - **眼震方向** (Direction: Left/Right/Up/Down/Torsional)
        - **慢相速度 SPV** (Slow Phase Velocity)
        - **眼震频率** (Frequency)
        """)
    
    with c2:
        st.subheader("🚀 后续规划参数")
        st.markdown("""
        - **潜伏期** (Latency)
        - **疲劳性** (Fatigability)
        - **持续时间** (Duration)
        - **固视抑制率** (Fixation Suppression Index)
        - **慢相波形形状特征**
        """)

    st.markdown("---")

    # 4. 升级规划与需求
    st.header("4️⃣ 性能升级需求")
    st.warning("为了捕捉更精细的眼动事件（如隐形扫视波），我们需要进一步提升硬件规格。")
    
    st.subheader("🎯 关键挑战：隐形扫视波 (Invisible Saccade)")
    st.markdown("""
    - **事件时长**: 约 **20 ms**
    - **采样需求**: 为在该事件窗口内采集 **10-20 个点**。
    """)
    
    target_col1, target_col2 = st.columns(2)
    with target_col1:
        st.markdown("#### 📸 采集升级")
        st.metric("目标采样率", "500 - 1000 Hz", "+300% ~ +700%")
        st.caption("以满足微小快速眼动事件的捕捉需求")
        
    with target_col2:
        st.markdown("#### ⚡️ 算力升级")
        st.markdown("**需求**: 引入 **GPU 硬件加速**")
        st.caption("为了在 500-1000Hz 的高采样率下保持实时处理，必须从 CPU 推理迁移至 GPU 加速。")

    st.markdown("---")
    st.caption("© 2023 VestibularScope Project Team")

if __name__ == "__main__":
    main()