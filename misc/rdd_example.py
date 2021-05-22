## Example for RDD

def read_file(file_name):
    res = []
    with open(file_name, 'r') as f:
        while True:
            line = f.readline()
            if (len(line) == 0):
                break
            res.append(line)
    return res

def mapper(input):
    """
    mapper of paper_conference table
    @input (paperID, paper name, year, conference ID)
    @output (conferenceID, tagA, paper_name)
    """
    output = []
    for line in input:
        line=line.strip()
        entry=line.split('\t')
        output.append(f"{entry[-1]}\tA\t{entry[1]}")
    return output


def mapper(input):
    """
    mapper of paper_conference table
    @input (conferenceID, conferenceName)
    @output (conferenceID, tagB, conference_name)
    """
    output = []
    for line in input:
        line=line.strip()
        entry=line.split('\t')
        output.append(f"{entry[1]}\tB\t{entry[0]}")
    return output



def reducer(input):
    """
    Write your reducer code here,
    the reducer should tak in a list of strings as input
    and return a list of strings as output
    """
    join_dict1 = {}
    join_dict2 = {}
    output = []

    for line in input:
        # remove leading and trailing whitespace
        line = line.strip()

        # parse the input we got from mapper.py
        entry = line.split("\t")
        tag = entry[1]
        conf_id = entry[0]
        contents = entry[2]
        
        if tag == 'A':
            if conf_id not in join_dict1:
                join_dict1[conf_id] = set()
            join_dict1[conf_id].add(contents)
        else:
            if conf_id not in join_dict2:
                join_dict2[conf_id] = set()
            join_dict2[conf_id].add(contents)
    
    for conf_id in join_dict1.keys():
        for conf in join_dict2[conf_id]:
            if conf_id in join_dict1:
                for paper in join_dict1[conf_id]:
                    output.append(f"{paper}\t{conf}")
    
    return output