from noaa_sdk import noaa
n = noaa.NOAA()
res = n.get_forecasts('11365', 'US', True)
x = [res]
