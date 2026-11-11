def filter_grades(dict,num):
  """
  Print the names of students whose grades are above num.

  >>> filter_grades({'Abe': 100, 'Beth': 62, 'Cameron': 93, 'Debbie': 100}, 95)
  'Abe'
  'Debbie'
  >>> filter_grades({'Abe': 100, 'Beth': 62, 'Cameron': 93, 'Debbie': 100}, 62)
  'Abe'
  'Cameron'
  'Debbie'
  """
  for name, grade in dict.items():
    if grade > num:
      print("'" + name + "'")
  
