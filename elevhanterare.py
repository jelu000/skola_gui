import elev
import pickle
import os

class ElevHanterare:

    #KONSTRUKTOR----------------------------------------------------------------------
    def __init__(self):
        self.elevlist = []
        self.filnamn = "elever.pkl"
        
        #try:
         #   self.read_from_file()
        #except ValueError:
         #   print("Kunde inte läsa från fil")

    #add_elev()--------------------------------------------------------------------------
    def add_elev(self, elevnamn, utbildning, tel):
        t_elev = elev.Elev(elevnamn, utbildning, tel)
        self.elevlist.append(t_elev)

        #sorterar
        self.elevlist= sorted(self.elevlist, key=lambda p: p.namn)

        return self.elevlist

    #del_elev()-------------------------------------------------------------------------
    def del_elev(self, index):
        
        # sort by namn
        self.elevlist= sorted(self.elevlist, key=lambda p: p.namn)
        
        status = "status"

        try:
            #self.elevlist = [p for p in self.elevlist if p.tel != tel]
            self.elevlist.pop(int(index))
            status = "\nEleven togs bort!"
        
        except ValueError:
            status = "\nKunde inte tabort elev!"

        return self.elevlist


    #print_elevlist()--------------------------------------------------------------------
    def get_elevlist(self):

        # sort by namn
        self.elevlist= sorted(self.elevlist, key=lambda p: p.namn)

        return self.elevlist
            
   
    #save_to_file()----------------------------------------------------------------------
    def save_to_file(self):
         
        # sort by namn
        self.elevlist= sorted(self.elevlist, key=lambda p: p.namn)
        #sparar till fil
        with open(self.filnamn, "wb") as f:
            # use pickle to dump the list of objects to the file
            pickle.dump(self.elevlist, f)

    #read_from_file()--------------------------------------------------------------------
    def read_from_file(self):
        
        #Om filen saknas
        if not os.path.exists(self.filnamn):
            with open(self.filnamn, "w") as f:
                f.write("")
                #print(f"{filename} created.")
        
        else:
            # open the file for reading
            with open(self.filnamn, "rb") as f:
                # use pickle to load the list of objects from the file
                elever = pickle.load(f)
                self.elevlist = elever

           

    #spara_avsluta()-------------------------------------------------------------------
    def spara_avsluta(self):
        self.save_to_file()

        

    
