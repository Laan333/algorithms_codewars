import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def pig_it(text:str):
    logger.info('Starting program')
    new_text:str = ''
    texted_list = text.split(' ')
    logger.info(f'Split the text {texted_list}')
    for i in range(len(texted_list)):
        if texted_list[i].isalpha():
            new_text += texted_list[i][1:] + texted_list[i][:1] + 'ay' + ' '
        else:
            new_text += texted_list[i]
    logger.info(f'Success, take your string: {new_text}')

    return new_text.strip()

dt = pig_it('Pig latin is cool !')
