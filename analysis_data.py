import pandas as pd
import analysis_process as ap
# Write Your function for analysis data here


class AnalysisData(object):

    def __init__(self):
        self.data = ap.get_data()
        self.data1 = pd.read_csv('out1.csv')
        self.data2 = pd.read_csv('out2.csv', encoding='utf-8')

    def LRFMC(self):
        li = list()
        li.append(self.data1.iloc[0])
        li.append(self.data1.iloc[1])
        li.append(self.data1.iloc[2])
        li.append(self.data1.iloc[3])
        li.append(self.data1.iloc[4])
        res = list()
        for l in li:
            for t in l:
                res.append(t)
        return res

    def classification(self):
        l1 = self.data[self.data["Level"] == 0]
        l2 = self.data[self.data["Level"] == 1]
        l3 = self.data[self.data["Level"] == 2]
        l4 = self.data[self.data["Level"] == 3]
        l5 = self.data[self.data["Level"] == 4]
        n1 = l1["Level"].count()
        n2 = l2["Level"].count()
        n3 = l3["Level"].count()
        n4 = l4["Level"].count()
        n5 = l5["Level"].count()
        return n1, n2, n3, n4, n5


analysis_data = AnalysisData()