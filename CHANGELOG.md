## 3.2.0

This release updates the built-in search support via Stork.

- Upgrade bundled [Stork](https://stork-search.net/) to latest stable version v1.6.0. CSS styles have been improved to optimize looks in both mobile and desktop.
- Enable search in example site.
- Update and recompile translations.
- Serve LESS 4.5.1 via CDN when `USE_LESS` is enabled.

## 3.1.0

This release includes accessibility improvements, pre-commit hooks, and various enhancements.

- Accessibility improvements:
  - Underline links inside main content, to make them recognizable without color.
  - Improve contrast of link colors
  - Add ARIA names to sidebar social icons.
- Add pre-commit hooks for code quality:
  - djlint for Jinja2 templates
  - Trailing whitespace
  - JSON/YAML checker
  - Assets build
- Move `static/`, `templates/`, and `translations/` directories back to root to make it easier to use the theme from source code (e.g. a `git clone`). Reflex remains installable via PyPI with the same interface.
- Upgrade Isso to 0.13.0.
- Highlight Isso comments made by the page author.
- Refactor footer templates.
- Remove Flex-inherited Google Analytics config.
- Mark AddThis as defunct in README (will be removed in Reflex 4.0.0).

## 3.0.3

This is a minor maintenance release.

- Fix links to Github on the PyPI project page.

## 3.0.2

This is a bugfix release.

- Fix wrong references to the project, from *python-theme-reflex* to *pelican-theme-reflex*. While this didn't affect the functionality of Reflex, it affected the installation instructions and most links.

## 3.0.1

This is the first release on PyPI as [pelican-theme-reflex](https://pypi.org/project/pelican-theme-reflex/).

- Fix Python package structure.
- Upgrade NPM dependencies.

## 3.0.0

First release after forking off [Flex](https://github.com/alexandrevicenzi/Flex) v2.5 by [alexandrevicenzi](https://github.com/alexandrevicenzi).

~~This is the first release on PyPI as [pelican-reflex](https://pypi.org/project/pelican-reflex/).~~ (the release was buggy and was pulled)

Changes since Flex 2.5:

- gulp watch support.
- Style for *toc* markdown extension.
- Fix styles for `figure` and `figcaption` HTML elements.
- Shynet tracking support.
- In-repo documentation instead of Github wiki.
- Updated Pygments styles, new themes available.
- Updated FontAwesome to 6.7.2.
- Make `<strong>` text bold (it was being overridden inside `<blockquote>` and potentially other tags)
- Revamped example site for testing and demonstration.
- Display language flags for alternative article languages.
- X (formerly Twitter) social icon.
- AGENTS.md for AI development.
- GitHub Actions workflows for CI/CD.

Thanks to [Loïc Penaud](https://github.com/lpenaud) for contributing the gulp watch task.
