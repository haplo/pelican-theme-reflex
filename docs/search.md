Reflex integrates with the [pelican-search](https://github.com/pelican-plugins/search) plugin to provide search from a self-hosted index.

Underneath it uses [Stork](https://github.com/jameslittle230/stork/), a fast search system for static sites. The index is generated at build/publish time and loaded by clients directly. This way you don't need a search provider, visitors search directly without any extra queries.

To enable it follow the [installation instructions](https://github.com/pelican-plugins/search#installation) of the plugin.

Control Stork settings by using `STORK_INPUT_SETTINGS` in your `pelicanconf.py`. This is a good starting point:

```python
STORK_INPUT_OPTIONS = {
    "break_on_file_error": True,  # detect errors early
    "stemming": "english",        # https://snowballstem.org/algorithms/
    "url_prefix": SITEURL,        # common URL prefix to all results
}
```

`STORK_OUTPUT_SETTINGS` can also be set, but they are mostly for debugging purposes.

All available input and output options are described in [Stork's documentation](https://stork-search.net/docs/config-ref).
