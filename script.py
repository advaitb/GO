# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import scipy.stats as stats
with open('/Users/advaitbalaji/Downloads/AdvaitB/vgenes_not_in_suppl_enrichr.txt','r') as openfile:
    content = [x.strip('\n') for x  in openfile.readlines()]
print('Genelist Okay')
data = pd.read_csv('/Users/advaitbalaji/Downloads/AdvaitB/Article_screen_combined_mbc_Gene_symbol_Brute_force.txt', sep='\t', header=0)
data = data[data.ProcessLevel == 3]
print('Ready!')
#content =  data.Symbol.unique()
#content = content.tolist()
'''
arr = []
for gene in content:
    df_temp = data[data['Symbol'] == gene]
    arr.append(df_temp)
final_frame = pd.concat(arr)
'''
modified_content = [(content[i],content[j]) for i in range(len(content)) for j in range(i+1, len(content))]

#def commonelements( a, b):
#    return list(set(a) & set(b))
print('Process Beginning...')    
for i in range(len(modified_content)):
    genea,geneb = modified_content[i]
    df_temp1 = data[data.Symbol == genea]
    df_temp2 = data[data.Symbol == geneb]
    processa  = df_temp1.ProcessName.unique().tolist()
    processb  = df_temp2.ProcessName.unique().tolist()
    totala = len(processa)
    totalb = len(processb)
    pp_list = [process for process in processa if process in processb]
    pp = len(pp_list)
    print('Genepair ' +str(i) + ' has '+ str(pp)+ ' processes in common.')
    pnp = totalb - pp
    npp = totala - pp
    temp = 780 - totala
    npnp = temp-pnp
    oddsratio, pvalue =  stats.fisher_exact([[pp,pnp],[npp,npnp]])
    #final_table[(genea,geneb)]= pvalue
    print('Genepair' + ' ' +str(i)+ '/'+str(len(modified_content)) +' ------>' + '    '+ genea + '    ' + geneb + '......' + str(pvalue) + '\n')
    with open('/Users/advaitbalaji/Downloads/AdvaitB/fp_contingencyfile_process.txt','a+') as f:
        f.write(genea+'\t'+geneb+'\t'+ str(pp) + '\t' + str(pnp) + '\t' + str(npp) + '\t' + str(npnp) + '\t' + str(pvalue) +'\n')
#print(final_table)