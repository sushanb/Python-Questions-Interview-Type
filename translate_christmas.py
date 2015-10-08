def translate_christmas(list1):
	'''
	(list) -> (list)
>>>translate_christmas(['happy', 'new', 'year'])
['gott', 'nytt', 'ar']
>>>translate_christmas(['merry', 'christmas'])
['god','jul']
'''
	list2 = []
	translate_dictionary = {'merry':'god','christmas':'jul', 'and':'och','happy':'gott','new':'nytt','year':'ar'}
	for items in list1:
		list2.append(translate_dictionary[items])
	return list2

print translate_christmas(['happy', 'new', 'year'])
print translate_christmas(['merry', 'christmas'])
