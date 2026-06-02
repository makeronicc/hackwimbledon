# HackWimbledon Site Build Tasks

# Default recipe (list available commands)
default:
    @just --list

# Build the site with minification and garbage collection
build:
    HUGO_ENV=production hugo --gc --minify

# Serve the site locally for development
serve:
    hugo server

# Clean the public directory
clean:
    rm -rf public/ resources/_gen/

# Build from scratch (clean + build)
rebuild: clean build

# Pull latest changes from git and rebuild
update:
    git pull
    hugo mod vendor
    just rebuild

# Check Hugo version
version:
    hugo version

# Validate config and template setup
check:
    hugo config
    hugo mod verify

# Quick build and restart nginx (for container deployment)
deploy: build
    sudo systemctl restart nginx

# Watch for changes and rebuild automatically (without server)
watch:
    hugo --watch
