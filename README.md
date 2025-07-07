This works fine

```
pytest tests/
```

But this fails during pytest execution stage
```
mutmut run
```

with the error:
> TypeError: 'async for' requires an object with __aiter__ method, got generator
