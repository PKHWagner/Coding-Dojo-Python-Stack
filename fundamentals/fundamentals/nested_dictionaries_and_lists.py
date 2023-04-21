x = [ [5,2,3], [10,8,9] ]
x[1][0]=15
print(x)

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name']='Bryant'
print(students[0]['last_name'])

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0]='Andres'
print(sports_directory['soccer'][0])

z = [ {'x': 10, 'y': 20} ]
z[0]['y']=30
print(z[0]['y'])


students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(source):
    for person in range(0,len(source)):
        message=''
        for location, data in source[person].items():
            message += f'{location} - {data},'
        print(message)
iterateDictionary(students)

def iterateDictionary2(pupil, source):
    for person in range(0, len(source)):
        for location, data in source[person].items():
            if location == pupil:
                print(data)

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(avail):
    for campus, faculty in avail.items():
        print('-----------')
        print(f'{len(faculty)}{campus.upper()}')
        for i in range(0, len(faculty)):
            print(faculty[i])
printInfo(dojo)
