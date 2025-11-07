# Quick Start Guide

## Running on Your Local Machine

### Step 1: Navigate to the Repository

First, you need to be in the project directory. Run:

```bash
cd /Users/tlf/ContentCreatorGenerator
```

Or if you haven't cloned it yet:

```bash
cd /Users/tlf
git clone <your-repo-url>
cd ContentCreatorGenerator
```

### Step 2: Choose Your Version

#### Option A: Command Line (Simplest - No Installation)

```bash
python3 content_generator.py
```

This runs the terminal-based version with a menu system.

#### Option B: Web Interface (Local)

```bash
# Install dependencies first (one time only)
pip3 install Flask flask-cors

# Run the web server
python3 api/index.py

# Open your browser to:
# http://localhost:5000
```

## Deploying to Vercel (Fix the 404)

### Method 1: Vercel Dashboard (Recommended)

1. Go to [vercel.com](https://vercel.com)
2. Sign in with GitHub
3. Click "New Project"
4. Import your `ContentCreatorGenerator` repository
5. Vercel auto-detects settings
6. Click "Deploy"
7. Wait 1-2 minutes
8. Visit your live URL!

### Method 2: Vercel CLI

```bash
# Install Vercel CLI
npm i -g vercel

# Navigate to project
cd /Users/tlf/ContentCreatorGenerator

# Deploy
vercel
```

## Troubleshooting

### "No such file or directory" Error

This means you're not in the right folder. Run:
```bash
pwd  # Shows your current directory
cd /Users/tlf/ContentCreatorGenerator  # Navigate to the project
ls   # You should see content_generator.py listed
```

### Vercel 404 Error

The new files I just created fix this! Just:
1. Pull the latest changes: `git pull`
2. Re-deploy on Vercel (it will auto-deploy if connected)

### Port Already in Use (Local Web Version)

If you see "Address already in use":
```bash
# Kill the process using port 5000
lsof -ti:5000 | xargs kill -9

# Or use a different port
python3 api/index.py --port 8000
```

## What Each File Does

- **content_generator.py** - Command-line interface (terminal app)
- **api/index.py** - Web server backend
- **index.html** - Web interface
- **content_generator_core.py** - Core logic (used by both versions)

## Need Help?

Run these commands to verify your setup:
```bash
# Check if you're in the right place
pwd

# List all files
ls -la

# Check Python version (need 3.7+)
python3 --version

# Try running the CLI version
python3 content_generator.py
```
