[English](README.en.md) | 简体中文

# Wiki-GRx-MJCF

<img src="./pictures/N1.png" width="300" />

本代码仓库提供将 URDF 文件转换为 MJCF 格式的工具。该工具专为 Fourier GRx 系列机器人 URDF 文件转换而开发，同时也适用于其他 URDF 文件的转换。

## 安装指南

1. 安装依赖库

   ```shell
   pip install -e .
   ```

2. 测试工具包是否安装成功

   ```shell
   urdf2mjcf --help
   ```

   ```
   usage: urdf2mjcf [-h] [-s SENSOR_CONFIG] [-m MUJOCO_NODE] [--ground] [--lighting] [--version] [-l] [urdf] [mjcf]
   
   Copyright (c) 2022 Fraunhofer IPA; use option '-l' to print license.
   
   Parse a URDF model into MJCF format
   
   positional arguments:
     urdf              the URDF file to convert (default: <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>)
     mjcf              the converted MJCF file (default: <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>)
   
   optional arguments:
     -h, --help        show this help message and exit
     -s SENSOR_CONFIG  the XML file of the sensor configuration (default: None)
     -m MUJOCO_NODE    the XML file defining the global MuJoCo configuration (default: None)
     --ground          whether to add the default ground plane to the MuJoCo model (default: True)
     --lighting        whether to add the default lighting to the MuJoCo model (default: True)
     --version         show program's version number and exit
     -l                print license information (default: False)
   ```

3. 转换 URDF 文件为 MJCF 格式

   ```shell
   urdf2mjcf /path/to/models /path/to/mjcf
   ```

   ```shell
   # 转换 N1 机器人示例
   urdf2mjcf ./models/N1/urdf/N1_raw.urdf ./models/N1/mjcf/N1_raw.xml
   ```

4. 调整机器人基座高度

   ```
   # 编辑 MJCF 文件中的 <body name="base">
   <body name="base" pos="0 0 0.70">
   ```

5. 优化 MJCF 文件：
    - 工具生成的 MJCF 文件为基础版本，您可以根据需求手动优化。
    - 优化完的 MJCF 文件放置于 `./models/N1/scene/` 目录下。

## 模型验证

1. 启动 Mujoco Viewer

   ```
   python -m mujoco.viewer
   ```

2. 把生成的 MJCF 文件拖到 Mujoco Viewer 窗口中，查看模型是否正确。

## 感谢

- https://github.com/balandbal/urdf2mjcf

---

感谢您对傅利叶智能 N1 机器人项目的关注！
希望本资源能为您的机器人开发提供有力支持！
