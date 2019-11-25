#!/usr/bin/env python3

from bson import ObjectId
from asltutor.models.module import Module
from asltutor.models.quiz import Quiz, Question
from asltutor.models.dictionary import Dictionary

def addall():
    a = Dictionary.object.get(word='a')
    question_a = Question(question_text='What does this sign mean?', word=a)
    question_a.save()
    b = Dictionary.object.get(word='b')
    question_b = Question(question_text='What does this sign mean?', word=b)
    question_b.save()
    c = Dictionary.object.get(word='c')
    question_c = Question(question_text='What does this sign mean?', word=c)
    question_c.save()
    d = Dictionary.object.get(word='d')
    question_d = Question(question_text='What does this sign mean?', word=d)
    question_d.save()
    e = Dictionary.object.get(word='e')
    question_e = Question(question_text='What does this sign mean?', word=e)
    question_e.save()
    f = Dictionary.object.get(word='f')
    question_f = Question(question_text='What does this sign mean?', word=f)
    question_f.save()
    g = Dictionary.object.get(word='g')
    question_g = Question(question_text='What does this sign mean?', word=g)
    question_g.save()
    h = Dictionary.object.get(word='h')
    question_h = Question(question_text='What does this sign mean?', word=h)
    question_h.save()
    i = Dictionary.object.get(word='i')
    question_i = Question(question_text='What does this sign mean?', word=i)
    question_i.save()
    j = Dictionary.object.get(word='j')
    question_j = Question(question_text='What does this sign mean?', word=j)
    question_j.save()
    k = Dictionary.object.get(word='k')
    question_k = Question(question_text='What does this sign mean?', word=k)
    question_k.save()
    l = Dictionary.object.get(word='l')
    question_l = Question(question_text='What does this sign mean?', word=l)
    question_l.save()
    m = Dictionary.object.get(word='m')
    question_m = Question(question_text='What does this sign mean?', word=m)
    question_m.save()
    o = Dictionary.object.get(word='o')
    question_o = Question(question_text='What does this sign mean?', word=o)
    question_o.save()
    p = Dictionary.object.get(word='p')
    question_p = Question(question_text='What does this sign mean?', word=p)
    question_p.save()
    q = Dictionary.object.get(word='q')
    question_q = Question(question_text='What does this sign mean?', word=q)
    question_q.save()
    r = Dictionary.object.get(word='r')
    question_r = Question(question_text='What does this sign mean?', word=r)
    question_r.save()
    s = Dictionary.object.get(word='s')
    question_s = Question(question_text='What does this sign mean?', word=s)
    question_s.save()
    t = Dictionary.object.get(word='t')
    question_t = Question(question_text='What does this sign mean?', word=t)
    question_t.save()
    u = Dictionary.object.get(word='u')
    question_u = Question(question_text='What does this sign mean?', word=u)
    question_u.save()
    v = Dictionary.object.get(word='v')
    question_v = Question(question_text='What does this sign mean?', word=v)
    question_v.save()
    w = Dictionary.object.get(word='w')
    question_w = Question(question_text='What does this sign mean?', word=w)
    question_w.save()
    x = Dictionary.object.get(word='x')
    question_x = Question(question_text='What does this sign mean?', word=x)
    question_x.save()
    y = Dictionary.object.get(word='y')
    question_y = Question(question_text='What does this sign mean?', word=y)
    question_y.save()
    z = Dictionary.object.get(word='z')
    question_z = Question(question_text='What does this sign mean?', word=z)
    question_z.save()

    # places
    house = Dictionary.object.get(word='house')
    question_house = Question(
        question_text='What does this sign mean?', word=house)
    question_house.save()
    museum = Dictionary.object.get(word='museum')
    question_museum = Question(
        question_text='What does this sign mean?', word=museum)
    question_museum.save()
    restaurant = Dictionary.object.get(word='restaurant')
    question_restaurant = Question(
        question_text='What does this sign mean?', word=restaurant)
    question_restaurant.save()
    city = Dictionary.object.get(word='city')
    question_city = Question(question_text='What does this sign mean?', word=city)
    question_city.save()
    restroom = Dictionary.object.get(word='restroom')
    question_restroom = Question(
        question_text='What does this sign mean?', word=restroom)
    question_restroom.save()
    store = Dictionary.object.get(word='store')
    question_store = Question(
        question_text='What does this sign mean?', word=store)
    question_store.save()
    park = Dictionary.object.get(word='park')
    question_park = Question(question_text='What does this sign mean?', word=park)
    question_park.save()
    kitchen = Dictionary.object.get(word='kitchen')
    question_kitchen = Question(
        question_text='What does this sign mean?', word=kitchen)
    question_kitchen.save()

    quiz_places = Quiz(quiz_name='Places Quiz', details='You will be quizzed on what you learned in the places module', questions=[question_house,question_museum,question_restaurant,question_city,question_restroom,question_store,question_park,question_kitchen])
    quiz_places.save()
    module_places = Module(module_name='Places', details='In this module you will learn the signs for common places', words=[house,museum,restaurant,city,restroom,store,park,kitchen], parent=ObjectId('5db21f18019bf84707b3a746'), quiz=[quiz_places])
    module_places.save()

    # Directions
    where = Dictionary.object.get(word='where')
    question_where = Question(
        question_text='What does this sign mean?', word=where)
    question_where.save()
    go = Dictionary.object.get(word='go')
    question_go = Question(question_text='What does this sign mean?', word=go)
    question_go.save()
    which = Dictionary.object.get(word='which')
    question_which = Question(
        question_text='What does this sign mean?', word=which)
    question_which.save()
    way = Dictionary.object.get(word='way')
    question_way = Question(question_text='What does this sign mean?', word=way)
    question_way.save()
    north = Dictionary.object.get(word='north')
    question_north = Question(
        question_text='What does this sign mean?', word=north)
    question_north.save()
    south = Dictionary.object.get(word='south')
    question_south = Question(
        question_text='What does this sign mean?', word=south)
    question_south.save()
    east = Dictionary.object.get(word='east')
    question_east = Question(question_text='What does this sign mean?', word=east)
    question_east.save()
    west = Dictionary.object.get(word='west')
    question_west = Question(question_text='What does this sign mean?', word=west)
    question_west.save()
    here = Dictionary.object.get(word='here')
    question_here = Question(question_text='What does this sign mean?', word=here)
    question_here.save()
    there = Dictionary.object.get(word='there')
    question_there = Question(
        question_text='What does this sign mean?', word=there)
    question_there.save()
    turn = Dictionary.object.get(word='turn')
    question_turn = Question(question_text='What does this sign mean?', word=turn)
    question_turn.save()
    left = Dictionary.object.get(word='left')
    question_left = Question(question_text='What does this sign mean?', word=left)
    question_left.save()
    right = Dictionary.object.get(word='right')
    question_right = Question(
        question_text='What does this sign mean?', word=right)
    question_right.save()
    straight = Dictionary.object.get(word='straight')
    question_straight = Question(
        question_text='What does this sign mean?', word=straight)
    question_straight.save()


    quiz_directions = Quiz(quiz_name='Directions Quiz', details='You will be quizzed on what you learned in the directions module', questions=[question_where,question_go,question_which,question_way,question_north,question_south,question_east,question_west,question_here,question_there,question_turn,question_left,question_right,question_straight])
    quiz_directions.save()
    module_directions = Module(module_name='Directions', details='In this module you will learn the signs for how to give directions', words=[where,go,which,way,north,south,east,west,here,there,turn,left,right,straight], quiz=[quiz_directions], parent=quiz_places.id)
    module_directions.save()

    # Food
    hungry = Dictionary.object.get(word='hungry')
    question_hungry = Question(
        question_text='What does this sign mean?', word=hungry)
    question_hungry.save()
    thirsty = Dictionary.object.get(word='thirsty')
    question_thirsty = Question(
        question_text='What does this sign mean?', word=thirsty)
    question_thirsty.save()
    eat = Dictionary.object.get(word='eat')
    question_eat = Question(question_text='What does this sign mean?', word=eat)
    question_eat.save()
    drink = Dictionary.object.get(word='drink')
    question_drink = Question(
        question_text='What does this sign mean?', word=drink)
    question_drink.save()
    breakfast = Dictionary.object.get(word='breakfast')
    question_breakfast = Question(
        question_text='What does this sign mean?', word=breakfast)
    question_breakfast.save()
    lunch = Dictionary.object.get(word='lunch')
    question_lunch = Question(
        question_text='What does this sign mean?', word=lunch)
    question_lunch.save()
    dinner = Dictionary.object.get(word='dinner')
    question_dinner = Question(
        question_text='What does this sign mean?', word=dinner)
    question_dinner.save()
    coffee = Dictionary.object.get(word='coffee')
    question_coffee = Question(
        question_text='What does this sign mean?', word=coffee)
    question_coffee.save()
    meat = Dictionary.object.get(word='meat')
    question_meat = Question(question_text='What does this sign mean?', word=meat)
    question_meat.save()
    vegetable = Dictionary.object.get(word='vegetable')
    question_vegetable = Question(
        question_text='What does this sign mean?', word=vegetable)
    question_vegetable.save()

    quiz_food = Quiz(quiz_name='Food Quiz', details='You will be quizzed on what you learned in the food module', questions=[question_hungry,question_thirsty,question_eat,question_drink,question_eat,question_breakfast,question_lunch,question_dinner,question_coffee,question_meat,question_vegetables])
    quiz_food.save()
    module_food = Module(module_name='Food', details='In this Module you will learn the signs for describing food', words=[hungry,thirsty,eat,drink,eat,breakfast,lunch,dinner,coffee,meat,vegetables,dinner], quiz=[quiz_food], parent=module_directions.id)
    module_food.save()

    # Nouns
    question_i = Question(question_text='What does this sign mean?', word=i)
    question_i.save()
    me = Dictionary.object.get(word='me')
    question_me = Question(question_text='What does this sign mean?', word=me)
    question_me.save()
    you = Dictionary.object.get(word='you')
    question_you = Question(question_text='What does this sign mean?', word=you)
    question_you.save()
    we = Dictionary.object.get(word='we')
    question_we = Question(question_text='What does this sign mean?', word=we)
    question_we.save()
    man = Dictionary.object.get(word='man')
    question_man = Question(question_text='What does this sign mean?', word=man)
    question_man.save()
    woman = Dictionary.object.get(word='woman')
    question_woman = Question(
        question_text='What does this sign mean?', word=woman)
    question_woman.save()
    he = Dictionary.object.get(word='he')
    question_he = Question(question_text='What does this sign mean?', word=he)
    question_he.save()
    she = Dictionary.object.get(word='she')
    question_she = Question(question_text='What does this sign mean?', word=she)
    question_she.save()
    it = Dictionary.object.get(word='it')
    question_it = Question(question_text='What does this sign mean?', word=it)
    question_it.save()
    they = Dictionary.object.get(word='they')
    question_they = Question(question_text='What does this sign mean?', word=they)
    question_they.save()
    name = Dictionary.object.get(word='name')
    question_name = Question(question_text='What does this sign mean?', word=name)
    question_name.save()

    quiz_nouns = Quiz(quiz_name='Quiz Nouns', details='You will be quizzed on what you learned in the nouns module', questions=[question_i,question_me,question_you,question_we,question_man,question_woman,question_he,question_she,question_it,question_they,question_name])
    quiz_nouns.save()
    module_nouns = Module(module_name='Nouns', details='In this module you will learn the nouns used to describe people', words=[i,me,you,we,man,woman,he,she,it,they,name], quiz=[quiz_nouns], parent=module_food.id)
    module_nouns.save()

    # verbs
    need = Dictionary.object.get(word='need')
    question_need = Question(question_text='What does this sign mean?', word=need)
    question_need.save()
    take = Dictionary.object.get(word='take')
    question_take = Question(question_text='What does this sign mean?', word=take)
    question_take.save()
    have = Dictionary.object.get(word='have')
    question_have = Question(question_text='What does this sign mean?', word=have)
    question_have.save()
    buy = Dictionary.object.get(word='buy')
    question_buy = Question(question_text='What does this sign mean?', word=buy)
    question_buy.save()
    like = Dictionary.object.get(word='like')
    question_like = Question(question_text='What does this sign mean?', word=like)
    question_like.save()
    love = Dictionary.object.get(word='love')
    question_love = Question(question_text='What does this sign mean?', word=love)
    question_love.save()
    hurt = Dictionary.object.get(word='hurt')
    question_hurt = Question(question_text='What does this sign mean?', word=hurt)
    question_hurt.save()
    hate = Dictionary.object.get(word='hate')
    question_hate = Question(question_text='What does this sign mean?', word=hate)
    question_hate.save()

    quiz_verbs = Quiz(quiz_name='Quiz Verbs', details='You will be quizzed on what you learned in the verbs module', questions=[question_need,question_take,question_have,question_buy,question_like,question_love,question_hurt,question_hate])
    quiz_verbs.save()
    module_verbs = Module(module_name='Verbs', details='In this quiz you will be quizzed on common verbs used to describe feelings', words=[need,take,have,buy,like,love,hurt,hate], quiz=[quiz_verbs], parent=module_nouns.id)
    module_verbs.save()

    print('Done')


print('This script will bulk add all of our learning modules to the database.')
print('##########################\n')
print('DO NOT USE THIS UNLESS YOU KNOW WHAT YOU ARE DOING!!!\n')
print('##########################\n')
inn = None
innn = None
innnn = None
print("Do you know what you are doing? [y/N]: ")
while inn == None:
    inn = input()
    if inn.lower() == 'y':
        print('Are you sure? [y/N]: ')
        while innn == None:
            innn = input()
            if innn.lower() == 'y':
                print('Like are you really, really fucking sure? We don\'t have an easy way of undoing this. [y/N]: ')
                while innnn == None:
                    innnn = input()
                    if innnn.lower() == 'y':
                        print('Ok')
                        addall()
                    elif innnn.lower() == 'n':
                        exit()
                    else:
                        print("Please enter [y/N]")
                        innnn = None
            elif innn.lower() == 'n':
                exit()
            else:
                print("Please enter [y/N]")
                innn = None
    elif inn.lower() == 'n':
        exit()
    else:
        print("Please enter [y/N]")
        inn = None
