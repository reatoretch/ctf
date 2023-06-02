#coding:utf-8
from PIL import Image

#画像の読み込み
im = Image.open("./output.png")

#RGBに変換
rgb_im = im.convert('RGB')

#画像サイズを取得
size = rgb_im.size

#取得したサイズと同じ空のイメージを新規に作成
im2 = Image.new('RGBA',size)
dict_color = {"r":(255,0,0),"b":(0,0,255),"g":(0,255,0),"y":(255,255,0),"c":(0,255,255),"m":(255,0,255),"k":(0,0,0),"w":(255,255,255),"a":(28,128,128)}
dict_char = {
    "A":["m","r","g","y","b","c"],
    "B":["r","m","g","y","b","c"],
    "C":["r","g","m","y","b","c"],
    "D":["r","g","y","m","b","c"],
    "E":["r","g","y","b","m","c"],
    "F":["r","g","y","b","c","m"],
    "G":["g","r","y","b","c","m"],
    "H":["g","y","r","b","c","m"],
    "I":["g","y","b","r","c","m"],
    "J":["g","y","b","c","r","m"],
    "K":["g","y","b","c","m","r"],
    "L":["y","g","b","c","m","r"],
    "M":["y","b","g","c","m","r"],
    "N":["y","b","c","g","m","r"],
    "O":["y","b","c","m","g","r"],
    "P":["y","b","c","m","r","g"],
    "Q":["b","y","c","m","r","g"],
    "R":["b","c","y","m","r","g"],
    "S":["b","c","m","y","r","g"],
    "T":["b","c","m","r","y","g"],
    "U":["b","c","m","r","g","y"],
    "V":["c","b","m","r","g","y"],
    "W":["c","m","b","r","g","y"],
    "X":["c","m","r","b","g","y"],
    "Y":["c","m","r","g","b","y"],
    "Z":["c","m","r","g","y","b"],
    ".":["k","w","w","k","k","w"],
    ",":["w","k","k","w","w","k"],
    " ":["w","w","w","w","w","w"],
    " ":["k","k","k","k","k","k"],
    "0":["k","a","w","k","a","w"],
    "1":["a","k","w","k","a","w"],
    "2":["a","w","k","k","a","w"],
    "3":["a","w","k","a","k","w"],
    "4":["a","w","k","a","w","k"],
    "5":["w","a","k","a","w","k"],
    "6":["w","k","a","a","w","k"],
    "7":["w","k","a","w","a","k"],
    "8":["w","k","a","w","k","a"],
    "9":["k","w","a","w","k","a"],
}
def get_hex(x,y):
    arr = []
    arr.append(rgb_im.getpixel((x    ,y)))
    arr.append(rgb_im.getpixel((x+1,y)))
    arr.append(rgb_im.getpixel((x    ,y+1)))
    arr.append(rgb_im.getpixel((x+1,y+1)))
    arr.append(rgb_im.getpixel((x    ,y+2)))
    arr.append(rgb_im.getpixel((x+1,y+2)))
    get_char(arr)

def get_char(arr):
    ar = []
    for i in range(6):
        for j in dict_color.keys():
            if (dict_color[j] == arr[i]):
                ar.append(j)
                exit
    check(ar)
    
def check(ar):
    for i in dict_char.keys():
        if (list(dict_char[i]) == ar):
            print(i,end="")

for y in range(2,size[1]-2,3):
    for x in range(2,size[0]-2,2):
        #ピクセルを取得
        get_hex(x,y)
