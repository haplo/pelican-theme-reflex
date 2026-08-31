Title: Reflex 4.0.1
Date: 2026-08-31 22:00
Category: News
Tags: pelican,python,theme
Slug: reflex-4.0.1

Reflex 4.0.1 is a bugfix release.

- Remove pkgutil shims from `pelican` namespace packages. Shipping `pelican/__init__.py` in the wheel overwrote Pelican's real top-level `__init__.py` when the theme was installed after Pelican, breaking Pelican entirely. Thanks to new contributor [dchemishanov](https://github.com/dchemishanov) for the fix.
