# Download windbg symbols offline

## Prepare *windbg.log* via windbg prompt
[Edit] -> [Open/Close Log File...] -> Input [Log file name:]

## Reload symbols and write download failure message to **windbg.log**
``` console
> !sym noisy
> .reload /f
```
## Download symbols file
``` console
> python3 offline_download.py
```

## Reference
https://blog.csdn.net/counsellor/article/details/104721338
