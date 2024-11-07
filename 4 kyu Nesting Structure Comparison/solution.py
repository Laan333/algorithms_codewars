import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

def same_structure_as(original,other):
    logger.info('Starting script')
    if isinstance(original,list) and isinstance(other, list):
        if len(original) != len(other):
            logger.warning('Lists doesnt have equal length')
            return False
    else:
        logger.warning('This is not the lists')
        return False
    for first_list, second_list in zip(original, other):
        if isinstance(first_list, list) and isinstance(second_list, list):
            if not same_structure_as(first_list, second_list):
                logger.warning('Lists doesnt have equals structure')
                return False
        elif isinstance(first_list,list) or isinstance(second_list, list):
            logger.warning('Lists doesnt have equals structure')
            return False
    logger.info('Lists have equal structure. Success')
    return True

same_structure_as([1,[1,1]],[2,[2,2]])