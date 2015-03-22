from glob import glob

# read list of files, sorting later

filelist = glob('wc_input/*.txt')

# because the numbers we are dealing with are integers, so I create a list as a histogram of length of lines

histogram = [0]

# initiate parameters storing total number of lines and maximum length

total = 0
maximum = 0

result = open('wc_output/med_result.txt','w')

# read file alphabetical

for filename in sorted(filelist):
    
    # read file and lines
    
    content = open(filename,'r')
    lines = content.readlines()
    
    for line in lines:
        
        # get line length
        
        number = len(line.split())
        
        # increase histogram size if needed
        
        if number > maximum:
            addlist = [0]*(number-maximum)
            histogram.extend(addlist)
            maximum = number
    
        # store the line length in histogram
    
        histogram[number] += 1
        
        # update the total numbers for calculation
        
        total += 1
        
        # initiate iterator and parameter for calculating median
        
        count = 0
        index = 0
        
        # add up from 0th of the histogram
        
        for index in range(maximum+1):
            
            # calculated the added up amount in the histogram
            
            count += histogram[index]
            
            # in case of even total numbers and the middle two elements are different
            
            if count == total/2.0:
                
                # find the next nonzero element in histogram, then calculate the mean as the median
                
                for right in range(index+1,maximum+1):
                    if histogram[right] != 0:
                        median = (right+index)*0.5
                        break
                break
        
            # otherwise, when the added up amount cover the median position, we have the result
        
            elif count > total/2.0:
                median = index
                break
    
        # write to output
    
        result.write('%s\n' %(median))
    
    content.close()

result.close()



