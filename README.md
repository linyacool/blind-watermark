# blind-watermark

# Usage
```shell
python encode.py --image <image file> --watermark <watermark file> --result <result file>

python decode.py --original <original image file> --image <image file> --result <result file>

Use --alpha to change the alpha (default 5.0).
```
# Example
## encode:
original image<br>
![image](./ori.png)

watermark<br>
![image](./watermark.png)


```shell
python encode.py --image ori.png --watermark watermark.png --result res.png
```
Or
```shell
python encode.py --image ori.png --watermark 'My Message' --result res.png
```

result<br>
![image](./res.png)

## decode:
```shell
python decode.py --original ori.png --image res.png --result extract.png
```
watermark<br>
![image](./extract.png)

