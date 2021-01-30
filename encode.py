# coding=utf-8
import cv2
import numpy as np
import random
import os
from argparse import ArgumentParser
from PIL import Image, ImageDraw, ImageFont
ALPHA = 5


def build_parser():
    parser = ArgumentParser()
    parser.add_argument('--image', dest='img', required=True)
    parser.add_argument('--watermark', dest='wm', required=True)
    parser.add_argument('--result', dest='res', required=True)
    parser.add_argument('--alpha', dest='alpha', default=ALPHA)
    return parser


def main():
    parser = build_parser()
    options = parser.parse_args()
    img = options.img
    wm = options.wm
    res = options.res
    alpha = float(options.alpha)
    if not os.path.isfile(img):
        parser.error("image %s does not exist." % img)
    if not os.path.isfile(wm):
        tmp_path = './wm.png'
        generate_watermark_from_text(wm, tmp_path)
        wm = tmp_path
        #parser.error("watermark %s does not exist." % wm)
    encode(img, wm, res, alpha)


def generate_watermark_from_text( text, watermark_path, width=512, height=64 ):
    background_color = ( 255, 255, 255 )
    font_color = ( 0, 0, 0 )
    size = ( width, height )
    img = Image.new('RGB', size, color=background_color)
    d = ImageDraw.Draw(img)
    fnt = ImageFont.truetype('./NotoSansCJKjp-Bold.otf', 32)
    d.text((10,10), text, font=fnt, fill=font_color)
    img.save( watermark_path )



def encode(img_path, wm_path, res_path, alpha):
    img = cv2.imread(img_path)
    img_f = np.fft.fft2(img)
    height, width, channel = np.shape(img)
    watermark = cv2.imread(wm_path)
    wm_height, wm_width = watermark.shape[0], watermark.shape[1]
    x, y = list(range(int(height / 2))), list(range(width))
    random.seed(height + width)
    random.shuffle(x)
    random.shuffle(y)
    tmp = np.zeros(img.shape)
    for i in range(int(height / 2)):
        for j in range(width):
            if x[i] < wm_height and y[j] < wm_width:
                tmp[i][j] = watermark[x[i]][y[j]]
                tmp[height - 1 - i][width - 1 - j] = tmp[i][j]
    res_f = img_f + alpha * tmp
    res = np.fft.ifft2(res_f)
    res = np.real(res)
    cv2.imwrite(res_path, res, [int(cv2.IMWRITE_JPEG_QUALITY), 100])


if __name__ == '__main__':
    main()
