```import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

sample ='90_cal'
#define the path for the samtools_depth output
def influenza_coverage(sample):
    path = 'depth/'+sample+'.consensus.depth.tsv'
    df = pd.read_csv(path, sep='\t',header = None) 
    df.columns =['Gene_segment', 'Position', 'Depth']
    df_sub = df.Gene_segment.str.split("|",expand = True)
    df['Segment'] = pd.DataFrame(df_sub[1])
    ###
    PB2 = (len(df[df['Segment']=='PB2']))
    PB1 = (len(df[df['Segment']=='PB1']))
    PA = (len(df[df['Segment']=='PA']))
    HA = (len(df[df['Segment']=='HA']))
    NP = (len(df[df['Segment']=='NP']))
    NA = (len(df[df['Segment']=='NA']))
    MP = (len(df[df['Segment']=='MP']))
    NS = (len(df[df['Segment']=='NS']))
    #calculate the position for each gene segments    
    PB2_pos = PB2
    PB1_pos = PB1+PB2_pos
    PA_pos = PA + PB1_pos
    HA_pos = HA + PA_pos
    NP_pos = NP + HA_pos
    NA_pos = NA + NP_pos
    MP_pos = MP + NA_pos
    NS_pos = NS + MP_pos
    # add the constant to depth for rows where gene segment equals target_gene_segment
    df.loc[df['Segment'] == 'PB1', 'Position'] += PB2_pos
    df.loc[df['Segment'] == 'PA', 'Position'] += PB1_pos
    df.loc[df['Segment'] == 'HA', 'Position'] += PA_pos
    df.loc[df['Segment'] == 'NP', 'Position'] += HA_pos
    df.loc[df['Segment'] == 'NA', 'Position'] += NP_pos
    df.loc[df['Segment'] == 'MP', 'Position'] += NA_pos
    df.loc[df['Segment'] == 'NS', 'Position'] += MP_pos
    # print the resulting dataframe
    plt.rcParams["figure.figsize"] = [10,4]
    plt.rcParams["figure.autolayout"] = True
    sns.lineplot(data=df, x="Position", y="Depth")
    axes = plt.gca()
    axes.set_xlim([-10, 13151])
    axes.set_ylim([-0.02,5000])
    plt.xlabel('Influenza Genome Position',fontsize=14)
    plt.ylabel('Read Depth',fontsize=13)
    plt.axvspan(0, 2280, color='peru', alpha=0.2, label='PB2')
    plt.axvspan(2280, 4554, color='burlywood', alpha=0.2, label='PB1')
    plt.axvspan(4554, 6705, color='blanchedalmond', alpha=0.2, label='PA')
    plt.axvspan(6705, 8406, color='wheat', alpha=0.2, label='HA')
    plt.axvspan(8406, 9921, color='khaki', alpha=0.2, label='NP')
    plt.axvspan(9921, 11331, color='beige', alpha=0.2, label='NA')
    plt.axvspan(11331, 12313, color='peachpuff', alpha=0.2, label='MP')
    plt.axvspan(12313, 13151, color='y', alpha=0.3, label='NS')
    #adding legend to the graph
    plt.legend()
    plt.text(900,5200, "PB2", size=13,rotation =0)
    plt.text(3200,5200, "PB1", size=13,rotation =0)
    plt.text(5500,5200, "PA", size=13,rotation =0)
    plt.text(7400,5200, "HA", size=13,rotation =0)
    plt.text(9000,5200, "NP", size=13,rotation =0)
    plt.text(10500,5200, "NA", size=13,rotation =0)
    plt.text(11680,5200, "MP", size=13,rotation =0)
    plt.text(12600,5200, "NS", size=13,rotation =0)
    plt.axhline(y = 200, color = 'black', linestyle = 'dashed', alpha=0.4)
    #plt.savefig('depth/sample_read_depth.pdf', dpi=300) ```
