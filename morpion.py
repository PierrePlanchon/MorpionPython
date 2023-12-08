from tkinter import*
fenetre=Tk()
fenetre.configure(width=600,height=450)
fenetre.title("morpion")

#variables globales utilisées dans les fonctions

Jeu = '---'
couleur = 'black'

#-----programme principal-----#

def main():
    #défintion de la grille
    grille = Canvas(fenetre)
    grille.configure(bg='white',width=600,height=450)
    grille.place(x=0,y=0)

    C1 = grille.create_rectangle(150,15,155,435, fill='black')
    C2 = grille.create_rectangle(305,15,310,435, fill='black')
    L1 = grille.create_rectangle(15,150,435,155, fill='black')
    L2 = grille.create_rectangle(15,305,435,310, fill='black')


    #affichage de fin de partie supp
    global rejouer
    rejouer.place_forget()
    global fin
    fin.place_forget()


    def stop(j):#pour tout désépingler quand il y a un gagnant
    #cases supp
        case1.place_forget()
        case2.place_forget()
        case3.place_forget()
        case4.place_forget()
        case5.place_forget()
        case6.place_forget()
        case7.place_forget()
        case8.place_forget()
        case9.place_forget()

    #boutons et textes en haut à droite supp
        j1.place_forget()
        j2.place_forget()
        erase.place_forget()
        T.place_forget()
        t.place_forget()

    #grille supp
        grille.place_forget()

    #affichage du gagnant et du bonton 'rejouer'
        fin.place(x=200,y=170)
        rejouer.place(x=527,y=422)

        global fin
        if case1['text'] and case2['text'] and case3['text'] and case4['text'] and case5['text'] and case6['text'] and case7['text'] and case8['text'] and case9['text'] is Jeu:
            fin.configure(text='égalité !', fg='black')
        else:
            fin.configure(text=j+' a gagné', fg=couleur)


    def compte(lcd): #pour compter le nombre de X ou O dans une ligne, colonne ou diagonale (indiquée en argument de fonction)
        if case1['text'] and case2['text'] and case3['text'] and case4['text'] and case5['text'] and case6['text'] and case7['text'] and case8['text'] and case9['text'] is Jeu :
            e = ''
            stop(e)
        #pour le joueur 1 (X)
        x = ' '
        a = 0
        for i in lcd:
            x = i
            if i == 'X':
                a = a+1
        if a==3 :
            stop(j1['text'])

        #pour le joueur 2 (O)
        z = ' '
        b = 0
        for k in lcd:
            z = k
            if k == 'O':
                b = b+1
        if b==3 :
            stop(j2['text'])


    def pion(case):
        #fonctionnement et définitions des lignes, colonnes et diagonales
            case.configure(text=Jeu, fg=couleur, font=('arial',9,'bold'))

            l1 = case1['text'], case2['text'], case3['text']
            l2 = case4['text'], case5['text'], case6['text']
            l3 = case7['text'], case8['text'], case9['text']

            c1 = case1['text'], case4['text'], case7['text']
            c2 = case2['text'], case5['text'], case8['text']
            c3 = case3['text'], case6['text'], case9['text']

            d1 = case1['text'], case5['text'], case9['text']
            d2 = case3['text'], case5['text'], case7['text']

            compte(l1), compte(l2), compte(l3), compte(c1), compte(c2), compte(c3), compte(d1), compte(d2)


    #boutons-cases
    case1 = Button(fenetre, width=17, height=8)
    case1.configure(command=lambda x=case1:pion(x))
    case1.place(x=20,y=15)

    case2 = Button(fenetre, width=19, height=8)
    case2.configure(command=lambda x=case2:pion(x))
    case2.place(x=160,y=15)

    case3 = Button(fenetre, width=17, height=8)
    case3.configure(command=lambda x=case3:pion(x))
    case3.place(x=315, y=15)

    case4 = Button(fenetre, width=17, height=8)
    case4.configure(command=lambda x=case4:pion(x))
    case4.place(x=20, y=165)

    case5 = Button(fenetre, width=19, height=8)
    case5.configure(command=lambda x=case5:pion(x))
    case5.place(x=160, y=165)

    case6 = Button(fenetre, width=17, height=8)
    case6.configure(command=lambda x=case6:pion(x))
    case6.place(x=315,y=165)

    case7 = Button(fenetre,width=17, height=7)
    case7.configure(command=lambda x=case7:pion(x))
    case7.place(x=20,y=315)

    case8 = Button(fenetre,width=19, height=7)
    case8.configure(command=lambda x=case8:pion(x))
    case8.place(x=160,y=315)

    case9 = Button(fenetre,width=17, height=7)
    case9.configure(command=lambda x=case9:pion(x))
    case9.place(x=315,y=315)


    #choix des couleurs et du symbole selon le joueur
    def J1():
        global Jeu
        Jeu = 'X'
        global couleur
        couleur = 'red'
    def J2():
        global Jeu
        Jeu = 'O'
        global couleur
        couleur = 'blue'

    def gomme():
        global Jeu
        Jeu = ' '


    #boutons en haut à droite : les joueurs
    j1 = Button(fenetre, text='J1', font=('arial',8,'bold'),width=6,height=1, command=J1)
    j1.place(x=465,y=15)
    T = Label(fenetre,text=('= X'), bg='white', fg='red', font=('arial',11,'bold'))
    T.place(x=520,y=17)

    j2 = Button(fenetre, text='J2', font=('arial',8,'bold'), width=6, height=1, command=J2)
    j2.place(x=465,y=45)
    t = Label(fenetre, text=('= O'), bg='white', fg='blue', font=('arial',11,'bold'))
    t.place(x=520,y=47)

    erase = Button(fenetre, text='Gomme', font=('arial',8,'bold'), width=6, height=1, command=gomme)
    erase.place(x=465,y=75)



#----- variables globales pour la fin -----#
rejouer = Button(fenetre, text='Rejouer', font=('arial', 10,'bold'), width=8,height=1, bg='black', fg='white', command=main)
fin = Label(fenetre, text=(' à gagné !'),font=('arial',30,'bold'), fg=couleur)


#fin
main()
fenetre.mainloop()