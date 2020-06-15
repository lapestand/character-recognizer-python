import cv2
import numpy as np


def divide_into_letters(image):
    def cut_img(img):
        wrds = []
        cur_word = []
        for row in img:
            if 0 in row:
                cur_word.append(row)
            elif cur_word:
                wrds.append(np.array(cur_word))
                cur_word = []
        return wrds
    words = cut_img(image.T)  # Find words
    n_words = []
    max_w = 0
    max_h = 0
    for w in words:
        cur_im = cut_img(w.T)[0]  # Resize height
        max_w = cur_im.shape[0] if cur_im.shape[0] > max_w else max_w
        max_h = cur_im.shape[1] if cur_im.shape[1] > max_h else max_h
        n_words.append(cur_im)

    return n_words, max_w, max_h


def extract_letters(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    (thresh, black_and_white_image) = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    images_of_letters, max_width, max_height = divide_into_letters(black_and_white_image)
    return images_of_letters
