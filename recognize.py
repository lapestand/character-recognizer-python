import cv2
import numpy as np

is_font_known = False
all_fonts = ["A", "T"]
all_puntos = range(10, 44)


def resize(img, target_row, target_col):
    base_row = img.shape[0]
    base_col = img.shape[1]
    # print(base_row, base_col, target_row, target_col)
    return [[img[int(base_row * r / target_row)][int(base_col * c / target_col)]
             for c in range(target_col)] for r in range(target_row)]


def calculate_fault(img, template):
    (row, col) = img.shape
    not_eq = 0
    for i in range(0, row):
        for j in range(0, col):
            # print("{},{} -> img: {}\tbase: {}".format(i, j, img[i, j], base_img[i, j]))
            if template[i, j] != img[i, j]:
                not_eq += 1
    return not_eq / (row * col)


def d_min(d, c=None):
    if c is None:
        c = []
    if all(not isinstance(i, dict) for i in d.values()):
        _m = min(d.values())
        yield c, {a: b for a, b in d.items() if b == _m}, _m
    else:
        yield from [i for a, b in d.items() for i in d_min(b, c + [a])]


def to_tuple(d, v):
    return d[0], v if not d[1:] else to_tuple(d[1:], v)


def recognize_letter(img):
    global is_font_known, all_fonts
    fault = {}
    chars = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
        'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
    ]
    if not is_font_known:
        for char in chars:
            fault[char] = {}
            for font in all_fonts:
                fault[char][font] = {}
                for punto in all_puntos:
                    template = cv2.imread("Templates/{}/{}{}.png".format(char, font, punto))[:, :, 0]
                    # print(
                    #     "Templates/{}/{}{}.png".format(char, font, punto),
                    #     img.shape
                    # )
                    resized_img = np.array(resize(img, template.shape[0], template.shape[1]))
                    fault[char][font][punto] = calculate_fault(resized_img, template)
    else:
        for char in chars:
            fault[char] = {}
            for font in all_fonts:
                fault[char][font] = {}
                for punto in all_puntos:
                    template = cv2.imread("Templates/{}/{}{}.png".format(char, font, punto))[:, :, 0]
                    # print(
                    #     "Templates/{}/{}{}.png".format(char, font, punto),
                    #     img.shape
                    # )
                    resized_img = np.array(resize(img, template.shape[0], template.shape[1]))
                    fault[char][font][punto] = calculate_fault(resized_img, template)

    p, result, _ = min(d_min(fault), key=lambda x: x[-1])
    # is_font_known = True  # <-- Doubles performance but may cause incorrect recognition
    # all_fonts = [p[1]]
    # all_puntos = [p[3]]
    # print(to_tuple(p, result))
    return p[0]


def recognize_letters(img_arr, features):
    global all_fonts, all_puntos, is_font_known
    if features[1] != ['A', 'T']:
        is_font_known = True
        all_fonts = features[1]
    all_puntos = features[2]

    letter = ""
    for img in img_arr:
        letter += recognize_letter(img)

    return letter
