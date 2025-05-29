class TagManager:
    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self) -> None:
        self.tags: dict[str, int] = {}

    def addTag(self, name: str, value: int):
        if name in self.tags.keys():
            raise IndexError(f"Tag {name} already exists")
        self.tags[name] = value

    def getTag(self, name: str) -> int:
        if name not in self.tags.keys():
            raise IndexError(f"Tag {name} not found")
        return self.tags[name]
