
from collections import deque

class File :
    """ Une classe pour les files FIFO
        utilisation 

        f = File() crée une file vide
    """

    def __init__(self) :
        self.data = deque()
        
    def est_vide(self) : 
        return self.data == deque()

    def enfiler(self, valeur) : 
        self.data.append(valeur)
        return self

    def defiler(self) :
        assert not self.est_vide() , ' Impossible de défiler une file vide '
        return self.data.popleft()

    def tete(self) : 
        assert not self.est_vide() , "tete n'est pas définie pour une file vide"
        return self.data[0]


    def __str__(self) :
        string = "File["
        for elt in self.data : string = string+" "+str(elt)+" "
        return string+"]"    

    
