class VortexBorderControl:
    def __init__(self):
        self.high_risk_zones = ["CN", "RU", "KP", "IR"]
    def inspect_origin(self, metadata):
        risk = 50 if metadata.get("country") in self.high_risk_zones else 0
        return {"risk_score": risk, "status": "BLOCK" if risk >= 50 else "PASS"}
