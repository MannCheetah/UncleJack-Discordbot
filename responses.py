import random

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there!'

    if message == 'roll':
        return str(random.randint(1, 100))

    if p_message == 'nigger':
        return '`You just broke "Rule #3" and I think the admins heard you!!`'

    if p_message == 'faggot':
        return '`You just broke "Rule #3" and I think the admins heard you!!`'

    if p_message == 'fag':
        return '`You just broke "Rule #3" and I think the admins heard you!!`'

    if p_message == 'fagg':
        return '`You just broke rule 3 and I think the admins heard you!!`'

    if p_message == 'fuck':
        return 'Hey Fellas. Cussing is not against the rules, ' \
               'however one of the owners is weirdly into god and might take action if it gets extreme"  '
    if p_message == 'shit':
        return 'Hi Friends. Cussing is not against the rules, ' \
               'however one of the owners is weirdly into god and might take action if it gets extreme"  '
    if p_message == 'bitch':
        return 'Hey Fellas. Cussing is not against the rules, ' \
               'however one of the owners is weirdly into god and might take action if it gets extreme"  '
