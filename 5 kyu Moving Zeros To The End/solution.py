import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def move_zeros(lst: list) -> list:
    '''Function for filter list and add to the ends zeros'''
    logger.info('Starting')
    filtered_list = list(filter(lambda n: n != 0, lst))
    logger.info(f'Filtering first time only with nums {filtered_list}')
    filtered_zeros = list(filter(lambda n: n == 0, lst))
    logger.info(f'Filtering second time {filtered_zeros}')
    logger.info(f'Success, here your list with ended zeros {filtered_list + filtered_zeros}')
    return filtered_list + filtered_zeros


move_zeros([1, 0, 1, 2, 0, 1, 3])  # returns [1, 1, 2, 1, 3, 0, 0]
