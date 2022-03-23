
from PIL import Image
from mpmath import mp


def to_ascii(image, size, resize=True, reverse=True, scale=" .:-=+*#%@", tresh_inex=0, tresh_val=1, tresh_mod=" ",
             LINE_SEP='\n', auto_print=False, return_type=1, xwidth=1, ywidth=1, seq="", seq_key="", seq_getchar=False):
    '''

    :type - EPIC DOCUMENTATION

    :param image - PIL image object
    :param size - size you want to rescale yout image to
    :param resize - if set to false the image wont be resized
    :param reverse - if set to true will reverse the ascii shadow scale
    :param scale - ascii shadow scale
    :param tresh_inex - index if set to 0 will add thresh modifier to the begining of the scale array
    :param tresh_val - how many times thresh modifier will be added to array
    :param tresh_mod - defined as thresh modifier will be added to the array thresh_val times at the begining/end of array
    :param LINE_SEP - separates lines in image processing
    :param auto_print - instead of returning the output simply print it
    :param return_type - return as a plain string(1) | return as 2d array(2) |
    :param xwidth - wide in x
    :param ywidth - wide in y
    '''

    if tresh_inex == 0:
        scale = tresh_mod * int(tresh_val) + scale
    if tresh_inex == 1:
        scale = scale + tresh_mod * int(tresh_val)

    if reverse == True:
        scale = reversed(scale)
    shadows = list(scale)
    if resize == True:
        im = image.resize((size, size))
    else:
        im = image

    im = im.convert("L")

    if return_type == 1 or return_type == 3:
        o = ""
        t_x_s = ""
    if return_type == 2:
        o = []
        t_x = []
    if seq == "":
        for y in range(im.size[1]):
            for x in range(im.size[0]):

                consts = int(255 / (len(shadows) - 1)) + 1

                if return_type == 1 or return_type == 3:
                    for i in range(xwidth):
                        t_x_s += shadows[int(im.getpixel((x, y)) / consts)]
                elif return_type == 2:
                    for i in range(xwidth):
                        t_x.append(shadows[int(im.getpixel((x, y)) / consts)])
            if return_type == 1 or return_type == 3:
                for i in range(ywidth):
                    o += t_x_s + LINE_SEP
                t_x_s = ""
            elif return_type == 2:
                for i in range(ywidth):
                    o.append(t_x)
                t_x = []
        if auto_print == True:
            print(o)
            return None
        if return_type == 3:
            with open("o.txt", "wb") as f:
                f.write(o.encode("utf-8"))
                f.close()
        return o
    else:

        for y in range(im.size[1]):
            for x in range(im.size[0]):

                consts = int(255 / (len(shadows) - 1)) + 1
                for i in range(xwidth):
                    t_x_s += shadows[int(im.getpixel((x, y)) / consts)]

            for i in range(ywidth):
                o += t_x_s + LINE_SEP
            t_x_s = ""

        if seq_getchar == True:
            r = 0
            for i in range(len(o)):
                if o[i] != seq_key:
                    r += 1
            return int(r)

        index = 0
        if return_type == 1 or return_type == 3:
            ou = ""

        for i in range(len(o)):
            if o[i] == seq_key:
                ou += seq[index]
                index += 1
            else:
                ou += o[i]

        if auto_print == True:
            print(ou)

        elif return_type == 1:
            return ou
        elif return_type == 2:
            return list(ou)
        elif return_type == 3:
            with open("o.txt", "wb") as f:
                f.write(ou.encode("utf-8"))
                f.close()

#wcale nieskomplikowana biblioteka do zamiany zdjęc na ascii
s = 10000
digits = to_ascii(image=Image.open("img_1.png"),size=s,return_type=1,scale="11111111",tresh_val=6,tresh_mod=' ',seq="asdasd",seq_key="1",seq_getchar=True)
print(f"Digits needed : {digits}")
mp.dps = digits
to_ascii(image=Image.open("img_1.png"),size=s,auto_print=False,return_type=3,scale="11111111",tresh_val=6,tresh_mod=' ',seq=str(mp.pi),seq_key="1")



