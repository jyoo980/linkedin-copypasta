from typing import *
from random import randrange
from constants import *

template: str = "I had a candidate reach out to me looking for a new position after a gap in his employment." \
                " He was not the traditional candidate, and most would have passed on him, but being the #{persona_hashtag}" \
                " {persona} that I am, I decided to speak to him on the phone. The conversation that transpired" \
                " was #{convo_hashtag}. I learned that he {person_action} and {person_action_2}. While he was {person_action_3}," \
                " a {animal_action} and he had to {person_ability} to {person_to_animal_action}. He {person_action_4} and" \
                " {person_action_5}. This explained his gap in employment. If it wasn't for my ability to #{persona_hashtag_2}" \
                " and give all candidates from all walks of life a chance, this individual would not have been able to find" \
                " fulfilling employment. Luckily we were able to match him with a fantastic #{company_descriptor} firm as a {job}." \
                " This is why I love my job. #GiveEveryoneAChance #DreamJob #PleaseSendMeAMessageForFantasticOpportunitiesLikeThis"

def get_random(arr: List[str]) -> str:
    limit: int = len(arr)
    rand_index: int = randrange(limit)
    return arr[rand_index]

print(template.format(persona_hashtag=get_random(PERSONA_HASHTAG_1), persona=get_random(PERSONAS), convo_hashtag=get_random(CONVERSATION_HASHTAG), 
                    person_action=get_random(PERSON_ACTION), person_action_2=get_random(PERSON_ACTION_2), person_action_3=get_random(PERSON_ACTION_3),
                    animal_action=get_random(ANIMAL_ACTION), person_ability=get_random(PERSON_ABILITY), person_to_animal_action=get_random(PERSON_TO_ANIMAL_ACTION),
                    person_action_4=get_random(PERSON_ACTION_4), person_action_5=get_random(PERSON_ACTION_5), persona_hashtag_2=get_random(PERSONA_HASHTAG_2),
                    company_descriptor=get_random(COMPANY_DESCRIPTOR), job=get_random(JOB))
) 
