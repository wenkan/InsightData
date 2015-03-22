from glob import glob

# get files in input folder

filelist = glob('wc_input/*.txt')

# set the symbols to remove

striplist = [',','.',';','-',"'"]

# create empty dict for word count

wc = {}

#read from file to file

for filename in filelist:
    
    content = open(filename,'r')
    
    #load file content into list of words
    
    words = content.read().lower().split()
    
    for word in words:
        
        #strip symbols
        
        for symbol in striplist:
            
            if symbol in word:
                
                word = word.replace(symbol,'')
    
    #check and store word count

        if word in wc:
            
            wc[word] += 1
        
        else:
            
            wc[word] = 1

    content.close()

#write result to output file

result = open('wc_output/wc_result.txt','w')

for key in sorted(wc):
    result.write('%-8s\t%s\n' %(key, wc[key]))

result.close()




