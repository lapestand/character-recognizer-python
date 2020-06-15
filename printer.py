import cv2
# import os
# import subprocess, platform


def show_and_destroy(img, win_name="test"):
    cv2.imshow(win_name, img)
    cv2.waitKey(0)
    cv2.destroyWindow(win_name)


def menu():
    print(
        "Re-rotation(De-skew) doesn't work! Please give image in horizontal\n"
        "Options are\n"
        "1) 200x50 -> PNG -> Times New Roman -> 20 punto -> Black On White -> Format: "
        "(2 digit city number, 2 digit alphabetic letters, and 2 digit natural numbers)\n"
        "2) 200x50 -> PNG -> Times New Roman -> 20 punto -> Black On White -> Format: "
        "(2 digit city number, 2 digit alphabetic letters, and 2, 3 or 4 digit natural numbers)\n"
        "3) 200x50 -> PNG -> Unknown font & punto -> Black On White -> Format: (Unknown)\n"
        "4) Unknown Size -> PNG -> Unknown font & punto -> Black On White -> Format: (Unknown)\n"
        "5) Unknown Size -> PNG -> Known font & punto & Background -> Format: (Unknown)\n"
        "6) Unknown Size -> PNG -> Unknown font & punto -> Known Background -> Format: (Unknown)\n"
        "7) Unknown Size -> PNG -> Unknown font & punto & Background -> Format: (Unknown)\n"
        "8) Open Source LPR software/tool to recognize LPR.(Doesn't work)"
    )


def select_option():
    opt = 0
    while not 0 < opt < 8:
        cls()
        menu()
        opt = int(input("Enter option: "))
    (size, font, punto, background, _format) = (None, ["A", "T"], range(10, 44), None, [])
    if opt == 1 or opt == 2:
        size = (200, 50)
        font = ["T"]
        punto = [20]
        _format = ["00AA00"] if opt == 1 else ["00AA00", "00AA000", "00AA0000"]
    elif opt == 3:
        size = (200, 50)
    elif opt == 5:
        tmp_font = input("Enter font. Example: times new roman -> ")
        if tmp_font == "arial" or "arial" in tmp_font:
            font = ["A"]
        elif tmp_font == "times new roman":
            font = ["T"]
        tmp_pnt = int(input("Enter punto. Example: 20: "))
        if 43 > tmp_pnt > 10:
            punto = [tmp_pnt]
        else:
            punto = [43] if tmp_pnt > 43 else [10]
        background = input("Enter background color. Example: red: ")
    elif opt == 6:
        background = input("Enter background color. Example: red: ")
    if not _format:
        print("You should give a format to analyse")
        print("Enter example format without space to recognize format")
        print("Example: 01AD75 is 2 digits 2 letters and 2 digits")
        tmp_plate = input("Please Enter example plate: ")
        _format.append(tmp_plate)
    return size, font, punto, background, _format


def cls():
    print(chr(27) + "[2J", end="")
    # print(u"{}[2J{}[;H".format(chr(27), chr(27)), end="")
    # if platform.system() == "Windows":
    #     subprocess.Popen("cls",
    #                      shell=True).communicate()
    # else:  # Linux and Mac
    #     print("\033c", end="")
