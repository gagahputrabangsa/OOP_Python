class gradeval:
  def __init__(self, value):
    self.value = value
  
  def get_name(name,id):
    return name,id

  
def get_grade(self):
    if self.value >= 80:
      return "A"
    elif self.value >= 77:
      return "A-"
    elif self.value >= 74:
      return "B+"
    elif self.value >= 68:
      return "B"
    elif self.value >= 65:
      return "B-"
    elif self.value >= 62:
      return "C+"
    elif self.value >= 56:
      return "C"
    elif self.value >= 45:
      return "D"
    else:
      return "E"

name= input('Name: ')
id = input('Id: ')
value = float(input("Input Score: "))
value_grade = gradeval(value)
grade = value_grade.get_grade()

print(f'\n---  Practice Data OOP 2024  ---')
print(f"name: {name}\nid: {id}")
print(f"Grade: {grade}")
