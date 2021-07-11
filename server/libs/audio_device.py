class AudioDevice:

    def __init__(self, id, name, default_sample_rate):
        self.id = id
        self.name = name
        self.default_sample_rate = default_sample_rate

    def to_string(self):
        return f"{self.id} - {self.name} - {self.default_sample_rate} Hz"
