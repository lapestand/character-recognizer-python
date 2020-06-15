import cv2
import extract
import printer as pr

_dir = "2/Templates/"
chars = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
        'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]
errors = []
for _ in range(10, 44):
    for font in ["A", "T"]:
        im_name = "{}{}{}.png".format(_dir, font, _)
        image = cv2.imread(im_name)
        # pr.show_and_destroy(image)
        letters = extract.extract_letters(image)
        if len(letters) == 36:
            for letter, char in zip(letters, chars):
                print("{}{}/{}{}.png".format("Templates/", char, font, _))
                cv2.imwrite("{}{}/{}{}.png".format("Templates/", char, font, _), letter)
        else:
            errors.append(im_name)
            # pr.show_and_destroy(image)
            # for let in letters:
            #     pr.show_and_destroy(let)
print("DONE")
print("Errors are: ")
for error in errors:
    print(error)
    img = cv2.imread(error)
    pr.show_and_destroy(img)
    letters = extract.extract_letters(img)
    for letter in letters:
        pr.show_and_destroy(letter)
        name = input("Enter name of char: ")
        if name != '.':
            cv2.imwrite("{}{}/{}{}.png".format("Templates/", name, 'T', 16), letter)
