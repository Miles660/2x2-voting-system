[![Docker Image](https://img.shields.io/docker/v/milo648/2x2-voting-system?label=Docker%20Hub)](https://hub.docker.com/r/milo648/2x2-voting-system)
# 2x2-Voting-System: 单机容器实现“二乘二取二系统表决”
[![Docker Pulls](https://img.shields.io/docker/pulls/milo648/2x2-voting-system)](https://hub.docker.com/r/milo648/2x2-voting-system)
[![GitHub Stars](https://img.shields.io/github/stars/Miles660/2x2-voting-system)](https://github.com/Miles660/2x2-voting-system)


---

## 项目概述

一个 **单机 Docker 模拟系统**，实现工业级 **“二乘二取二”安全计算平台** 的核心逻辑。

- **4 个主机容器**：`channel1-task`, `channel1-vote`, `channel2-task`, `channel2-vote`
- **1 个协调器**：收集输入 → 发送 POST → 表决 → 输出结果
- **计算逻辑**：`output = input + 10`
- **故障检测**：输入不一致 → `Fault Reported`

---

## 快速开始

```bash
1. 克隆仓库
git clone https://github.com/Miles660/2x2-voting-system.git
cd 2x2-voting-system

2. 启动系统
docker-compose up -d

3. 进入协调器输入
docker attach 2x2_voting_system_coordinator_1

输入示例（制造故障）：
textEnter input for channel1-task: 42
Enter input for channel1-vote: 42
Enter input for channel2-task: 50
Enter input for channel2-vote: 51  (不一致!)

输出：
textChannel 1: Pass
Channel 2: Input mismatch
Overall Decision: Fault Reported



