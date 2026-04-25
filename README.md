# Fincept Terminal

## 项目介绍

### 简体中文

🎉 **Fincept Terminal** 是一款开源、轻量级、跨平台的金融分析终端，为个人投资者和金融分析师提供专业级的市场分析工具。

### 核心价值
- 替代昂贵的商业金融终端（如Bloomberg）
- 提供实时市场数据和专业分析工具
- 支持多平台运行（Windows、macOS、Linux）
- 开源免费，社区驱动发展

### 解决的痛点
- 金融市场数据分散，难以集中分析
- 专业金融终端价格昂贵，个人投资者难以承受
- 投资决策缺乏数据支持
- 金融数据可视化复杂，操作门槛高

### 自研差异化亮点
1. **性能优化**：采用异步数据获取和处理，提升数据处理速度
2. **易用性提升**：直观的用户界面，简化操作流程
3. **功能补全**：集成多种数据源和分析工具
4. **跨平台兼容**：支持Windows、macOS、Linux多平台
5. **UI/UX改进**：现代化界面设计，支持深色/浅色模式

### 灵感来源
- 参考了 GitHub Trending 上的 FinceptTerminal 项目
- 融合了多种金融分析工具的优点

---

### 繁體中文

🎉 **Fincept Terminal** 是一款開源、輕量級、跨平台的金融分析終端，為個人投資者和金融分析師提供專業級的市場分析工具。

### 核心價值
- 替代昂貴的商業金融終端（如Bloomberg）
- 提供實時市場數據和專業分析工具
- 支持多平台運行（Windows、macOS、Linux）
- 開源免費，社區驅動發展

### 解決的痛點
- 金融市場數據分散，難以集中分析
- 專業金融終端價格昂貴，個人投資者難以承受
- 投資決策缺乏數據支持
- 金融數據可視化複雜，操作門檻高

### 自研差異化亮點
1. **性能優化**：採用異步數據獲取和處理，提升數據處理速度
2. **易用性提升**：直觀的用戶界面，簡化操作流程
3. **功能補全**：集成多種數據源和分析工具
4. **跨平台兼容**：支持Windows、macOS、Linux多平台
5. **UI/UX改進**：現代化界面設計，支持深色/淺色模式

### 靈感來源
- 參考了 GitHub Trending 上的 FinceptTerminal 項目
- 融合了多種金融分析工具的優點

---

### English

🎉 **Fincept Terminal** is an open-source, lightweight, cross-platform financial analysis terminal that provides professional market analysis tools for individual investors and financial analysts.

### Core Value
- Alternative to expensive commercial financial terminals (like Bloomberg)
- Provides real-time market data and professional analysis tools
- Supports multi-platform operation (Windows, macOS, Linux)
- Open-source and free, community-driven development

### Pain Points Solved
- Financial market data is scattered and difficult to analyze centrally
- Professional financial terminals are expensive and unaffordable for individual investors
- Investment decisions lack data support
- Financial data visualization is complex with high operation thresholds

### Self-developed Differentiation Highlights
1. **Performance Optimization**: Adopts asynchronous data acquisition and processing to improve data processing speed
2. **Usability Improvement**: Intuitive user interface, simplified operation流程
3. **Feature Completion**: Integrates multiple data sources and analysis tools
4. **Cross-platform Compatibility**: Supports Windows, macOS, Linux platforms
5. **UI/UX Improvement**: Modern interface design with dark/light mode support

### Inspiration Source
- Referenced the FinceptTerminal project on GitHub Trending
- Integrated the advantages of various financial analysis tools

---

## ✨ 核心特性

### 市场数据模块
- 股票实时行情
- 指数数据
- 外汇市场数据
- 加密货币数据
- 商品市场数据

### 分析工具模块
- 技术指标分析（MA、MACD、RSI等）
- 基本面分析
- 风险评估
- 投资组合分析
- 回测工具

### 数据可视化模块
- 实时图表（K线、分时、成交量）
- 热力图
- 相关性分析图表
- 自定义仪表盘

### 经济数据模块
- 宏观经济指标
- 行业数据
- 公司财报数据
- 新闻分析

### 决策支持模块
- AI辅助分析
- 投资建议生成
- 市场情绪分析
- 事件影响评估

---

## 🚀 快速开始

### 环境要求
- Python 3.8 或更高版本
- pip 包管理器

### 安装步骤

#### 中国大陆网络环境
```bash
# 使用国内镜像源安装依赖
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

#### 其他地区
```bash
# 直接安装依赖
pip install -r requirements.txt
```

### 启动命令
```bash
# 运行应用
python main.py
```

### 一键运行命令
```bash
# 安装依赖并运行
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple && python main.py
```

---

## 📖 详细使用指南

### 功能说明
1. **Dashboard**：查看市场概览和主要指数
2. **Charts**：查看详细的金融图表和技术指标
3. **Settings**：配置API密钥和应用设置

### 参数说明
- **API设置**：需要配置Alpha Vantage和News API密钥以获取完整功能
- **显示设置**：可选择主题和语言
- **数据设置**：可配置自动刷新频率

### 场景示例
1. **股票分析**：输入股票代码，选择时间周期，查看K线图和技术指标
2. **市场监控**：在Dashboard页面查看主要市场指数的实时数据
3. **投资组合分析**：分析投资组合的风险和收益

---

## 💡 设计思路与迭代规划

### 设计理念
- 以用户为中心，简化操作流程
- 模块化设计，便于扩展和维护
- 性能优先，确保数据处理速度
- 跨平台兼容，满足不同用户需求

### 技术选型理由
- **Python**：生态丰富，金融库支持好
- **PyQt6**：跨平台GUI框架，性能好，界面美观
- **pandas/numpy**：强大的数据处理能力
- **plotly**：交互式数据可视化
- **yfinance**：免费的金融数据来源

### 后续路线图
1. **v1.0.0**：基础功能实现
2. **v1.1.0**：增加更多技术指标和分析工具
3. **v1.2.0**：添加投资组合管理功能
4. **v1.3.0**：实现自动化交易策略
5. **v2.0.0**：添加Web版本和移动应用

### 社区贡献方向
- 增加新的数据源
- 开发新的分析工具
- 改进用户界面
- 修复bug和优化性能

---

## 📦 打包与部署指南

### 构建方法
```bash
# 使用PyInstaller打包
pyinstaller --onefile --windowed main.py
```

### 打包步骤
1. 安装PyInstaller：`pip install pyinstaller`
2. 执行打包命令
3. 在`dist`目录找到可执行文件

### 部署方式
- **本地部署**：直接运行可执行文件
- **Docker部署**：使用Docker容器运行

### 支持环境
- Windows 10及以上
- macOS 10.15及以上
- Linux (Ubuntu 20.04及以上)

---

## 🤝 贡献指南

### PR 规范
- 提交前确保代码通过测试
- 提交信息遵循Angular Commit规范
- 提供详细的PR描述

### Issue 反馈方式
- 在GitHub Issues中提交问题
- 提供详细的错误信息和复现步骤
- 如有可能，附上截图

### 分支建议
- `main`：主分支，稳定版本
- `develop`：开发分支
- `feature/*`：功能分支
- `fix/*`：修复分支

---

## 📄 开源协议说明

本项目采用 MIT 开源协议，详见 [LICENSE](LICENSE) 文件。

---

## 联系方式

- GitHub：[https://github.com/gitstq/fincept-terminal](https://github.com/gitstq/fincept-terminal)
- 邮箱：gitstq@example.com

欢迎Star和Fork本项目！
