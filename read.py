import sys
import pandas as pd

bd = pd.read_csv('../fnc-1/train_bodies.csv',index_col='Body ID')
st = pd.read_csv('../fnc-1/train_stances.csv')

st['article'] = bd.loc[st['Body ID']].values

for idx in st.index:
	if st.loc[idx].Stance==sys.argv[1]:
		sys.stdout.write("Index: %d\n" % idx)
		sys.stdout.write("Claim: %s\n" % st.loc[idx,'Headline'])
		sys.stdout.write("Verdict: %s\n" % st.loc[idx,'Stance'])
		sys.stdout.write("Article:\n%s\n\n\n\n" % st.loc[idx,'article'].replace('\n\n','\n'))
