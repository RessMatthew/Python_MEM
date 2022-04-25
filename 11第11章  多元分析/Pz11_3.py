# 程序文件Pz11_3
import matplotlib.pyplot as plt
import numpy as np;
from sklearn.cluster import KMeans;

X = np.load("Pzdata11_1.npy")
TSSE = [];
K = 10
for k in range(1, K + 1):
    SSE = []
    md = KMeans(n_clusters=k);
    md.fit(X)
    labels = md.labels_;
    centers = md.cluster_centers_
    for label in set(labels):
        SSE.append(np._sum((X[labels == label, :] - centers[label, :]) ** 2))
    TSSE.append(np._sum(SSE))
plt.rc('font', family='SimHei');
plt.style.use('ggplot');
plt.plot(range(1, K + 1), TSSE, 'b*-')
plt.xlabel('簇的个数');
plt.ylabel('簇内离差平方和之和');
plt.show()
