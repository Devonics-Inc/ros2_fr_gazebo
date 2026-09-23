#!/usr/bin/env python3

import os
from ament_index_python.packages import get_package_share_directory
import yaml

MOVEIT_PKG_MAP = {
    "fairino3":  "fairino3_v6_moveit2_config",
    "fairino5":  "fairino5_v6_moveit2_config",
    "fairino10": "fairino10_v6_moveit2_config",
    "fairino16": "fairino16_v6_moveit2_config",
    "fairino20": "fairino20_v6_moveit2_config",
    "fairino30": "fairino30_v6_moveit2_config",
}

def _flatten(_dict):
    """Flattens nested dicts so existing flat defaults.get('key') calls keep working."""
    items = {}
    for k, v in _dict.items():
        # keep both the plain key (for leaf lookups) and prefixed key
        if isinstance(v, dict):
            items.update(_flatten(v))
        else:
            items[k] = v
    return items

def load_yaml(package_name, file_path):
    package_path = get_package_share_directory(package_name)
    absolute_file_path = os.path.join(package_path, file_path)

    try:
        with open(absolute_file_path) as file:
            return yaml.safe_load(file)
    except OSError:  # parent of IOError, OSError *and* WindowsError where available
        return None

# LOADS THE FILE DENOTED BY THE "launch_params.yaml"
def load_rail_config(filename):
    """
    Loads mount/rail_length/rail_width from a rail-config YAML file.
    Returns {} if missing so hardcoded fallbacks still apply.
    """
    config_path = os.path.join(
        get_package_share_directory("fairino_gazebo_config"),
        "config",
        filename,
    )
    try:
        with open(config_path) as f:
            return yaml.safe_load(f) or {}
    except OSError:
        print(f"[INFO] No rail config found at {config_path}, using built-in defaults")
        return {}


def load_launch_defaults():
    config_path = os.path.join(
        get_package_share_directory("fairino_gazebo_config"),
        "config",
        "launch_params.yaml",
    )
    try:
        with open(config_path) as f:
            raw = yaml.safe_load(f) or {}

        return _flatten(raw)
        
    except OSError:
        print(f"[INFO] No launch_params.yaml found at {config_path}, using built-in defaults")
        return {}


def _truthy(value: str) -> bool:
    return value.strip().lower() == "true"
