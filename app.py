import streamlit as st
import os
from pathlib import Path

# 设置页面配置
st.set_page_config(
    page_title="VestibularScope 项目展示",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 创建媒体文件夹路径
MEDIA_DIR = Path("media")
IMAGES_DIR = MEDIA_DIR / "images"
VIDEOS_DIR = MEDIA_DIR / "videos"

def main():
    st.title("🔬 VestibularScope 原型机展示")
    
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

if __name__ == "__main__":
    main()