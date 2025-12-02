#!/usr/bin/env python3
"""
VestibularScope 项目展示网站启动脚本

使用方法：
python run.py
"""

import subprocess
import sys
import os

def check_dependencies():
    """检查必要的依赖是否已安装"""
    try:
        import streamlit
        print(f"✅ Streamlit 已安装 (版本: {streamlit.__version__})")
        return True
    except ImportError:
        print("❌ Streamlit 未安装，请运行: pip install -r requirements.txt")
        return False

def install_dependencies():
    """安装项目依赖"""
    print("📦 正在安装依赖包...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ 依赖安装完成")
        return True
    except subprocess.CalledProcessError:
        print("❌ 依赖安装失败")
        return False

def run_app():
    """运行 Streamlit 应用"""
    print("🚀 启动 VestibularScope 项目展示网站...")
    print("📱 应用将在浏览器中自动打开")
    print("🔗 默认地址: http://localhost:8501")
    print("❌ 按 Ctrl+C 停止服务\n")

    try:
        # 运行 streamlit 应用
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.port", "8501",
            "--server.address", "localhost"
        ])
    except KeyboardInterrupt:
        print("\n👋 应用已停止")
    except Exception as e:
        print(f"❌ 启动失败: {e}")

def main():
    print("🔬 VestibularScope 项目展示网站")
    print("=" * 40)

    # 检查依赖
    if not check_dependencies():
        choice = input("是否现在安装依赖包? (y/n): ").lower().strip()
        if choice == 'y':
            if not install_dependencies():
                sys.exit(1)
        else:
            print("请先安装依赖包: pip install -r requirements.txt")
            sys.exit(1)

    # 运行应用
    run_app()

if __name__ == "__main__":
    main()
