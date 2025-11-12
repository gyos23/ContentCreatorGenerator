# 🎯 Teaching the Generator YOUR Style

The content generator now learns from YOUR own successful content! Add examples of your best posts, and the generator will prioritize your voice and style.

## 📝 How It Works

The generator checks for your examples **FIRST**, then falls back to built-in content:

1. **User Examples** (YOUR content) - Priority #1
2. **Built-in Tips** (from expertise) - Priority #2
3. **Mix of Both** - When you don't have enough examples

## 📁 Where to Add Examples

Edit: `user_examples.json`

The file has three sections:

### 1. Tips (`tips`)

Add individual tips for any topic:

```json
"tips": {
  "your_topic_here": [
    {
      "title": "your tip title",
      "explanation": "Your explanation with [start B-roll] markers [end B-roll] if needed",
      "b_roll": true,
      "notes": "Why this works - high engagement, clear, relatable, etc."
    }
  ]
}
```

### 2. Hooks (`hooks`)

Add attention-grabbing hooks that worked:

```json
"hooks": {
  "your_topic_here": [
    {
      "hook": "Your proven hook text here",
      "notes": "Why it worked - honest, relatable, sparked curiosity"
    }
  ]
}
```

### 3. Full Scripts (`full_scripts`)

Add complete reel scripts that performed well:

```json
"full_scripts": [
  {
    "topic": "your topic",
    "hook": "...",
    "intro": "...",
    "transition": "...",
    "tips": [...],
    "cta": "...",
    "notes": "What made this successful",
    "performance": "high/medium/baseline"
  }
]
```

## 💡 Best Practices

### ✅ DO:
- **Add content that actually worked** - high engagement, saves, shares
- **Include your notes** - why did it work? What made it effective?
- **Use your own words** - don't sanitize your voice
- **Mark B-roll sections** - `[start B-roll]` and `[end B-roll]`
- **Update regularly** - after posting, add what performed well

### ❌ DON'T:
- Add content you haven't tested
- Copy other people's exact wording
- Skip the "notes" field - that's how you remember what works
- Forget to commit/push the updated file

## 🎬 Example: Adding a Tip

You posted about delegation and it got great engagement. Here's how to add it:

```json
{
  "title": "delegate your strengths first",
  "explanation": "Don't just delegate what you hate. [start B-roll] Start with tasks you're good at - it shows trust and builds capability faster. [end B-roll] The tasks you're avoiding? Those come later.",
  "b_roll": true,
  "notes": "This one surprised people - got 200+ saves. Counter-intuitive advice works."
}
```

## 🚀 Quick Add via API

You can also add examples via the API:

```bash
curl -X POST http://localhost:5000/api/user-examples/add \
  -H "Content-Type: application/json" \
  -d '{
    "type": "tip",
    "topic": "delegation skills",
    "content": {
      "title": "your tip",
      "explanation": "your explanation",
      "b_roll": true,
      "notes": "why it works"
    }
  }'
```

## 📊 How the Generator Uses Your Examples

- **Tips**: When you have 3+ user tips for a topic, generator uses ONLY yours
- **Tips (mixed)**: If you have 1-2 tips, generator mixes yours with built-in
- **Hooks**: 30% chance to use your hooks when available (keeps variety)
- **Full Scripts**: Reference for structure and flow

## 🔄 Workflow

1. **Post content** → Track performance
2. **Add winners** → Edit `user_examples.json`
3. **Commit changes** → `git add user_examples.json && git commit`
4. **Push to GitHub** → `git push`
5. **Deploy updated** → Vercel auto-deploys from GitHub

## 📈 Over Time

As you add more examples, the generator becomes **more YOU**:

- Week 1: Mostly built-in content, some of yours
- Month 1: 50/50 mix
- Month 3: Mostly your voice with built-in variety
- Month 6: Nearly all your proven content patterns

## 💬 Tips for Better Examples

### Write Good Notes

Bad: `"notes": "good tip"`

Good: `"notes": "Counter-intuitive. People expected 'delegate what you hate.' This flip got 200 saves and 40+ comments asking for more."`

### Capture What Works

After posting, ask:
- What made people stop scrolling?
- What line got quoted in comments?
- What concept got the most saves?
- What made it shareable?

Add THAT to your examples.

### Don't Overthink It

Start simple:
1. Post content
2. See what performs
3. Copy it to `user_examples.json`
4. Done

The generator gets smarter every time you add a winner.

---

**Remember**: The generator learns from YOU. The more you add, the more it sounds like you. 🎯
