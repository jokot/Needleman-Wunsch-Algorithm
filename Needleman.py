import numpy as np

def createBlosum62():
    blosum62 = {
    'C':{'C':9, 'S':-1, 'T':-1, 'P':-3, 'A':0,  'G':-3, 'N':-3, 'D':-3, 'E':-4, 'Q':-3, 'H':-3, 'R':-3, 'K':-3, 'M':-1, 'I':-1, 'L':-1, 'V':-1, 'F':-2, 'Y':-2, 'W':-2},
    'S':{'C':-1,'S':4,  'T':1,  'P':-1, 'A':1,  'G':0,  'N':1,  'D':0,  'E':0,  'Q':0,  'H':-1, 'R':-1, 'K':0,  'M':-1, 'I':-2, 'L':-2, 'V':-2, 'F':-2, 'Y':-2, 'W':-3},
    'T':{'C':-1,'S':1,  'T':4,  'P':1,  'A':-1, 'G':1,  'N':0,  'D':1,  'E':0,  'Q':0,  'H':0,  'R':-1, 'K':0,  'M':-1, 'I':-2, 'L':-2, 'V':-2, 'F':-2, 'Y':-2, 'W':-3},
    'P':{'C':-3,'S':-1, 'T':1,  'P':7,  'A':-1, 'G':-2, 'N':-2, 'D':-1, 'E':-1, 'Q':-1, 'H':-2, 'R':-2, 'K':-1, 'M':-2, 'I':-3, 'L':-3, 'V':-2, 'F':-4, 'Y':-3, 'W':-4},
    'A':{'C':0, 'S':1,  'T':-1, 'P':-1, 'A':4,  'G':0,  'N':-2, 'D':-2, 'E':-1, 'Q':-1, 'H':-2, 'R':-1, 'K':-1, 'M':-1, 'I':-1, 'L':-1, 'V':0, 'F':-2, 'Y':-2, 'W':-3},
    'G':{'C':-3,'S':0,  'T':1,  'P':-2, 'A':0,  'G':6,  'N':0, 'D':-1, 'E':-2, 'Q':-2, 'H':-2, 'R':-2, 'K':-2, 'M':-3, 'I':-4, 'L':-4, 'V':-3,  'F':-3, 'Y':-3, 'W':-2},
    'N':{'C':-3,'S':1,  'T':0,  'P':-2, 'A':-2, 'G':0,  'N':6,  'D':1,  'E':0,  'Q':0,  'H':1, 'R':0,  'K':0,  'M':-2, 'I':-3, 'L':-3, 'V':-3, 'F':-3, 'Y':-2, 'W':-4},
    'D':{'C':-3,'S':0,  'T':1,  'P':-1, 'A':-2, 'G':-1, 'N':1,  'D':6,  'E':2,  'Q':0,  'H':-1, 'R':-2, 'K':-1, 'M':-3, 'I':-3, 'L':-4, 'V':-3, 'F':-3, 'Y':-3, 'W':-4},
    'E':{'C':-4,'S':0,  'T':0,  'P':-1, 'A':-1, 'G':-2, 'N':0,  'D':2,  'E':5,  'Q':2,  'H':0,  'R':0,  'K':1,  'M':-2, 'I':-3, 'L':-3, 'V':-2, 'F':-3, 'Y':-2, 'W':-3},
    'Q':{'C':-3,'S':0,  'T':0,  'P':-1, 'A':-1, 'G':-2, 'N':0,  'D':0,  'E':2,  'Q':5,  'H':0,  'R':1,  'K':1,  'M':0,  'I':-3, 'L':-2, 'V':-2, 'F':-3, 'Y':-1, 'W':-2},
    'H':{'C':-3,'S':-1, 'T':0,  'P':-2, 'A':-2, 'G':-2, 'N':1,  'D':-1,  'E':0,  'Q':0,  'H':8,  'R':0,  'K':-1, 'M':-2, 'I':-3, 'L':-3, 'V':-3, 'F':-1, 'Y':2,  'W':-2},
    'R':{'C':-3,'S':-1, 'T':-1, 'P':-2, 'A':-1, 'G':-2, 'N':0,  'D':-2, 'E':0,  'Q':1,  'H':0,  'R':5,  'K':2,  'M':-1, 'I':-3, 'L':-2, 'V':-3, 'F':-3, 'Y':-2, 'W':-3},
    'K':{'C':-3,'S':0,  'T':0,  'P':-1, 'A':-1, 'G':-2, 'N':0,  'D':-1, 'E':1,  'Q':1,  'H':-1, 'R':2,  'K':5,  'M':-1, 'I':-3, 'L':-2, 'V':-2, 'F':-3, 'Y':-2, 'W':-3},
    'M':{'C':-1,'S':-1, 'T':-1, 'P':-2, 'A':-1, 'G':-3, 'N':-2, 'D':-3, 'E':-2, 'Q':0,  'H':-2, 'R':-1, 'K':-1, 'M':5,  'I':1,  'L':2,  'V':1, 'F':0,  'Y':-1, 'W':-1},
    'I':{'C':-1,'S':-2, 'T':-2, 'P':-3, 'A':-1, 'G':-4, 'N':-3, 'D':-3, 'E':-3, 'Q':-3, 'H':-3, 'R':-3, 'K':-3, 'M':1,  'I':4,  'L':2,  'V':3,  'F':0,  'Y':-1, 'W':-3},
    'L':{'C':-1,'S':-2, 'T':-2, 'P':-3, 'A':-1, 'G':-4, 'N':-3, 'D':-4, 'E':-3, 'Q':-2, 'H':-3, 'R':-2, 'K':-2, 'M':2,  'I':2,  'L':4,  'V':1,  'F':0,  'Y':-1, 'W':-2},
    'V':{'C':-1,'S':-2, 'T':-2, 'P':-2, 'A':0,  'G':-3, 'N':-3, 'D':-3, 'E':-2, 'Q':-2, 'H':-3, 'R':-3, 'K':-2, 'M':1,  'I':3,  'L':1,  'V':4,  'F':-1, 'Y':-1, 'W':-3},
    'F':{'C':-2,'S':-2, 'T':-2, 'P':-4, 'A':-2, 'G':-3, 'N':-3, 'D':-3, 'E':-3, 'Q':-3, 'H':-1, 'R':-3, 'K':-3, 'M':0,  'I':0,  'L':0,  'V':-1, 'F':6,  'Y':3,  'W':1},
    'Y':{'C':-2,'S':-2, 'T':-2, 'P':-3, 'A':-2, 'G':-3, 'N':-2, 'D':-3, 'E':-2, 'Q':-1, 'H':2,  'R':-2, 'K':-2, 'M':-1, 'I':-1, 'L':-1, 'V':-1, 'F':3,  'Y':7,  'W':2},
    'W':{'C':-2,'S':-3, 'T':-3, 'P':-4, 'A':-3, 'G':-2, 'N':-4, 'D':-4, 'E':-3, 'Q':-2, 'H':-2, 'R':-3, 'K':-3, 'M':-1, 'I':-3, 'L':-2, 'V':-3, 'F':1,  'Y':2,  'W':11}
    }
    return blosum62

def needlemanWunsch():
    S = np.zeros((height,width))
    Track = np.chararray((height,width),unicode=True)
    Track[:]=''

    for i in range(height):
        for j in range(width):
            if(i==0): S[i][j]=-6*j
            elif(j==0): S[i][j]=-6*i
            else:         
                blosumScore = blosum62[sequence1[i-1]][sequence2[j-1]]               
                diagonal = S[i-1][j-1]+blosumScore

                # vertical = S[i-1][j]-6
                # horizontal = S[i][j-1]-6

                vertical = max([S[x][j]-6*(i-x) for x in range(0,i)])
                horizontal = max([S[i][x]-6*(j-x) for x in range(0,j)])            
                S[i][j] = max(diagonal,vertical,horizontal)
                if(S[i][j]==diagonal):
                    Track[i][j]='D'
                elif(S[i][j]==vertical):
                    Track[i][j]='V'
                else: 
                    Track[i][j]='H'

    return S,Track

def sequenceAlligment():
    i = height-1
    j = width-1

    alignment1 = ''
    alignment2 = ''

    while(i>0 or j>0):        
        # print(i,j)
        arrow = Track[i][j] 
        # print(arrow)       
        if(arrow=='D'):
            alignment1=sequence1[i-1]+alignment1
            alignment2=sequence2[j-1]+alignment2
            i = i-1
            j = j-1
        elif(arrow=='V'):
            alignment1=sequence1[i-1]+alignment1
            alignment2='-'+alignment2
            i = i-1
        else:
            alignment1='-'+alignment1
            alignment2=sequence2[j-1]+alignment2
            j = j-1
    
    return alignment1,alignment2


if __name__ == "__main__":
    
    blosum62 = createBlosum62()

#     sequence1 = 'NALMSQA'
#     sequence2 = 'MNALQM'

    sequence1 = 'WFGTHKF'
    sequence2 = 'TWFGKT'
    
    height = len(sequence1)+1
    width = len(sequence2)+1

    S,Track = needlemanWunsch()

    print("Score:")            
    print(S)
    print("Track:")
    print(Track)

    alignment1,alignment2 = sequenceAlligment()

    print("Sequence Alligment:")
    print(alignment1)
    print(alignment2)