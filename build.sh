#!/bin/bash
set -e

echo "Building Tailwind CSS..."

# Install Node.js dependencies
cd theme/static_src
npm install

# Build Tailwind CSS
npm run build

# Go back to project root
cd ../..

echo "CSS build complete!"
