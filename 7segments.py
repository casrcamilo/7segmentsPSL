import urllib2,unicodedata

file=open("7segments.txt","r")
infile=file.readlines()
code=""
fullNumber=""
number= {
    ".....|..|": "1",
    "._.._||_.": "2",
    "._.._|._|": "3",
    "...|_|..|": "4",
    "._.|_.._|": "5",
    "._.|_.|_|": "6",
    "._...|..|": "7",
    "._.|_||_|": "8",
    "._.|_|..|": "9",
    "._.|.||_|": "0",
}

for n in range(0,len(infile),3):
        try:
            #a variable goes through the first 3 lines every 4 characters
            for i in range(0,len(infile[n])-1,4):
                #Other variables go throught the 3 characters of every line,
                #read the value of the position and concatenate it in a String. 
                for j in range (n,n+3):
                    for k in range (i,i+3):
                        code=code+infile[j][k]
                fullNumber=fullNumber+number[code]
                code=""
            #print the full Number
            print(fullNumber)
            fullNumber=""
        except:
            print ("Sorry, There was a problem in this line, check the input file and try again.")
            code=""
            fullNumber=""
            continue
