#!/bin/bash

# 简单的本地服务器启动脚本
cd "$(dirname "$0")"
PORT=8888

echo "=========================================="
echo "🚀 启动本地服务器..."
echo "=========================================="
echo ""
echo "📁 目录: $(pwd)"
echo "🌐 端口: $PORT"
echo ""
echo "✅ 服务器启动后，请在浏览器中访问："
echo ""
echo "   http://localhost:$PORT"
echo "   http://localhost:$PORT/weeks/week1.html"
echo ""
echo "按 Ctrl+C 停止服务器"
echo "=========================================="
echo ""

python3 -m http.server $PORT
