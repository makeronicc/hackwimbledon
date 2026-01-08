# HackWimbledon Site Build Tasks

# Variables
hugo := if path_exists("/usr/bin/hugo") == "true" { "hugo" } else { "~/bin/hugo-0.153" }

# Default recipe (list available commands)
default:
    @just --list

# Build the site with minification and garbage collection
build:
    {{hugo}} --gc --minify

# Serve the site locally for development (with correct baseURL)
serve:
    {{hugo}} server --baseURL http://localhost:1313/

# Clean the public directory
clean:
    rm -rf public/ resources/_gen/

# Build from scratch (clean + build)
rebuild: clean build

# Pull latest changes from git and rebuild
update:
    git pull
    just rebuild

# Check Hugo version
version:
    {{hugo}} version

# Validate config and check for errors
check:
    {{hugo}} --gc --minify --verbose

# Quick build and restart nginx (for container deployment)
deploy: build
    sudo systemctl restart nginx

# Watch for changes and rebuild automatically
watch:
    {{hugo}} --gc --minify --watch
