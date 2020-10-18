
'''

A set of utility function that can convert csv file data in json format

'''

import json
def csvToFile(fileName, outputName):
    if fileName==None or type(fileName) != str:
        raise Exception('Entered file name is invalid')

    with open(fileName) as f:
        header = f.readline().strip().split(',')

        data_arr = [
            dict(zip(header, line.strip().split(',')))
            for line in f
        ]
        # for line in f:
        #     values = line.strip().split(',')
        #     data = dict(zip(header, values))
        #     data_arr.append(data)

    with open(outputName, mode='w') as o:
        json.dump(data_arr, o, indent=3)

def main():
    inputfile = str(input('Entered .csv file name: '))
    outptfile = str(input('Entered output file name: '))
    csvToFile(inputfile, outptfile)

if __name__ == "__main__":
    main()
