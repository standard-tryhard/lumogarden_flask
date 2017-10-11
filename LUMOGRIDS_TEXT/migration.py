import os
import codecs
from argparse import ArgumentParser
from app.card import Card
from app.card_steps import CardSteps


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

            name_from_txt = fname[0:-4]
            created_card_ref = name_from_txt.title()

            if not Card.objects(card_name=name_from_txt):
                new_card = Card()
                new_card.card_in_jar = dir_name.lower()
                new_card.card_name = name_from_txt.title()

            else:
                print("You've already got:  ...{}...".format(
                                                    name_from_txt.upper()))

            open_me = ('{}/{}'.format(dir_name, fname))

            new_card.save()

            card_tasks = envelope(open_me)
            card_steps = CardSteps()

            print("{} created".format(new_card.card_name))

            i = 0
            if card_tasks:
                for ct in card_tasks:
                    print('task added to {}:.....{}'.format(name_from_txt, ct))
                    card_steps.step_name = ct
                    card_steps.step_no = i
                    i += 1

                    updated = Card.objects(
                        card_name=created_card_ref).update_one(
                        push__card_steps=card_steps)
                    print('status: {}'.format(updated))

            else:
                print('none to add')


if __name__ == '__main__':
    iterate_up_on_it('WRTE')
