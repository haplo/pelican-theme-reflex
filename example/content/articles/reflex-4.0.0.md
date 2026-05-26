Title: Reflex 4.0.0
Date: 2026-05-26 14:00
Category: News
Tags: pelican,python,theme
Slug: reflex-4.0.0

Reflex 4.0.0 is a major release with breaking changes.

Breaking changes:

- Remove AddThis integration. AddThis was discontinued in 2023; the `ADD_THIS_ID` setting and the `partial/addthis.html` template are gone. Remove `ADD_THIS_ID` from your `pelicanconf.py`.
- Remove Tipue Search support. Use the built-in Stork-based search (`pelican.plugins.search`) instead. See the [search documentation](https://github.com/haplo/pelican-theme-reflex/blob/main/docs/search.md) for details.

New features:

- Internationalize article series strings. Includes a new Spanish (`es`) translation and updates to all existing catalogs.

Other changes:

- Fixes to search in example site.
- Bump GitHub Actions workflow versions.
