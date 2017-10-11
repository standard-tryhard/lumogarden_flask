import os
import codecs
from argparse import ArgumentParser
from app.card import Card


def envelope(text_file):
    with codecs.open(text_file, 'r', encoding='utf-8', errors='ignore') as fin:
        lines = fin.readlines()
        tasks = [line.strip() for line in lines if line != '\n']
        return tasks


parser = ArgumentParser()

parser.add_argument(
    '-d',
    action='store',
    dest='sub_dir',
    help='What directory to test out?')

options = parser.parse_args()
options.sub_dir = '.'
dir_to_use = options.sub_dir


def iterate_up_on_it(directory='.'):
    for dir_name, subdir_list, file_list in os.walk(directory):
        print('..............{}...............'.format(dir_name))
        for fname in file_list:

            if fname.startswith('.DS_'):
                continue

            name_from_file = fname[0:-4]



            if not Card.objects(card_name=name_from_file):
                new_card = Card()
                new_card.name_from_file = name_from_file.title()

            else:
                print("You've already got:  ...{}...".format(
                                                    name_from_file.upper()))


            open_me = ('{}/{}'.format(dir_name, fname))

            card_tasks = envelope(open_me)
            print()
            print(name.upper())

            for ct in card_tasks:
                card_steps = CardSteps()
                card_steps.step_name = ct

                print(ct)




# steps = CardSteps()
# steps.step_name = "Find mouse"
# steps.step_no = 0
# steps.step_status = 1


# card = Card()
# card.name = 'works in blue'.title()
#
# card_steps = CardSteps()
# card_steps.step_name = 'email 20 galleries'
# card_steps.step_no = 1

# card.save()

# updated = Card.objects(name='works in blue'.title()).update_one(push__steps=card_steps)



if __name__ == '__main__':
    iterate_up_on_it('ARTE')

