from statsmodels.tsa.arima.model import ARIMA
import pandas as pd

lebron_stats = pd.read_csv("lebron_career.csv", parse_dates=["date"])
lebron_stats["Year"] = lebron_stats.date.dt.year
lebron_stats["Month"] = lebron_stats.date.dt.month

years = lebron_stats.Year.unique()

for year in years:
    if year == 2003:
        continue
    train_data = lebron_stats.query(f"Year == {year} and Month < 6").iloc[:-5]
    test_data = lebron_stats.query(f"Year == {year} and Month < 6").iloc[-5:]

    model = ARIMA(
        train_data["pts"], order=(15, 1, 1)
    )  # Order AR is comparing previous 10 weeks of scoring
    model_fit = model.fit()

    # Forecast 5 years ahead
    forecast = model_fit.forecast(steps=5)  # Forecasting 4 weeks
    df = forecast.to_frame(name="pts")
    # Creating yearly forecast for pts for the next year
    forecast_dates = pd.Series(test_data.date)
    forecast_dates = forecast_dates.to_frame()
    forecast_dates.reset_index(inplace=True)
    forecast_pts = pd.Series(forecast.array, index=range(0, 5))
    forecast_df = pd.concat(
        [forecast_pts.rename("pts"), forecast_dates["date"]], axis=1
    )

    forecast_df.to_csv(f"forecast{year}.csv", index=False)
