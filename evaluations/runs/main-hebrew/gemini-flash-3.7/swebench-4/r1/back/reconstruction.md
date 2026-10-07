<|user|>Remote connections cannot be completed for two processes
Steps to reproduce:

```
ipython console --ip=0
```

And then, try to connect to it from another window:

```
ipython console --exiting
```

and it will hang. If you don't specify --ip, everything works, because the local code goes through a slightly different code path. Just opening this now so that @minrk has something to refer to when he submits the fix

<|assistant|>1. Modify IPython/consoleapp.py
2. Modify IPython/kernel/client.py
3. Modify IPython/qt/console/qtconsoleapp.py
