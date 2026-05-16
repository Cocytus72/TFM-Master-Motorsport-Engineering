import fastf1
import pandas as pd

# Años que queremos cargar
years = [2020, 2021, 2022, 2023, 2024, 2025]
GP = 'Spanish Grand Prix'
gps_data = {
    "Spain": 4.657,
    "British Grand Prix": 5.891,
    "Italian Grand Prix": 5.793,
    "Belgian Grand Prix": 7.004,
    "Bahrain Grand Prix": 5.412
}
# La Q es de Qualy, y FP1/FP2/FP3 indican que sesion de entrenamientos libres
sessions_to_load = ['FP1', 'FP2', 'FP3', 'Q']

# Lista para guardar DataFrames de vueltas
all_laps = []
for year in years:
    for ses in sessions_to_load:
        try:
            print(f"Loading {year} {ses}")
            session = fastf1.get_session(year, "Spain", ses)
            session.load()
            laps = session.laps.copy()
            laps['LapTime(s)'] = laps["LapTime"].dt.total_seconds()
            laps['GP'] = 'Spain'
            laps["CircuitDistance"] = 4.657
            laps["Year"] = year
            laps["Session"] = ses
            all_laps.append(laps)

        except Exception as e:
            print(f"Failed {year} {ses}: {e}")

laps_all = pd.concat(all_laps, ignore_index=True)

laps_all.to_csv("Spain.csv", index=False)

print("Shape del dataset:", laps_all.shape)
laps_all.info()
laps_all.describe()


# CARGA DATASET SOLO MONACO
all_laps_test = []

# 2025
session_ = fastf1.get_session(2025, "Monaco", 'Q')
session_.load()
laps_ = session_.laps.copy()
laps_['LapTime(s)'] = laps_["LapTime"].dt.total_seconds()
laps_["CircuitDistance"] = 3.337
laps_["Year"] = 2025
laps_["Session"] = 'Q'
laps_[GP] = 'Monaco'
all_laps_test.append(laps_)

# 2024
session_ = fastf1.get_session(2024, "Monaco", 'Q')
session_.load()
laps_ = session_.laps.copy()
laps_['LapTime(s)'] = laps_["LapTime"].dt.total_seconds()
laps_["CircuitDistance"] = 3.337
laps_["Year"] = 2024
laps_["Session"] = 'Q'
laps_[GP] = 'Monaco'
all_laps_test.append(laps_)

# 2023
session_ = fastf1.get_session(2023, "Monaco", 'Q')
session_.load()
laps_ = session_.laps.copy()
laps_['LapTime(s)'] = laps_["LapTime"].dt.total_seconds()
laps_["CircuitDistance"] = 3.337
laps_["Year"] = 2023
laps_["Session"] = 'Q'
laps_[GP] = 'Monaco'
all_laps_test.append(laps_)

laps_test = pd.concat(all_laps_test, ignore_index=True)
laps_test.to_csv("Monaco_test.csv", index=False)

print("Monaco del dataset:", laps_test.shape)


# CARGA DATASET TODOS
all_laps2 = []
for year in years:
    for gp, dist in gps_data.items():
        for ses in sessions_to_load:
            try:
                print(f"Loading {year} {gp} {ses}")
                session = fastf1.get_session(year, gp, ses)
                session.load()
                laps = session.laps.copy()
                laps['LapTime(s)'] = laps["LapTime"].dt.total_seconds()
                laps['GP'] = gp
                laps["CircuitDistance"] = dist
                laps["Year"] = year
                laps["Session"] = ses
                all_laps2.append(laps)

            except Exception as e:
                print(f"Failed {year} {gp} {ses}: {e}")

laps_all2 = pd.concat(all_laps2, ignore_index=True)
laps_all2.to_csv("All_GPs.csv", index=False)
print("Shape del dataset:", laps_all2.shape)
