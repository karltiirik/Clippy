import os
import EST_id_gen


def add_to_clip_board(text):
    """ Adds text to clipboard. Inspiration http://stackoverflow.com/a/9409898 """
    command = 'echo ' + text + '| clip'
    os.system(command)

random_id = EST_id_gen.gen_est_id()
add_to_clip_board(random_id)

