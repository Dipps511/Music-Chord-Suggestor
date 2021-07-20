f=open('Guitar Chords.txt', 'r')
f1=open('Transposed.txt','a')
f1.truncate(0)
#print(f.read())
Aee=(['C ','C# ','D ','D# ','E ','F ','F# ','G ','G# ','A ','A# ','B ','C ','C# ','D ','D# ','E ','F ','F# ','G ','G# ','A ','A# ','B ','C ','C# ','D ','D# ','E ','F ','F# ','G ','G# ','A ','A# ','B ','C ','C# ','D ','D# ','E ','F ','F# ','G ','G# ','A ','A# ','B '])
#should be space both before and after in Ae or Aee
Ae=([' C',' C#',' D',' D#',' E',' F',' F#',' G',' G#',' A',' A#',' B',' C',' C#',' D',' D#',' E',' F',' F#',' G',' G#',' A',' A#',' B',' C',' C#',' D',' D#',' E',' F',' F#',' G',' G#',' A',' A#',' B',' C',' C#',' D',' D#',' E',' F',' F#',' G',' G#',' A',' A#',' B'])
Aeee=(['C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B'])
Aem=(['Cm ','C#m ','Dm ','D#m ','Em ','Fm ','F#m ','Gm ','G#m ','Am ','A#m ','Bm ','Cm ','C#m ','Dm ','D#m ','Em ','Fm ','F#m ','Gm ','G#m ','Am ','A#m ','Bm ','Cm ','C#m ','Dm ','D#m ','Em ','Fm ','F#m ','Gm ','G#m ','Am ','A#m ','Bm ','Cm ','C#m ','Dm ','D#m ','Em ','Fm ','F#m ','Gm ','G#m ','Am ','A#m ','Bm '])
n = int(input("Transpose key by -3, -2, -1, +1, +2 , +3 "))  # input from user
for i in range(100):
    string=(f.readline())
    #print(string,end='')

    for i in range(12, 24):
        if Aee[i] in string:
            c = '('+Aeee[i + n]+')'  # use.split'(' to remove brackets later
            string = string.replace(Aee[i], c)

    for i in range(12, 24):
        if Aem[i] in string:
            c = '('+Aeee[i + n]+'m)'  # use.split'(' to remove brackets later
            string = string.replace(Aem[i], c)
    for i in range(12, 24):
        if Ae[i] in string:
            c = '('+Aeee[i + n]+')'  # use.split'(' to remove brackets later
            string = string.replace(Ae[i], c)
    print(string, end="")
    f1.write(string)

#print(f.readline())

#f2=open('abc','w')

#for data in f:
 #   print(data)
    #f2.write(data)