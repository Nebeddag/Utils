class GreenYellowRedGradient:
    def __init__(self, g_val, y_val, r_val):
        assert g_val < y_val < r_val or g_val > y_val > r_val, 'wrong order of values'

        self.g_val = g_val
        self.y_val = y_val
        self.r_val = r_val
    
    def get_rgb(self, value):
        if self.g_val <= value <= self.y_val or self.g_val >= value >= self.y_val:
            r = (value - self.g_val) / (self.y_val - self.g_val) * 255
            return (int(r), int(255), int(0))
        elif self.y_val <= value <= self.r_val or self.y_val >= value >= self.r_val:
            g = 255 - (value - self.y_val) / (self.r_val - self.y_val) * 255
            return (int(255), int(g), int(0))