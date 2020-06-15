import cv2
import extract
import recognize
import syntax
import printer as pr


def main():
    # size, font, punto, background, _format = pr.select_option()
    features = pr.select_option()
    # print(features)
    pr.cls()  # If you run from terminal, cls will work
    print("Image loading...")
    # im_name = "tests/40-arial.png"
    # im_name = "tests/40.png"
    im_name = input("Enter image name(Enter absolute path or add file into the same dir with main.py)(Example: home/"
                    "izzet/resimler/resim.png  OR resim.png)\n")
    # im_name = "tests/01AD75.png"
    image = cv2.imread(im_name)
    print("Image loaded, Preprocessing started!")
    images_of_letters = extract.extract_letters(image)  # Detecting Characters
    print("Pre-processing DONE! Recognizing Starting...")
    letters = recognize.recognize_letters(images_of_letters, features)  # Recognizing Characters
    print("Recognizing DONE!")
    print("Plate is: " + letters)
    print("Syntax controlling starting...")
    if syntax.is_correct(letters, features[4]):
        print("Syntax correct!")
    else:
        print("Syntax wrong!")


if __name__ == '__main__':
    main()
