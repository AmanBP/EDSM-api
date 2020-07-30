import requests
import csv

def sif(name):
    '''System info finder'''
    found = 0
    star_csv = open('stars.csv','r')
    for line in star_csv:
        if name in line:
            found = 1
            print("Found",name,"in the saved file. \nDetails:",line)
    star_csv.close()     
    if found == 0:
        print(name,"was not found in the file, requesting details from EDSM.net!")
        requestData = {"systemName":name,"showCoordinates":1}
        data = requests.get("https://www.edsm.net/api-v1/system",requestData)
        if data.status_code == 200:
            print("Server returned Sucess(200)... Parsing Data!")
            d = data.json()
            print("Printing details:")
            print("\t",d['name'])
            print('\t\tx =',d['coords']['x'])
            print('\t\ty =',d['coords']['y'])
            print('\t\tz =',d['coords']['z'])
            print("Adding to stars.csv!")
            with open('stars.csv',mode = "a",newline = '') as st:    
                star_wr=csv.writer(st,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
                star_wr.writerow([d["name"],d['coords']['x'],d['coords']['y'],d['coords']['z']])
            st.close()
        else:
            raise ("request returned bad response code %d" % (data.status_code))

def distance(x1,y1,z1,x2,y2,z2):
    a = pow(x1-x2,2)
    b = pow(y1-y2,2)
    c = pow(z1-z2,2)
    return pow(a+b+c,0.5)

empi = ["Ch'eng","Amenta","Achenar","Omicron Gruis","HR 1475","Grebegus","Theta Indi","Shinigami","HIP 113632","Sekh","Mandhrithar","Pictavul","HR 571",
        "Gliese 900.1","HIP 10694","LTT 16385","Iota Hydri","Siksikas","HR 706","Nunus","Beker","HIP 11661","Eta-2 Hydri","Gabjaujis","Quile",
        "Facece","Jumuzgo","HIP 118169","Piorimudjar","Serktomes","Tiangchi","Cubeo"]

feds = ["G 203-47","Blatrimpe","Oduduro","Sol","Inti","HR 5632","Coriccha","LP 339-7","Rana","Thunderbird","BD-00 632","Aura","LHS 6309","Eta-1 Pictoris",
        "Beta Trianguli Australis","Dao Jungu","19 Phi-2 Ceti","Duamta","BD+49 1280","Rhea","MET 20","Lalande 22701","13 Orionis","Idununn","Hyldekagati",
        "Ugrashtrim","n Puppis","Kalb","LHS 142","Laksak","LTT 4599","Hu Jona","V640 Cassiopeia","Dierfar","41 Lambda Hydrae","Uchaluroja"]

traders = ["Timbalderis","LHS 317","Heveri","CPD-51 3323","Nagnatae","Aasgay","Berzitibi","Helgaedi","LHS 277","Salibal","Nyanktona","Varayah","Liu Links",
           "Nanditi","Belanit","LP 672-42","Winiama","Mundii","Kwattrages","Bunuras","Kayimali","Ross 478","Leucosimha","LTT 4376","CD-30 9687","Tian Di",
           "LHS 54","LHS 2494","Monoto","Condovichs","Lombi","BV Phoenicis","Beta-2 Tucanae","Pleutarama","Damona","Ruganike","Karama","Miquitagat",
           "Shanteneri","Dongzi","Mara","Clayahu","Kausan","Ch'i Lin","Badia","Ember","HIP 20277","Putamasin","Crom Dubh","HIP 1885","Maityan","Belanit",
           "Luan Yun Di","Sungai","Ye'kuape","Nyanktona","Nagnatae","Corngari","Liu Links","Hmargk","Nanditi","Berzitibi","Callici","Monoto","Mantuate",
           "Ngombivas","Aasgay","Timbalderis","Hun Chonses","Salibal","Corn Pin","Wiljanherbi","Helgaedi","HIP 80221","CPD-51 3323","Arigens","Contien"]

def mapper():
    file1 = open("stars.csv",mode = "r")
    newdic = {}
    for line in file1:
        words = line.rstrip().split(",")
        output = {words[0] : words[1:]}
        newdic.update(output)
    file1.close()
    closest_empis = []
    for trader in traders:
        em_dist = []
        for emp in empi:
            em_dist.append(distance(float(newdic[trader][0]),float(newdic[trader][1]),float(newdic[trader][2]),float(newdic[emp][0]),float(newdic[emp][1]),float(newdic[emp][2])))
        closest = em_dist.index(min(em_dist))
        print(empi[closest])

    for syss in empi:
        for trader in traders:
            
def make_csv():
    for place in empi:
        sif(place)
    for place in feds:
        sif(place)
    for place in traders:
        sif(place)


def main():
    mapper()

if __name__ == "__main__":
    main()