#!/bin/bash

# Fab Academy 2026 本地服务器启动脚本
# 使用方法: ./start-server.sh

PORT=8888
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "🚀 正在启动 Fab Academy 2026 本地服务器..."
echo "📁 目录: $DIR"
echo "🌐 端口: $PORT"
echo ""
echo "访问地址: http://localhost:$PORT"
echo ""
echo "按 Ctrl+C 停止服务器"
echo "================================"
echo ""

cd "$DIR"
python3 -m http.server $PORT
