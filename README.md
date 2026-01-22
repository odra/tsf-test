Test trudag cli and TSF.

## Build project

```
make hello
```

## Use TSF (via trudag)


```
trudag manage set-item HELLO-BIN
trudag manage lint
trudag score
```

To save trudag score data arifact:

```
trudag score --validate --dump tsf.json
```

Publish results in `docs/` (markdown files):
```
trudag publish
```
