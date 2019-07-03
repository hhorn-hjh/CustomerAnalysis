import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "SimHei"
plt.rcParams["axes.unicode_minus"] = False


def get_data():         # function for getting the Analysis data,
    data = pd.read_csv("air_data.csv")
    data = data[data["SUM_YR_1"].notnull() & data["SUM_YR_2"].notnull()]
    index1 = data['SUM_YR_1'] != 0
    index2 = data['SUM_YR_2'] != 0
    index3 = (data['SEG_KM_SUM'] == 0) & (data['avg_discount'] == 0)
    data = data[index1 | index2 | index3]
    return data


def reduction_data(data):
    data = data[['LOAD_TIME', 'FFP_DATE', 'LAST_TO_END',
                 'FLIGHT_COUNT', 'SEG_KM_SUM', 'avg_discount']]
    d_ffp = pd.to_datetime(data['FFP_DATE'])
    d_load = pd.to_datetime(data['LOAD_TIME'])
    res = d_load - d_ffp
    data2 = data.copy()
    data2['L'] = res.map(lambda x: x / np.timedelta64(30 * 24 * 60, 'm'))
    data2['R'] = data['LAST_TO_END']
    data2['F'] = data['FLIGHT_COUNT']
    data2['M'] = data['SEG_KM_SUM']
    data2['C'] = data['avg_discount']
    data3 = data2[['L', 'R', 'F', 'M', 'C']]
    return data3


def zscore_data(data):
    data = (data - data.mean(axis=0)) / data.std(axis=0)
    data.columns = ['Z' + i for i in data.columns]
    return data


def analysis():                 # algorithms for the analysis process
    k = 5
    data = get_data()
    data3 = reduction_data(data)
    data4 = zscore_data(data3)
    kmodel = KMeans(n_clusters=k, n_jobs=4)
    kmodel.fit(data4)
    r1 = pd.Series(kmodel.labels_).value_counts()
    r2 = pd.DataFrame(kmodel.cluster_centers_)
    r = pd.concat([r2, r1], axis=1)
    r.columns = list(data4.columns) + ['类别数目']
    # print(r)
    r.to_csv("out1.csv",index=False)
    r = pd.concat([data4, pd.Series(kmodel.labels_, index=data4.index)], axis=1)
    r.columns = list(data4.columns) + ['Level']
    r.to_csv("out2.csv", index=False)


analysis()





