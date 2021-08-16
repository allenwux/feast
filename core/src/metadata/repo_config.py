from typing import Any

class RepoConfig:
    registry: str
    project: str
    provider: str
    online_store: Any
    offline_store: Any

    def __init__(self, raw_config: dict):
        for k, v in raw_config.items():
            setattr(self, k, v)