class hero:
    def __init__(self, name, attributes, hp=[],):
        self.name=name
        self.attributes=attributes
        self.hp=hp
    def take_damage(self, damage,name_list):
        self.name_list=name_list
        self.damage=damage 
        self.hp=hp
        hp[name_list]=hp.append(hp[name_list]-damage)
        if hp[name_list] < 0:
            hp[name_list]=0
        print (self.name,"'s health is now ",hp,"/100 !!!")

name=[]
hp=[]
attributes=[]
user_dec=1

while True:
    while user_dec==2:
        while user_dec==1:
            name= name.append(str(input("Enter the name of your hero:")))
            hp=hp.append(100)
            attributes= attributes.append(str(input("Enter an attribute your hero has:")))
            user_dec= str(input('''Enter "1" to make another hero
            Enter "2" to damage your heroes
            Enter "3" to escape program
            '''))
        for i in len(name):
            print (f"{i+1}. {name[1]}")
        user_choice2=str(input("Who do you like to damage? Enter number:"))
        user_choice3=str(input("Enter damage:"))

        hp.take_damage(user_choice2,user_choice3)

        for i in len(name):
            print (f"{name[i]}'s ,with the attribute {attributes[i]}, has {hp[i]}/100 hp left!")
       
        user_dec= str(input('''Enter "1" to make another hero
        Enter "2" to damage your heroes
        Enter "3" to escape program
        '''))
    break

        
        