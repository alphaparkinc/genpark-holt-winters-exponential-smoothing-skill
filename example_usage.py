from client import HoltWintersSmoother

series = [10, 12, 15, 9, 11, 13, 16, 10, 12, 14, 17, 11]
hw = HoltWintersSmoother(season_length=4)
res = hw.fit_forecast(series, horizon=3)

print("Holt-Winters Model Results:")
print(f"Final Level: {res['level']:.2f}, Trend: {res['trend']:.2f}")
print(f"Next 3 Forecasts: {[round(f, 2) for f in res['forecasts']]}")
