dessert = {
'gateau chocolat' : {'chocolat', 'oeuf' , 'farine' , 'sucre' , 'beurre'} ,
'gateau yaourt' : {'yaourt' , 'oeuf' , 'farine' , 'sucre'} ,
'crepes' : {'oeuf' , 'farine' , 'lait'} ,
'gateau-quarts' : {'oeuf' , 'farine' , 'beurre' , 'sucre'} , 
}

def creer_recette(dessert):
	while(1):
		recette= raw_input("saisir le nom de recette ")
		if recette=="" :
			break
		dessert[recette]=set()
		while (1):
			element= raw_input("ajouter un ingredient ")
			if element=="":
				break
			else:
				dessert[recette].add(element)

def nb_ingredients(livre_rec,rec):
	return len(livre_rec[rec])

def recette_avec(livre,ing):
	total=set()
	for recette in livre :
		if ing in livre[recette] :
			total.add(recette)
	return total

def tous_ingredients(livre):
	total=set()
	for recette in livre :
		for ing in livre[recette] :
			total.add(ing)
	return total

def ingredient_principal(livre):
	total=dict()
	for recette in livre :
		for ing in livre[recette] :
			if ing in total :
				total[ing]+=1
			else :
				total[ing]=1
	v=list(total.values())
	k=list(total.keys())
	return k[v.index(max(v))]

def recettes_sans(livre,ing):
	total=set()
	for recette in livre :
		if ing in livre[recette] :
			continue
		total.add(recette)
	return total





creer_recette(dessert)
print nb_ingredients(dessert,"crepes")
print recette_avec(dessert,"oeuf")
print tous_ingredients(dessert)
print ingredient_principal(dessert)
print recettes_sans(dessert,"sucre")
#print dessert
