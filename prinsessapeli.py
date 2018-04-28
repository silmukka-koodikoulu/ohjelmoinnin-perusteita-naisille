# Prinsessan koitokset v1
# tulostaminen
print('Prinsessan koitokset versio 1!')
print('Prinsessa ja prinssi ovat piilosilla linnassa.')
print('On prinsessan vuoro etsiä. Minne prinssi on piiloutunut')
print('*****')
print(' ')
# luodaan ensimmäinen muuttuja nimeltä 'prinssi_hukassa'
prinssi_hukassa = True
# luodaan toinen muuttuja nimeltä 'prinssin_huone'
prinssin_huone = 1
print(prinssin_huone)
print(prinssi_hukassa)
# luodaan silmukka eli luuppi, joka pyörii niin kauan kuin
# muuttuja 'prinssi_hukassa' on True
# silmukka luodaan while -ehto :
# huomaa sisennykset! Paina enteriä kaksoispisteen jälkeen
# IDLE editori hoitaa puolestasi pythonin vaatimat sisennykset
# tämän jälkeen paina enteriä jokaisen rivin lopussa, jotta pysyt silmukan sisällä
while prinssi_hukassa:
    #
    # tässä annetaan ohjelman käyttäjälle ohjeita, jotka tulostetaan
    print('Käytävällä on 4 huonetta. Missä huoneessa on prinssi? Arvaa!')
    #
    # Ohjelma on interaktiivinen. Tässä kysytään käyttäjältä syötettä 
    print('Kirjoita sen huoneen numero, johon haluat kurkistaa')
    #
    # luodaan uusi muuttuja 'kayttajan_syote' käyttäjän syötettä varten
    # muuttuja saa arvokseen funktion input. 
    # Input antaa ohjelman käyttäjän kirjoittaa ohjelmalle numeroita tai tekstiä.
    kayttajan_syote = input('Syötä huoneen numero 1,2,3 tai 4:  ')
    print('*****')
    print(' ')
    #
    # kerrotaan vielä Pythonille, että kayttajan_syote on integer eli kokonaisluku.
    # Jos syöte on jotain muuta kuin kokonaisluku, tapahtuu virhe!
    # (Tässä ohjelmassa tuota virhettä ei kuitenkaan käsitellä ja ohjelma kaatuu, mutta oikeassa
    # ohjelmistokehityksessä koodareitten on varauduttava mm. kaikenlaisiin virhetilanteisiin,
    # jotta ohjelman käyttäminen olisi mahdollisimman miellyttävää eikä se jatkuvasti kaatuilisi!)
    arvattu_huone = int(kayttajan_syote)
    # Ohjelmamme on sen verran yksinkertainen, että sille kelpaa mikä vaan syötteeksi
    # Oikeasti vain numerolla 1 on merkitystä, koska se ohjaa ohjelman seuraavaa kohtaa.
    #
    # luodaan ehtolause if-else
    # tässä suoritetaan jompi kumpi koodinpätkä.   
    # Jos arvot olivat eri, hypätään kohtaan else ja suoritetaan sen jälkeinen 1 rivi
    # tämän jälkeen palataan silmukan alkuun kohtaan while ja suoritetaan koko silmukka alusta asti uudelleen
    if prinssin_huone == arvattu_huone:
        # Jos (If) prinssin_huone, jonka arvoksi laitettiin aiemmin 1 on sama kuin arvattu_huone
        # suoritetaan sen jälkeiset kaksi riviä.
        # Printataan onnittelut ja vaihdetaan prinssi_hukassa muuttujan arvo.
        # Palataan while -silmukan alkuun. Koska prinssi_hukassa on false, poistutaan silmukasta
        print('Löysit prinssin! Onneksi olkoon!!!')
        prinssi_hukassa = False
    else:
        print('Prinssi ei ollut tässä huoneessa. Arvaa uudelleen.')
#
# kun prinssi_hukassa = False poistutaan silmukasta ja palataan pääohjelmaan
# Tulostetaan loppulauseet, jonka jälkeen ohjelma loppuu
print('Olipa jännittävä piiloleikki! Kiva, että pelasit.')

    
    
    
    



