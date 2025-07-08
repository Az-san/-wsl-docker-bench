#!/bin/bash
set -e

# ROS環境を読み込み
source /opt/ros/noetic/setup.bash

# 引数で指定されたコマンドを実行（デフォルトはbash）
exec "$@" 