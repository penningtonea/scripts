import pandas as pd 
with open('input_file.csv') as inputFile:
    df = pd.read_csv(inputFile)
    
# categorize rows based on mature peptide
bins=[0,489,588,1148,1436]
labels=['gag','protease','reverse transcriptase','integrase']    
df['labels']=pd.cut(df['AAPOS'], bins=bins, labels=labels, include_lowest=True) 

# change the value in CDS to reflect the mature peptides
df.loc[df['labels']=='protease', 'CDS'] = 'NP_705926.1'
df.loc[df['labels']=='reverse transcriptase', 'CDS'] = 'NP_705927.1'
df.loc[df['labels']=='integrase', 'CDS'] = 'NP_705928.1'

# Change AAPOS to the correct value mapped to the mature peptide
df.loc[df['labels'] == 'protease','AAPOS'] -= 488
df.loc[df['labels'] == 'reverse transcriptase','AAPOS'] -= 587
df.loc[df['labels'] == 'integrase','AAPOS'] -= 1147

# remove gag-pol rows that are not in the mature peptide CDS regions and save to a new CSV file labeled "outfile"
slabels = ['protease','reverse transcriptase','integrase']
df1 = df[df['labels'].isin(slabels)]
df1.drop('labels', axis=1, inplace=True)
df1.to_csv('outfile.csv', index=False)