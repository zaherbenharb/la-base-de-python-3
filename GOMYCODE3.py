#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''Question 1: 

Écrivez un programme Python pour multiplier tous les éléments d'une liste.

par exemple liste=[2, 3, 6]

résultat = 36
'''
my_list=[2,3,6]
print ('résultat =',my_list[0]*my_list[1]*my_list[2])


# In[13]:


'''Question 2:

Écrivez un programme Python pour obtenir une liste, triée par ordre croissant par le dernier élément de chaque tuple à partir d'une liste donnée de tuples non vides.
Exemple de liste : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Résultat attendu : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)] 
'''
def secondElement(elem):
    return elem[1]
list1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
list1.sort(key=secondElement) 
print(list1)


# In[26]:


#Qustion 2 :
#Avec un nombre entier n donné,
#écrivez un programme pour créer un dictionnaire qui contient (i, i*i) 
#tel qu'il soit un nombre entier compris entre 1 et n (tous deux inclus). 
#puis le programme doit imprimer le dictionnaire. Supposons que l'entrée suivante soit fournie au programme :
# 8 Ensuite, la sortie doit être : {1 : 1, 2 : 4, 3 : 9, 4 : 16, 5 : 25, 6 : 36, 7 : 49, 8 : 64 } 

n = int(input('Entrez un nombre : '))
{x: x*x for x in range(1,n+1)}


# In[27]:


'''Question 3: 

Écrivez un programme Python pour combiner deux dictionnaires en ajoutant des valeurs pour les clés communes.

d1 = {'a' : 100, 'b' : 200, 'c' : 300}
d2 = {'a' : 300, 'b' : 200, 'd' : 400}
Sortie attendue : {'a' : 400, 'b' : 400, 'd' : 400, 'c' : 300}'''

from collections import Counter
d1 = {'a' : 100, 'b' : 200, 'c' : 300}
d2 = {'a' : 300, 'b' : 200, 'd' : 400}
dict = Counter(d1)+Counter(d2)
print(dict)


# In[23]:


'''Qustion5
Écrivez un programme pour trier un tuple par son élément flottant.
Par exemple list= [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
Sortie attendue : [('item3', '24.5'), ( 'élément2', '15.10'), ('élément1', '12.20')]
'''
def Sort(list): 
    return(sorted(list, key = lambda x: float(x[1]), reverse = True)) 
  
list= [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')] 
print(Sort(list)) 


# In[ ]:





# In[ ]:




