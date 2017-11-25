names=[1047, 1691, 1755, 1858, 1993, 4178, 4393, 4584, 5264, 6338, 6412, 6438, 6501, 6812, 8108, 8161, 8326, 8369, 8716, 9016, 9018, 9257, 9489, 9868, 10356, 10377]
fp=open("decision_tree_train.csv","r")
t_len=0
for i in fp:
	if(i[0]=='s'):
		continue
	t_len+=1
	if(t_len-1 in names):
		print(i)