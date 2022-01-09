import os 
import pandas as pd 
import numpy as np  
mutate_sites = [28,29,30,31,32,33, 37,38,54,55,56 ] # 突变位点 
var58_dict = '/Users/xrk.study/Desktop/var58' 
def get_seq(fasta) : 
    num_seq = {}    # dict record relations between number and sequence 
    i = 0 
    with open(fasta , 'r+') as f : 
        for line in f : 
            if line.startswith('>') : 
                continue 
            else : 
                i +=1 
                num_seq[i] = line.strip()
    return num_seq  
    os.chdir('/Users/xrk.study/Desktop/var58')
base_path = '/Users/xrk.study/Desktop/var58/var58_mutations'
# os.mkdir('/Users/xrk.study/Desktop/var58/var58_mutations')
os.chdir('/Users/xrk.study/Desktop/var58/var58_mutations') 
for x in seqs : 
    print(x)
    os.mkdir(os.path.join(base_path , x)) 
    os.chdir(os.path.join(base_path, x ))     # 切换到 突变的目录下  
    os.system('rm -rf chains_to_move.txt') 
    os.system('rm -rf nataa_mutations.resfile')
    os.system('touch chains_to_move.txt') 
    os.system('touch nataa_mutations.resfile')
    with open('chains_to_move.txt' , 'r+') as f : 
        f.write('B')
        f.write('\n') 
        f.close() 
    with open('nataa_mutations.resfile' , 'r+') as f1 : 
        f1.write('NATAA') 
        f1.write('\n') 
        f1.write('start')
        f1.write('\n') 
        for i in range(len(x)) : 
            f1.write(str(mutate_sites[i]) ) 
            f1.write(' ')
            f1.write('A PIKAA') 
            f1.write(' ') 
            f1.write(x[i])
            f1.write('\n') 
        f1.close()  
