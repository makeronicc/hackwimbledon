# hackwimbledon

The [HackWimbledon](https://hackwimbledon.org) website, built with [Hugo](https://gohugo.io/) and the [Ananke](https://github.com/gohugo-ananke/ananke) theme.

## Development

```zsh
hugo server
```

## Updating the Ananke theme

```zsh
# Get the latest version (or pin a specific one)
hugo mod get github.com/gohugo-ananke/ananke/v2@latest

# Regenerate the vendor directory
hugo mod vendor

# Check for warnings or errors
hugo build
```

After updating, check whether any of the project's theme overrides in `layouts/_partials/` need updating against the new theme version:

```zsh
for f in site-header site-navigation page-header; do
  echo "=== $f ==="
  diff layouts/_partials/${f}.html \
       _vendor/github.com/gohugo-ananke/ananke/v2/layouts/_partials/${f}.html
done
```

The files `head-additions.html`, `site-scripts.html`, and `tags.html` in `layouts/_partials/` are project-specific and do not need to be checked against the theme.
