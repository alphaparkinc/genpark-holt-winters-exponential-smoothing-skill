# genpark-holt-winters-exponential-smoothing-skill

Agent Skill implementing **Holt-Winters Additive Triple Exponential Smoothing** for capturing dynamic level, linear trend, and cyclic seasonality in time series.

## Architectural Overview
```mermaid
flowchart TD
    Series["Time Series Data Y_t"] --> Level["Level Update: L_t = alpha * (Y_t - S_{t-m}) + (1-alpha)*(L_{t-1} + T_{t-1})"]
    Level --> Trend["Trend Update: T_t = beta * (L_t - L_{t-1}) + (1-beta)*T_{t-1}"]
    Trend --> Season["Seasonal Update: S_t = gamma * (Y_t - L_t) + (1-gamma)*S_{t-m}"]
    Level & Trend & Season --> Forecast["Forecast: Y_{t+h} = L_t + h * T_t + S_{t-m+h}"]
```
