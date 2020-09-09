#### Complete code for Stable Marriage Problem
## Declaring the required datastructures
guy_preferences = {
    'andrew': ['caroline', 'abigail', 'betty'],
    'bill': ['caroline', 'betty', 'abigail'],
    'chester': ['betty', 'caroline', 'abigail'],
}

gal_preferences = {
    'abigail': ['andrew', 'bill', 'chester'],
    'betty': ['bill', 'andrew', 'chester'],
    'caroline': ['bill', 'chester', 'andrew']
}

## Defining required methods    
def new_over_old(woman, man_old, man_new):
    for i in gal_preferences[woman]:
        if i==man_old:
            return False
        elif i==man_new:
            return True
        
def stable_marriage_algo(guy_preferences, gal_preferences):
    guy_gal = {}
    guy_gal_sum = {}

    ## Initializing the Datastructures
    for i in guy_preferences:
        guy_gal[i]=''
        guy_gal_sum[i] = 0
    for j in gal_preferences:
        guy_gal[j]=''
        guy_gal_sum[j] = 0

    ## Logic
    while sum(list(guy_gal_sum.values()))<len(guy_gal):
        for i in guy_preferences:
            z = 0
            while z<len(guy_preferences[i]):
                
                if sum(list(guy_gal_sum.values()))==len(guy_gal):
                    break
                    
                if new_over_old(guy_preferences[i][z],guy_gal[guy_preferences[i][z]],i):
                    
                    guy_gal[guy_preferences[i][z]]=''
                    guy_gal_sum[guy_preferences[i][z]]=0

                    guy_gal[guy_preferences[i][z]]=i
                    guy_gal[i]=guy_preferences[i][z]
                    guy_gal_sum[i] = 1
                    guy_gal_sum[guy_preferences[i][z]]=1

                    break

                else:
                    z+=1
    
    return guy_gal

##main function
if __name__ == "__main__":
    print("The most stable arrangement of couples: ")
    print(stable_marriage_algo(guy_preferences, gal_preferences))
