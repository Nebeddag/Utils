from typing import List, Tuple

Color = Tuple[int, int, int]
Value = float
Stage = Tuple[float, Color]

class Gradient:
    def __init__(self, stages: List[Stage]):
        assert len(stages) > 1, 'less than two values passed'

        values = [st[0] for st in stages]
        assert len(values) == len(set(values)), 'values is not unique'

        self.min = min(values)
        self.max = max(values)
        self.stages = sorted(stages, key=lambda x:x[0])
    
    def get_color(self, value: float) -> Tuple[int, int, int]:
        if value <= self.min:
            return self.stages[0][1]

        if value >= self.max:
            return self.stages[-1][1]

        for i in range(len(self.stages)):
            st1 = self.stages[i]
            st2 = self.stages[i + 1]
            if value > st1[0] and value <= st2[0]:
                r_dif = st2[1][0] - st1[1][0]
                g_dif = st2[1][1] - st1[1][1]
                b_dif = st2[1][2] - st1[1][2]
                v_norm = (value - st1[0]) / (st2[0] - st1[0])
                r = st1[1][0] + int(r_dif * v_norm)
                g = st1[1][1] + int(g_dif * v_norm)
                b = st1[1][2] + int(b_dif * v_norm)
                return (r, g, b)
