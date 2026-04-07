from Vortex_Border_Control import VortexBorderControl
class VortexQuantumCore:
    def __init__(self):
        self.border = VortexBorderControl()
    def secure_process(self, prompt, metadata):
        return self.border.inspect_origin(metadata)
