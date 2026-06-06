# 🐳 AI Container Tools

AI容器工具，支持Docker设计、Kubernetes、容器编排。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🏗️ 容器架构设计
- 📋 Dockerfile生成
- 🐳 Docker Compose生成
- ☸️ Kubernetes清单生成
- ⎈ Helm Chart生成
- ⚡ 镜像优化

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_container_tools import create_tools

tools = create_tools()

# 架构设计
arch = tools.design_container_architecture("微服务应用", "中型")

# Dockerfile
dockerfile = tools.generate_dockerfile("Web应用", "FastAPI")

# Docker Compose
compose = tools.generate_docker_compose(services)

# Kubernetes清单
k8s = tools.generate_k8s_manifest("my-app", config)

# Helm Chart
helm = tools.generate_helm_chart("my-app", values)

# 镜像优化
optimized = tools.optimize_container_image("500MB", "Python")
```

## 📁 项目结构

```
ai-container-tools/
├── tools.py       # 容器工具核心
└── README.md
```

## 📄 许可证

MIT License
