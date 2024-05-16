class Modul:
    def __init__(self, artifactId, modul):
        self._artifactId = artifactId
        self.parent = modul

    @property
    def artifactId(self):
        return self._artifactId

    @artifactId.setter
    def artifactId(self, value):
        self._artifactId = value

    @property
    def parent(self):
        return self._modul

    @parent.setter
    def parent(self, value):
        self._modul = value

# Example usage
modul_instance = Modul("example_artifact_id", Modul("example_modul", None))
print(modul_instance.artifactId)  # Output: example_artifact_id
print(modul_instance.parent.artifactId)       # Output: example_modul