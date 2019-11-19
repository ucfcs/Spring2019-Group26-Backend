#!/usr/bin/env python3

from bson import ObjectId
from asltutor.models.module import Module
from asltutor.models.quiz import Quiz, Question
from asltutor.models.dictionary import Dictionary

def addall():
    a = Dictionary(
        word='a', url='https://animations.theasltutor.com.s3.amazonaws.com/a.mp4', in_dictionary='True')
    a.save()
    question_a = Question(question_text='What does this sign mean?', word=a)
    question_a.save()
    b = Dictionary(
        word='b', url='https://animations.theasltutor.com.s3.amazonaws.com/b.mp4', in_dictionary='True')
    b.save()
    question_b = Question(question_text='What does this sign mean?', word=b)
    question_b.save()
    c = Dictionary(
        word='c', url='https://animations.theasltutor.com.s3.amazonaws.com/c.mp4', in_dictionary='True')
    c.save()
    question_c = Question(question_text='What does this sign mean?', word=c)
    question_c.save()
    d = Dictionary(
        word='d', url='https://animations.theasltutor.com.s3.amazonaws.com/d.mp4', in_dictionary='True')
    d.save()
    question_d = Question(question_text='What does this sign mean?', word=d)
    question_d.save()
    e = Dictionary(
        word='e', url='https://animations.theasltutor.com.s3.amazonaws.com/e.mp4', in_dictionary='True')
    e.save()
    question_e = Question(question_text='What does this sign mean?', word=e)
    question_e.save()
    f = Dictionary(
        word='f', url='https://animations.theasltutor.com.s3.amazonaws.com/f.mp4', in_dictionary='True')
    f.save()
    question_f = Question(question_text='What does this sign mean?', word=f)
    question_f.save()
    g = Dictionary(
        word='g', url='https://animations.theasltutor.com.s3.amazonaws.com/g.mp4', in_dictionary='True')
    g.save()
    question_g = Question(question_text='What does this sign mean?', word=g)
    question_g.save()
    h = Dictionary(
        word='h', url='https://animations.theasltutor.com.s3.amazonaws.com/h.mp4', in_dictionary='True')
    h.save()
    question_h = Question(question_text='What does this sign mean?', word=h)
    question_h.save()
    i = Dictionary(
        word='i', url='https://animations.theasltutor.com.s3.amazonaws.com/i.mp4', in_dictionary='True')
    i.save()
    question_i = Question(question_text='What does this sign mean?', word=i)
    question_i.save()
    j = Dictionary(
        word='j', url='https://animations.theasltutor.com.s3.amazonaws.com/j.mp4', in_dictionary='True')
    j.save()
    question_j = Question(question_text='What does this sign mean?', word=j)
    question_j.save()
    k = Dictionary(
        word='k', url='https://animations.theasltutor.com.s3.amazonaws.com/k.mp4', in_dictionary='True')
    k.save()
    question_k = Question(question_text='What does this sign mean?', word=k)
    question_k.save()
    l = Dictionary(
        word='l', url='https://animations.theasltutor.com.s3.amazonaws.com/l.mp4', in_dictionary='True')
    l.save()
    question_l = Question(question_text='What does this sign mean?', word=l)
    question_l.save()
    m = Dictionary(
        word='m', url='https://animations.theasltutor.com.s3.amazonaws.com/m.mp4', in_dictionary='True')
    m.save()
    question_m = Question(question_text='What does this sign mean?', word=m)
    question_m.save()
    o = Dictionary(
        word='o', url='https://animations.theasltutor.com.s3.amazonaws.com/o.mp4', in_dictionary='True')
    o.save()
    question_o = Question(question_text='What does this sign mean?', word=o)
    question_o.save()
    p = Dictionary(
        word='p', url='https://animations.theasltutor.com.s3.amazonaws.com/p.mp4', in_dictionary='True')
    p.save()
    question_p = Question(question_text='What does this sign mean?', word=p)
    question_p.save()
    q = Dictionary(
        word='q', url='https://animations.theasltutor.com.s3.amazonaws.com/q.mp4', in_dictionary='True')
    q.save()
    question_q = Question(question_text='What does this sign mean?', word=q)
    question_q.save()
    r = Dictionary(
        word='r', url='https://animations.theasltutor.com.s3.amazonaws.com/r.mp4', in_dictionary='True')
    r.save()
    question_r = Question(question_text='What does this sign mean?', word=r)
    question_r.save()
    s = Dictionary(
        word='s', url='https://animations.theasltutor.com.s3.amazonaws.com/s.mp4', in_dictionary='True')
    s.save()
    question_s = Question(question_text='What does this sign mean?', word=s)
    question_s.save()
    t = Dictionary(
        word='t', url='https://animations.theasltutor.com.s3.amazonaws.com/t.mp4', in_dictionary='True')
    t.save()
    question_t = Question(question_text='What does this sign mean?', word=t)
    question_t.save()
    u = Dictionary(
        word='u', url='https://animations.theasltutor.com.s3.amazonaws.com/u.mp4', in_dictionary='True')
    u.save()
    question_u = Question(question_text='What does this sign mean?', word=u)
    question_u.save()
    v = Dictionary(
        word='v', url='https://animations.theasltutor.com.s3.amazonaws.com/v.mp4', in_dictionary='True')
    v.save()
    question_v = Question(question_text='What does this sign mean?', word=v)
    question_v.save()
    w = Dictionary(
        word='w', url='https://animations.theasltutor.com.s3.amazonaws.com/w.mp4', in_dictionary='True')
    w.save()
    question_w = Question(question_text='What does this sign mean?', word=w)
    question_w.save()
    x = Dictionary(
        word='x', url='https://animations.theasltutor.com.s3.amazonaws.com/x.mp4', in_dictionary='True')
    x.save()
    question_x = Question(question_text='What does this sign mean?', word=x)
    question_x.save()
    y = Dictionary(
        word='y', url='https://animations.theasltutor.com.s3.amazonaws.com/y.mp4', in_dictionary='True')
    y.save()
    question_y = Question(question_text='What does this sign mean?', word=y)
    question_y.save()
    z = Dictionary(
        word='z', url='https://animations.theasltutor.com.s3.amazonaws.com/z.mp4', in_dictionary='True')
    z.save()
    question_z = Question(question_text='What does this sign mean?', word=z)
    question_z.save()

    # places
    house = Dictionary(
        word='house', url='https://animations.theasltutor.com.s3.amazonaws.com/house.mp4', in_dictionary='True')
    house.save()
    question_house = Question(
        question_text='What does this sign mean?', word=house)
    question_house.save()
    museum = Dictionary(
        word='museum', url='https://animations.theasltutor.com.s3.amazonaws.com/museum.mp4', in_dictionary='True')
    museum.save()
    question_museum = Question(
        question_text='What does this sign mean?', word=museum)
    question_museum.save()
    restaurant = Dictionary(
        word='restaurant', url='https://animations.theasltutor.com.s3.amazonaws.com/restaurant.mp4', in_dictionary='True')
    restaurant.save()
    question_restaurant = Question(
        question_text='What does this sign mean?', word=restaurant)
    question_restaurant.save()
    city = Dictionary(
        word='city', url='https://animations.theasltutor.com.s3.amazonaws.com/city.mp4', in_dictionary='True')
    city.save()
    question_city = Question(question_text='What does this sign mean?', word=city)
    question_city.save()
    restroom = Dictionary(
        word='restroom', url='https://animations.theasltutor.com.s3.amazonaws.com/restroom.mp4', in_dictionary='True')
    restroom.save()
    question_restroom = Question(
        question_text='What does this sign mean?', word=restroom)
    question_restroom.save()
    store = Dictionary(
        word='store', url='https://animations.theasltutor.com.s3.amazonaws.com/store.mp4', in_dictionary='True')
    store.save()
    question_store = Question(
        question_text='What does this sign mean?', word=store)
    question_store.save()
    park = Dictionary(
        word='park', url='https://animations.theasltutor.com.s3.amazonaws.com/park.mp4', in_dictionary='True')
    park.save()
    question_park = Question(question_text='What does this sign mean?', word=park)
    question_park.save()
    kitchen = Dictionary(
        word='kitchen', url='https://animations.theasltutor.com.s3.amazonaws.com/kitchen.mp4', in_dictionary='True')
    kitchen.save()
    question_kitchen = Question(
        question_text='What does this sign mean?', word=kitchen)
    question_kitchen.save()

    quiz_places = Quiz(quiz_name='Places Quiz', details='You will be quizzed on what you learned in the places module', questions=[question_house,question_museum,question_restaurant,question_city,question_restroom,question_store,question_park,question_kitchen])
    quiz_places.save()
    module_places = Module(module_name='Places', details='In this module you will learn the signs for common places', words=[house,museum,restaurant,city,restroom,store,park,kitchen], parent=ObjectId('5db21f18019bf84707b3a746'), quiz=[quiz_places])
    module_places.save()

    # Directions
    where = Dictionary(
        word='where', url='https://animations.theasltutor.com.s3.amazonaws.com/where.mp4', in_dictionary='True')
    where.save()
    question_where = Question(
        question_text='What does this sign mean?', word=where)
    question_where.save()
    go = Dictionary(
        word='go', url='https://animations.theasltutor.com.s3.amazonaws.com/go.mp4', in_dictionary='True')
    go.save()
    question_go = Question(question_text='What does this sign mean?', word=go)
    question_go.save()
    which = Dictionary(
        word='which', url='https://animations.theasltutor.com.s3.amazonaws.com/which.mp4', in_dictionary='True')
    which.save()
    question_which = Question(
        question_text='What does this sign mean?', word=which)
    question_which.save()
    way = Dictionary(
        word='way', url='https://animations.theasltutor.com.s3.amazonaws.com/way.mp4', in_dictionary='True')
    way.save()
    question_way = Question(question_text='What does this sign mean?', word=way)
    question_way.save()
    north = Dictionary(
        word='north', url='https://animations.theasltutor.com.s3.amazonaws.com/north.mp4', in_dictionary='True')
    north.save()
    question_north = Question(
        question_text='What does this sign mean?', word=north)
    question_north.save()
    south = Dictionary(
        word='south', url='https://animations.theasltutor.com.s3.amazonaws.com/south.mp4', in_dictionary='True')
    south.save()
    question_south = Question(
        question_text='What does this sign mean?', word=south)
    question_south.save()
    east = Dictionary(
        word='east', url='https://animations.theasltutor.com.s3.amazonaws.com/east.mp4', in_dictionary='True')
    east.save()
    question_east = Question(question_text='What does this sign mean?', word=east)
    question_east.save()
    west = Dictionary(
        word='west', url='https://animations.theasltutor.com.s3.amazonaws.com/west.mp4', in_dictionary='True')
    west.save()
    question_west = Question(question_text='What does this sign mean?', word=west)
    question_west.save()
    here = Dictionary(
        word='here', url='https://animations.theasltutor.com.s3.amazonaws.com/here.mp4', in_dictionary='True')
    here.save()
    question_here = Question(question_text='What does this sign mean?', word=here)
    question_here.save()
    there = Dictionary(
        word='there', url='https://animations.theasltutor.com.s3.amazonaws.com/there.mp4', in_dictionary='True')
    there.save()
    question_there = Question(
        question_text='What does this sign mean?', word=there)
    question_there.save()
    turn = Dictionary(
        word='turn', url='https://animations.theasltutor.com.s3.amazonaws.com/turn.mp4', in_dictionary='True')
    turn.save()
    question_turn = Question(question_text='What does this sign mean?', word=turn)
    question_turn.save()
    left = Dictionary(
        word='left', url='https://animations.theasltutor.com.s3.amazonaws.com/left.mp4', in_dictionary='True')
    left.save()
    question_left = Question(question_text='What does this sign mean?', word=left)
    question_left.save()
    right = Dictionary(
        word='right', url='https://animations.theasltutor.com.s3.amazonaws.com/right.mp4', in_dictionary='True')
    right.save()
    question_right = Question(
        question_text='What does this sign mean?', word=right)
    question_right.save()
    straight = Dictionary(
        word='straight', url='https://animations.theasltutor.com.s3.amazonaws.com/straight.mp4', in_dictionary='True')
    straight.save()
    question_straight = Question(
        question_text='What does this sign mean?', word=straight)
    question_straight.save()


    quiz_directions = Quiz(quiz_name='Directions Quiz', details='You will be quizzed on what you learned in the directions module', questions=[question_where,question_go,question_which,question_way,question_north,question_south,question_east,question_west,question_here,question_there,question_turn,question_left,question_right,question_straight])
    quiz_directions.save()
    module_directions = Module(module_name='Directions', details='In this module you will learn the signs for how to give directions', words=[where,go,which,way,north,south,east,west,here,there,turn,left,right,straight], quiz=[quiz_directions], parent=quiz_places.id)
    module_directions.save()

    # Food
    hungry = Dictionary(
        word='hungry', url='https://animations.theasltutor.com.s3.amazonaws.com/hungry.mp4', in_dictionary='True')
    hungry.save()
    question_hungry = Question(
        question_text='What does this sign mean?', word=hungry)
    question_hungry.save()
    thirsty = Dictionary(
        word='thirsty', url='https://animations.theasltutor.com.s3.amazonaws.com/thirsty.mp4', in_dictionary='True')
    thirsty.save()
    question_thirsty = Question(
        question_text='What does this sign mean?', word=thirsty)
    question_thirsty.save()
    eat = Dictionary(
        word='eat', url='https://animations.theasltutor.com.s3.amazonaws.com/eat.mp4', in_dictionary='True')
    eat.save()
    question_eat = Question(question_text='What does this sign mean?', word=eat)
    question_eat.save()
    drink = Dictionary(
        word='drink', url='https://animations.theasltutor.com.s3.amazonaws.com/drink.mp4', in_dictionary='True')
    drink.save()
    question_drink = Question(
        question_text='What does this sign mean?', word=drink)
    question_drink.save()
    breakfast = Dictionary(
        word='breakfast', url='https://animations.theasltutor.com.s3.amazonaws.com/breakfast.mp4', in_dictionary='True')
    breakfast.save()
    question_breakfast = Question(
        question_text='What does this sign mean?', word=breakfast)
    question_breakfast.save()
    lunch = Dictionary(
        word='lunch', url='https://animations.theasltutor.com.s3.amazonaws.com/lunch.mp4', in_dictionary='True')
    lunch.save()
    question_lunch = Question(
        question_text='What does this sign mean?', word=lunch)
    question_lunch.save()
    dinner = Dictionary(
        word='dinner', url='https://animations.theasltutor.com.s3.amazonaws.com/dinner.mp4', in_dictionary='True')
    dinner.save()
    question_dinner = Question(
        question_text='What does this sign mean?', word=dinner)
    question_dinner.save()
    coffee = Dictionary(
        word='coffee', url='https://animations.theasltutor.com.s3.amazonaws.com/coffee.mp4', in_dictionary='True')
    coffee.save()
    question_coffee = Question(
        question_text='What does this sign mean?', word=coffee)
    question_coffee.save()
    meat = Dictionary(
        word='meat', url='https://animations.theasltutor.com.s3.amazonaws.com/meat.mp4', in_dictionary='True')
    meat.save()
    question_meat = Question(question_text='What does this sign mean?', word=meat)
    question_meat.save()
    vegetables = Dictionary(
        word='vegetables', url='https://animations.theasltutor.com.s3.amazonaws.com/vegetables.mp4', in_dictionary='True')
    vegetables.save()
    question_vegetables = Question(
        question_text='What does this sign mean?', word=vegetables)
    question_vegetables.save()

    quiz_food = Quiz(quiz_name='Food Quiz', details='You will be quizzed on what you learned in the food module', questions=[question_hungry,question_thirsty,question_eat,question_drink,question_eat,question_breakfast,question_lunch,question_dinner,question_coffee,question_meat,question_vegetables])
    quiz_food.save()
    module_food = Module(module_name='Food', details='In this Module you will learn the signs for describing food', words=[hungry,thirsty,eat,drink,eat,breakfast,lunch,dinner,coffee,meat,vegetables,dinner], quiz=[quiz_food], parent=module_directions.id)
    module_food.save()

    # Nouns
    question_i = Question(question_text='What does this sign mean?', word=i)
    question_i.save()
    me = Dictionary(
        word='me', url='https://animations.theasltutor.com.s3.amazonaws.com/me.mp4', in_dictionary='True')
    me.save()
    question_me = Question(question_text='What does this sign mean?', word=me)
    question_me.save()
    you = Dictionary(
        word='you', url='https://animations.theasltutor.com.s3.amazonaws.com/you.mp4', in_dictionary='True')
    you.save()
    question_you = Question(question_text='What does this sign mean?', word=you)
    question_you.save()
    we = Dictionary(
        word='we', url='https://animations.theasltutor.com.s3.amazonaws.com/we.mp4', in_dictionary='True')
    we.save()
    question_we = Question(question_text='What does this sign mean?', word=we)
    question_we.save()
    man = Dictionary(
        word='man', url='https://animations.theasltutor.com.s3.amazonaws.com/man.mp4', in_dictionary='True')
    man.save()
    question_man = Question(question_text='What does this sign mean?', word=man)
    question_man.save()
    woman = Dictionary(
        word='woman', url='https://animations.theasltutor.com.s3.amazonaws.com/woman.mp4', in_dictionary='True')
    woman.save()
    question_woman = Question(
        question_text='What does this sign mean?', word=woman)
    question_woman.save()
    he = Dictionary(
        word='he', url='https://animations.theasltutor.com.s3.amazonaws.com/he.mp4', in_dictionary='True')
    he.save()
    question_he = Question(question_text='What does this sign mean?', word=he)
    question_he.save()
    she = Dictionary(
        word='she', url='https://animations.theasltutor.com.s3.amazonaws.com/she.mp4', in_dictionary='True')
    she.save()
    question_she = Question(question_text='What does this sign mean?', word=she)
    question_she.save()
    it = Dictionary(
        word='it', url='https://animations.theasltutor.com.s3.amazonaws.com/it.mp4', in_dictionary='True')
    it.save()
    question_it = Question(question_text='What does this sign mean?', word=it)
    question_it.save()
    they = Dictionary(
        word='they', url='https://animations.theasltutor.com.s3.amazonaws.com/they.mp4', in_dictionary='True')
    they.save()
    question_they = Question(question_text='What does this sign mean?', word=they)
    question_they.save()

    quiz_nouns = Quiz(quiz_name='Quiz Nouns', details='You will be quizzed on what you learned in the nouns module', questions=[question_i,question_me,question_you,question_we,question_man,question_woman,question_he,question_she,question_it,question_they])
    quiz_nouns.save()
    module_nouns = Module(module_name='Nouns', details='In this module you will learn the nouns used to describe people', words=[i,me,you,we,man,woman,he,she,it,they], quiz=[quiz_nouns], parent=module_food.id)
    module_nouns.save()

    # verbs
    need = Dictionary(
        word='need', url='https://animations.theasltutor.com.s3.amazonaws.com/need.mp4', in_dictionary='True')
    need.save()
    question_need = Question(question_text='What does this sign mean?', word=need)
    question_need.save()
    take = Dictionary(
        word='take', url='https://animations.theasltutor.com.s3.amazonaws.com/take.mp4', in_dictionary='True')
    take.save()
    question_take = Question(question_text='What does this sign mean?', word=take)
    question_take.save()
    have = Dictionary(
        word='have', url='https://animations.theasltutor.com.s3.amazonaws.com/have.mp4', in_dictionary='True')
    have.save()
    question_have = Question(question_text='What does this sign mean?', word=have)
    question_have.save()
    buy = Dictionary(
        word='buy', url='https://animations.theasltutor.com.s3.amazonaws.com/buy.mp4', in_dictionary='True')
    buy.save()
    question_buy = Question(question_text='What does this sign mean?', word=buy)
    question_buy.save()
    like = Dictionary(
        word='like', url='https://animations.theasltutor.com.s3.amazonaws.com/like.mp4', in_dictionary='True')
    like.save()
    question_like = Question(question_text='What does this sign mean?', word=like)
    question_like.save()
    love = Dictionary(
        word='love', url='https://animations.theasltutor.com.s3.amazonaws.com/love.mp4', in_dictionary='True')
    love.save()
    question_love = Question(question_text='What does this sign mean?', word=love)
    question_love.save()
    hurt = Dictionary(
        word='hurt', url='https://animations.theasltutor.com.s3.amazonaws.com/hurt.mp4', in_dictionary='True')
    hurt.save()
    question_hurt = Question(question_text='What does this sign mean?', word=hurt)
    question_hurt.save()
    hate = Dictionary(
        word='hate', url='https://animations.theasltutor.com.s3.amazonaws.com/hate.mp4', in_dictionary='True')
    hate.save()
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
