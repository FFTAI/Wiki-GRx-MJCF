import os

from .core import Element
from .core import (
    resolve_uris,
    add_mujoco_node,
    pass_through_mujoco,
    populate_sensors,
)
from .default_elements.ground import add_ground
from .default_elements.lighting import add_lighting


def full_pipeline(
        urdf_file_path: str,
        urdf: Element,

        mujoco_node: Element = None,

        # 传感器配置
        sensor_config: Element = None,

        # 默认加入地面
        default_ground: bool = True,

        # 默认加入光源
        default_lighting: bool = True,
) -> Element:
    """
    Convert URDF object to MJCF
    """

    urdf_file_folder_abs_path = urdf_file_path.replace(os.path.basename(urdf_file_path), "")

    resolve_uris(urdf, base_path=urdf_file_folder_abs_path)

    # 把所有相对路径的文件名转换为绝对路径
    add_mujoco_node(urdf, mujoco_node)

    # URDF -> MUJOCO -> MJCF
    mjcf = pass_through_mujoco(urdf)

    if sensor_config is not None:
        populate_sensors(mjcf, sensor_config)
        mjcf = pass_through_mujoco(mjcf)

    if default_ground:
        add_ground(mjcf)

    if default_lighting:
        add_lighting(mjcf)

    return mjcf
