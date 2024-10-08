from src import scene


class SceneManager:
    def __init__(self):
        self._scene_dict = dict()
        self._next = None
        self._current = None

    def init(self, starting_scene_name: str, starting_scene: scene.Scene):
        self[starting_scene_name] = starting_scene
        self._next = starting_scene_name
        self._current = starting_scene

    def __getitem__(self, name: str):
        """return the scene"""
        return self._scene_dict[name]

    def __setitem__(self, name: str, scene: scene.Scene):
        """register the scene"""
        self._scene_dict[name] = scene

    def pop(self, name: str):
        """remove and return the scene"""
        if name == self._next:
            self._next = None
        return self._scene_dict.pop(name)

    def update(self):
        """turn the frame"""
        if self.current is None:
            raise RuntimeError("SceneManager is not initialized")

        if self.next:
            self._current = self[self.next]
            self.next = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_name: str):
        if next_name in self._scene_dict or next_name is None:
            self._next = next_name
        else:
            raise ValueError(f"{next_name} is not exists")

    @property
    def current(self):
        return self._current
