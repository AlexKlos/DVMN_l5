import file_operations
import datetime
import time
import random
import os
from faker import Faker


NUMBER_OF_CARDS = 3
TEMPLATE_PATH = 'src/charsheet.svg'
OUTPUT_PATH = 'output/svg/result.svg'
SKILLS = [
    'Стремительный прыжок',
    'Электрический выстрел',
    'Ледяной удар',
    'Стремительный удар',
    'Кислотный взгляд',
    'Тайный побег',
    'Ледяной выстрел',
    'Огненный заряд'
]
LETTERS_MAPPING = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}



def replace_letters(text, mapping):
    result =''
    for char in text:
        result += mapping[char] if char in mapping else result+char
    return result

def main():
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    unic_output_path = OUTPUT_PATH.replace('.', f'_{timestamp}.')
    fake = Faker("ru_RU")
    random_gender = random.randint(0, 1)
    random_skils = random.sample(SKILLS, 3)

    modifed_random_skills = []
    for skill in random_skils:
        modifed_skill = replace_letters(skill, LETTERS_MAPPING)
        modifed_random_skills.append(modifed_skill)

    context = {
        'job': 	fake.job(),
        'town': fake.city(),
        'strength': random.randint(3, 18),
        'agility': random.randint(3, 18),
        'endurance': random.randint(3, 18),
        'intelligence': random.randint(3, 18),
        'luck': random.randint(3, 18),
        'skill_1': modifed_random_skills[0],
        'skill_2': modifed_random_skills[1],
        'skill_3': modifed_random_skills[2]
    }

    context['first_name'] = fake.first_name_female() if random_gender==0 else fake.first_name_male()
    context['last_name'] = fake.last_name_female() if random_gender==0 else fake.last_name_male()

    output_folder = OUTPUT_PATH.rsplit('/', 1)[0]
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    file_operations.render_template(TEMPLATE_PATH, unic_output_path, context)

if __name__ == '__main__':
    for number in range(NUMBER_OF_CARDS):
        main()
        time.sleep(1)
