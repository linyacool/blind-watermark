# blind-watermark

# Usage
```shell
python encode.py --image <image file> --watermark <watermark file> --result <result file>

python decode.py --original <original image file> --image <image file> --result <result file>

# Use --alpha to change the alpha (default 5.0).

python remove.py <image file>  # You can also drag and drop the file onto remove.py.

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


## remove:
```shell
python remove.py res.png
```
cleaned image<br>
![image](https://github.com/warm-ice0x00/blind-watermark/blob/python3/cleaned.png)
```shell
python decode.py --original ori.png --image cleaned.png --result extract_from_cleaned.png
```
decoded watermark<br>
![image](https://github.com/warm-ice0x00/blind-watermark/blob/python3/extract_from_cleaned.png)