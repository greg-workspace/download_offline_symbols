# Download windbg symbols offline

## Prepare *windbg.log* via windbg prompt
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
