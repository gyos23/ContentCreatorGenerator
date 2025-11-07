# Local Setup Guide - Fix "No Such File" Error

## 🚨 The Problem

When you see this error:
```
/usr/local/bin/python3: can't open file '/Users/tlf/content_generator.py': [Errno 2] No such file or directory
```

It means you're not in the right folder!

## ✅ The Solution (Easy Way)

### Option 1: Use the Launcher Script (Easiest!)

**Step 1:** Open Terminal (Applications → Utilities → Terminal)

**Step 2:** Navigate to the project:
```bash
cd /Users/tlf/ContentCreatorGenerator
```

**Step 3:** Run the launcher:
```bash
./run.sh
```

**That's it!** The launcher will:
- ✅ Check if you're in the right place
- ✅ Let you choose CLI or Web version
- ✅ Auto-install dependencies if needed
- ✅ Start the app

### Option 2: Manual Commands

**For CLI Version:**
```bash
cd /Users/tlf/ContentCreatorGenerator
python3 content_generator.py
```

**For Web Version:**
```bash
cd /Users/tlf/ContentCreatorGenerator
pip3 install Flask flask-cors
python3 api/index.py
```

Then open: http://localhost:5000

## 🔍 Finding Your Project

**Don't know where your project is?**

```bash
# Search for it
find ~ -name "ContentCreatorGenerator" -type d 2>/dev/null

# This will show you the path, like:
# /Users/tlf/ContentCreatorGenerator
```

Then:
```bash
cd /Users/tlf/ContentCreatorGenerator   # Use the path it found
./run.sh
```

## 📂 Project Structure

When you're in the right folder, you should see these files:

```bash
ls -la
```

Should show:
```
content_generator.py       ← CLI version
content_generator_core.py  ← Core logic
api/                       ← Web server folder
  └── index.py
index.html                 ← Web interface
run.sh                     ← Launcher script
run.bat                    ← Windows launcher
```

## ⚠️ Common Mistakes

### ❌ Wrong:
```bash
# Being in your home directory
cd ~
python3 content_generator.py  # ← Won't work! File not here.
```

### ✅ Correct:
```bash
# Being in the project directory
cd /Users/tlf/ContentCreatorGenerator
python3 content_generator.py  # ← Works! File is here.
```

## 🎯 Quick Test

**Are you in the right place?**

```bash
# Run this:
ls content_generator.py

# If you see:
# content_generator.py  ← ✅ You're in the right place!

# If you see:
# No such file or directory  ← ❌ Wrong folder!
```

## 🚀 First Time Setup (One Time Only)

```bash
# 1. Navigate to project
cd /Users/tlf/ContentCreatorGenerator

# 2. Make launcher executable
chmod +x run.sh

# 3. Run it!
./run.sh
```

## 💻 For Windows Users

Use `run.bat` instead:

```cmd
cd C:\Users\YourName\ContentCreatorGenerator
run.bat
```

## 🆘 Still Not Working?

### Check Python Installation:
```bash
python3 --version
```

Should show: `Python 3.7` or higher

**Not installed?** Download from: https://www.python.org

### Check Current Directory:
```bash
pwd
```

Should show: `/Users/tlf/ContentCreatorGenerator`

If not, you're in the wrong place!

### Start Fresh:
```bash
# Go home
cd ~

# Clone the repo (if needed)
git clone https://github.com/gyos23/ContentCreatorGenerator.git

# Enter it
cd ContentCreatorGenerator

# Make launcher executable
chmod +x run.sh

# Run it
./run.sh
```

## 📱 Quick Reference Card

**Print this out or save it:**

```
╔════════════════════════════════════════╗
║   SOCIAL MEDIA CONTENT GENERATOR       ║
║   Quick Start Commands                 ║
╠════════════════════════════════════════╣
║                                        ║
║  1. Open Terminal                      ║
║                                        ║
║  2. cd /Users/tlf/ContentCreatorGenerator
║                                        ║
║  3. ./run.sh                           ║
║                                        ║
║     OR                                 ║
║                                        ║
║     python3 content_generator.py       ║
║                                        ║
╚════════════════════════════════════════╝
```

## ✨ Pro Tip: Create an Alias

Add this to your `~/.zshrc` or `~/.bash_profile`:

```bash
alias content="cd /Users/tlf/ContentCreatorGenerator && ./run.sh"
```

Then reload:
```bash
source ~/.zshrc   # or source ~/.bash_profile
```

Now from anywhere, just type:
```bash
content
```

And it runs! 🎉
