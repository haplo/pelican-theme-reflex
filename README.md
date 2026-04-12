# Reflex

A minimalist [Pelican](https://getpelican.com/) theme, forked from [Flex](https://github.com/alexandrevicenzi/Flex).

Check out the [live example site](https://haplo.github.io/pelican-theme-reflex/).
Its source code is [in the example directory](https://github.com/haplo/pelican-theme-reflex/tree/main/example).

## Differences with Flex

- [In-repo documentation](https://github.com/haplo/pelican-theme-reflex/tree/main/docs) instead of Github wiki.
- Shynet tracking support.
- [Table of contents](https://github.com/haplo/pelican-theme-reflex/blob/main/docs/toc.md) styling.
- [Figures and captions](https://github.com/haplo/pelican-theme-reflex/blob/main/docs/figures.md) support.
- X social icon.

## Features

- Mobile First
- Responsive
- Semantic
- SEO best practices
- Open Graph
- Rich Snippets (JSON-LD)
- Related Posts (via [plugin](https://github.com/getpelican/pelican-plugins/tree/master/related_posts) or [AddThis](https://en.wikipedia.org/wiki/AddThis) (*defunct*))
- Series (via [plugin](https://github.com/pelican-plugins/series))
- Minute read (via [plugin](https://github.com/getpelican/pelican-plugins/tree/master/post_stats))
- [Multiple code highlight styles](https://github.com/haplo/pelican-theme-reflex/blob/main/docs/code_highlight.md)
- [Translation support](https://github.com/haplo/pelican-theme-reflex/blob/main/docs/translation.md)
- [Dark mode](https://github.com/haplo/pelican-theme-reflex/blob/main/docs/dark_theme.md)

## Integrations

- [AddThis](http://www.addthis.com/)
- [Disqus](https://disqus.com/)
- [Gauges Analytics](http://get.gaug.es/)
- [Google AdSense](https://www.google.com.br/adsense/start/)
- [Google Analytics](https://www.google.com/analytics/web/)
- [Google Tag Manager](https://www.google.com/tagmanager/)
- [Matomo Analytics (formerly Piwik)](https://matomo.org/)
- [StatusCake](https://www.statuscake.com/)
- [Isso](https://posativ.org/isso/)
- [Microsoft Clarity](https://clarity.microsoft.com)
- [Shynet](https://github.com/milesmcc/shynet)

## Plugins Support

- [Github Corners](https://github.com/tholman/github-corners)
- [I18N Sub-sites](https://github.com/getpelican/pelican-plugins/tree/master/i18n_subsites)
- [Minute read](https://github.com/getpelican/pelican-plugins/tree/master/post_stats)
- [Related Posts](https://github.com/getpelican/pelican-plugins/tree/master/related_posts)
- [Series](https://github.com/pelican-plugins/series)
- [Representative image](https://github.com/getpelican/pelican-plugins/tree/master/representative_image)
- [Neighbors](https://github.com/getpelican/pelican-plugins/tree/master/neighbors)
- [Pelican Search](https://github.com/pelican-plugins/search) (requires [Stork](https://stork-search.net/))
- [Tipue Search](https://github.com/getpelican/pelican-plugins/blob/master/tipue_search/) (deprecated)
- [SEO](https://github.com/pelican-plugins/seo)

## Install

The theme can be installed from PyPI:

```
pip install pelican-theme-reflex
```

Then in your *pelicanconf.py*:

```python
from pelican.themes import reflex
THEME = reflex.path()
```

The alternative way is to clone this repository.
The `main` branch should be stable and safe to checkout.
Then point your `THEME` setting in the pelican project to its path.

## Settings

Look at [settings documentation](https://github.com/haplo/pelican-theme-reflex/blob/main/docs/settings.md) for details.

## Sites using Reflex

- [https://blog.fidelramos.net/](https://blog.fidelramos.net/) ([source code](https://github.com/haplo/blog.fidelramos.net))

If you have a site using Reflex feel free to open a PR to add it here.

## Contributing

Always open an issue before sending a PR.
Discuss the problem/feature that you want to code.
After discussing, send a PR with your changes.

See the [development documentation](https://github.com/haplo/pelican-theme-reflex/blob/main/docs/developing.md).

Thank you to all contributors!

- [Loïc Penaud](https://github.com/lpenaud)

## License

MIT ([full license](https://github.com/haplo/pelican-theme-reflex/blob/main/LICENSE))
