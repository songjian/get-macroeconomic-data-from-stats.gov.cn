# 从国家统计局获取宏观经济数据

## 运行指南

### 环境配置

```bash
pip install -r requirements.txt
```

### 下载数据

你需要下载的数据保存在tasks.csv中，编辑tasks.csv文件，这个csv文件有两列，第一列是指标代码，第二列是日期周期，可以参考 https://github.com/songjian/cnstats 的README.md中指标代码部分。

tasks.csv示例：

```csv
A0D0101,199001-202303
A0D0103,199001-202303
A0D0105,199001-202303
```

编辑完tasks.csv，在命令行运行：

```bash
python run_downloads.py
```

下载的数据保存在data目录中：

```bash
data/
├── A0D0101.csv
├── A0D0103.csv
└── A0D0105.csv
```

## 交流

沟通项目使用、数据分析可以加我Q：724385768
