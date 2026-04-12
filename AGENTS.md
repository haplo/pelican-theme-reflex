# AGENTS.md - Development Guide for Reflex Pelican Theme

## Project Overview

Reflex is a minimalist Pelican theme using Jinja2 templates, LESS stylesheets, and JavaScript. It uses Gulp for asset compilation.

## Directories to Ignore

When exploring or searching the codebase, skip these directories — they contain generated, cached, or third-party content with no project source code:

- `.git/` — VCS internals
- `dist/` — Build output (wheel/sdist)
- `node_modules/` — Third-party JS dependencies
- `.venv/` — Python virtual environment
- `__pycache__/` — Python bytecode cache
- `.mypy_cache/` — Type checker cache
- `.pdm-build/` — PDM build temp directory
- `example/output/` — Generated example site

## Build Commands

### Node.js/Gulp (Asset Compilation)

```bash
# Install dependencies
npm install

# Build all assets (CSS, JS, fonts, pygments)
npm run build
# or: gulp default

# Watch for changes and rebuild automatically
npm run watch
# or: gulp watch

# Individual gulp tasks:
gulp less        # Compile LESS to CSS
gulp uglify      # Minify JS
gulp cp          # Copy font-awesome assets
gulp pygments    # Minify pygments CSS
```

### Python/Pelican (Testing)

```bash
# Build example site (test the theme)
pelican -s example/pelicanconf.py
```

### Example Site (in example/ directory)

```bash
cd example/

# Generate site
make html

# Serve locally
make serve PORT=8000

# Development server with auto-regeneration
make devserver PORT=8000

# Clean build
make clean

# Publish (production settings)
make publish
```

## Code Style Guidelines

### Jinja2 Templates

- Use 2-space indentation
- Use snake_case for variables
- Use double quotes for HTML attributes
- Include spaces inside Jinja2 delimiters: `{{ var }}` not `{{var}}`
- Use `-` for whitespace control in macros: `{%- macro -%}`
- Place template comments on their own line: `{# comment #}`
- Use `{% include %}` with quotes: `{% include "partial/sidebar.html" %}`
- Check for plugin availability before including: `{% if PLUGINS and 'plugin_name' in PLUGINS %}`

### LESS/CSS

- Use 2-space indentation
- Place opening brace on same line: `selector {`
- Use lowercase with hyphens for class names: `.dark-theme`
- Import variables at top: `@import "variables.less";`
- Use variables from variables.less for colors and fonts
- Add trailing semicolons
- Group related properties together

### JavaScript

- Use 2-space indentation
- Use semicolons
- Use camelCase for variables and functions
- Use PascalCase for constructor functions
- Prefer single quotes for strings
- Add spaces around operators: `var x = a + b;`
- Document functions with inline comments

### File Naming

- Templates: lowercase with hyphens (e.g., `base.html`, `dark-theme.less`)
- Partials: place in templates/partial/ directory
- Stylesheets: use `.less` extension for source, `.min.css` for compiled
- JavaScript: use `.js` extension for source, `.min.js` for minified

## Project Structure

```
.
├── pelican/
│   └── themes/
│       └── reflex/
│           └── __init__.py    # path() function for Pelican
├── static/                    # Static assets
│   ├── stylesheet/            # LESS/CSS files
│   ├── dark-theme/            # Dark theme JS
│   ├── pygments/              # Code highlighting styles
│   ├── font-awesome/          # Font Awesome assets
│   └── stork/                 # Stork search JS/WASM/CSS
├── templates/                 # Jinja2 templates
│   ├── partial/               # Reusable template partials
│   ├── base.html              # Base template
│   ├── article.html           # Article page
│   └── index.html             # Index page
├── translations/              # i18n translations
├── docs/                      # Documentation
├── example/                   # Example Pelican site
├── gulpfile.js                # Gulp build configuration
├── pdm_build.py               # Build hook for package distribution
└── package.json               # Node.js dependencies
```

## Pre-commit Hooks

Pre-commit hooks run automatically on `git commit` to ensure code quality:

```bash
# Install pre-commit (one-time setup)
pip install pre-commit
pre-commit install

# Run manually on all files
pre-commit run --all-files
```

Hooks configured:
- **trailing-whitespace** - File hygiene
- **check-json / check-yaml** - Validate config files
- **djlint** - Format and lint Jinja2 templates
- **npm-build-check** - Verify compiled assets are up to date (runs only when source files change)

## Testing

- Tests build the example/ site as a smoke test
- No unit tests - testing is done by building the theme

## Dependencies

### Node.js (package.json)

- gulp: ^4.0.2
- gulp-cssnano: ^2.1.3
- gulp-less: ^4.0.1
- gulp-rename: ^2.0.0
- gulp-uglify: ^3.0.2

### Python (for testing)

- pelican
- pelican-search (for search functionality)
- Dependencies in example/requirements.txt

### System Dependencies

- **Stork** (v1.6.0): Required by pelican-search plugin for generating search indexes. Install from [stork-search.net](https://stork-search.net/docs/install). The theme bundles Stork JS/WASM/CSS assets in `static/stork/`.

## Common Tasks

### Adding a New Template Partial

1. Create file in `templates/partial/`
2. Include in base.html or relevant template
3. Follow 2-space indentation
4. Use existing partials as reference

### Adding New Styles

1. Edit appropriate `.less` file in `static/stylesheet/`
2. Use variables from `variables.less`
3. Run `gulp less` or `npm run watch` to compile
4. Test in both light and dark themes

### Adding JavaScript

1. Edit source file in `static/dark-theme/`
2. Run `gulp uglify` to minify
3. Ensure minified version is referenced in templates

### Enabling Search

The theme supports search via pelican-search plugin with Stork:

1. Install stork binary system-wide
2. Add `'pelican.plugins.search'` to `PLUGINS` in pelicanconf.py
3. Set `STORK_VERSION` to use CDN, or omit to use bundled assets
4. The search input is in `templates/partial/sidebar.html`
5. Stork assets are in `static/stork/` (bundled: v1.6.0)

Settings for pelicanconf.py:
```python
PLUGINS = ['pelican.plugins.search']
STORK_VERSION = "1.6.0"  # Use CDN (recommended)
# OR omit STORK_VERSION to use bundled assets

# Optional: configure stork indexing
STORK_INPUT_OPTIONS = {
    "url_prefix": SITEURL,
}
```

## Releasing

See [RELEASE.md](RELEASE.md) for the full release process.

Quick summary:

1. Update version in `pyproject.toml` and `package.json`
2. Update `CHANGELOG.md`
3. Write new article in `/example/content/articles/`
4. Run `npm run build`
5. Commit and tag: `git tag -a vX.Y.Z -m "Release vX.Y.Z"`
6. Push tag: `git push origin vX.Y.Z`
7. Create GitHub release: `gh release create vX.Y.Z --generate-notes`

PyPI publishing is automated via the `pypi-publish.yml` workflow when a `v*` tag is pushed. The workflow calls `check-npm-build.yml` to verify assets are up to date before publishing.

## Translations

The theme uses Babel for i18n. Translations are in `translations/` as `.po` (catalog) and `.mo` (compiled) files. The `.pot` file is the template extracted from Jinja2 templates.

### Translation workflow when templates change

**Any time templates are added, removed, or their translatable strings change**, you must update translations:

1. **Extract** — Regenerate the `.pot` file from current templates:
   ```bash
   ./translate.sh extract
   ```

2. **Update** — Propagate changes to all `.po` catalogs (new strings added, removed strings marked `#~` obsolete):
   ```bash
   ./translate.sh update
   ```

3. **Edit** — If needed, fix obsolete entries in `.po` files (remove `#~` blocks for deleted strings, translate new `msgstr ""` entries).

4. **Compile** — Build `.mo` binary files from `.po` catalogs:
   ```bash
   ./translate.sh compile
   ```

All four steps must be run in order. Do not skip compile — `.mo` files must be committed alongside `.po` changes.

### Adding a new language

```bash
./translate.sh new <lang_code>
```

Then edit the generated `.po` file and run `./translate.sh compile`.

### Key details

- Translatable strings in templates use `{{ _("string") }}` or `{% trans %}string{% endtrans %}`
- The `babel.cfg` in `translations/` maps template extraction rules
- `.pot` = message template, `.po` = per-language catalog, `.mo` = compiled binary used at runtime

## Notes

- Pre-commit hooks enforce code style and verify compiled assets
- A PR check (`check-npm-build.yml`) verifies that built assets are up to date; PRs with stale assets cannot be merged
- The theme supports both light and dark modes
- Font Awesome is copied from node_modules to static/
- Pygments styles are minified but kept as separate files
