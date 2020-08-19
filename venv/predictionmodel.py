import preparation_of_data
import pandas
from sklearn import neural_network,linear_model
data=preparation_of_data.get_pl_from_position('ST')
traindata=pandas.DataFrame(data.iloc[:1000,:])
validata=pandas.DataFrame(data.iloc[1001:1500,:])
traindata_x=preparation_of_data.getbasic_stats(traindata)
traindata_y=preparation_of_data.get_only_ovr(traindata)
validata_x=preparation_of_data.getbasic_stats(validata)
validata_y=preparation_of_data.get_only_ovr(validata)

#clf =  neural_network.MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(400,200),max_iter=5000, random_state=1)
clf=linear_model.LinearRegression()
clf.fit(traindata_x,traindata_y)
predictions=pandas.DataFrame(clf.predict(validata_x)).reset_index()



players_and_ovl=pandas.DataFrame()
players_and_ovl['Player']=validata['player_extended_name']
players_and_ovl['Overall in game']=validata_y
players_and_ovl=players_and_ovl.reset_index()
players_and_ovl['Overall predicted']=predictions.iloc[:,1]
players_and_ovl.to_csv('pilkarze.csv')
params=pandas.DataFrame()
params['Attribute']=validata_x.columns
params['Param']=''
print(players_and_ovl)
for i in range(35):
    params.at[i,'Param']=(clf.coef_[i])
print(params)
params.to_csv('parametry.csv')