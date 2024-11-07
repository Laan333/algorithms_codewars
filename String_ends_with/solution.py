import logging

logger = logging.getLogger(__name__)



def solution(text:str, ending:str) -> bool:
    logger.info(f'Первоначальный текст: {text} \nОкончание : {ending}')
    len_text_endings = len(ending)
    if text[len(text) - len_text_endings:] == ending:
        return True
    else:
        return False



dt = solution('samurai', 'ra')
print(dt)
