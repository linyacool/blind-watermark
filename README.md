# blind-watermark
This was written in Python2.7  
[Python3 Version](https://github.com/linyacool/blind-watermark/tree/python3)  
# Usage
```shell
python encode.py --image <image file> --watermark <watermark file> --result <result file>

python decode.py --original <original image file> --image <image file> --result <result file>

Use --alpha to change the alpha (default 5.0).
```
# Example
## encode:
original image<br>
![image](https://github.com/linyacool/blind-watermark/blob/master/ori.png)

watermark<br>
![image](https://github.com/linyacool/blind-watermark/blob/master/watermark.png)


```shell
python encode.py --image ori.png --watermark watermark.png --result res.png
```
result<br>
![image](https://github.com/linyacool/blind-watermark/blob/master/res.png)

## decode:
```shell
python decode.py --original ori.png --image res.png --result extract.png
```
watermark<br>
![image](https://github.com/linyacool/blind-watermark/blob/master/extract.png)
