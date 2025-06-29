import cv2
import random
import os

areas = [  # для img2 - img23
    (500, 350, 800, 950),  # корзинка для столовых приборов
    (1320, 250, 1750, 700),  # салат
    (1800, 100, 2500, 830),  # для ребрышек
    (1380, 830, 1700, 1200),  # левая чашка
    (1700, 830, 2100, 1200),  # правая чашка
    (2300, 780, 2900, 1230),  # чайник
    (1100, 1280, 1700, 1950),  # цезарь
    (1650, 1280, 2500, 2100),  # рыба
    (850, 1450, 1200, 1800),  # суп
    (820, 200, 1350, 1000)  # борщ
]
areas_fragment = [
    [(500, 350, 650, 950), (650, 350, 800, 950), (500, 350, 800, 650), (500, 650, 800, 950)],
     [(1320, 250, 1535, 700), (1535, 250, 1750, 700), (1320, 250, 1750, 475), (1320, 475, 1750, 700)],
     [(1800, 100, 2150, 830), (2150, 100, 2500, 830), (1800, 100, 2500, 465), (1800, 465, 2500, 830)],
     [(1380, 830, 1540, 1200), (1540, 830, 1700, 1200), (1380, 830, 1700, 1015), (1380, 1015, 1700, 1200)],
     [(1700, 830, 1900, 1200), (1900, 830, 2100, 1200), (1700, 830, 2100, 1015), (1700, 1015, 2100, 1200)],
     [(2300, 780, 2600, 1230), (2600, 780, 2900, 1230), (2300, 780, 2900, 1005), (2300, 1005, 2900, 1230)],
     [(1100, 1280, 1400, 1950), (1400, 1280, 1700, 1950), (1100, 1280, 1700, 1615), (1100, 1615, 1700, 1950)],
     [(1650, 1280, 2075, 2100), (2075, 1280, 2500, 2100), (1650, 1280, 2500, 1690), (1650, 1690, 2500, 2100)],
     [(850, 1450, 1025, 1800), (1025, 1450, 1200, 1800), (850, 1450, 1200, 1625), (850, 1625, 1200, 1800)],
     [(820, 200, 1085, 1000), (1085, 200, 1350, 1000), (820, 200, 1350, 600), (820, 600, 1350, 1000)]

]
probability = 0.5
probability_fragment = 0.5
counter = 0

output_folder = 'result'

os.makedirs(output_folder, exist_ok=True)

for _ in range(5):

    for img_num in range(2, 24):
        img = cv2.imread(f'img/img{img_num}.jpg')

        for idx, (x1, y1, x2, y2) in enumerate(areas):
            is_not_hidden = True

            if random.random() < probability:
                is_not_hidden = False
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                cv2.rectangle(img, (x1, y1), (x2, y2), color, -1)

            if is_not_hidden and random.random() < probability_fragment:
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                x1, y1, x2, y2 = areas_fragment[idx][random.randint(0, 3)]
                cv2.rectangle(img, (x1, y1), (x2, y2), color, -1)

        cv2.imwrite(f'result/result{counter}.jpg', img)
        counter += 1
