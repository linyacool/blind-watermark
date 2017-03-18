# blind-watermark
# Usage
```shell
python encode.py --image <image file> --watermark <watermark file> --result <result file>

python decode.py --original <original image file> --image <image file> --result <result file>

Use --alpha to change the alpha (default 2.0).
```
# Example
## encode:
original image<br>
![image](https://github.com/linyacool/blind-watermark/blob/master/ori.png)

watermark<br>
![image](https://github.com/linyacool/blind-watermark/blob/master/watermark.png)

result<br>
![image](https://github.com/linyacool/blind-watermark/blob/master/res.png)

## decode:
watermark<br>
![image](https://github.com/linyacool/blind-watermark/blob/master/extract.png)
