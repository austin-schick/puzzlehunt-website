import random

letterDict = {
    "a": ['<td><img src="staff-photos/yuzhes.jpg"/>Alex (yuzhes)</td>', '<td><img src="staff-photos/ambikac.jpg"/>Ambika (ambikac)</td>',
          '<td><img src="staff-photos/agwu.jpg"/>Amy (agwu)</td>', '<td><img src="staff-photos/arestrad.jpg"/>Andrea (arestrad)</td>',
          '<td><img src="staff-photos/aschreff.jpg"/>Andrew (aschreff)</td>', '<td><img src="staff-photos/asilbaug.jpg"/>Anne (asilbaug)</td>',
          '<td><img src="staff-photos/ahavanur.jpg"/>Apoorva (ahavanur)</td>', '<td><img src="staff-photos/aschick.jpg"/>Austin (aschick)</td>',
          '<td><img src="staff-photos/armanh.jpg"/>Arman (armanh)</td>'],
    "b": ['<td><img src="staff-photos/ybb.png"/>Bulut (ybb)</td>'],
    "c": ['<td><img src="staff-photos/mengyinf.jpg"/>Cathy (mengyinf)</td>', '<td><img src="staff-photos/cwurman.jpg"/>Chaya (cwurman)</td>'],
    "d": ['<td><img src="staff-photos/dzq.jpg"/>Doug (dzq)</td>'],
    "e": ['<td><img src="staff-photos/edryer.jpg"/>Eddie (edryer)</td>', '<td><img src="staff-photos/eclinch.jpg"/>Eric (eclinch)</td>', '<td><img src="staff-photos/eyluo.jpg"/>Eugene (eyluo)</td>'],
    "f": ['<td><img src="staff-photos/fmarsh.jpg"/>Fletcher (fmarsh)</td>'],
    "g": ['<td><img src="staff-photos/kghiam.jpg"/>Kamyar (k<strong>g</strong>hiam)</td>'],
    "h": ['<td><img src="staff-photos/hshalaby.png"/>Habiba (hshalaby)</td>', '<td><img src="staff-photos/hnelson1.jpg"/>Henry (hnelson1)</td>'],
    "i": ['<td><img src="staff-photos/aykilinc.jpg"/>Ike (aykilinc)</td>'],
    "j": ['<td><img src="staff-photos/jxgong.jpg"/>Jason G. (jxgong)</td>', '<td><img src="staff-photos/jasonh1.jpg"/>Jason H. (jasonh1)</td>', '<td><img src="staff-photos/judyz.jpg"/>Judy (judyz)</td>', '<td><img src="staff-photos/oweijin.jpg"/>Justyn (oweijin)</td>'],
    "k": ['<td><img src="staff-photos/kghiam.jpg"/>Kamyar (kghiam)</td>', '<td><img src="staff-photos/kdchin.jpg"/>Kyle (kdchin)</td>'],
    "l": ['<td><img src="staff-photos/ldegroot.jpg"/>Lisanne (ldegroot)</td>', '<td><img src="staff-photos/ethrashe.jpg"/>Lizzy (ethrashe)</td>'],
    "m": ['<td><img src="staff-photos/mbgardne.jpg"/>Madeline (mbgardne)</td>', '<td><img src="staff-photos/ymkong.jpg"/>Matt (ymkong)</td>', '<td><img src="staff-photos/mnowrooz.jpg"/>Mina (mnowrooz)</td>'],
    "n": ['<td><img src="staff-photos/nanakis.jpg"/>Nanaki (nanakis)</td>', '<td><img src="staff-photos/nviggian.jpg"/>Nick V. (nviggian)</td>', '<td><img src="staff-photos/nawilson.jpg"/>Nick W. (nawilson)</td>', '<td><img src="staff-photos/nraju.png"/>Nitya (nraju)</td>'],
    "o": ['<td><img src="staff-photos/oweiss.jpg"/>Olly (oweiss)</td>', '<td><img src="staff-photos/ouk.jpg"/>Omkar (ouk)</td>'],
    "p": ['<td><img src="staff-photos/plocula.jpg"/>Pranathi (plocula)</td>', ],
    "q": ['<td><img src="staff-photos/dzq.jpg"/>Doug (dz<strong>q</strong>)</td>'],
    "r": ['<td><img src="staff-photos/raahuja.jpg"/>Rahul (raahuja)</td>', '<td><img src="staff-photos/ramgopav.jpg"/>Ramgopal (ramgopav)</td>', '<td><img src="staff-photos/raunaksg.jpg"/>Raunak (raunaksg)</td>', '<td><img src="staff-photos/rishabhc.jpg"/>Rishabh (rishabhc)</td>', '<td><img src="staff-photos/rkaufman.jpg"/>Roman (rkaufman)</td>'],
    "s": ['<td><img src="staff-photos/sbhartiy.jpg"/>Sanjna (sbhartiy)</td>'],
    "t": ['<td><img src="staff-photos/cowarang.jpg"/>Tian (cowarang)</td>'],
    "u": ['<td><img src="staff-photos/uar.jpg"/>Udit (uar)</td>'],
    "v": ['<td><img src="staff-photos/vbaskar.png"/>Vishal (vbaskar)</td>'],
    "w": ['<td><img src="staff-photos/oweiss.jpg"/>Olly (o<strong>w</strong>eiss)</td>'],
    "x": ['<td><img src="staff-photos/xinhuig.jpg"/>Xinhui (xinhuig)</td>'],
    "y": ['<td><img src="staff-photos/yongyiz.jpg"/>Yongyi (yongyiz)</td>'],
    "z": ['<td><img src="staff-photos/yongyiz.jpg"/>Yongyi (yongyi<strong>z</strong>)</td>'],
}

def wordToTA(word, anagram=False):
    if anagram:
        wordList = list(word)
        random.shuffle(wordList)
        word = ''.join(wordList)

    out = "<tr>\n"
    for c in word:
        out += ("\t" + random.choice(letterDict[c]) + "\n")
    out += "</tr>"

    return out

word = input("Word: ")
print(wordToTA(word))
