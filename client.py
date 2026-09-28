"""Holt-Winters Triple Exponential Smoothing Engine.
100% Python Standard Library.
"""

class HoltWintersSmoother:
    """Holt-Winters Additive Triple Exponential Smoothing (Level, Trend, Seasonality)."""
    def __init__(self, season_length=4, alpha=0.2, beta=0.1, gamma=0.3):
        self.m = season_length
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma

    def fit_forecast(self, series, horizon=2):
        n = len(series)
        assert n >= self.m * 2, "Series must have at least 2 complete seasons"
        m = self.m

        level = sum(series[:m]) / m
        trend = sum(series[m + i] - series[i] for i in range(m)) / (m**2)
        seasonals = [series[i] - level for i in range(m)]

        for i in range(n):
            val = series[i]
            last_level = level
            last_trend = trend
            s_idx = i % m
            level = self.alpha * (val - seasonals[s_idx]) + (1 - self.alpha) * (last_level + last_trend)
            trend = self.beta * (level - last_level) + (1 - self.beta) * last_trend
            seasonals[s_idx] = self.gamma * (val - level) + (1 - self.gamma) * seasonals[s_idx]

        forecasts = []
        for h in range(1, horizon + 1):
            s_idx = (n + h - 1) % m
            f = level + h * trend + seasonals[s_idx]
            forecasts.append(f)
        return {"level": level, "trend": trend, "seasonals": seasonals, "forecasts": forecasts}
