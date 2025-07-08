FROM ros:noetic-ros-core-focal

ENV DEBIAN_FRONTEND=noninteractive \
    LANG=ja_JP.UTF-8 \
    LC_ALL=ja_JP.UTF-8

# ロケール
RUN apt-get update \
 && apt-get install -y locales \
 && locale-gen ja_JP.UTF-8 \
 && rm -rf /var/lib/apt/lists/*

# ROS、Python、X11、NVIDIA GPUサポート
RUN apt-get update \
 && apt-get install -y \
      curl gnupg lsb-release \
      python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential \
      ros-noetic-desktop-full \
      x11-apps \
      mesa-utils \
      libgl1-mesa-glx \
      libglib2.0-0 \
      libsm6 \
      libxext6 \
      libxrender-dev \
      libgomp1 \
      libgcc-s1 \
      libstdc++6 \
      libc6 \
      libnvidia-gl-525 \
      python3.9 python3-pip python3.9-dev \
      python3-numpy python3-scipy python3-matplotlib python3-pandas \
      git vim nano \
      python3-catkin-tools \
 && rm -rf /var/lib/apt/lists/*

# Python 3.9をデフォルトに設定
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1

# バージョン確認
RUN python3 --version \
 && pip3 --version

# NVIDIA Container Toolkit用の環境変数
ENV NVIDIA_VISIBLE_DEVICES=all \
    NVIDIA_DRIVER_CAPABILITIES=compute,utility,graphics

# PyTorchを再インストール
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124

# 作業ディレクトリの設定
WORKDIR /workspace

# requirements.txtをコピーしてPythonパッケージをインストール
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# エントリポイント：ROS環境を読み込みつつ、CMDで指定されたコマンドを実行可能
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["bash"]
