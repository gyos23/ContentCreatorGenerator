# Development Workflow Guide

## 🔄 How the Workflow Works

You have a **2-way sync** setup! GitHub is the middleman, and you can make changes from either end:

```
Claude Code  <---->  GitHub  <---->  Replit
     ↓                  ↓                ↓
  Generate          Source of        Edit & Test
   & Build            Truth            Live
```

## ✅ Option 1: Claude Code → GitHub → Replit

**Best for:** Major features, new functionality, complex changes

### Steps:
1. **Make changes with Claude Code**
   - Claude generates/modifies code
   - Changes are committed to your branch

2. **Push to GitHub**
   ```bash
   git push origin your-branch-name
   ```

3. **Pull in Replit**
   ```bash
   git pull origin your-branch-name
   ```

4. **Test in Replit**
   - Run the app
   - Test features
   - Deploy if it works

## ✅ Option 2: Replit → GitHub → Claude Code

**Best for:** Quick fixes, testing tweaks, UI adjustments

### Steps:
1. **Make changes in Replit**
   - Edit files directly
   - Test immediately

2. **Commit in Replit**
   ```bash
   git add .
   git commit -m "Your change description"
   git push origin your-branch-name
   ```

3. **Pull in Claude Code** (next time you open it)
   - Claude Code will detect changes
   - Or manually pull if needed

## 🎯 Recommended Workflow Pattern

### For Your Use Case:

**Phase 1: Building (Claude Code)**
- Use Claude Code to generate new features
- Add major functionality
- Fix complex issues
- Push to GitHub when done

**Phase 2: Testing & Tweaking (Replit)**
- Pull changes from GitHub
- Test the app live
- Make small UI tweaks
- Adjust copy/text
- Push fixes back to GitHub

**Phase 3: Deploying (Vercel)**
- Vercel watches your GitHub main branch
- Automatically deploys when you merge/push
- No manual steps needed!

## ⚠️ Important: Avoiding Conflicts

### Before Starting Work (Either Platform):
```bash
# Always pull first!
git pull origin your-branch-name
```

### If You Get Merge Conflicts:
**In Replit:**
1. Open conflicted files
2. Look for `<<<<<<<` and `>>>>>>>` markers
3. Choose which changes to keep
4. Remove conflict markers
5. Commit the resolved files

**In Claude Code:**
1. Ask Claude to help resolve conflicts
2. Claude can read both versions and merge them

## 🔑 Best Practices

### 1. **Commit Often**
- Small, focused commits are better
- Clear commit messages
```bash
git commit -m "Add custom topic input feature"
```

### 2. **Pull Before Push**
Always pull before pushing to avoid conflicts:
```bash
git pull origin your-branch-name
git push origin your-branch-name
```

### 3. **Use Branches**
- Main branch for production
- Feature branches for development
- Claude Code creates branches like `claude/feature-name`

### 4. **Test Before Merging**
- Test in Replit first
- Merge to main when ready
- Vercel auto-deploys main

## 📋 Quick Reference

### Common Commands (Use in Replit or Claude Code):

```bash
# See what changed
git status

# See your changes
git diff

# Pull latest from GitHub
git pull origin branch-name

# Add all changes
git add .

# Commit with message
git commit -m "Description of changes"

# Push to GitHub
git push origin branch-name

# Create new branch
git checkout -b feature-name

# Switch branches
git checkout branch-name

# See all branches
git branch -a
```

## 🎬 Your Custom Topic Feature Workflow Example

Let's say you want to:
1. Generate feature in Claude Code ✓ (Done!)
2. Test in Replit
3. Make UI tweaks
4. Deploy

### Step-by-Step:

**In Claude Code (Already Done):**
```bash
# Claude created:
# - Custom topic generator
# - API endpoint
# - UI form
# Committed and pushed to GitHub ✓
```

**In Replit (Next Steps):**
```bash
# 1. Pull the changes
git pull origin claude/social-media-content-generator-011CUsPcst5srbnKQLBmzFYq

# 2. Test the new feature
python3 api/index.py

# 3. If you need to tweak something (e.g., change button color)
# Edit the file in Replit
# Then:
git add .
git commit -m "Change custom topic button to green"
git push

# 4. Ready for production?
# Merge to main:
git checkout main
git merge claude/social-media-content-generator-011CUsPcst5srbnKQLBmzFYq
git push origin main

# Vercel auto-deploys! 🚀
```

## 💡 Pro Tips

1. **GitHub Desktop**: If command line feels clunky, use GitHub Desktop app for easier Git management

2. **VS Code Git**: Has built-in Git UI that's very intuitive

3. **Replit Git UI**: Replit has a Git panel you can use instead of terminal

4. **Protection**: Never force push (`git push -f`) unless you know what you're doing

5. **Backup**: GitHub IS your backup - commit often!

## ❓ Common Questions

**Q: Can I work on both Claude Code and Replit at the same time?**
A: Not recommended. Finish on one platform, push, then pull on the other.

**Q: What if I forget to pull first?**
A: You might get conflicts. Pull, resolve conflicts, then push.

**Q: Should I use main branch or feature branches?**
A: Feature branches for development, main for production.

**Q: How do I know which changes are mine vs Claude's?**
A: Check `git log` to see commit history and authors.

**Q: Can I edit directly on GitHub?**
A: Yes, but not recommended for code. Good for README updates.

## 🎯 Summary

**Yes, it's 2-way sync!** GitHub is the source of truth in the middle.

- ✅ Start with Claude Code for major work
- ✅ Switch to Replit for testing and tweaks
- ✅ Always pull before starting work
- ✅ Commit and push when done
- ✅ Vercel watches GitHub and auto-deploys

You have full flexibility to work from either end!
