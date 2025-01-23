class Movie:
    ''' This class gives Movie details'''
    def __init__(self,title,hero,heroine):
        self.title = title
        self.hero = hero
        self.heroine = heroine
    def info(self):
        
        print('Movie Name:',self.title)
        print('Hero Name:',self.hero)
        print('Heroine Name:',self.heroine)
    


print(Movie.__doc__)
movie_list=[]
while True:
    print('Enter the following details')
    title=input('Movie Name:')
    hero=input('Hero:')
    heroine=input('heroine:')
    m=Movie(title,hero,heroine)
    movie_list.append(m)
    print('Movie added successfully')
    option=input('Do you want to add more movies?[Yes/No]')
    if option.lower()=='no' and option.lower()!='yes':
        break
print('Movie Details are:')
for m in movie_list:
    m.info()
    print()
