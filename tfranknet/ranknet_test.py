import os
import numpy as np
from ranknet import RankNet
from sklearn.cross_validation import cross_val_predict

os.system("rm -rf testlog")
data1 = np.random.rand(10000, 30)
data2 = np.random.rand(10000, 30)
label = [True]*10000

rn = RankNet(hidden_units=[20, 10], logdir="testlog",
             learning_rate=0.01)
data = rn.pack_data(data1, data2)

cvpred = cross_val_predict(rn, data, label, cv=2)

rn.fit(data)

input1 = np.random.rand(10, 30)
input2 = np.random.rand(10, 30)
input_ = rn.pack_data(input1, input2)
prob = rn.predict_prob(input_)
pred = rn.predict(input_)
score = rn.get_scores(input1)
score = rn.get_scores(input2)
