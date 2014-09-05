:: sqlcmd -S . -d FCDBackup20100900 -E -s, -W -Q "SELECT * FROM [FCDBackup20100900].[dbo].[VehicleData20100901]" > "D:\Taxi Export\VehicleData20100901.csv"
:: sqlcmd -S . -d FCDBackup20100900 -E -s, -W -Q "SELECT * FROM [FCDBackup20100900].[dbo].[VehicleData20100902]" > "D:\Taxi Export\VehicleData20100902.csv"
:: sqlcmd -S . -d FCDBackup20100900 -E -s, -W -Q "SELECT * FROM [FCDBackup20100900].[dbo].[VehicleData20100903]" > "D:\Taxi Export\VehicleData20100903.csv"

:: FCDBackup20100901 is only compatible with SQL Server 2008 and below
:: sqlcmd -S . -d FCDBackup20100901 -E -s, -W -Q "SELECT * FROM [FCDBackup20100901].[dbo].[VehicleData20100904]" > "D:\Taxi Export\VehicleData20100904.csv"
:: sqlcmd -S . -d FCDBackup20100901 -E -s, -W -Q "SELECT * FROM [FCDBackup20100901].[dbo].[VehicleData20100905]" > "D:\Taxi Export\VehicleData20100905.csv"
:: sqlcmd -S . -d FCDBackup20100901 -E -s, -W -Q "SELECT * FROM [FCDBackup20100901].[dbo].[VehicleData20100906]" > "D:\Taxi Export\VehicleData20100906.csv"
sqlcmd -S . -d FCDBackup20100901 -E -s, -W -Q "SELECT * FROM [FCDBackup20100901].[dbo].[VehicleData20100907]" > "D:\Taxi Export\VehicleData20100907.csv"

:: sqlcmd -S . -d FCDBackup20100902 -E -s, -W -Q "SELECT * FROM [FCDBackup20100902].[dbo].[VehicleData20100908]" > "D:\Taxi Export\VehicleData20100908.csv"
:: sqlcmd -S . -d FCDBackup20100902 -E -s, -W -Q "SELECT * FROM [FCDBackup20100902].[dbo].[VehicleData20100909]" > "D:\Taxi Export\VehicleData20100909.csv"
:: sqlcmd -S . -d FCDBackup20100902 -E -s, -W -Q "SELECT * FROM [FCDBackup20100902].[dbo].[VehicleData20100910]" > "D:\Taxi Export\VehicleData20100910.csv"
:: sqlcmd -S . -d FCDBackup20100902 -E -s, -W -Q "SELECT * FROM [FCDBackup20100902].[dbo].[VehicleData20100911]" > "D:\Taxi Export\VehicleData20100911.csv"

:: sqlcmd -S . -d FCDBackup20100903 -E -s, -W -Q "SELECT * FROM [FCDBackup20100903].[dbo].[VehicleData20100912]" > "D:\Taxi Export\VehicleData20100912.csv"
:: sqlcmd -S . -d FCDBackup20100903 -E -s, -W -Q "SELECT * FROM [FCDBackup20100903].[dbo].[VehicleData20100913]" > "D:\Taxi Export\VehicleData20100913.csv"
:: sqlcmd -S . -d FCDBackup20100903 -E -s, -W -Q "SELECT * FROM [FCDBackup20100903].[dbo].[VehicleData20100914]" > "D:\Taxi Export\VehicleData20100914.csv"
:: sqlcmd -S . -d FCDBackup20100903 -E -s, -W -Q "SELECT * FROM [FCDBackup20100903].[dbo].[VehicleData20100915]" > "D:\Taxi Export\VehicleData20100915.csv"