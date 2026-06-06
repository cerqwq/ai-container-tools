"""
AI Container Tools - AI容器工具
支持Docker设计、Kubernetes、容器编排
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIContainerTools:
    """
    AI容器工具
    支持：Docker、Kubernetes、编排
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def design_container_architecture(self, application: str, scale: str) -> Dict:
        """设计容器架构"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为{application}设计{scale}规模的容器架构：

请返回JSON格式：
{{
    "services": [
        {{"name": "服务名", "image": "镜像", "replicas": "副本数"}}
    ],
    "networking": "网络方案",
    "storage": "存储方案"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"architecture": content}

    def generate_dockerfile(self, application: str, framework: str) -> str:
        """生成Dockerfile"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请为{framework} {application}生成Dockerfile：

要求：
1. 多阶段构建
2. 最小镜像
3. 安全最佳实践"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500
        )

        return response.choices[0].message.content

    def generate_docker_compose(self, services: List[Dict]) -> str:
        """生成Docker Compose"""
        if not self.client:
            return "LLM客户端未配置"

        services_text = json.dumps(services, ensure_ascii=False)

        prompt = f"""请生成Docker Compose配置：

服务：{services_text}

要求：
1. 网络配置
2. 卷配置
3. 健康检查"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_k8s_manifest(self, application: str, config: Dict) -> str:
        """生成Kubernetes清单"""
        if not self.client:
            return "LLM客户端未配置"

        config_text = json.dumps(config, ensure_ascii=False)

        prompt = f"""请为{application}生成Kubernetes清单：

配置：{config_text}

请生成Deployment、Service、Ingress的YAML："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def generate_helm_chart(self, application: str, values: Dict) -> str:
        """生成Helm Chart"""
        if not self.client:
            return "LLM客户端未配置"

        values_text = json.dumps(values, ensure_ascii=False)

        prompt = f"""请为{application}生成Helm Chart：

Values：{values_text}

要求：
1. Chart.yaml
2. values.yaml
3. templates/"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def optimize_container_image(self, current_size: str, framework: str) -> Dict:
        """优化容器镜像"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请优化{framework}容器镜像：

当前大小：{current_size}

请返回JSON格式：
{{
    "techniques": ["优化技术"],
    "expected_size": "预期大小"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"optimization": content}


def create_tools(**kwargs) -> AIContainerTools:
    """创建容器工具"""
    return AIContainerTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Container Tools")
    print()

    # 测试
    arch = tools.design_container_architecture("微服务应用", "中型")
    print(json.dumps(arch, ensure_ascii=False, indent=2))
